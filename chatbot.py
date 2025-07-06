#if-elif-else

print("Chatbot: Hello! I am your assistant. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == 'hello' or user_input == 'Hii':
        print("Chatbot: Hello! How can I help you today?")
    elif "your name" in user_input:
        print("Chatbot: I am a simple chatbot created in Python.")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
    elif "help" in user_input:
        print("Chatbot: Sure! I can answer questions like 'your name', 'how are you', or say 'bye' to exit.")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    else:
        print("Chatbot: I'm sorry, I didn't understand that.")
