'''Программа для изучения Английского языка'''
#Подключение необходимых библиотек
from tkinter import *

from alphabetDict import ALPHABET
from word import Word

#Создаем класс для возможности извлечения значений из словаря, 
#проигрывания слова, 
#получения пользовательского ввода, 
#обработки полученной информации, проверки на правильность и вывода результата 

word = Word()



window = Tk()
window.geometry("640x480")
btnChangeDict = Button(window, text = "Алфавит", command = word.changeDict(ALPHABET))
btnPlay = Button(window, text = "Играть", command = word.playWord)
txtAnswer = Entry(window, width = 5)
btnCheckAnswer = Button(window, text = "Проверить", command = word.checkAnswer) 
result = Label(window, text = '')
btnNewWord = Button(window, text = "Новая буква", command = word.newWord)
btnPutRating = Button(window, text = "Получить оценку", command = word.putRating)
lblMark = Label(window, text = '')

word.txtAnswer = txtAnswer
word.result = result
word.lblMark = lblMark

btnChangeDict.grid(column = 1, row = 0)
btnPlay.grid(column = 1, row = 1)
txtAnswer.grid(column = 2, row = 1)
btnCheckAnswer.grid(column = 3, row = 1)
result.grid(column = 4, row = 1)
btnNewWord.grid(column = 1, row = 2)
btnPutRating.grid(column = 2, row = 3)
lblMark.grid(column = 2, row = 4)
window.mainloop()
