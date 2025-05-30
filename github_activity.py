import sys
import requests 
from datetime import datetime

def get_activity(username):
    # github api
    url = f"https://api.github.com/users/{username}/events/public"
    try:
        res = requests.get(url, timeout=10)

        if res.status_code == 404:
            print(f"Error: {username} not found")
        elif res.status_code == 403:
            print("Error: Request limit reached. Please try again later.")
        elif res.status_code != 200:
            print(f"Unexpected error: {res.status_code}")
        else:
            data = res.json()
            if not data:
                print("This user has no recent public activity")
            else:
                print(f"\nLatest public activities by {username}:")
                for event in data[:5]: #show the latest 5
                    created_at = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                    formatted_date = created_at.strftime("%d %b %Y, %H:%M")
                    print(f"{event['type']} in {event['repo']['name']} at {formatted_date}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Error: You must provide a GitHub username.")
        sys.exit(1)
    username = sys.argv[1]
    get_activity(username)


if __name__ == "__main__":
    main()