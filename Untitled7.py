#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_label.config(text=f"Fahrenheit: {fahrenheit:.2f}")
    except ValueError:
        fahrenheit_label.config(text="Invalid input")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_label.config(text=f"Celsius: {celsius:.2f}")
    except ValueError:
        celsius_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and configure Celsius frame
celsius_frame = tk.Frame(root)
celsius_frame.pack(side=tk.LEFT, padx=10, pady=10)
celsius_label = tk.Label(celsius_frame, text="Enter Celsius:", font=("Arial", 12))
celsius_label.pack()
celsius_entry = tk.Entry(celsius_frame, font=("Arial", 12))
celsius_entry.pack()
convert_celsius_button = tk.Button(celsius_frame, text="Convert", command=celsius_to_fahrenheit, font=("Arial", 12))
convert_celsius_button.pack()

# Create and configure Fahrenheit frame
fahrenheit_frame = tk.Frame(root)
fahrenheit_frame.pack(side=tk.LEFT, padx=10, pady=10)
fahrenheit_label = tk.Label(fahrenheit_frame, text="Enter Fahrenheit:", font=("Arial", 12))
fahrenheit_label.pack()
fahrenheit_entry = tk.Entry(fahrenheit_frame, font=("Arial", 12))
fahrenheit_entry.pack()
convert_fahrenheit_button = tk.Button(fahrenheit_frame, text="Convert", command=fahrenheit_to_celsius, font=("Arial", 12))
convert_fahrenheit_button.pack()

# Start the application
root.mainloop()


# In[ ]:




