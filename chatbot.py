print("🤖 Chatbot: Hello! I'm PYbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("PYbot: Hey there! 👋")
    elif "how are you" in user_input:
        print("PYbot: I'm just code, but I'm feeling awesome!")
    elif "your name" in user_input:
        print("PYbot: I'm PYbot, your Python-powered buddy!")
        
    elif "bye" in user_input:
        print("PYbot: Bye! Talk to you soon! 💻")
        break
    else:
        print("PYbot: Hmm... I don't understand that yet. 😅")
