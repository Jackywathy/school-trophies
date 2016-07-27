from tkinter import *
from tkinter.filedialog import *
import tkinter.ttk as ttk
from platform import system
import trophy

class Application:
    def __init__(self):
        self.arguments = set()
        self.tk = Tk()
        self.tk.bind("<Button-1>", self.callback)
        self.notebook = ttk.Notebook(self.tk)

        self.photo = PhotoImage(file='icon.ico')

        self.tk.wm_title("Trophy Creator \u0254\u20DD Forge")
        self.tk.iconbitmap('icon.ico')

        # windows only setup
        if system() == "Windows":
            self.setupWin()
        elif system() == "Darwin":
            self.setupMac()

        # spare
        self.csvFile = StringVar()
        self.output = StringVar()


        # create grafix
        self.create_frames()

        self.tk.update()



        self.tk.minsize(self.page1.winfo_width(), self.page1.winfo_height())
        mainloop()

    def create_frames(self):

        self.page1 = ttk.Frame()
        self.page2 = ttk.Frame()

        self.csvFrame = Frame(self.page1)
        self.csvText = Label(self.csvFrame, text="Enter the CSV file")
        self.csvBrowse = Button(self.csvFrame,command = self.getFile, text="Browse")
        self.csvIn = Entry(self.csvFrame)
        self.csvIn.bind("<Return>", self.getCsvText)

        self.csvSelected = Label(self.csvFrame, textvariable=self.csvFile)
        self.csvSeperator = ttk.Separator(self.page1, orient=HORIZONTAL)

        self.csvText.grid(row=0,columnspan=2)
        self.csvIn.grid(row=1,column=0)
        self.csvBrowse.grid(row=1,column=1)
        self.csvSelected.grid(row=2,columnspan=2)




        ####### Options-

        self.optionFrame = Frame(self.page1)
        self.optionLabel = Label(self.optionFrame, text="Standard Options")
        out_temp = BooleanVar()
        delete_temp = BooleanVar()
        self.outLine = Checkbutton(self.optionFrame,text='Outline', variable=out_temp)
        self.outLine.var = out_temp

        self.deletecsv = Checkbutton(self.optionFrame, text='Delete csv afterwards?', variable=delete_temp)
        self.deletecsv.var = delete_temp

        self.outLine.grid(row=0, column=0)
        self.deletecsv.grid(row=0,column=1)




        ### Output location & button

        self.outputFrame = Frame(self.page1)

        self.outputEntry = Entry(self.outputFrame,text="Enter Output Location: ")
        self.outputEntry.bind("<Return>", self.getOutputLocation)
        self.outputEntry.grid(row=0,column=0)

        self.outputBrowse = Button(self.outputFrame,command = self.getOutputFile, text="Browse")
        self.outputBrowse.grid(row=0,column=1)
        self.outputLabel = Label(self.outputFrame, textvariable=self.output)
        self.outputLabel.grid(row=1)

        # Page1 Frame Grids'
        self.csvFrame.grid(row=0,column=0,rowspan=2)
        self.csvSeperator.grid(row=0,column=1,rowspan=2)
        self.optionFrame.grid(row=0,column=2)
        self.outputFrame.grid(row=1,column=2)

        # Page2 Frame Grid's
        self.csvFrame.grid(row=0, column=0, rowspan=2)


        self.notebook.add(self.page1, text='Trophy', sticky=E+S)
        self.notebook.add(self.page2, text='Medal', sticky=E+S)
        self.notebook.pack(anchor=E)



    def getFile(self):
        self.csvFile.set(askopenfilename())

    def getCsvText(self, event):
        self.csvFile.set("../" + self.csvIn.get().split('/')[-1])



    def callback(self,event):
        print(self.outLine.var.get())

    def getOutputLocation(self,event):
        self.output.set("../" + self.outputEntry.get().split('/')[-1])

    def getOutputFile(self):
        self.output.set(askopenfilename())

    def createDXF(self, *args):
        trophy.main(list(self.arguments).append(self.csvFile.get()))

    def setupWin(self):
        self.tk.wm_iconbitmap(default='icon.ico')
    def setupMac(self):
        self.tk.wm_iconbitmap(bitmap='icon.ico')



Application()