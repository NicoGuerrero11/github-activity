# GitHub Activity CLI

This is a simple command-line interface (CLI) tool built with Python. It allows users to check the most recent public activities of a specified GitHub user using the GitHub public API.

## Features

- Fetch and display the latest public activity of a GitHub user.
- Error handling for:
  - Missing username argument.
  - Nonexistent GitHub user.
  - GitHub user with no public activity.
- Friendly and informative terminal output.

## How to Use

Run the script from the terminal and pass a GitHub username as an argument:

```
python github_activity.py <github_username>
```

## Requirements

- Python 3.x
- `requests` library (install with `pip3 install requests`)

## GitHub API Used

This project uses the following endpoint from the GitHub public API:

```
https://api.github.com/users/{username}/events/public
```

## Project Roadmap

Project listed on: [roadmap.sh](https://roadmap.sh/projects/github-user-activity)
