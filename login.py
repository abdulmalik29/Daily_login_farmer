from tkinter import *
import schedule
import time
import os


def start_game():
    os.startfile("steam://rungameid/200210")

def close():
    global window
    window.destroy()


def reminder():
    global window, Canvas
    window = Tk()                               #creat the reminder window
    window.title("Reminder")
    window.resizable(False, False)
    window.configure(background='white')

    screen_width = window.winfo_screenwidth()
    screen_hight = window.winfo_screenheight()
    senter_x = (screen_width/2) - (250/2)
    senter_y = (screen_hight/2) - (250/2)           # to senter the window
    window.geometry('%dx%d+%d+%d' % (350, 100, senter_x, senter_y))

    canvas = Canvas(window, bg= "white")
    canvas.place(relwidth= 1,relheight=1, relx= 0, rely=0)
    reminder_text = canvas.create_text(170,50, fill="black", font="Arial 20 italic bold", text="Daily loging? ")
    window.update()

    # window.after(4000)
    window.mainloop()



# schedule.every().day.at("12:28").do(start_game)
schedule.every().day.at("07:24").do(start_game)
#
# loop = True
#
while True:
    schedule.run_pending()
    time.sleep(1)
# reminder()
