import requests
import json

def blocklist_or_unblock(api_token, link, action):
    """
    Function to blocklist or unblocklist a link using Adjust Blocklist API.

    :param api_token: Adjust API token
    :param link: Adjust link to blocklist or unblocklist
    :param action: Either 'blocklist' or 'unblocklist'
    """

    if action == "blocklist":
        url = f"https://api.adjust.com/dashboard/api/trackers/{link}/blacklist"
    elif action == "unblocklist":
        url = f"https://api.adjust.com/dashboard/api/trackers/{link}/unblacklist"
    else:
        print("Invalid action. Use 'blocklist' or 'unblocklist'.")
        return

    headers = {
        "Authorization": f"Token token={api_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  

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

    api_token = input("Enter your Adjust API token: ").strip()

    links = input("Enter the Adjust link token(s) (e.g., abc123), or tokens separated by commas: ").strip()

    action = input("Do you want to 'blocklist' or 'unblocklist' the link(s)? ").strip().lower()

    if action not in ["blocklist", "unblocklist"]:
        print("Invalid action. Use 'blocklist' or 'unblocklist'.")
    else:
        link_tokens = [link.strip() for link in links.split(",") if link.strip()]
        for link in link_tokens:
            print(f"\nProcessing link: {link}")
            blocklist_or_unblock(api_token, link, action)
            print(f"\nSuccess!")