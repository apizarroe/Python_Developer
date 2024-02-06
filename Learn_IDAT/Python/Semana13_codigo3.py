import serial
import tkinter as tk
from datetime import datetime
from openpyxl import Workbook

puerto = serial.Serial('COM3',9600,timeout=2)

ventana = tk.Tk()
ventana.title("Lectura de LM35")
ventana.geometry("800x600")
ventana.configure(bg="beige")

workbook = Workbook()
sheet_counter = 1

label = tk.Label(ventana, text='', font=('Arial', 13), bg='beige', fg='blue')
label.grid(row=0, column=0, padx=50, pady=5, columnspan=2)

def create_new_sheet():
    global sheet_counter
    new_sheet = workbook.create_sheet(f'Sheet_{sheet_counter}')
    new_sheet.append(['Timestamp','Temperature'])
    sheet_counter += 1
    return new_sheet

current_sheet = create_new_sheet()
current_sheet_row = 2
current_temperatures = []

def update_gui():
    temperature_text = '\n'.join([f'Temperature {i+1}: {temp[1]} ºC - Time: {temp[0]}' for i, temp in enumerate(current_temperatures)])
    label.config(text=temperature_text)
    #text_widget.delete(1.0, tk.END)
    #text_widget.insert(tk.END, temperature_text)
    
def write_to_excel(timestamp,temperature):
    global current_sheet, current_sheet_row
    for timestamp, temperature in current_temperatures:
        current_sheet.append([timestamp,temperature])
        current_sheet_row += 1
    if current_sheet_row >52:
        current_sheet = create_new_sheet()
        current_sheet_row = 2
    current_temperatures.clear()
    workbook.save('temperature_log.xlsx')

def read_temperature():
    data = puerto.readline().decode('utf-8').strip()
    if data:
        temperature = float(data)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_temperatures.append((timestamp,temperature))
        if len(current_temperatures) >= 50:
            write_to_excel(timestamp,temperature)
        update_gui()
    ventana.after(1000,read_temperature)

#text_widget = tk.Text(ventana, font=('Arial',13), bg='beige', fg='blue', height=30, width=60)
#text_widget.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

read_temperature()

ventana.mainloop()