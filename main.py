import os
import random
import json
from typing import Optional


class ChatBot:
    def __init__(self, name: str, /) -> None:
        self.name = name
        self.current_data = []
        self.memory_path = os.path.normpath("memory.json")

        if os.path.exists(self.memory_path):
            with open(self.memory_path, mode="r") as file:
                self.current_data = json.load(file).get("memory")

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


def run_chat_bot_conversation(name: str) -> None:
    chat_bot = ChatBot(name)

    while True:
        user_input = input("You: ")
        if user_input == "--teach":
            user_input = input("Teacher: ")
            new_answer = input("Answer: ")
            chat_bot.learn_something_new(user_input, new_answer)
        else:
            answer = chat_bot.get_answer(user_input)
            if answer is None:
                new_answer = input("I don't know how to answer this. Can you teach me? Answer: ")
                chat_bot.learn_something_new(user_input, new_answer)
            else:
                print(f"{chat_bot.name}: {answer}")

        option = input("Do you want to continue (Y/N): ").lower()
        if option == "y":
            pass
        elif option == "n":
            chat_bot.save_current_data()
            break
        else:
            chat_bot.save_current_data()
            print("Unknown option!")
            break


if __name__ == "__main__":
    run_chat_bot_conversation("Aria")
