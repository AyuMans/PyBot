print("Hello, Ayush. I am your First ChatBot, and definitely not the last. How may I help you today?")

greetings = [
    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",
    "howdy",
    "greetings",
    "welcome",
    "what's up",
    "what’s going on",
    "how are you",
    "how's it going",
    "how do you do",
    "nice to meet you",
    "pleased to meet you",
    "yo",
    "sup",
    "whassup",
    "wassup",
    "‘sup",
    "hey there",
    "heyyy",
    "hiya",
    "hiiii",
    "holla",
    "yo yo",
    "what’s good",
    "what's poppin",
    "what’s cookin",
    "howzit",
    "hey buddy",
    "how you doin’",
    "long time no see",
    "hola",
    "bonjour",
    "ciao",
    "namaste",
    "salam",
    "konnichiwa",
    "annyeong",
    "ola",
    "sawasdee",
    "hallo"
]

how_are_you_phrases = [
    "how are you",
    "how are you doing",
    "how’s it going",
    "how are things",
    "how have you been",
    "how do you do",
    "you good",
    "what’s up",
    "what up",
    "sup",
    "how you doing",
    "how r u",
    "how are u",
    "how u doing",
    "you okay",
    "are you okay",
    "everything good",
    "you doing fine",
    "what’s going on",
    "are you alright",
    "im fine how are you",
    "i'm fine how are you",
    "i am fine how are you",
    "i’m doing good how about you",
    "i’m okay how are you",
    "i’m great how are you",
    "all good how about you",
    "doing fine what about you"
]

who_are_you_phrases = [
    "who are you",
    "who r u",
    "what is your name",
    "what’s your name",
    "tell me your name",
    "identify yourself",
    "can you tell me your name",
    "who is this",
    "who am i talking to",
    "who am i speaking to",
    "what do i call you",
    "are you a bot",
    "are you human",
    "are you real",
    "you real",
    "are you alive",
    "what are you",
    "what even are you",
    "what kind of bot are you",
    "you ai",
    "are you ai"
]

while True:
    userInput = input("You: ").lower()
    
    
    if any(phrase in userInput for phrase in how_are_you_phrases):
        print("Mybot: I am good. Thank you for asking.")
    elif any(x in userInput for x in who_are_you_phrases):
        print("Mybot: I am Mybot, the first proper chatbot created by Ayush Manna")
    elif any(greet in userInput for greet in greetings):
        print("Mybot: Hey there! How are you?")
    elif userInput == "bye":
        print ("Mybot: Bye! See you later!")
        break
    else:
        print("Mybot: I do not understand.")

    