'''
--------------------------------
Name: Dallas Fraser
Date: 09/17/2013
Purpose: The interface
---------------------------------
'''
from tkinter import *
import functions
import pprint

class Application(Frame):
    def process(self):
        info = self.data.get()
        array = self.helper.make_array(info)
        self.pprint.pprint(array)
        ave = "Average:" + str(self.helper.find_average(array)) + "\n"
        self.output.insert(END, ave)
        mad = "Mean Absolute Deviation:" + str(self.helper.find_mad(array)) +"\n"
        self.output.insert(END, mad)
        st_dev = "Standard Deviation:" + str(self.helper.find_standard_deviation(array))
        self.output.insert(END, st_dev)

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Get Input"
        self.hi_there["command"] = self.process

        self.hi_there.pack({"side": "left"})
        self.data = Entry(self)
        self.data.pack({"side":"left"})
        self.output = Text(self)
        self.output.pack({"side":"left"})
        
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.helper = functions.helper_functions()
        self.pprint = pprint.PrettyPrinter(indent=4)
        
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
    