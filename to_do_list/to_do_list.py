#let's import tkinter module to create GUI'S 
import tkinter as tk

#lets use dir() function to see whats inside the tkinter module 
#print(dir(tk))

# let's create an empty/ root gui
root = tk.Tk()

#lets define functions
def add():
    print('Adding task to the list')

    #lets get the task written inside the entry widget
    data = entry.get() 

    #lets check first if data is empty or not
    if data:

        #shift that text to listbox
        #arguments : index number (0 --> first element), data you want to put
        #task_list.insert(0, data)
        task_list.insert(tk.END, data)

        #lets clean the entry widget
        entry.delete(0, tk.END)

def delete():
    print('Deleting task from the list')

    #lets delete the active element
    task_list.delete(tk.ACTIVE)

# lets define the height and width of the gui
root.geometry('400x400') 
#stop resizing
root.resizable(width=False,height=False)

#lets change the title
root.title('To_Do_List')

#lets add entry widget
entry = tk.Entry(root)
entry.pack(padx=30, pady=10, fill='x')

#lets add a button --> dd task
add_button = tk.Button(root, text='Add Task', width=20, bg='grey', fg='white', command=add)
add_button.pack()

#lets add the task list
task_list = tk.Listbox(root)
task_list.pack(fill='x', padx=20, pady =10)

#lets add delete button
delete_button = tk.Button(root, text='Delete Task', width=20, command=delete)
delete_button.pack()

# lets call the mainloop function
root.mainloop()