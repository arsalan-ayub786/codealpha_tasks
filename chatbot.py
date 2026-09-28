# Basic Rule-Based Chatbot - CodeAlpha Python Internship (Task 4)


def clean_input(user_input):
    # Convert to lowercase and remove common punctuation
    text = user_input.lower().strip()
    for mark in ["?", "!", "."]:
        text = text.replace(mark, "")
    return text.strip()


def get_response(user_input):
    text = clean_input(user_input)

    if text == "hello" or text == "hi":
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "what is your name":
        return "I am a simple Python chatbot."
    elif text == "help":
        return "You can say: hello, how are you, what is your name, or bye."
    elif text == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can answer."


def main():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot: " + response)

        if clean_input(user_input) == "bye":
            break


main()