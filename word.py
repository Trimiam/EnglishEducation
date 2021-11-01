import random
from playsound import playsound


class Word():
    def __init__(self):
        self.dict = ''
        self.word = ''
        self.answer = ''
        self.keys = []
        self.values = []
        self.numOfAttempt = 0
        self.numOfCorrectAnswer = 0
        self.mistakes = 0
        self.rating = 0
    #получение случайного значения из словаря
    def changeDict(self, dict):
        self.dict = dict
        for i, j in dict.items():
            self.keys.append(i)
            self.values.append(j)
        return self.keys, self.values, self.dict    
    def newWord(self):
        self.word = self.dict[random.choice(list(self.dict))]
        return self.word    
    #проигрываем аудиозапись    
    def playWord(self):
        playsound(self.word)    
    #проверка ответа и выдача результата
    def checkAnswer(self):
        self.answer = self.txtAnswer.get()
        if self.dict[self.answer.upper()] == self.word:
            self.result.configure(text = "Верно!")
            self.numOfCorrectAnswer += 1
        else:
            self.result.configure(text = "Ошибка!")  
        self.numOfAttempt += 1
    def putRating(self):
        self.mistakes = self.numOfAttempt - self.numOfCorrectAnswer
        if self.mistakes == 0:
            self.rating = 5
        elif self.mistakes > 0 and self.mistakes <= 2:
            self.rating = 4
        elif self.mistakes > 2 and self.mistakes <= 4:   
            self.rating = 3
        else:
            self.rating = 2
        self.lblMark.configure(text = self.rating)
    