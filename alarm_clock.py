import tkinter as tk
from tkinter import messagebox
from playsound3 import playsound
import datetime

def set_alarm():
    alarm_hour = int(hour_entry.get())
    alarm_minute = int(minute_entry.get())
    alarm_am_pm = am_pm_var.get()

    if alarm_am_pm == "PM" and alarm_hour != 12:
        alarm_hour += 12
    elif alarm_am_pm == "AM" and alarm_hour == 12:
        alarm_hour = 0

    alarm_time = datetime.time(hour=alarm_hour, minute=alarm_minute)
    current_time = datetime.datetime.now().time()

    while current_time < alarm_time:
        current_time = datetime.datetime.now().time()

    playsound("Entry.mp3")
    messagebox.showinfo("Alarm", "Wake up!")

# GUI setup
root = tk.Tk()
root.title("Alarm Clock")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

hour_label = tk.Label(frame, text="Hour:")
hour_label.grid(row=0, column=0, padx=5, pady=5)
hour_entry = tk.Entry(frame, width=5)
hour_entry.grid(row=0, column=1, padx=5, pady=5)

minute_label = tk.Label(frame, text="Minute:")
minute_label.grid(row=0, column=2, padx=5, pady=5)
minute_entry = tk.Entry(frame, width=5)
minute_entry.grid(row=0, column=3, padx=5, pady=5)

am_pm_var = tk.StringVar()
am_pm_var.set("AM")  

am_radio = tk.Radiobutton(frame, text="AM", variable=am_pm_var, value="AM")
am_radio.grid(row=1, column=1, padx=5, pady=5)

pm_radio = tk.Radiobutton(frame, text="PM", variable=am_pm_var, value="PM")
pm_radio.grid(row=1, column=3, padx=5, pady=5)

set_button = tk.Button(frame, text="Set Alarm", command=set_alarm)
set_button.grid(row=2, columnspan=4, padx=5, pady=10)

root.mainloop()
