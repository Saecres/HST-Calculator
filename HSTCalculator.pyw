# Windowed Python file
# file.pyw

# Name: Kaitlin Penaranda
# Date: Novemeber 21st 2022
# App Name: HST Calculator
# Description: Show a dollar amount with addest HST

from tkinter import *       # Import the tkinter module
from tkinter.ttk import *    # replaces the w95 look with modern one

# Constants
HST = 1.13

# Define functions - below imports
def calculate_click():
    """Executed when the calculate button is clicked"""

    # Get the dollar amount from the input entry
    dollar_amount = input_entry.get()

    # Remove the $ from the dollar amount
    dollar_amount = dollar_amount.replace("$", "")

    # Try to convert to float
    try:
        dollar_amount = float(dollar_amount)
        numeric = True
    except:
        numeric = False

    # Error in case not numeric
    if not numeric or dollar_amount < 0:
        # Display something  in the output entry
        output_text.set("Error - input is not valid!")

    # It's not numeric
    else:
        # Add 13% to the dollar amount
        result = dollar_amount * HST

        # Display the result
        output_text.set(f"${result:.2f}")
        input_text.set(f"${dollar_amount:.2f}")

def clear_click():
    """Reset both input and otuput to $0.00"""
    output_text.set("$0.00")
    input_text.set("$0.00")

def key_handler(event:Event):
    """Handles key presses"""
    if event.keysym == "Return":
        calculate_click()
    elif event.keysym == "Escape":
        clear_click()

# Setup the window
window = Tk()                                       # create a window
window.title("HST Calculator - Kaitlin Penaranda")  # Change the title
window.iconbitmap("Moneysign.ico")                  # Change window's icon
window.resizable(width=False, height=False)         # not resizable
window.bind("<Key>", key_handler)                   # K is uppercase        

# Frame - holds all other widgets
frame = Frame()

# Create labels
input_label = Label(frame, text="Enter a dollar amount: ")
output_label = Label(frame, text="Amount + HST: ")

# Variables
input_text = Variable()
output_text = Variable()

# Set the default values
input_text.set("$0.00")
output_text.set("$0.00")

# Create entries
input_entry = Entry(frame, width=60, textvariable=input_text)
output_entry = Entry(frame, width=60, state="readonly", cursor="no", textvariable=output_text)

# Create the buttons
calculate_button = Button(frame, text="Calculate", command=calculate_click)
clear_button = Button(frame, text="Clear", command=clear_click)

# Place widgets in the window
frame.pack(padx=10, pady=10)            # 10px padding aroudn the frame
input_label.pack(anchor="w")            # Moves the text to the left
input_entry.pack(pady=(0,10))           # Padding at the bottom
output_label.pack(anchor="w")           # Moves the text to the left
output_entry.pack(pady=(0,10))          # Padding at the bottom
calculate_button.pack(side="right")     # Place on the right side
clear_button.pack(side="left")          # Place on the left side

# Make the window visible
window.mainloop()