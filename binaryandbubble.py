import tkinter as tk
from tkinter import *
from tkinter import font

window = tk.Tk()


# Simple UI and GUI ------------------------------------------------------------------


style1 = font.Font(size=25)
style2 = font.Font(size=20)
style3 = font.Font(size=15)

# Pages
page1 = Frame(window, bg='white')
page2 = Frame(window, bg='white')
  
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")

# Titles
lb1 = Label(page1, text="Binary Search and Bubble Sort 😁", bg='white', font=style1)  # title
lb1.pack(pady=50, padx=50)

lb2 = Label(page2, text="You ready to search and sort?", bg='white', font=style1)  # title
lb2.pack(pady=20, padx=50)


# Navigation Buttons (Back and Forth Navigation)
btn1 = Button(page1, text="Start", command=lambda: page2.tkraise(), font=style2)  # takes user to binary search page
btn1.pack()

btn2 = Button(page2, text="Main Menu", command=lambda: page1.tkraise(), font=style3)  # takes user back to home screen
btn2.pack()


# Algorithm Page ------------------------------------------------------------------


import random  # This will be used for the 'random.shuffle' part of the algorithm which lets the shuffle feature work
from tkinter import *


simarray1 = [42, 32, 23, 12, 19, 54]  # array itself, will initially be unsorted, numbers can be modified


arraytext = Label(page2, text=(simarray1), bg='white', font=style1)  # Visually showing the array
arraytext.pack(pady=20, padx=50)


input_var = StringVar()  # StringVar() acts as a mediator between the GUI and the Python code
midpoint_value = StringVar()



def binary_search():    # Binary Search Aglorithm
    try:
        target = int(input_var.get())  # Get the input value as an integer
    except ValueError:
        answer1.config(text="Invalid input. Please enter a valid number.", fg="red")
        return  # Tests to see if it's an invalid input (letters or special characters)

    target = int(input_var.get())  # Get the input value as an integer
    
    if not is_sorted(simarray1):
        answer1.config(text="Array is not sorted. Please sort the array first.", fg="red")
        return  # if the array isn't sorted, this red text will appear

    low_index = 0  # index 0 is the lowest value (12)
    high_index = len(simarray1) - 1  # the length of the array-1 as the high (because array counting starts at 0)

    while low_index <= high_index:  # sees if the search range is valid during the loop
        mid = low_index + (high_index - low_index) // 2  # finding the middle of array
        midpoint_value.set(simarray1[mid])  # Update midpoint_value with the current midpoint
        if simarray1[mid] == target:
            answer1.config(text="Your number: {}, is at index {}".format(target, mid), fg="green")  # Number found
            return
        elif target < simarray1[mid]:  # Changing the high or low depending on if the target is greater or lower
            high_index = mid - 1  # target is lower than mid value so the mid becomes new high
        else:
            low_index = mid + 1  # target is higher than mid, mid becomes the new low

    answer1.config(text="The number {} is not found in the array.".format(target), fg="red")  # If not found



input_entry = Entry(page2, textvariable=input_var, font=('calibre', 10, 'normal'))
input_entry.pack()  # input box

answer1 = Label(page2, text="", bg='white')
answer1.pack(pady=20, padx=50)  # the text that will appear, invalid message or says where the number is

sub_btn = Button(page2, text='Submit', command=binary_search, font=style3)
sub_btn.pack()  # submit button, starts the binary search algorithm


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
# Checks if an array is sorted in ascending order.


# Bubble Sort --------------------------------------------------------------


def bubble():  # bubble sort algorithm
    index_length = len(simarray1) - 1 
    sorted = False   # Flag to track whether the array is sorted or not

    while not sorted:   # Continue looping until the array is sorted  
        sorted = True  

        for i in range(0, index_length): 
            if simarray1[i] > simarray1[i+1]:   # Check if the current element is greater than the next element
                sorted = False 
                simarray1[i], simarray1[i+1] = simarray1[i+1], simarray1[i] # Swaps the elements
    arraytext.config(text=simarray1)  # Update the label to display the sorted array


sub_btn2 = Button(page2, text='Bubble Sort', command=bubble, font=style2)  # Button that sorts the array, sends a command to start def bubble()
sub_btn2.pack()

def shuffle():  # shuffling the array algorithm
    random.shuffle(simarray1)
    arraytext.config(text=simarray1)  # Update the label to display the shuffled array


btn5 = Button(page2, text="Shuffle", command=shuffle, font=style2)  # Button that shuffles the array, sends a command to start def shuffle()
btn5.pack()


# ----------------------------------------------------------------------------

# creation of the window when pressing run
page1.tkraise()
window.geometry("550x450")
window.title("Binary Search and Bubble Sort")
window.config(background="white")


window.mainloop()
