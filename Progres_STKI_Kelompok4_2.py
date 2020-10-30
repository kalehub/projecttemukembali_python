import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import tkinter
from tkinter import *
import tkinter.filedialog

class DemoOpenFile:
    def __init__(self, induk, judul):
        self.induk = induk

        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
        self.induk.resizable(False, False)

        self.aturKomponen()

    def aturKomponen(self):
        # atur frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)

        ## frame_teks
        fr_file = Frame(mainFrame, bd=5)
        fr_file.pack(fill=BOTH, expand=YES)

        # atur komponen Label, Entri, Button
        # input file.
        Label(fr_file, text="Nama File: ", anchor=W).pack(side=LEFT)

        self.entFile = Entry(fr_file)
        self.entFile.pack(side=LEFT, fill=X, expand=1, padx=5)

        self.btnCari = Button(fr_file, text='Cari', command=self.onCari)
        self.btnCari.pack(side=LEFT)

        # atur komponen Text
        # tampilkan file
        fr_teks = Frame(mainFrame, bd=5)
        fr_teks.pack(fill=BOTH, expand=YES)

        self.txtFile = Text(fr_teks, wrap=NONE)

        sbVer = Scrollbar(fr_teks, orient=VERTICAL,
                          command=self.txtFile.yview)
        sbHor = Scrollbar(fr_teks, orient=HORIZONTAL,
                          command=self.txtFile.xview)

        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)

        self.txtFile.config(yscrollcommand=sbVer.set,
                            xscrollcommand=sbHor.set)
        self.txtFile.pack()

        # atur Button keluar
        Button(mainFrame, text='Keluar', command=self.tutup).pack(pady=5)

        # atur statusbar
        Label(mainFrame, text='Progres Kelompok 4',
              bd=1, relief=RIDGE, foreground='blue').pack(
            side=BOTTOM, fill=X)

    def onCari(self, event=None):
        # membuka file dialog
        namafile = askopenfilename(filetypes=[('File TXT', '*.txt')])

        # jika file terbuka, maka judul file
        # ditampilkan pada komponen Entry.
        if namafile:
            self.entFile.delete(0, END)
            self.entFile.insert(END, namafile)

            # panggil fungsi isidata
            self.isiDataFile(namafile)

    def isiDataFile(self, nmfile):
        # buka file dengan fungsi Open ---> mode Baca('r')
        teksFile = open(nmfile, 'r').read()

        # isikan data file pada komponen Text.
        self.txtFile.delete('1.0', END)
        self.txtFile.insert('1.0', teksFile)

        # menutup file
        teksFile.close()

    def tutup(self, event=None):
        self.induk.destroy()


if __name__ == '__main__':
    root = Tk()

    app = DemoOpenFile(root, ":: Demo Open File ::")

    root.mainloop()

input_str=""
with open("source.txt","r") as f:
    for line in f.readline():
        input_str=input_str+line

stop_words = set(stopwords.words('english'))
token=word_tokenize(input_str)

print(stop_words, file=open('stopword.txt', 'a'))
print('-- STOPWORDS --')
print(stop_words)
print('Jumlah Kata Stop Words : ',len(stop_words))
print('\n')

hasil=[
    i for i in token
        if not i in stop_words
]
print(hasil, file=open('tokenization.txt', 'a'))
print('-- TOKENIZATION --')
print(hasil)
print('Jumlah Kata Token : ',len(hasil))


