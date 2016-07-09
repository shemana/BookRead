from tkinter import *


class Books:
    def __init__(self, title, desc, img, frame):
        self.title = title
        self.desc = desc
        self.img = img
        self.frame = frame

    def show_book(self):
        frameBook = Frame(self.frame, width=100, height=200)
        frameBook.pack()
        #image = PhotoImage(file="~/PycharmProjects/BookRead/hp.png")
        cover = Canvas(frameBook, width=50, height=100)
        cover.pack()

        bookTitle = Label(frameBook, text=self.title)
        bookTitle.pack()

    def single_book(self):
        frameSingleBook = Frame(self.frame, width=500, height=500)
        frameSingleBook.pack()
        coverSingle = Canvas(frameSingleBook, width=100, height=250)
        coverSingle.pack(side=RIGHT)

        bookSingleTitle = Label(frameSingleBook, text=self.title)
        bookSingleTitle.pack(side=LEFT)

        bookSingleDesc = Label(frameSingleBook, text= self.desc)
        bookSingleDesc.pack()