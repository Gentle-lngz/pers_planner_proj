#Planner Desktop App
import tkinter as tk

#initializing the window
window_ = tk.Tk()
window_.title("Weekly Planner")

#centering the window
window_width = 1300
window_height = 800
screen_width = window_.winfo_screenwidth()
screen_height = window_.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height /2)

window_.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window_.resizable(False, False)

#changing the default icon
#make icon and convert it to .ico format
window_.iconbitmap('')

#removing the border, manually design the border
window_.overrideredirect(True)

#widgets initializing
label = tk.Label(window_, text = "Hello!")
label.pack()
button = tk.Button(window_, text = "Click me!", command=print("Click"))
button.pack()

window_.mainloop()