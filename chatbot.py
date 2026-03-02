"""
chatbot.py
This module initializes and trains the ChatterBot instance.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chatbot():
    """
    Create and train the chatbot instance.
    Returns:
        ChatBot object
    """

    # Initialize chatbot
    chatbot = ChatBot(
        'TerminalBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )

    # Trainer
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train with English corpus
    trainer.train('chatterbot.corpus.english')

    return chatbot