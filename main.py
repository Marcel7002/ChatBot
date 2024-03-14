from chat_bot import *


def run_chat_bot_conversation() -> None:
    with ChatBotManager(ChatBot("Aria")) as chat_bot:
        while True:
            print("-"*60)
            print("1) Conversation mode\n2) learning mode\n3) exit")
            print("-" * 60)
            option = input("Option: ")
            if option == "1":
                conversation_mode(chat_bot)
            elif option == "2":
                learning_mode(chat_bot)
            elif option == "3":
                break
            else:
                print("Unknown option!")
                break


if __name__ == "__main__":
    run_chat_bot_conversation()
