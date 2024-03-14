import os
import random
import json
from types import TracebackType
from typing import Optional, Type


class ChatBot:
    def __init__(self, name: str, /) -> None:
        self.name = name
        self.current_data = []
        self.memory_path = os.path.normpath("chat_bot/memory.json")

        if os.path.exists(self.memory_path):
            with open(self.memory_path, mode="r") as file:
                self.current_data = json.load(file).get("memory", [])

    def learn_something_new(self, user_input: str, answer: str, /) -> None:
        option = {"user_input": user_input, "answer": answer}
        if option not in self.current_data:
            self.current_data.append(option)

    def get_answer(self, user_input: str, /) -> Optional[str]:
        possible_options = []
        for option in self.current_data:
            if option["user_input"] == user_input:
                possible_options.append(option["answer"])
        if len(possible_options) > 0:
            return random.choice(possible_options)

    def save_current_data(self) -> None:
        with open(self.memory_path, mode="w") as file:
            json.dump({"memory": self.current_data}, file, indent=4)


class ChatBotManager:
    def __init__(self, chat_bot: ChatBot) -> None:
        self.chat_bot = chat_bot

    def __enter__(self) -> ChatBot:
        return self.chat_bot

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc_type:
            print(f"Something went wrong: {exc_val}")
        self.chat_bot.save_current_data()


def conversation_mode(chat_bot: ChatBot) -> None:
    user_input = input("You: ")
    answer = chat_bot.get_answer(user_input)
    if answer is None:
        new_answer = input("I don't know how to answer this. Can you teach me? Answer: ")
        chat_bot.learn_something_new(user_input, new_answer)
    else:
        print(f"{chat_bot.name}: {answer}")


def learning_mode(chat_bot: ChatBot) -> None:
    user_input = input("user_input: ")
    new_answer = input("answer: ")
    chat_bot.learn_something_new(user_input, new_answer)