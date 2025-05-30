def greet_user():
    print("Hello! How are you feeling today?")
    mood = input("Please enter your mood (happy, neutral, sad): ").lower()

    if mood == "sad":
        print("I'm sorry to hear that. I'm here to support you.")
    elif mood == "neutral":
        print("How was your day?")
        input("Tell me about it: ")
    elif mood == "happy":
        print("That's great! I'm glad to hear that.")
    else:
        print("I didn't understand your mood. Please try again.")
        return

    while True:
        follow_up = input("Would you like to ask another question? (yes/no): ").lower()
        if follow_up == "yes":
            input("Ask away: ")
        elif follow_up == "no":
            print("Goodbye! Have a great day.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
if __name__ == "__main__":
    greet_user()
    