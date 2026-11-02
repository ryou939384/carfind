class QuizGame:
    def __init__(self, questions, display):
        self.questions = questions
        self.display = display

        self.current_question = 0
        self.score = 0

    def get_question(self):
        return self.questions[self.current_question]

    def check_answer(self, answer):
        question = self.get_question()

        correct = answer == question["answer"]

        if correct:
            self.score += 1

        self.display.show_result(correct)

    def next_question(self):
        self.current_question += 1

        if self.current_question >= len(self.questions):
            self.display.show_final_score(
                self.score,
                len(self.questions)
            )
        else:
            self.display.show_question()