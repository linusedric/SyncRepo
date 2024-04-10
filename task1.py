import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import threading
import time

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Alarm Clock")
        self.master.geometry("350x200")

        self.alarm_time_label = tk.Label(master, text="Set Alarm Time (HH:MM):")
        self.alarm_time_label.grid(row=0, column=0, padx=10, pady=10)

        self.alarm_entry = tk.Entry(master)
        self.alarm_entry.grid(row=0, column=1, padx=10, pady=10)

        self.date_label = tk.Label(master, text="Set Alarm Date (DD-MM-YYYY):")
        self.date_label.grid(row=1, column=0, padx=10, pady=10)

        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)

        self.set_button = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.cancel_button = tk.Button(master, text="Cancel Alarm", command=self.cancel_alarm)
        self.cancel_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.alarm_thread = None
        self.alarm_active = False

    def set_alarm(self):
        alarm_time_str = self.alarm_entry.get()
        alarm_date_str = self.date_entry.get()
        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M").time()
            alarm_date = datetime.strptime(alarm_date_str, "%d-%m-%Y").date()
            alarm_datetime = datetime.combine(alarm_date, alarm_time)
            current_datetime = datetime.now()

            if alarm_datetime < current_datetime:
                messagebox.showerror("Error", "Alarm time cannot be in the past.")
                return

            self.cancel_alarm()  # Cancel any existing alarm

            time_difference = (alarm_datetime - current_datetime).total_seconds()
            self.alarm_thread = threading.Timer(time_difference, self.activate_alarm)
            self.alarm_thread.start()

            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_datetime}")

        except ValueError:
            messagebox.showerror("Error", "Please enter time in HH:MM format and date in YYYY-MM-DD format.")

    def cancel_alarm(self):
        if self.alarm_thread and self.alarm_thread.is_alive():
            self.alarm_thread.cancel()
            messagebox.showinfo("Alarm Canceled", "Alarm has been canceled.")
            self.alarm_active = False

    def activate_alarm(self):
        self.alarm_active = True
        while self.alarm_active:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            messagebox.showinfo("Alarm", f"Wake up! It's {current_time}")
            time.sleep(60)  # Check every minute if the alarm should still be active

def main():
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
