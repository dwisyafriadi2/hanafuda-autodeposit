import sys
import requests
import time

# Read bearer token from file
with open("token.txt", "r") as f:
    bearer_token = f.read().strip()

# Hanafuda API URL
hanafuda_url = "https://hanafuda-backend-app-520478841386.us-central1.run.app/graphql"

headers_hanafuda = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",
    "Accept": "application/graphql-response+json, application/json"
}

# Function to check Grow Points & Open Card status
def check_garden_status():
    payload = {
        "query": """
            query GetGardenForCurrentUser {
                getGardenForCurrentUser {
                    gardenStatus {
                        growActionCount
                        gardenRewardActionCount
                    }
                }
            }
        """,
        "operationName": "GetGardenForCurrentUser"
    }
    response = requests.post(hanafuda_url, json=payload, headers=headers_hanafuda)
    data = response.json()
    
    try:
        status = data["data"]["getGardenForCurrentUser"]["gardenStatus"]
        return status["growActionCount"], status["gardenRewardActionCount"]
    except Exception as e:
        print("Error fetching garden status:", e)
        return 0, 0

# Function to execute Grow Action
def execute_grow_action():
    payload = {
        "query": """
            mutation ExecuteGrowAction($withAll: Boolean) {
                executeGrowAction(withAll: $withAll) {
                    baseValue
                    leveragedValue
                    totalValue
                    multiplyRate
                }
            }
        """,
        "variables": {"withAll": True},
        "operationName": "ExecuteGrowAction"
    }
    response = requests.post(hanafuda_url, json=payload, headers=headers_hanafuda)
    data = response.json()
    print("Grow Action Response:", data)

# Function to execute Open Card Action
def execute_open_card():
    payload = {
        "query": """
            mutation executeGardenRewardAction($limit: Int!) {
                executeGardenRewardAction(limit: $limit) {
                    data {
                        cardId
                        group
                    }
                    isNew
                }
            }
        """,
        "variables": {"limit": 10},
        "operationName": "executeGardenRewardAction"
    }
    response = requests.post(hanafuda_url, json=payload, headers=headers_hanafuda)
    data = response.json()
    print("Open Card Response:", data)

# Ask user for actions
auto_grow = input("Do you want Auto Grow? (Y/N): ").strip().lower() == "y"
auto_open_card = input("Do you want Auto Open Card? (Y/N): ").strip().lower() == "y"

while True:
    grow_count, card_count = check_garden_status()
    print(f"Grow Points: {grow_count}, Card Open Points: {card_count}")
    
    if auto_grow and grow_count > 0:
        execute_grow_action()
    elif auto_grow and grow_count == 0:
        print("No Grow Points available. Waiting 40 minutes...")
        time.sleep(2400)  # 40 minutes
        continue
    
    if auto_open_card and card_count > 0:
        execute_open_card()
    elif auto_open_card and card_count == 0:
        print("No more cards to open. Stopping.")
        break
    
    time.sleep(5)
