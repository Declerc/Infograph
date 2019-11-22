from tkinter import *

def main():
  root=Tk()
  root.title("Test Numbers")
  root.geometry("550x350")
  def d(event):
      print(event.width,event.height)
  root.bind('<Configure>',d)
  root.mainloop()

if __name__=="__main__":
  main()