from tkinter import *
import requests
import xmltodict
from Book import SingleBook


class AllBooks:

    def __init__(self):
        self.api_key = 'l1eCwD6ckPZinhRvhA9MSQ'
        self.url = 'https://www.goodreads.com/review/list/46998003.xml?key={}&v=2'.format(self.api_key)

    def getBooks(self):
        request = requests.get(self.url)

        dict_books = xmltodict.parse(request.text)

        return dict_books

    def showBooks(self, dict_books, frame):
        i = 0
        frame_book_left = Frame(frame, width=100, height=200)
        frame_book_left.pack(side=LEFT)
        frame_book_right = Frame(frame, width=100, height=200)
        frame_book_right.pack(side=RIGHT)
        for book in dict_books['GoodreadsResponse']['reviews']['review']:
            def single(id_book):
                see_book = SingleBook(id_book)
                dict_book = see_book.getBook()
                show_book = see_book.showBook(dict_book, frame)

            if i <= 6:

                single_book_left = Frame(frame_book_left)
                single_book_left.pack(padx=10, pady=10)
                id_left = book['book']['id']['#text']
                book_title_left = Label(single_book_left, text=book['book']['title'], font=("Helvetica bold", 14))
                book_author_left = Label(single_book_left, text=book['book']['authors']['author']['name'])
                see_book_left = Button(single_book_left, text="See", command=lambda: single(id_left))

                book_title_left.pack()
                book_author_left.pack()
                see_book_left.pack(side=RIGHT)
            elif i <= 12:
                single_book_right = Frame(frame_book_right)
                single_book_right.pack(padx=10, pady=10)
                id_right = book['book']['id']['#text']
                book_title_right = Label(single_book_right, text=book['book']['title'], font=("Helvetica bold", 14))
                book_author_right = Label(single_book_right, text=book['book']['authors']['author']['name'])
                see_book_right = Button(single_book_right, text="See", command=lambda: single(id_right))

                book_title_right.pack()
                book_author_right.pack()
                see_book_right.pack(side=RIGHT)
            i += 1
