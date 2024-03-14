from chat_bot import *


def run_conversation() -> None:
    with ChatBotManager(ChatBot("Aria")) as chat_bot:
        while True:
            print("-"*60)
            print("A) Conversation mode\nB) Math solver mode\nC) Learning mode\nD) Exit")
            print("-" * 60)
            option = input("Option: ").upper()
            match option:
                case "A":
                    conversation_mode(chat_bot)
                case "B":
                    math_solver_mode(chat_bot)
                case "C":
                    learning_mode(chat_bot)
                case "D":
                    break
                case _:
                    print("Unknown option!")
                    break


if __name__ == "__main__":
    run_conversation()
