#importing tkinter
import tkinter as tk

#importing ttk module from tkinter as it has the combobox class
from tkinter import ttk

#lets get teh language list in this file
import backend

import googletrans
language_translator = googletrans.Translator()

#importing the os module
import os

#import gtts and playsound module
import gtts
import playsound

#lets create do_translation function
def do_translation():

   #step 1 --> get the source and target language from the combobox
    source_lang = source_cb.get()
    target_lang = target_cb.get()
    #print(source_lang, target_lang)

    #step 2 --> lets fetch what is written in the text box 
    user_message = input_text.get(1.0, tk.END)
    #print(user_message)

    #step 3 --> lets do the translation
    output = language_translator.translate(text=user_message ,src=source_lang ,dest=target_lang)
    translated_text = output.text 

    #step 4 --> Put it on the label
    output_label.config(text = translated_text) 

#clear text function
def clear_text():

    #clear the text box and label
    output_label.config(text = '')
    input_text.delete(1.0, tk.END)

#lets create speak text function
def speak_text():

    #lets get the text
    text_on_label = output_label.cget('text')
    
    #lets get the target language abbreviation 
    target_language = target_cb.get()

    #lets check the index of target language in language list
    index_of_target_language = languages.index(target_language)
    
    #lets get the abbreviation
    abbrev = abbreviations[index_of_target_language] 

    #lets create the tts engine
    tts_engine = gtts.gTTS(text = text_on_label, lang = abbrev)

    #lets save the audio
    if os.path.isfile('result.mp3'): 

        #lets remove it
        os.remove('result.mp3')
        
    #saving the file     
    tts_engine.save('result.mp3')
    
    #lets play it
    playsound.playsound('result.mp3')
   
#lets create the language list
languages = backend.get_languages()
abbreviations = backend.get_abbreviations()

#creating root gui
root = tk.Tk()

#properties  of root gui
root.geometry('700x400')
root.resizable(width=False, height=False)
root.title('Language Translator')
root.config(bg='#1e90ff')

#universal variables
py = 10
px = 30
bg_color = '#3DED97' 
fg_color = '#354A21'
button_font = 'Helvetica'
button_font_size = 12

#adding widgets
welcome_label = tk.Label(root, text='LANGUAGE TRANSLATOR',bg='#99edc3',fg='#012a4a', font=('Arial', 30))
welcome_label.pack(pady=20)

#creating a frame to arrange my widget in grid layout
frame = tk.Frame(root, bg='#1e90ff', width=500, height=100)
frame.pack(padx=10, pady=10, fill='both', expand=True)

#source and target language labels
source_label = tk.Label(frame, text='Source Language', bg='#99edc3', fg='#012a4a', font=('Comic Sans MS', 20))
target_label = tk.Label(frame, text='Target Language', bg='#99edc3', fg='#012a4a', font=('Comic Sans MS', 20))
source_label.grid(row=0, column=0, padx=px, pady=py)
target_label.grid(row=0, column=2, padx=px, pady=py) 

# add comboboxes
source_cb = ttk.Combobox(frame, values=languages, width=30)
#setting the default language
source_cb.current(21)
target_cb = ttk.Combobox(frame, values=languages, width=30)
target_cb.current(38)
source_cb.grid(row=1, column=0, padx=px, pady=py)
target_cb.grid(row=1, column=2, padx=px, pady=py)

#adding row 2 elements --> Input text area, clear button, output label
input_text = tk.Text(frame, width=25, height=5)
translate_button = tk.Button(frame, text='Translate', bg='#1560bd', fg='white', font=(button_font, 15), command=do_translation)
output_label = tk.Label(frame,  text='No Translations Yet!', bg='white', width=30, height=5)
input_text.grid(row=2, column=0, padx=px, pady=py)
translate_button.grid(row=2, column=1, padx=px, pady=py)
output_label.grid(row=2, column=2, padx=px, pady=py)

#adding row 3 elements --> voice button, clear and speak
voice_button = tk.Button(frame, text= 'Say Something', bg='#1560bd', fg='white', font=(button_font, button_font_size))
clear_button = tk.Button(frame, text= 'Clear', bg='#1560bd', fg='white', font=(button_font, button_font_size), command=clear_text)
speak_button = tk.Button(frame, text= 'Speak Translation', bg='#1560bd', fg='white', font=(button_font, button_font_size), command =speak_text)
voice_button.grid(row=3, column=0, padx=px, pady=py)
clear_button.grid(row=3, column=1, padx=px, pady=py)
speak_button.grid(row=3, column=2, padx=px, pady=py)

#for continuous display
root.mainloop()
