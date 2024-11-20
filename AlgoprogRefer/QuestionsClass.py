class Questions():
    def __init__(self, questions, Answers: list, Correct):
        self.questions = questions
        self.Answers = Answers
        self.Correct = Correct
    def __str__(self):
        return f'{self.questions} = {self.Answers} {self.Correct}'
    def getquestions(self):
        return self.questions
    def getAnswers(self):
        return self.Answers
    def getCorrect(self):
        return self.Correct
    
a = Questions("AA",["A","B","C","D"],"A")

print(str(a))

