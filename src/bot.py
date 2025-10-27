from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from prepare_csv import prepare_dataset

CORPUS_FILE = "personality.csv"

chatbot = ChatBot("Gabbot")


trainer = ListTrainer(chatbot)
cleaned_corpus = prepare_dataset(CORPUS_FILE)

# Train for each conversation and don't lose coherence
for conversation in cleaned_corpus[
    :100
]:  # The output is too long without the [:100] slice.
    trainer.train(conversation)


print("✅ Entrenamiento completo.")

# Create a conversation loop with exit conditions.
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🤖 {chatbot.get_response(query)}")
