from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pathlib
from odf import text, teletype
from odf.opendocument import load
import pyttsx3
import PyPDF2
import docx2txt

root = Tk()
root.geometry('300x150')
root.resizable(False, False)
root.title('Kutxa Audio Library')


def process_audio():
    """Prompting user for file to be converted to audio"""
    file_types = [('All files', '*'), ('PDF files', '.pdf'), ('Text files', '.txt'), ('Open files', '.odt'),
                  ('Office files', '.docx')]
    bk = filedialog.askopenfilename(initialdir='/home/oduor/Desktop', filetypes=file_types)
    path = pathlib.Path(bk)  # handles file path

    """Handling Files"""
    if path.suffix == '.pdf':
        with open(bk, 'rb') as book:
            full_text = " "
            reader = PyPDF2.PdfFileReader(book)

            audio_reader = pyttsx3.init()
            audio_reader.setProperty("rate", 140)
            audio_reader.setProperty("voice", 'english_rp+f3')  # setting female voice

            for page in range(reader.numPages):
                next_page = reader.getPage(page)
                content = next_page.extractText()
                full_text += content

                audio_reader.say(content)  # to listen to your audiobook live same as streaming
                # audio_reader.save_to_file(file_text, "audio.wav") #  to save your audiobook for later
                audio_reader.runAndWait()

    elif path.suffix == '.odt':
        document = load(bk)
        contents = document.getElementsByType(text.P)
        for cont in contents:
            teletype.extractText(cont)

            audio_reader = pyttsx3.init()
            audio_reader.setProperty("rate", 140)
            audio_reader.setProperty("voice", 'english_rp+f3')  # setting female voice

            audio_reader.say(cont)

    elif path.suffix == '.txt':
        with open(bk) as f:
            contents = f.readlines()
            for content in contents:
                audio_reader = pyttsx3.init()
                audio_reader.setProperty("rate", 140)
                audio_reader.setProperty("voice", 'english_rp+f3')

                audio_reader.say(content)
                audio_reader.runAndWait()
    elif path.suffix == '.docx':
        docx = docx2txt.process(bk)
        audio_reader = pyttsx3.init()
        audio_reader.setProperty("rate", 140)
        audio_reader.setProperty("voice", 'english_rp+f3')  # setting female voice

        audio_reader.say(docx)
        audio_reader.runAndWait()


lb = ttk.Label(root, text='KUTXA AUDIO', font=('Elephant', 15))
lb.pack()
lb1 = ttk.Label(root, text="'Listen to your Documents speak'", font=('Terminal', 8))
lb1.pack()
lb2 = ttk.Label(root, text="Choose your document: ", font=('Terminal', 10))
lb2.place(x=20, y=70)

btn1 = ttk.Button(root, text='FILES', command=process_audio)
btn1.place(x=200, y=65)

root.mainloop()
