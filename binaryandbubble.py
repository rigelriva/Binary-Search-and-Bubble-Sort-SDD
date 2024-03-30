import tkinter as tk
from tkinter import *
from tkinter import font

window = tk.Tk()

# Simple UI ------------------------------------------------------------------

style1 = font.Font(size=25)
style2 = font.Font(size=20)

# Pages
page1 = Frame(window, bg='white')
page2 = Frame(window, bg='white')
page3 = Frame(window, bg='white')

  
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")

# Titles
lb1 = Label(page1, text="Binary Search and Bubble Sort 😁", bg='white', font=style1)
lb1.pack(pady=50, padx=50)

lb2 = Label(page2, text="Binary Search", bg='white', font=style1)
lb2.pack(pady=20, padx=50)

lb3 = Label(page3, text="Bubble Sort", bg='white', font=style1)
lb3.pack(pady=20, padx=50)

# Navigation Buttons (Back and Forth Navigation)
btn1 = Button(page1, text="Binary Search", command=lambda: page2.tkraise(), font=style2)
btn1.pack()

btn2 = Button(page2, text="Back", command=lambda: page1.tkraise(), font=style2)

btn3 = Button(page1, text ="Bubble Sort", command=lambda: page3.tkraise(), font=style2)

btn4 = Button(page3, text="Back", command=lambda: page1.tkraise(), font=style2)

btn2.pack()
btn3.pack()
btn4.pack()


# Binary Search Page (Page 2) ------------------------------------------------------------------

simarray1 = [12, 19, 23, 32, 42, 54]
lb4 = Label(page2, text=(simarray1), bg='white', font=style1)  #Visually showing the array
lb4.pack(pady=20, padx=50)

input_var = StringVar()     #StringVar() acts as a mediator between the GUI and the Python code
midpoint_value = StringVar()

def binary_search():
    try:
        target = int(input_var.get())  # Get the input value as an integer
    except ValueError:
        answer1.config(text="Invalid input. Please enter a valid number.", fg="red") 
        return         # Handle invalid input (letters or special characters)

    target = int(input_var.get())  # Get the input value as an integer
    low_index = 0   # index 0 is the lowest value
    high_index = len(simarray1) - 1    # the length of the array-1 as the high (because array counting starts at 0)

    while low_index <= high_index:
        mid = low_index + (high_index - low_index) // 2     # finding the middle of array 
        midpoint_value.set(simarray1[mid])  # Update midpoint_value with the current midpoint
        if simarray1[mid] == target:
            answer1.config(text="Your number: {}, is at index {}".format(target, mid), fg="green") # Number found
            return
        elif target < simarray1[mid]:   #Changing the high or low depending on if the target is greater or lower
            high_index = mid - 1    
        else:
            low_index = mid + 1

    answer1.config(text="Number {} not found in the array.".format(target), fg="red")  # If not found

input_entry = Entry(page2, textvariable=input_var, font=('calibre', 10, 'normal'))
input_entry.pack()  # input box

answer1 = Label(page2, text="", bg='white')
answer1.pack(pady=20, padx=50)  # the text that will appear

sub_btn = Button(page2, text='Submit', command=binary_search)
sub_btn.pack()  # submit button, starts the binary search algorithm 

# Bubble Sort (Page3) ------------------------------------------------------------------

import random
from tkinter import *

simarray2 = [32, 42, 54, 12, 19, 23]

lb5 = Label(page3, text=simarray2, bg='white', font=style1)
lb5.pack()

def bubble():
    index_length = len(simarray2) - 1 
    sorted = False 

    while not sorted:   # Continue looping until the array is sorted  
        sorted = True  

        for i in range(0, index_length): 
            if simarray2[i] > simarray2[i+1]:   # Check if the current element is greater than the next element
                sorted = False 
                simarray2[i], simarray2[i+1] = simarray2[i+1], simarray2[i] # Swaps the elements
    lb5.config(text=simarray2)  # Update the label to display the sorted array

def shuffle():
    random.shuffle(simarray2)
    lb5.config(text=simarray2)  # Update the label to display the shuffled array

sub_btn2 = Button(page3, text='Sort', command=bubble, font=style2)  # Button that sorts the array
sub_btn2.pack()

btn5 = Button(page3, text="Shuffle", command=shuffle, font=style2)  # Button that shuffles the array
btn5.pack()

# --------------------------------------------------------------------
page1.tkraise()
window.geometry("550x450")
window.title("Binary Search and Bubble Sort")
window.config(background="white")


window.mainloop()