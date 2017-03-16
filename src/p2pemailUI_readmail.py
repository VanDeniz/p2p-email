# Haomin He, Yanting Liu, Zhibin Zhang
# CIS 433 Winter 2017

# Reading an incoming email
# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. 
# It is a thin object-oriented layer on top of Tcl/Tk.


from Tkinter import *
import textwrap

class readmail_tk(Tk):
	def __init__(self,parent):
		Tk.__init__(self, parent)
		self.parent = parent
		ScreenSizeX = self.winfo_screenwidth()
		ScreenSizeY = self.winfo_screenheight()
    		self.FrameSizeX  = 800
    		self.FrameSizeY  = 600
    		FramePosX  = (ScreenSizeX - self.FrameSizeX)/2
    		FramePosY  = (ScreenSizeY - self.FrameSizeY)/2
    		self.geometry("%sx%s+%s+%s" % (self.FrameSizeX,self.FrameSizeY,FramePosX,FramePosY))
    		self.resizable(width=False, height=False)
		
		self.fromemail = fromadd

		wrapped = textwrap.fill(content, 50)
		self.content = wrapped
		self.initialize()


	def initialize(self):
		self.grid()
		self.columnconfigure(0, weight=1)
    		self.rowconfigure(0, weight=1)

		self.lableonetext = StringVar()
		self.labelone = Label(self, 
		textvariable = self.lableonetext, 
		relief = RAISED,
		justify = LEFT,
		bg="dark blue",
		fg="white",
		font=("Helvetica", 16, "italic"))
		self.labelone.grid(row=0, column = 1, sticky=W+E+N+S)
		self.lableonetext.set("Reading an email from: \n"+self.fromemail)

		self.logo = PhotoImage(file="animations-mail.gif")
		#resize the image
		#self.logo = self.logo.zoom(25)
		#self.logo = self.logo.subsample(32)
		self.ltwo = Label(self, image=self.logo, bg="dark blue",)
		self.ltwo.grid(row=2, 
		column=1,
		sticky=W+E+N+S,
		padx=5,
		pady=5)

		self.lable3text = StringVar()
		self.label3 = Label(self, 
		textvariable = self.lable3text, 
		relief = RAISED,
		justify = LEFT,
		bg="dark blue",
		fg="white",
		font=("Helvetica", 16))
		self.label3.grid(row=0, column=0, rowspan=3, sticky=W+E+N+S)
		self.lable3text.set(self.content)
		
		

if __name__ == "__main__":
	#read email from this email address
	fromadd = "hahaha@123.com"
	#email content
	content = "Hello, hope you have a nice day!"
	app = readmail_tk(None)
	app.title('P2P Email-Reading')
	app.mainloop() 

	 
  



