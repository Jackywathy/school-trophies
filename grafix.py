from tkinter import *
from tkinter.filedialog import *
import tkinter.ttk as ttk
import tkinter.messagebox as message
from platform import system
import trophy
import string
import sys
counter = 0
alpha = string.ascii_letters * 10

LIMIT = 28 # limit of string

WINDOWS = 'win'
ELSE = 'lin'



class Application:
    def quit(self, *args):
        self.tk.quit()
        sys.exit()
    def fill_file(self, *args):
        global counter; counter += 1
        self.csvIn.delete(0, END)
        self.csvIn.insert(0,alpha[:counter])
        sys.stdout.write(str(counter) + '\n')
        sys.stdout.flush()

    def __init__(self):
        self.arguments = set()
        self.tk = Tk()
        self.tk.bind("<Escape>", self.quit)

        self.notebookFrame = Frame(self.tk, width=100, padx=60)
        self.notebook = ttk.Notebook(self.notebookFrame)


        self.tk.wm_title("Trophy Creator \u0254\u20DD Forge")
        self.tk.iconbitmap('icon.ico')

        # windows only setup
        if system() == "Windows":
            self.setupWin()
            self.os = WINDOWS
        elif system() == "Darwin":
            self.setupMac()
            self.os = ELSE

        # spare
        self.csvFile = StringVar()
        self.outputFile = StringVar()


        # create grafix
        self.create_frames()

        self.tk.update()



        self.tk.minsize(self.page1.winfo_width(), self.page1.winfo_height())
        mainloop()

    def create_frames(self):

        # frames
        self.page1 = ttk.Frame(self.tk)
        self.page2 = ttk.Frame(self.tk)
        self.csvAndOK = Frame(self.tk)
        self.csvFrame = LabelFrame(self.csvAndOK,text="CSV In", width=100, height=100)
        self.outputFrame = LabelFrame(self.tk, text='Output', width=100)
        self.optionFrame = Frame(self.page1, width=100)

        self.csvFrame.grid(row=0,column=0,columnspan=3)


        self.okButton = Button(self.csvAndOK, text="OK",command=self.getOutputFile)
        self.okButton.grid(row=0,column=4)
        # csv frame- tis should be but on the very top, above the notebook
        self.csvText = Label(self.csvFrame, text="File Path", anchor=W)
        self.csvBrowse = Button(self.csvFrame,command = self.getCsvFile, text="Browse")
        self.csvIn = Entry(self.csvFrame, width=35)
        self.csvIn.bind("<Return>", self.getCsvText)

        self.csvText.grid(row=0,column=0)
        self.csvIn.grid(row=0,column=1,columnspan=2)
        self.csvBrowse.grid(row=0,column=4)




        ####### Options-
        out_temp = BooleanVar()
        delete_temp = BooleanVar()
        self.outLine = Checkbutton(self.optionFrame,text='Outline', variable=out_temp)
        self.outLine.var = out_temp

        self.deletecsv = Checkbutton(self.optionFrame, text='Delete csv afterwards?', variable=delete_temp)
        self.deletecsv.var = delete_temp

        self.outLine.grid(row=0, column=0, padx=10,pady=5)
        self.deletecsv.grid(row=0,column=1, padx=10,pady=5)




        # Page1 Frame Grids'
        self.optionFrame.grid(row=0,column=2)



        # Page2 Frame Grid's

        self.notebook.pack(fill=BOTH,expand=1)

        self.notebook.add(self.page1, text='Trophy', sticky=E+S)
        self.notebook.add(self.page2, text='Medal', sticky=E+S)
        # csv INPUT frame
        self.csvAndOK.pack(fill=BOTH,expand=1,padx=10,pady=5)
        self.notebookFrame.pack(fill=BOTH,expand=1,padx=10,pady=5,anchor=W)
        self.outputFrame.pack(fill=BOTH,expand=1,padx=10,pady=5)

    def getCsvFile(self):
        self.csvFile.set(askopenfilename())
        x = self.csvFile.get()
        try:
            if not ((x[-4]=='.') and (x[-3]=='c' or x[-3]=='C') and (x[-2]=='s' or x[-2]=='S') and (x[-1]=='v' or x[-1]=='V')):
                message.showwarning(title='spam',message='The file does not end in .csv')

            else:
                self.csvIn.delete(0,END)
                self.csvIn.insert(0,self.csvFile.get())
        except IndexError:
            message.showwarning(title='spam',message='The file does not end in .csv')


    def getCsvText(self, event):
        x = os.path.expanduser(self.csvIn.get())
        if not os.path.exists(x):
            message.showwarning(title='spam',message='The file does not exist')
            # test for existance
        try: # test for csv fileness
            if not ((x[-4]=='.') and (x[-3]=='c' or x[-3]=='C') and (x[-2]=='s' or x[-2]=='S') and (x[-1]=='v' or x[-1]=='V')):
                message.showwarning(title='spam',message='The file does not end in .csv')
            else:
                self.csvFile.set(x)

        except IndexError:
            message.showwarning(title='spam',message='The file does not end in .csv')


    def getOutputFile(self, *args):
        if self.csvFile.get():
            self.outputFile = asksaveasfilename(defaultextension='.dxf')
            templist = ['popped'] + list(self.arguments) + ['--filename', 'lol filename doesnt work yet' + [self.csvFile.get()]
            
        else:
            message.showwarning(title='spam', message='Select a .csv file first!')


    def setupWin(self):
        self.tk.wm_iconbitmap(default='icon.ico')

    def setupMac(self):
        self.tk.wm_iconbitmap(bitmap='icon.ico')




Application()
