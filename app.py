import requests
import json

def blocklist_or_unblock(api_token, link, action):
    """
    Function to blocklist or unblocklist a link using Adjust Blocklist API.

    :param api_token: Adjust API token
    :param link: Adjust link to blocklist or unblocklist
    :param action: Either 'blocklist' or 'unblocklist'
    """
    # Define the endpoint based on the action
    if action == "blocklist":
        url = f"https://api.adjust.com/dashboard/api/trackers/{link}/blacklist"
    elif action == "unblocklist":
        url = f"https://api.adjust.com/dashboard/api/trackers/{link}/unblacklist"
    else:
        print("Invalid action. Use 'blocklist' or 'unblocklist'.")
        return

    # Set up headers for authentication
    headers = {
        "Authorization": f"Token token={api_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Pretty-print the JSON response if successful
        if response.status_code == 200:
            print("Success:")
            print(json.dumps(response.json(), indent=4))  
        else:
            print(f"Unexpected response code: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return  

if __name__ == "__main__":
    print("Adjust Blocklist API Script")

    # Ask the user for their API token
    api_token = input("Enter your Adjust API token: ").strip()

    # Ask the user for the links to blocklist/unblocklist
    links = input("Enter the Adjust link token(s) (e.g., abc123), or tokens separated by commas: ").strip()

    # Ask the user for the action
    action = input("Do you want to 'blocklist' or 'unblocklist' the link(s)? ").strip().lower()

    # Validate the action
    if action not in ["blocklist", "unblocklist"]:
        print("Invalid action. Use 'blocklist' or 'unblocklist'.")
    else:
        # Split the links by commas and iterate over them
        link_tokens = [link.strip() for link in links.split(",") if link.strip()]
        for link in link_tokens:
            print(f"\nProcessing link: {link}")
            blocklist_or_unblock(api_token, link, action)