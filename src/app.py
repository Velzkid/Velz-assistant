import os
from utils import greet_user

def run_agent():
    print("🤖 Velz Assistant is running!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Agent stopped.")
            break
        else:
            response = greet_user(user_input)
            print(f"Velz Assistant: {response}")

if __name__ == "__main__":
    run_agent()
