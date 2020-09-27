import time
import datetime as dt
import tkinter
from tkinter import messagebox
import winsound

## Main script here:
t_now = dt.datetime.now()           # Current time 
t_pom = 15                          # Pomodoro time               
t_delta = dt.timedelta(0, t_pom)    # Time delta in mins          
t_fut = t_now + t_delta             # Future time, ending pomodoro 
Ldelta_sec = 5                      # Long Break time
Sdelta_sec = 1                      # Short Break time
condelta_sec = 1                    # decision time
t_con = t_now + dt.timedelta(0, t_pom+ condelta_sec) #decision upper limit
#t_fin = t_now + dt.timedelta(0, t_pom+delta_sec) # Final time (w/ 5 mins breaks)
total_pomodoros = 0

# GUI set pomodoro
root = tkinter.Tk() #Starts a new Window
root.withdraw() # Method hides the main window, allowing you to use only the message box

# Show alert message - Started
messagebox.showinfo("Pomodoro Started!", "\nIt is now" + t_now.strftime("%H:%M") + " hrs. \nTimer set for 25mins.")
# Displays a simple window on the screen with information

while True: 
    # Pomodoro time
    if t_now < t_fut:
        print('pomodoro')

    elif t_fut <= t_now <= t_con:
        decision = messagebox.askyesno("Pomodoro Finished!", "Did you finish more than 4 task?")
        
        if decision == True:
            t_fin = t_now + dt.timedelta(0, t_pom + Ldelta_sec) 
        else:
            t_fin = t_now + dt.timedelta(0, t_pom + Sdelta_sec)

    elif t_fut <= t_now <= t_fin:
        print('Break time!')

    #Pomodoro and break finished. Check if ready for another pomodoo!
    else:
        print('Third tnow > tfut - Finished')
        # Ring a bell (with print('\a') to alert of end of program.
        print('\a')
        # Annoy!
        for i in range(10):
            winsound.Beep((i+100), 500)    
        usr_ans = messagebox.askyesno("Pomodoro Finished!","Would you like to start another pomodoro?")
        #usr_ans = input("Timer has finished. \nWould you like to start another pomodoro? \nY/N:  ")
        total_pomodoros += 1
        if usr_ans == True:
            # user wants another pomodoro! Update values to indicate new timeset.
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0,t_pom)
            t_con = t_now + dt.timedelta(0, t_pom + condelta_sec*2)
            continue
        
        elif usr_ans == False:
            print(f'Pomodoro timer complete! \nYou have completed {total_pomodoros} pomodoros today.')
            # unlock the websites
            # Show a final message)
            messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+timenow+
            "\nYou completed "+ str(total_pomodoros) +" pomodoros today!")
            break

    # check every 3 seconds and update current time    
    time.sleep(2)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")