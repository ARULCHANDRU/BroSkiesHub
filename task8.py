# chatbot.py
import datetime

def chatbot_response(user_input):
    """
    Generates a response based on keywords in the user's input.
    This function contains the core "rules" of the chatbot.
    """
    # Convert user input to lowercase to make matching case-insensitive
    processed_input = user_input.lower()

    # --- Define Rules and Responses ---
    
    # Greeting Intents
    if 'hello' in processed_input or 'hi' in processed_input or 'hey' in processed_input:
        return "Hello there! How can I help you today?"

    # Well-being Intents
    elif 'how are you' in processed_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."

    # Time-related Intents
    elif 'time' in processed_input:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p") # e.g., "09:30 PM"
        return f"The current time is {current_time}."

    # Bot Identity Intents
    elif 'your name' in processed_input or 'who are you' in processed_input:
        return "I am a simple rule-based chatbot created to assist you."

    # Task-related Intents
    elif 'task' in processed_input or 'help' in processed_input:
        return "You can ask me for the current time, or just have a simple chat. Type 'bye' to exit."

    # Fallback Response (if no other rule matches)
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    """
    The main function that runs the chatbot's conversation loop.
    """
    print("Chatbot: Hi! I'm your friendly rule-based assistant. Type 'bye' or 'quit' to exit.")
    
    # The main loop for the conversation
    while True:
        # Collect user input
        user_input = input("You: ")
        
        # Check for exit command
        if user_input.lower() in ['bye', 'quit', 'exit']:
            print("Chatbot: Goodbye! Have a great day.")
            break # This exits the loop
        
        # Get the response from the bot's brain and print it
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# This ensures the main() function runs when the script is executed
if __name__ == "__main__":
    main()