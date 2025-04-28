def get_bot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey", "greetings"]:
        return "Hi there! How can I assist you?"

    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! Have a nice day!"

    elif user_input in ["how are you", "how r u", "how you doing"]:
        return "I'm just a chatbot, but I'm doing great!"

    elif user_input == "what are the best colleges from pune?":
        return "Some of the best colleges are: PCCOE, PICT, VIT, and COEP."

    elif user_input == "what are the top branch cut-offs for vit?":
        return "VIT Top Branch Cut-offs:\n- Computer Engineering: 99.8 percentile\n- IT Engineering: 97.1 percentile\n- ENTC Engineering: 96.2 percentile"

    elif user_input == "what are the top branch cut-offs for pccoe?":
        return "PCCOE Top Branch Cut-offs:\n- Computer Engineering: 99.8 percentile\n- No IT branch available\n- ENTC Engineering: 99.2 percentile"

    elif user_input == "which are the best engineering branches?":
        return "Top Engineering Branches are: Computer Engineering, IT Engineering, and ENTC Engineering."

    else:
        return "I'm sorry, I didn't understand that. Can you please ask something else?"

def main():
    print("Welcome to the College Chatbot!")
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["bye", "exit", "quit", "goodbye"]:
            print("Bot:", get_bot_response(user_input))
            break

        print("Bot:", get_bot_response(user_input))

if __name__ == "__main__":
    main()
