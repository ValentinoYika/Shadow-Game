from tkinter import Tk, Frame, Label, Entry, Button, StringVar
from tkinter import messagebox
from PIL import Image, ImageTk
from time import time, sleep
from random import randint, choice
from itertools import count, cycle

font1 = ("Verdana",20,"bold")
font2 = ("Verdana",10,"bold")
background1 = "#171717"
background2 = "red"
background3 = "#a6a6a6"
foreground1 = "gray42"
relief1 = "groove"
relief2 = "sunken"
cursor1 = "heart"
cursor2 = "hand2"
banner1 = "DEDICADO A MI PERRO SHADOW"
ICONFILE = "dog.png"
billetera = 0

class Application(Tk):
	
	def __init__(self, *arg, **kwargs):
		# global billetera
		Tk.__init__(self, *arg, **kwargs)
		container = Frame(self)
		container.pack(side = "top", fill = "both", expand = 1)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}
		

		for i in (Lobby, Game, Info, Shop, Craft, Bank, BackPack, Pet_zone):

			frame = i(container, self)

			self.frames[i] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame(Lobby)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class Lobby(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent, width="520", height="520", bg=background1,
						relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima = Image.open("Shadow.png")	
		image = ImageTk.PhotoImage(ima)
		lblBottom = Label(self, image = image, bg = background1)
		lblBottom.image = image
		lblBottom.pack()

		lblTitle = Label(self, text = "SHADOW'S GAME", font = font1, bg = background1, fg = foreground1)
		lblTitle.place(x = 120, y = 60)

		btnPlay=Button(self, text = "PLAY", activebackground = foreground1, width = 5,	bg = background1, 
							fg = foreground1, font = font2, command = lambda: controller.show_frame(Game), 
							cursor = cursor1)
		btnPlay.place(x = 190, y = 355)

		btnQuit = Button(self, text = "QUIT", activebackground = "orange red", width = 5, bg = background2, 
								fg = background1, font = font2, command = self.quit, cursor = cursor2)
		btnQuit.place(x = 250, y = 355)

class Game(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent, width = "520", height = "520", bg = background1,
						relief = relief2, bd = 10)

		#--------------------------------------Obj Variables-------------------------------------------#
		self.commands_var = StringVar()
		self.command_var = StringVar()

		self.cmd = False
		self.contador = 0

		#------------------------------------imagen de fondo-------------------------------------------#
		ima1 = Image.open("Logo2.png")	
		image1 = ImageTk.PhotoImage(ima1)
		bottom1 = Label(self, image = image1, bg = background1)
		bottom1.image = image1
		bottom1.pack()
		
		#------------------------------ventana donde irán los comandos---------------------------------#
		self.lblCommands = Label(self, width = 55, height = 15, relief = relief2, textvariable = self.commands_var,
									bg = background1, fg = foreground1, anchor = "nw", justify = "left")
		self.lblCommands.place(x = 65, y = 135)

		#--------------------------ventana donde se escribirán los comandos----------------------------#
		self.entCommand = Entry(self, bg = background1, fg = foreground1, font = font2, width = 43, textvariable = self.command_var)
		self.entCommand.bind("<Return>", self.save_records)
		self.entCommand.place(x = 65, y = 380)

		#--------------------------------------Dedicatoria---------------------------------------------#
		lblBanner = Label(self, text = banner1, width = 28, height = 1, bg = background1, fg = foreground1, font = font2)
		lblBanner.place(x = 200, y = 460)
		
		#-------------------------------------botón de info--------------------------------------------#
		btnInfo = Button(self, text = "INFO", activebackground = foreground1, bg = background1, fg = foreground1, 
							font = font2, command = lambda: controller.show_frame(Info))
		btnInfo.place(x = 408, y = 50)

		#--------------------------------boton para ir a la tienda-------------------------------------#
		btnShop = Button(self, text = "SHOP", activebackground = foreground1, bg = background1, fg = foreground1, 
							font = font2, command = lambda: controller.show_frame(Shop))
		btnShop.place(x = 408, y = 420)

		#----------------------------boton para ir a la mesa de crafteo--------------------------------#
		btnCraft = Button(self, text = "CRAFT", activebackground = foreground1, bg = background1, fg = foreground1, 
							font = font2, command = lambda: controller.show_frame(Craft))
		btnCraft.place(x = 348, y = 420)

		#---------------------------------boton para ir al banco---------------------------------------#
		btnBank = Button(self, text = "BANK", activebackground = foreground1, bg = background1, fg = foreground1, 
							font = font2, command = lambda: controller.show_frame(Bank))
		btnBank.place(x = 295, y = 420)

		#-------------------------------boton para ir al inventario------------------------------------#
		btnBackpack = Button(self, text = "BACKPACK", activebackground = foreground1, bg = background1, fg = foreground1, 
								font = font2, command = lambda: controller.show_frame(BackPack))
		btnBackpack.place(x = 204, y = 420)

		#-----------------------------boton para visitar a tu mazcota----------------------------------#
		btnPetZone = Button(self, text = "PET ZONE", activebackground = foreground1, bg = background1, fg = foreground1, 
								font = font2, command = lambda: controller.show_frame(Pet_zone))
		btnPetZone.place(x = 65, y = 420)

		self.entCommand.focus()

	def save_records(self, handle):
		commands = self.commands_var
		command = self.command_var.get()
		
		if command == "$daily":

			global billetera
			
			self.cmd = True
			money = randint(500,1000)
			self.comando = str(command) + f"\nHas ganado {money}" + " Sc"
			
			billetera += money
			print (str(billetera))
			
			self.contador += 2

		elif command == "$crime":
			self.cmd = True

			probabilidad = ["Robaste un banco", "Te arrestaron"]
			reaccion = choice(probabilidad)

			if reaccion == probabilidad[0]:
				self.comando = str(command) + f"\n{reaccion}" + "\nHas ganado " + str(randint(100,500)) + " Sc"				
			else:
				self.comando = str(command) + f"\n{reaccion}" + '\nHas sido arrestado y te han descontado ' + str(randint(0, 100)) + " Sc"

			self.contador += 3
		elif command == "$fish":
			self.cmd = True
			self.commando = str(command) + "\nHas ganado " + str(randint(0,200)) + " Sc"
			self.contador += 2
		elif command == "$mine":
			self.cmd = True
			self.comando = str(command) + "\nHas ganado " + str(randint(0,200)) + " Sc"
			self.contador += 2
		elif command == "$work":
			self.cmd = True
			self.comando = str(command) + "\nHas ganado " + str(randint(100,200)) + " Sc"
			self.contador += 2
		elif command == "$slots":
			self.cmd = True
			self.comando = str(command) + "\nHas ganado " + str(randint(500,1000)) + " Sc"
			self.contador += 2
		elif command == "$claim":
			self.cmd = True
			self.comando = str(command) + "\nHas ganado " + str(randint(1000,2000)) + " Sc"
			self.contador += 2
		elif command == "$buy":
			self.cmd = True
			self.commando = str(command) + "\nPara comprar, ir a la tienda"
			self.contador += 2
		elif command == "$craft":
			self.cmd = True
			self.comando = str(command) + "\nPara craftear, ir a la mesa de crafteo"
			self.contador += 2
		elif command == "$withdraw" or command == "$wd":
			self.cmd = True
			self.comando = str(command) + "\nPara retirar dinero, ir al banco"
			self.contador += 2
		elif command == "$use":
			self.cmd = True
			self.comando = str(command) + "\nHas ganado " + str(randint(500,1000)) + " Sc"
			self.contador += 2
		elif command == "$sell":
			self.cmd = True
			self.comando = str(command) + "\nPara vender, ir a la tienda"
			self.contador += 2
		elif command == "$deposit" or command == "$dp":
			self.cmd = True
			self.comando = str(command) + "\nPara depositar, ir al banco"
			self.contador += 2
		elif command == "":
			self.cmd = False
			self.comando = str(command)
		else:
			self.cmd = False
			self.comando = command
			self.contador +=1

		if self.cmd == False:
			print("Sin comandos")
		else:
			print(self.comando)

		if not command == '':	
			commands.set(commands.get() + self.comando + '\n')

		cntLetras = 0
		letter = '' 
		cntLineas = 0

		if (self.contador > 15):

			resta = self.contador - 15
			
			for i in commands.get():
				cntLetras +=1
				if i == '\n':
					cntLineas += 1
				if cntLineas == resta:
					self.contador = 15
					break
			for j in range(cntLetras,len(commands.get())):
				letter+=commands.get()[j]
			commands.set(letter)

		self.entCommand.delete(0, 'end')

class Info(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent, width = "520", height = "520", bg = background1,
			relief = relief2, bd = 10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima2 = Image.open("Logo2.png")	
		image2 = ImageTk.PhotoImage(ima2)
		bottom2 = Label(self, image = image2, bg = background1)
		bottom2.image = image2
		bottom2.pack()

		#-----------------------------------botón de regreso-------------------------------------------#
		btnBack = Button(self, text = "BACK", activebackground = "orange red",
			bg = background2, fg = background1, font = font2, command = lambda: controller.show_frame(Game))
		btnBack.place(x = 400, y = 50)

class Shop(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent, width = "520", height = "520", bg = background1, relief = relief2, bd = 10)

		#--------------------------------------Obj Variables-------------------------------------------#
		self.contador = 0
		self.item_var = StringVar()
		self.itemComprado_var = StringVar()
		self.dinero_var = StringVar() 

		#------------------------------------imagen de fondo-------------------------------------------#
		ima3 = Image.open("Logo2.png")	
		image3 = ImageTk.PhotoImage(ima3)
		lblBottom3 = Label(self, image = image3, bg = background1)
		lblBottom3.image = image3
		lblBottom3.pack()
		
		#----------------------------------menú de la tienda-------------------------------------------#
		ima4 = Image.open("Tienda1.png")	
		image4 = ImageTk.PhotoImage(ima4)
		lblShop = Label(self, image = image4, bg = background1, relief = relief2)
		lblShop.image = image4
		lblShop.place(x = 100, y = 100)

		#----------------------------------------compra------------------------------------------------#
		self.lblCompra = Label(self, font = 'Arial 11 bold', bg = background1, fg = foreground1, textvariable = self.itemComprado_var)
		self.lblCompra.place(x = 160, y = 421)

		#-----------------------------------------ids--------------------------------------------------#
		lblIds = Label(self, text = "IDs: ", font = 'Arial 11 bold', bg = background1, fg = foreground1)
		lblIds.place(x = 210, y = 461)	

		#----------------------------------------compra------------------------------------------------#
		self.lblDinero = Label(self, font = 'Arial 11 bold', bg = background1, fg = foreground1, textvariable = self.dinero_var)
		self.lblDinero.place(x = 100, y = 463)	

		#-------------------------ventana donde se escribirán los compras------------------------------#
		self.entItem = Entry(self, bg = background1, fg = foreground1, font = font2, textvariable = self.item_var, width = 10)
		self.entItem.place(x = 250, y = 463)

		#-----------------------------------botón de regreso-------------------------------------------#
		btnBack = Button(self, text = "BACK", activebackground= "orange red", bg = background2, fg = background1, 
							font = font2, command = lambda: controller.show_frame(Game))
		btnBack.place(x = 400, y = 50)
		
		#-----------------------------------boton siguiente--------------------------------------------#
		self.btnNext = Button(self, text = "⏵", activebackground = background3, bg = background1, fg = foreground1, 
								font = font2, command = self.siguiente)
		self.btnNext.place(x = 375, y = 420)

		#------------------------------------boton anterior--------------------------------------------#
		self.btnPreviuos = Button(self, text = "⏴", activebackground = background3, bg = background1, fg = foreground1, 
									font = font2, command = self.anterior)
		self.btnPreviuos.place(x = 100, y = 420)

		#-------------------------------------boton comprar--------------------------------------------#
		self.btnBuy = Button(self, text = "BUY", activebackground = background3, bg = background1, fg = foreground1, 
								font = font2, command = self.comprar)
		self.btnBuy.place(x = 362, y = 460)

		self.itemComprado_var.set("Has comprado el ID: ")
		self.dinero()
	
	def dinero(self):
		dinero = self.dinero_var
		print(str(billetera))
		dinero.set(str(billetera))


	def comprar(self):
		item = self.item_var
		itemComprado = self.itemComprado_var

		itemComprado.set("Has comprado el ID: " + item.get())
		print(str(billetera))
		self.entItem.delete(0, 'end')

	def siguiente(self):
		ima4 = Image.open("Tienda2.png")	
		image4 = ImageTk.PhotoImage(ima4)
		lblShop = Label(self, image = image4, bg = background1, relief = relief2)
		lblShop.image = image4
		lblShop.place(x = 100, y = 100)
		self.contador += 1
	
	def anterior(self):
		ima4 = Image.open("Tienda1.png")	
		image4 = ImageTk.PhotoImage(ima4)
		lblShop = Label(self, image = image4, bg = background1, relief = relief2)
		lblShop.image = image4
		lblShop.place(x = 100, y = 100)
		self.contador += 1
		pass

class Craft(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima5=Image.open("Logo2.png")	
		image5=ImageTk.PhotoImage(ima5)
		bottom4=Label(self,image=image5,bg=background1)
		bottom4.image = image5
		bottom4.pack()

		#-----------------------------------botón de regreso-------------------------------------------#
		button_back=Button(self,text="BACK",activebackground="orange red",
			bg=background2,fg=background1,font=font2,command=lambda:controller.show_frame(Game))
		button_back.place(x=400,y=50)

		craft_frame = Label(self,width=55,height=24,bg=background1,relief=relief1)
		craft_frame.place(x=63,y=105)
		
		self.labels()

	def labels(self):
		x=80
		y=120
		for i in range(9):
			Label(self,width=16,height=7,bg=foreground1,relief=relief2).place(x=x,y=y)
			x+=120
			if x>320:
				x=80
				y+=113
				if y>346:
					continue

class Bank(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima6=Image.open("Logo2.png")	
		image6=ImageTk.PhotoImage(ima6)
		bottom5=Label(self,image=image6,bg=background1)
		bottom5.image = image6
		bottom5.pack()

		#-----------------------------------botón de regreso-------------------------------------------#
		button_back=Button(self,text="BACK",activebackground="orange red",
			bg=background2,fg=background1,font=font2,command=lambda:controller.show_frame(Game))
		button_back.place(x=400,y=50)

class BackPack(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima7=Image.open("Logo2.png")	
		image7=ImageTk.PhotoImage(ima7)
		bottom6=Label(self,image=image7,bg=background1)
		bottom6.image = image7
		bottom6.pack()

		#-----------------------------------botón de regreso-------------------------------------------#
		button_back=Button(self,text="BACK",activebackground="orange red",
			bg=background2,fg=background1,font=font2,command=lambda:controller.show_frame(Game))
		button_back.place(x=400,y=50)

class Pet_zone(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		lbl = ImageLabel(self)
		lbl.pack()
		lbl.load('gifpet.gif')

		# #------------------------------------imagen de fondo-------------------------------------------#
		# ima8=Image.open("gifpet.gif")	
		# image8=ImageTk.PhotoImage(ima8)
		# bottom7=Label(self,image=image8,bg=background1)
		# bottom7.image = image8
		# bottom7.pack()

		#-----------------------------------botón de regreso-------------------------------------------#
		button_back=Button(self,text="BACK",activebackground="#a6a6a6",
			bg="#c0bbc1",fg=background1,font=font2,command=lambda:controller.show_frame(Game))
		button_back.place(x=400,y=50)

class Secret_Win(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		# ima0=Image.open("Logo2.png")	
		# image0=ImageTk.PhotoImage(ima0)
		# bottom0=Label(self,image=image0,bg=background1)
		# bottom0.image = image0
		# bottom0.pack()
		self.cavas()
		#-----------------------------------botón de regreso-------------------------------------------#
		button_back=Button(self,text="BACK",activebackground="orange red",
			bg=background2,fg=background1,font=font2,command=lambda:controller.show_frame(Game))
		button_back.place(x=400,y=50)

	def c4nvas(self):
		animation = pyglet.image.load_animation('gifpet.gif')
		animSprite = pyglet.sprite.Sprite(animation)
		 
		 
		w = animSprite.width
		h = animSprite.height
		 
		window = pyglet.window.Window(width=w, height=h)
		 
		r,g,b,alpha = 0.5,0.5,0.8,0.5
		 
		 
		pyglet.gl.glClearColor(r,g,b,alpha)
		 
		@window.event
		def on_draw():
		    window.clear()
		    animSprite.draw()		 		 
		 
		pyglet.app.run()
#el objeto de abajo la descargue de internet y no sé cómo funciona pero funciona, así que no lo toques
class ImageLabel(Label):
    """
    A Label that displays images, and plays them if they are gifs

    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame) #lo copie por internet, asi que no sé cómo funciona pero funciona

def main():
	app = Application()
	app.title("Shadow's Game")
	app.iconbitmap(ICONFILE)
	app.resizable(0,0)
	app.bind("<Escape>", lambda x: app.destroy())
	app.mainloop()

if __name__ == '__main__':
	main()
