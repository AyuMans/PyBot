print("QuizBot: Hey there! I am QuizBot! Can you solve my Quizzes!?")
print("Type 'start' to begin!")
print("Type 'quit' to exit quiz mode!")
print("Type 'end' to exit program!")

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

bye_phrases = [
    "bye",
    "goodbye",
    "see you",
    "see ya",
    "later",
    "catch you later",
    "talk to you later",
    "see you later",
    "ciao",
    "peace",
    "farewell",
    "take care",
    "gotta go",
    "i'm out",
    "i have to go",
    "bye bye",
    "see ya later",
    "gtg",
    "ttyl",
    "adios",
    "ok bye",
    "ok goodnight",
    "good night",
    "night",
    "buh bye",
    "have a good day",
    "have a nice day",
    "until next time",
    "cya"
]

questions = {
    "What is the capital of France?": "Paris",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the boiling point of water in Celsius?": "100",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal in the world?": "Blue Whale",
    "In which year did India gain independence?": "1947",
    "What is the chemical symbol for Gold?": "Au",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the square root of 64?": "8",
    "Who is known as the father of computers?": "Charles Babbage"
}

from myfunc import quiz

while True:
    op = input("You: ").strip().lower()
    
    if op == 'end':
        break
    if op == 'start':
        quiz(questions)
        
        userinput = input("Try again?(yes/no): ").strip().lower()
        if userinput == "yes":
            quiz(questions)
        elif userinput == "no":
            pass
        
    elif any(phrase in op for phrase in how_are_you_phrases):
        print("QuizBot: I am fine! Ready for my quiz!?")
    elif any(phrase in op for phrase in who_are_you_phrases):
        print("QuizBot: I am QuizBot! I have a quiz for you! Type 'start' to begin!!")
    elif any(greet in op for greet in greetings):
        print("QuizBot: Hi there!!")
    elif any(phrase in op for phrase in bye_phrases):
        print("QuizBot: Goodbye! Type 'End' to exit program...")
    else:
        print("QuizBot: Sorry, I do not understand.")
        continue
        
    