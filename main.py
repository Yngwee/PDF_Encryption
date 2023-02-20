import tkinter.filedialog
import tkinter
from PyPDF2 import PdfWriter, PdfReader


def choose_file():
    filetypes = (("PDF-файлы", "*.pdf"),)
    filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        return filename


pdfwriter = PdfWriter()
try:
    filename = choose_file()
    pdf = PdfReader(filename)
    for page in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page])
    password = input('Введите пароль для защиты файла: ')
    pdfwriter.encrypt(password)

    with open('protected.pdf', 'wb') as file:
        pdfwriter.write(file)

    print('Шифрование успешно завершено!')
except:
    print('Файл не найден')
