#imports
from tkinter import *
from tkinter import scrolledtext
from nltk import text
from textblob import TextBlob as tb


#creating window
r = Tk()
r.geometry('400x800')
r.configure(bg = '#151515')
r.resizable(0,0)


#Label widgets
head_title = Label(r, text = 'Spelling Correction', font = 'arial 15 bold', fg = 'white', bg = '#151515')
input_title = Label(r, text = 'Enter the Text', font = "arial 10 bold", fg = 'white', bg = '#151515')
correct_title = Label(r, text = 'Corrected Sentence', font = 'arial 10 bold', fg = 'white', bg = '#151515')
wrong_title = Label(r, text = 'Words that are misspelt', font = 'arial 10 bold', fg = 'white', bg = '#151515')


#ScrolledText widget
text_input = scrolledtext.ScrolledText(r, height = 8, width = 30, padx = 10, pady = 10, wrap = 'word', fg = '#151515', bg = '#A3DDCB')
correct_sentence = scrolledtext.ScrolledText(r,height = 8, width = 30, padx = 10, pady = 10, wrap = 'word', fg = '#151515', bg = '#A3DDCB')
wrong_words = scrolledtext.ScrolledText(r,height = 8, width = 30, padx = 10, pady = 10, wrap = 'word', fg = '#151515', bg = '#A3DDCB')

#functions
def correction():
    split_list = []
    corrected = []
    wrng = []
    inp = text_input.get("1.0","end-1c")
    x = inp.split(' ')
    for i in x:
        split_list.append(tb(i))
    for i in split_list:
        c=i.correct()
        corrected.append(c)
    sentence = (' '.join(map(str,corrected)))
    correct_sentence.insert(END, sentence)
    for i in range(0,len(split_list)):
        if(split_list[i]!=corrected[i]):
            wrong_words.insert(END,str(corrected[i] + ' '))
    if(inp == sentence):
        wrong_words.insert(END,"No Misspelt words")
            

def Exit():
    r.destroy()

def Reset():
    text_input.delete("1.0","end")
    correct_sentence.delete("1.0","end")
    wrong_words.delete("1.0","end")


#Buttons        
Correct_button = Button(r,text = 'Correct', font = 'arial 10 bold', bg = '#FFE3D8', width = 15, command = correction)
Reset_button = Button(r,text = 'Reset', font = 'arial 10 bold', width = 15, bg = '#BBBBBB', command = Reset)
Exit_button = Button(r, text = 'Exit', font = 'arial 10 bold', bg = '#E94560', command = Exit, width = '4')


#Layout managing
head_title.pack(pady = 10)
input_title.pack(pady = 10)
text_input.pack(pady = 5)
Correct_button.pack(pady = 8)
Reset_button.pack(pady = 5)
correct_title.pack(pady = 10)
correct_sentence.pack(pady = 5)
wrong_title.pack(pady = 10)
wrong_words.pack(pady = 5)
Exit_button.pack(pady = 10)

#runs the program
r.mainloop()