import tkinter as tk
import customtkinter as CTk
from tkinter import filedialog
from docx import Document
from reportlab.pdfgen import canvas

customtkinter = CTk.set_appearance_mode("Dark")

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word to PDF Converter")

        self.btn_word_to_pdf = CTk.CTkButton(root, text="Word to PDF", command=self.word_to_pdf)
        self.btn_word_to_pdf.pack(padx=10, pady=10)

        self.btn_pdf_to_word = CTk.CTkButton(root, text="PDF to Word", command=self.pdf_to_word)
        self.btn_pdf_to_word.pack(padx=10, pady=10)

    def word_to_pdf(self):
        word_file = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
        if word_file:
            pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if pdf_file:
                self.convert_pdf_to_word(pdf_file, word_file)
                self.textbox = CTk.CTkTextbox(master=self, width=40)
                self.textbox.grid(row=0, column=0, sticky="nsew")
                self.textbox.insert("Conversão Concluía")
    def pdf_to_word(self):
        pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_file:
            word_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
            if word_file:
                self.convert_pdf_to_word(pdf_file, word_file)
                self.textbox = CTk.CTkTextbox(master=self, width=40)
                self.textbox.grid(row=0, column=0, sticky="nsew")
                self.textbox.insert("Conversão Concluía")



    def convert_word_to_pdf(self, word_file, pdf_file):
        doc = Document(word_file)
        pdf_canvas = canvas.Canvas(pdf_file)
        for para in doc.paragraphs:
            pdf_canvas.drawString(10, 800, para.text)
            pdf_canvas.showPage()
        pdf_canvas.save()

    def convert_pdf_to_word(self, pdf_file, word_file):

        pass

if __name__ == "__main__":
    root = CTk.CTk()
    app = ConverterApp(root)
    root.mainloop()
