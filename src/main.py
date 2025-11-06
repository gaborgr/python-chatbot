from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from prepare_csv import prepare_dataset

CORPUS_FILE = "personality.csv"

chatbot = ChatBot("Gabbot")


trainer = ListTrainer(chatbot)
cleaned_corpus = prepare_dataset(CORPUS_FILE)


def train_bot():
    # Train for each conversation and don't lose coherence - only 100 becouse its too much info.
    for conversation in cleaned_corpus[:100]:
        trainer.train(conversation)

    return print("✅ Entrenamiento completo.")


# Create a conversation loop with exit conditions.
def start_bot():
    exit_conditions = (":q", "quit", "exit")
    while True:
        query = input("> ")
        if query in exit_conditions:
            break
        else:
            print(f"🤖 {chatbot.get_response(query)}")


if __name__ == "__main__":
    train_bot()
    start_bot()
