# Haomin He, Yanting Liu, Zhibin Zhang
# CIS 433 Winter 2017

# Sending an outgoing email
# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. 
# It is a thin object-oriented layer on top of Tcl/Tk.


from Tkinter import *
import textwrap
import tkMessageBox
import ScrolledText

class sendmail_tk(Tk):
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
		self.labelone.grid(row=0, column=1, sticky=W+E+N+S)
		self.lableonetext.set("Sending an email to:")

		self.e1 = Entry(self, bd = 3,
		bg="light blue",
		font=("Helvetica", 16))
		self.e1.grid(row=1, column=1, sticky=W+E+N+S)

		Button(self, text='Send', command=self.sendthisemail, font=("Helvetica", 16)).grid(row=2, column=1, sticky=W+E+N+S)
		
		
		self.textfield = ScrolledText.ScrolledText(self, wrap=WORD, bd = 3,
		bg="light blue",
		font=("Helvetica", 16))
		self.textfield.grid(row=0, column=0, rowspan=4, sticky=W+E+N+S)
		


		self.logo = PhotoImage(file="animations-mail.gif")
		#resize the image
		#self.logo = self.logo.zoom(25)
		#self.logo = self.logo.subsample(32)
		self.ltwo = Label(self, image=self.logo, bg="dark blue",)
		self.ltwo.grid(row=3, 
		column=1,
		sticky=W+E+N+S,
		padx=5,
		pady=5)


	def sendthisemail(self):
		toadd = self.e1.get()
		content = self.textfield.get(0.0,END)
		tkMessageBox.showinfo("Email Status", "Your email has been sent")
		print toadd, content
		return toadd, content


if __name__ == "__main__":
	#send email to this email address
	toadd = ""
	#email content
	content = ""
	app = sendmail_tk(None)
	app.title('P2P Email-Sending')
	app.mainloop() 

	 
  



