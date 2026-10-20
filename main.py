def chatbot_reply(user_input):
    # Convert input to lowercase and remove extra spaces
    message = user_input.lower().strip()

    # Predefined rules and replies
    if message == "hello" or message == "hi":
        return "Hi! Welcome to the chatbot!"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "I'm CodeAlpha Basic Chatbot."

    elif message == "help":
        return (
            "You can say hello, ask how are you, "
            "ask my name, say thanks, or type bye."
        )

    elif message == "thanks" or message == "thank you":
        return "You're welcome!"

    elif message == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that message."


def main():
    print("================================")
    print("   Welcome to Basic Chatbot")
    print("================================")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to end the conversation.")

    # Keep the conversation running
    while True:
        user_input = input("\nYou: ")

        # Handle empty input
        if not user_input.strip():
            print("Bot: Please type a message.")
            continue

        # Get the chatbot's reply
        reply = chatbot_reply(user_input)
        print("Bot:", reply)

        # Stop when the user types bye
        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()