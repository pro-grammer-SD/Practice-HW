from textblob import TextBlob
from colorama import init, Fore, Style
import time
import sys
import re

init(autoreset=True)

conversation = []
counts = {'positive': 0, 'negative': 0, 'neutral': 0}

def show_processing_animation():
    animation = ['[■□□□□]', '[■■□□□]', '[■■■□□]', '[■■■■□]', '[■■■■■]']
    for frame in animation:
        sys.stdout.write(f'\rAnalyzing sentiment {frame}')
        sys.stdout.flush()
        time.sleep(0.3)
    print('\r' + ' ' * 25, end='\r')

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = 'positive'
    elif polarity < -0.1:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return sentiment, polarity

def execute_command(command, username):
    cmd = command.lower()
    if cmd == 'summary':
        total = sum(counts.values())
        print(f"\n{Fore.CYAN}--- Sentiment Summary ---")
        print(f"Total messages analyzed: {total}")
        print(f"{Fore.GREEN}Positive: {counts['positive']}")
        print(f"{Fore.RED}Negative: {counts['negative']}")
        print(f"{Fore.YELLOW}Neutral : {counts['neutral']}\n")
    elif cmd == 'reset':
        conversation.clear()
        for k in counts:
            counts[k] = 0
        print(Fore.MAGENTA + "Data reset. Starting fresh.")
    elif cmd == 'history':
        if not conversation:
            print(Fore.MAGENTA + "No conversation history yet.")
            return
        print(Fore.CYAN + "\n--- Conversation History ---")
        for i, (msg, sent, pol) in enumerate(conversation, 1):
            color = Fore.GREEN if sent == 'positive' else Fore.RED if sent == 'negative' else Fore.YELLOW
            print(f"{i}. {msg} -> {color}{sent} (polarity: {pol:.2f})")
        print()
    elif cmd == 'help':
        print(Fore.CYAN + "\nAvailable commands:\n"
              "summary  - Show sentiment statistics\n"
              "reset    - Clear all data\n"
              "history  - Show all analyzed messages\n"
              "help     - Show this help message\n"
              "exit     - Quit and save report\n")
    else:
        print(Fore.MAGENTA + "Unknown command. Type 'help' for options.")

def get_valid_name():
    while True:
        name = input("Enter your name, Agent: ").strip()
        if name.isalpha():
            return name.capitalize()
        print("Only alphabets allowed. Try again.")

def main():
    username = get_valid_name()
    print(f"\nWelcome, Agent {username}. Your sentiment analysis mission starts now.")
    print("Type anything to analyze sentiment or enter commands. Type 'help' for commands.\n")

    while True:
        user_input = input(Fore.WHITE + "You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == 'exit':
            total = sum(counts.values())
            print(f"\nMission complete, Agent {username}!")
            print(f"Total messages analyzed: {total}")
            print(f"{Fore.GREEN}Positive: {counts['positive']}")
            print(f"{Fore.RED}Negative: {counts['negative']}")
            print(f"{Fore.YELLOW}Neutral : {counts['neutral']}\n")

            report_lines = [
                f"Sentiment Analysis Report for Agent {username}\n",
                f"Total messages: {total}\n",
                f"Positive: {counts['positive']}\n",
                f"Negative: {counts['negative']}\n",
                f"Neutral: {counts['neutral']}\n\n",
                "Detailed conversation:\n"
            ]
            for i, (msg, sent, pol) in enumerate(conversation, 1):
                report_lines.append(f"{i}. {msg} -> {sent} (polarity: {pol:.2f})\n")
            filename = f"{username}_sentiment_analysis.txt"
            with open(filename, 'w') as f:
                f.writelines(report_lines)
            print(f"Report saved to {filename}")
            break

        if user_input.lower() in ['summary', 'reset', 'history', 'help']:
            execute_command(user_input, username)
            continue

        show_processing_animation()
        sentiment, polarity = analyze_sentiment(user_input)
        counts[sentiment] += 1
        conversation.append((user_input, sentiment, polarity))

        color = Fore.GREEN if sentiment == 'positive' else Fore.RED if sentiment == 'negative' else Fore.YELLOW
        strength = "strong" if abs(polarity) > 0.5 else "mild"
        print(color + f"Sentiment: {sentiment.upper()} ({strength}, polarity={polarity:.2f})\n")

if __name__ == '__main__':
    main()
