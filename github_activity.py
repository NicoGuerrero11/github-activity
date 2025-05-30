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
            print(f"Error unexpected: {res.status_code}")
        else:
            data = res.json()
            if not data:
                print("This user has no recent public activity")
            else:
                print(f"\nLatest activities of {username}:")
                for event in data[:5]: #show the latest 5
                    print(f"{event['type']} in {event['repo']['name']} at {event['created_at']}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Error: you must add a github username")
        sys.exit(1)
    username = sys.argv[1]
    get_activity(username)


if __name__ == "__main__":
    main()