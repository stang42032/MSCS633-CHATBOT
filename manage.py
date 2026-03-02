#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# --------------------------------------------------------
# Terminal Chat Client (runs when no Django commands passed)
# --------------------------------------------------------
def run_terminal_chat():
    """
    Launch a terminal-based chatbot client.
    """
    from chat.chatbot import create_chatbot

    print("Initializing chatbot...")
    bot = create_chatbot()

    print("Chatbot is ready! Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("user: ")

            if user_input.lower() == "exit":
                print("bot: Goodbye!")
                break

            response = bot.get_response(user_input)
            print(f"bot: {response}")

        except (KeyboardInterrupt, EOFError):
            print("\nbot: Goodbye!")
            break


# If run without Django commands, start chat client
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        run_terminal_chat()