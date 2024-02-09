import time
import requests
import json

def is_osu_playing():
    # Simulated game detection logic - replace this with your actual game detection mechanism
    return True  # Change this based on your detection logic

def get_user_stats(username):
    api_url = f'https://osu.ppy.sh/api/get_user?k=YOUR_API_KEY&u={username}&m=0'  # Replace YOUR_API_KEY with your API key

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = json.loads(response.text)

        if not data:
            print(f"User '{username}' not found.")
            return None

        return data[0]

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

    return None

def display_user_stats(user_data):
    if user_data:
        print(f"\nUsername: {user_data['username']}")
        print(f"Global Rank: #{user_data['pp_rank']}")
        print(f"PP: {user_data['pp_raw']}")
        print(f"Accuracy: {user_data['accuracy']}%")
        print(f"Play Count: {user_data['playcount']}")
    else:
        print("Failed to fetch user stats.")

if __name__ == "__main__":
    username = input("Enter your OSU! username: ")

    while True:
        if is_osu_playing():
            user_stats = get_user_stats(username)
            display_user_stats(user_stats)
        else:
            print("OSU! is not currently playing.")

        time.sleep(60)  # Refresh every 1 minute

