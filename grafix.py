from tkinter import *
from tkinter.filedialog import *
from platform import system
import trophy


class Application:
    def __init__(self):
        self.arguments = set()
        self.root = Tk()
        self.root.bind("<Button-1>", self.callback)

        self.root.wm_title("Trophy Creator \u0254\u20DD Forge")
        self.root.iconbitmap('ico.ico')

        # windows only setup
        if system() == "Windows"or 1:
            self.setupWin()

        # spare
        self.csvFile = StringVar()
        self.output = StringVar()


        # create grafix
        self.create_frames()

        self.root.update()


        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        mainloop()

    def create_frames(self):
        self.csvFrame = Frame(self.root)


        self.csvText = Label(self.csvFrame, text="Enter the CSV file")

        self.csvBrowse = Button(self.csvFrame,command = self.getFile, text="Browse")

        self.csvIn = Entry(self.csvFrame)
        self.csvIn.bind("<Return>", self.getCsvText)

        self.csvSelected = Label(self.csvText.pack(), textvariable=self.csvFile)


        self.csvText.pack()
        self.csvBrowse.pack()
        self.csvIn.pack()
        self.csvSelected.pack()

        ####### Options-

        self.optionFrame = Frame(self.root)
        self.optionLabel = Label(self.optionFrame, text="Standard Options")
        out_temp = IntVar()
        delete_temp = IntVar()
        self.outLine = Checkbutton(self.optionFrame,text='Outline', variable=out_temp)
        self.outLine.var = out_temp

        self.deletecsv = Checkbutton(self.optionFrame, text='Delete csv afterwards?', variable=delete_temp)
        self.deletecsv.var = delete_temp

        self.outLine.grid(row=0, column=0)
        self.deletecsv.grid(row=0,column=1)




        ### Output location & button

        self.outputFrame = Frame()

        self.outputEntry = Entry(self.outputFrame,text="Enter Output Location: ")
        self.outputEntry.bind("<Return>", self.getOutputLocation)
        self.outputEntry.grid(row=0,column=0)

        self.outputBrowse = Button(self.outputFrame,command = self.getOutputFile, text="Browse")
        self.outputBrowse.grid(row=0,column=1)
        self.outputLabel = Label(self.outputFrame, textvariable=self.output)
        self.outputLabel.grid(row=1)



        self.csvFrame.pack()
        self.csvFrame.pack()
        self.optionFrame.pack()





    def getFile(self):
        self.csvFile.set(askopenfilename())

    def getCsvText(self, event):
        self.csvFile.set(self.csvIn.get())

    def showAdvancedPressed(self):
        if self.showAdvanced:
            self.showAdvanced = False
            self.showAdvancedButton.grid_forget()
            self.advancedFrame.grid(row = 10, columnspan=2)

        else:
            self.showAdvanced = True
            self.showAdvancedButton.grid(row=10, columnspan=2)
            self.advancedFrame.grid_forget()

    def callback(self,event):
        print(self.outLine.var.get())

    def getOutputLocation(self,event):
        self.output.set(self.outputEntry.get())

    def getOutputFile(self):
        self.output.set(askopenfilename())

    def createDXF(self, *args):
        trophy.main(list(self.arguments).append(self.csvFile.get()))

    def setupWin(self):
        self.root.wm_iconbitmap('ico.ico')


Application()