class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)

    def start(self):
        for flashcard in self.flashcards:
            print(f"Question: {flashcard.question}")
            input("Press Enter to reveal the answer...")
            print(f"Answer: {flashcard.answer}")
            print()

flashcard_app = FlashcardApp()
flashcard_app.add_flashcard("What is the capital of France?", "Paris")
flashcard_app.add_flashcard("What is the square root of 16?", "4")
flashcard_app.start()
