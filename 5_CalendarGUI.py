from tkinter import *

import calendar

def Make_Cal():
    window=Tk()
    window.config(background="grey")
    window.title("Complete Calendar")
    window.geometry("1000x1000")

    get_year=int(year_entry.get())
    window_content=calendar.calendar(get_year)

    year_cal=Label(window, text=window_content, font=("Arial", 10,"bold"))
    year_cal.grid(row=5, column=1)

    window.mainloop()


if __name__ == '__main__':
    
    root= Tk()
    root.config(background="grey")
    root.title("GUI Calendar")

    # Designs the window size
    root.geometry("300x300")

    # Gives name of application 
    name=Label(root, text="CALENDAR", font=("Times New Roman", 15, "bold"))
    name.grid(row='1', column=125)

    # label for users to identify text box
    year_name=Label(root, text="Enter the Date", fg="red", font=("Times New Roman", 10, "bold"))
    year_name.grid(row='20', column=125)

    # text box to enter year value
    year_entry=Entry(root, bg='white', font=("Arial", 10, "italic", "bold"))
    year_entry.grid(row=30, column=125)

    GUI_button= Button(root, text="Show Calendar!",fg="blue", font=("Arial", 10,"bold"), command=Make_Cal()) #Avoid () after function call, program throws an error
    GUI_button.grid(row=50, column=125)

    root.mainloop()
