import json
import requests
import string 

# GitHub repository owner and name
owner = "opensearch-project"
repo = "OpenSearch-Dashboards"
token = "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"; # Replace with your token

# API endpoint to fetch issues
base_url = f"https://api.github.com/repos/{owner}/{repo}/issues"

# Headers with authorization token
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

def fetch_all_issues():
    issues = []
    page = 1

    while True:
        # API request with pagination
        response = requests.get(base_url, headers=headers, params={"state": "all", "per_page": 100, "page": page})

        # Check for successful response
        if response.status_code != 200:
            print(f"Error: Unable to fetch issues (HTTP {response.status_code})")
            print(response.json())
            break

        # Parse JSON response
        data = response.json()
        issues.extend(data)

        # Check if more pages are available
        if "next" not in response.links:
            break

        # Increment page
        page += 1

    return issues

# Fetch issues and save them to a JSON file
all_issues = fetch_all_issues()

# Save the data to a JSON file
output_file = "github_issues.json"
with open(output_file, "w") as f:
    json.dump(all_issues, f, indent=4)

print(f"Fetched {len(all_issues)} issues and saved to {output_file}")
