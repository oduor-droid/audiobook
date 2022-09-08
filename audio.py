import PyPDF2
import pyttsx3

bk = input("select the book you wish to convert into an audio book:  ")

with open(bk, 'rb') as book:
    full_text = " "
    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 140)
    audio_reader.setProperty("voice", 'english_rp+f3') # setting female voice

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content

        audio_reader.say(content)  # to listen to your audiobook live same as streaming
        # audio_reader.save_to_file(file_text, "audio.wav") #  to save your audiobook for later
        audio_reader.runAndWait()
