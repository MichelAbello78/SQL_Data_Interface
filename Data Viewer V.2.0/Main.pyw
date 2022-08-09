from tkinter import *
from Interface import *

def main():
    root = Tk()
    root.wm_title("Data Viewer")
    app=ventana(root) 
    app.mainloop()

    

if __name__ == "__main__":
    main()