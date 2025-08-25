class Questions:
    def __init__(self, questions):
        self.questions = questions
        self.questions_count = len(questions)

    def get_questions(self):
        return self.questions
    def get_total_question(self):
        return self.questions_count
