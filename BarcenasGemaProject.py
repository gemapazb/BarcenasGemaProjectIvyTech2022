import tkinter as tk
#creating main window 


window= tk.Tk()
window.title("Locator 1.0")

#creating window for BHV & OV Locations

def open():
    win2 = tk.Toplevel()
    win2_label = tk.Label(win2, text="OV/BHV Available Locations ").pack()
    win2_label = tk.Label(win2, text=" Enter skids to Locate then click Next").pack()
    win2.geometry("300x300")

    skids= tk.Entry(win2, width=5)
    skids.pack()

    next = tk.Button(win2, text='Next',command=open3)
    next.pack(side=tk.TOP)




#creating window for BNC Locations
def open2():
    win3 = tk.Toplevel()
    win3_label = tk.Label(win3, text="BNC Available Locations").pack()
    win3_label = tk.Label(win3, text="Enter skids to locate Then click Next").pack()
    win3.geometry("300x300")

    skids_BNC= tk.Entry(win3, width=5)
    skids_BNC.pack()

    next = tk.Button(win3, text='Next',command=open3)
    next.pack(side=tk.TOP)

#window 3 will calculate the skid spaces needed depending on the staking instructions    
def open3():
    win4 = tk.Toplevel()
    win4_label = tk.Label(win4, text="How do you want to stack the skids?").pack()

    win4.geometry("300x300")

    S_S= tk.Button(win4,text='Single stack')
    S_S.pack(side=tk.TOP)

    D_S= tk.Button(win4,text='Double stack')
    D_S.pack(side=tk.TOP)

    T_S= tk.Button(win4,text='Triple stack')
    T_S.pack(side=tk.TOP)

#adjusting size of main Window
window.geometry("300x300")
#creatring 1st label 
label_1=tk.Label(text="Welcome to Locator 2022")
label_1.pack(padx=60, pady=60)
label_1.pack()

#framing the buttons/menu main window
frame= tk.Frame(window)
frame.pack(side=tk.TOP)
bottom_frame= tk.Frame(window)
bottom_frame.pack(side=tk.TOP)

#creating 1st button /main window
OV_BHVbtn= tk.Button(frame, text='Click to Locate OV/BHV', command=open)
OV_BHVbtn.pack(side=tk.TOP)

#creating 2nd Button/main window
BNC_btn = tk.Button(bottom_frame, text='CLick to locate BNC',command=open2)
BNC_btn.pack(side=tk.TOP)



window.mainloop()

