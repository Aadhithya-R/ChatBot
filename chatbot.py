"""
A simple rule-based chatbot.
Run it with: python chatbot.py
Type 'quit', 'exit', or 'bye' to end the conversation.
"""

import random

# Patterns mapped to possible responses.
# Each key is a lowercase keyword/phrase to look for in the user's input.
RESPONSES = {
    "hello": ["Hey there!", "Hello!", "Hi, how can I help?"],
    "hi": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I'm just code, but I'm doing well!", "Running smoothly, thanks for asking!"],
    "your name": ["I'm a simple chatbot you just built in Python.", "You can call me ChatBot."],
    "help": ["I can chat with you about simple things. Try asking how I am, or say hello!"],
    "weather": ["I can't check the weather, but I hope it's nice outside!"],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I told a UDP joke, but you might not get it.",
    ],
    "thank": ["You're welcome!", "No problem at all!", "Anytime!"],
}

DEFAULT_RESPONSES = [
    "Interesting, tell me more.",
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, can you say that another way?",
    "I don't have a great answer for that yet.",
]

EXIT_WORDS = {"quit", "exit", "bye", "goodbye"}


def get_response(user_input: str) -> str:
    text = user_input.lower()

    if any(word in text for word in EXIT_WORDS):
        return "Goodbye! Have a great day."

    for keyword, replies in RESPONSES.items():
        if keyword in text:
            return random.choice(replies)

    return random.choice(DEFAULT_RESPONSES)


def main():
    print("ChatBot: Hi! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        reply = get_response(user_input)
        print(f"ChatBot: {reply}")

        if user_input.lower() in EXIT_WORDS:
            break


if __name__ == "__main__":
    main()
