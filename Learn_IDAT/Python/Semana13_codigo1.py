import serial
from tkinter import *
from datetime import datetime
from openpyxl import Workbook

puerto = serial.Serial('COM3',9600,timeout=2)
workbook = Workbook()
sheet = workbook.active
sheet.append(['Timestamp','Temperature'])

ventana = Tk()
ventana.title("Lectura de LM35")
ventana.geometry("500x1000")
ventana.configure(bg="beige")

label = Label(ventana, text='', font=('Arial', 13), bg='beige', fg='blue')
label.grid(row=0, column=0, padx=50, pady=5, columnspan=2)

last_10_temperatures = []

def read_temperature():
    data = puerto.readline().decode('utf-8').strip()
    if data:
        temperature = float(data)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_10_temperatures.append((timestamp, temperature))
        if len(last_10_temperatures) > 10:
            last_10_temperatures.pop(0)
        update_gui()
        log_to_excel(timestamp,temperature)
    ventana.after(1000, read_temperature)

def update_gui():
    temperature_text = '\n'.join([f'Temperature {i+1}: {temp[1]} ºC - Time: {temp[0]}' for i, temp in enumerate(last_10_temperatures)])
    label.config(text=temperature_text)
    
def log_to_excel(timestamp,temperature):
    sheet.append([timestamp,temperature])
    workbook.save('temp.xlsx')
    
read_temperature()

ventana.mainloop()