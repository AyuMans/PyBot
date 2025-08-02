print("MultiBot: Hey there! I am MultiBot! I can do Many things!")
print("Type 'features' to see what I can do!")
print("Type 'End' to close program.")





import multibotfunc
import variables
Q = variables.questions
while True:
    
    user = input("You: ").strip().lower()
    
    if user == "end":
        break
    elif user == "exit":
        print("MultiBot: If you're trying to close program, type 'End'.")
        continue
    if user == "quiz":
        while True:
            
            finished = multibotfunc.quiz(Q)
            if not finished:
                break
            
            again = input("Try Again? (yes/no): ").strip().lower()
            
            if again != "yes":
                print("Exiting Quiz Mode...")
                break
        continue    
    elif user == "calc":
        multibotfunc.calc()
        continue
        
    elif user == "features":
        print("""MultiBot: These are my Features:
-Caclculator ( Type 'Calc' to activate)
-Quiz (Type 'Quiz' to activate)
If you need further instructions type 'help'""")
        continue
    
    chat = multibotfunc.chat(user)
    if chat:
        print(f"MultiBot: {chat}")    
    else:
        print("Sorry, I do not understand that yet.")    
        
        
        
        