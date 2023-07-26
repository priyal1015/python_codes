#importing module
import tkinter as tk

#creating an empty gui
root = tk.Tk() 

#function
def test(event):
   print('Button is pressed')

#properties
   root.geometry('200x200')

#adding 2 buttons
button_1 = tk.Button(root, text='1', width=5, height=2)


#right click event --> 'Button-3'
button_1.bind('<Button-3>', test)