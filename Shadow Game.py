from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
from random import *
from itertools import count, cycle


#variables
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

class Application(Tk):
	def __init__(self,*arg,**kwargs):
		Tk.__init__(self,*arg,**kwargs)
		container=Frame(self)
		container.pack(side="top",fill="both",expand=1)

		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.frames={}

		for i in (Lobby,Game,Info,Shop,Craft,Bank,BackPack,Pet_zone):

			frame = i(container,self)

			self.frames[i] = frame

			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(Lobby)

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

class Lobby(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima=Image.open("Shadow.png")	
		image=ImageTk.PhotoImage(ima)
		bottom=Label(self,image=image,bg=background1)
		bottom.image = image
		bottom.pack()

		#----------------------------------------título------------------------------------------------#
		title=Label(self, text="SHADOW'S GAME",
			font=font1,bg=background1,fg=foreground1)
		title.place(x=120,y=60)

		#--------------------------------------botón jugar---------------------------------------------#
		button_play=Button(self,text="PLAY",activebackground=foreground1,
			bg=background1,fg=foreground1,font=font2,command=lambda:controller.show_frame(Game),
			cursor=cursor1)
		button_play.place(x=200,y=355)

		#--------------------------------------botón salir---------------------------------------------#
		button_quit=Button(self,text="QUIT",activebackground="orange red",
			bg=background2,fg=background1,font=font2,command=self.quit, cursor=cursor2)
		button_quit.place(x=250,y=355)

class Game(Frame):
	
	commands = None
	text = None
	content = None
	cont = 0

	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#---------------------------------------variables----------------------------------------------#
		Game.commands = {
			'dict1':{
				'$daily':self.__money(500,1000),
				'$crime':self.__money(100,500),
				'$fish':self.__money(0,200),
				'$mine':self.__money(0,200),
				'$work':self.__money(500,1000),
				'$slots':self.__money(0,500),
				'$claim':self.__money(1000,2000)
				},

			'dict2':{
				'$buy':'Para comprar, ir a la tienda',
				'$craft':'Para craftear, ir a la mesa de crafteo',
				'$withdraw':'Para retirar dinero, ir al banco',
				'$use':'Para usar un item  ir a la mochila',
				'$sell':'Para vender, ir a la tienda',
				'$deposit':'Para depositar, ir al banco'
				}
		}

		Game.content = StringVar()

		#------------------------------------imagen de fondo-------------------------------------------#
		ima1=Image.open("Logo2.png")	
		image1=ImageTk.PhotoImage(ima1)
		bottom1=Label(self,image=image1,bg=background1)
		bottom1.image = image1
		bottom1.pack()

		#-------------------------------------botón de info--------------------------------------------#
		button_info=Button(self,text="INFO",activebackground=foreground1,
			bg=background1,fg=foreground1,font=font2,command=lambda:controller.show_frame(Info))
		button_info.place(x=408,y=50)

		#------------------------------ventana donde irán los comandos---------------------------------#
		command_window=Label(self,width=55,height=15,relief=relief2,textvariable=Game.content,
			bg=background1,fg=foreground1,anchor="nw",justify="left")
		command_window.place(x=65,y=135)

		#--------------------------ventana donde se escribirán los comandos----------------------------#
		Game.text=Entry(self,bg=background1,fg=foreground1,font=font2,width=43)
		Game.text.bind("<Return>",self.__func_save_command)	
		Game.text.place(x=65,y=380)
		
		#--------------------------------boton para ir a la tienda-------------------------------------#
		button_shop=Button(self,text="SHOP",activebackground=foreground1,
			bg=background1,fg=foreground1,font=font2,command=lambda:controller.show_frame(Shop))
		button_shop.place(x=408,y=420)

		#----------------------------boton para ir a la mesa de crafteo--------------------------------#
		button_craft=Button(self,text="CRAFT",activebackground=foreground1,
			bg=background1,fg=foreground1,font=font2,command=lambda:controller.show_frame(Craft))
		button_craft.place(x=348,y=420)

		#---------------------------------boton para ir al banco---------------------------------------#
		button_bank=Button(self,text="BANK",activebackground=foreground1,
			bg=background1,fg=foreground1,font=font2,command=lambda:controller.show_frame(Bank))
		button_bank.place(x=295,y=420)

		#-------------------------------boton para ir al inventario------------------------------------#
		button_backpack=Button(self,text="BACKPACK",activebackground=foreground1,
			bg=background1,fg=foreground1,font=font2,command=lambda:controller.show_frame(BackPack))
		button_backpack.place(x=204,y=420)

		#-----------------------------boton para visitar a tu mazcota----------------------------------#
		button_pet_zone=Button(self,text="PET ZONE",activebackground=foreground1,
			bg=background1,fg=foreground1,font=font2,command=lambda:controller.show_frame(Pet_zone))
		button_pet_zone.place(x=65,y=420)

		#--------------------------------------Dedicatoria---------------------------------------------#
		banner=Label(self,text=banner1,width=28,height=1,
			bg=background1,fg=foreground1,font=font2)
		banner.place(x=200,y=460)
	"""
		..............................................................................................
		.........................................Métodos..............................................
		..............................................................................................

	"""	
	def __money(self,a,b):
		var=randint(a,b)		
		return f'Has recibido {var} Shadow Coins'
		

	def __find_word(self,var,var2):
		try:
			return var2[var]
		except:
			if var.startswith('$'):
				try:
					for i in var2:
						if type(var2[i]) is dict:
							try:
								return var2[i][var]
							except:
								for j in var2[i]:
									if type(var2[i][j]) is dict:
										try:
											return var2[i][j][var]
										except:
											for k in var2[i][j]:
												if type(var2[i][j][k]) is dict:
													return var2[i][j][k][var]
				except:
					return var
			else:
				return ''

	def __show_screen(self,var,var2,var3):
		if var3 == None:
			print(var2)
			var.set(var.get()+var2+'\n')
		elif var3 == '':
			print(var2)
			var.set(var.get()+var2+'\n')
		elif var3 == var:
			print(var2)
			var.set(var.get()+var2+'\n')
		else:
			print(var2+'\n'+var3)
			var.set(var.get()+var2+'\n'+var3+'\n')

	def __reset(self):
		var = 0
		var2=Game.content.get()
		letter ='' 
		if (Game.cont>=16):
			for i in var2:
				var+=1
				if i == '\n':
					break
			for j in range(var,len(var2)):
				letter+=var2[j]
			Game.content.set(letter)

	def __func_save_command(self,event):
		Game.cont+=1
		command = Game.text.get()
		find_word = self.__find_word(command,Game.commands)
		Game.text.delete(0,"end")
		self.__show_screen(Game.content,command,find_word)
		self.__reset()

	"""
		..............................................................................................
		..............................................................................................
		..............................................................................................
		
	"""	
		
class Info(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima2=Image.open("Logo2.png")	
		image2=ImageTk.PhotoImage(ima2)
		bottom2=Label(self,image=image2,bg=background1)
		bottom2.image=image2
		bottom2.pack()

		#-----------------------------------botón de regreso-------------------------------------------#
		button_back = Button(self,text="BACK",activebackground="orange red",
			bg=background2,fg=background1,font=font2,command=lambda:controller.show_frame(Game))
		button_back.place(x=400,y=50)

class Shop(Frame):

	item=None

	def __init__(self,parent,controller):
		Frame.__init__(self,parent,width="520", height="520", bg=background1,
			relief=relief2, bd=10)

		#------------------------------------imagen de fondo-------------------------------------------#
		ima3=Image.open("Logo2.png")	
		image3=ImageTk.PhotoImage(ima3)
		bottom3=Label(self,image=image3,bg=background1)
		bottom3.image = image3
		bottom3.pack()

		#-----------------------------------botón de regreso-------------------------------------------#
		button_back=Button(self,text="BACK",activebackground="orange red",
			bg=background2,fg=background1,font=font2,command=lambda:controller.show_frame(Game))
		button_back.place(x=400,y=50)
		
		#----------------------------------menú de la tienda-------------------------------------------#
		ima4=Image.open("Tienda1.png")	
		image4=ImageTk.PhotoImage(ima4)
		shop=Label(self,image=image4,bg=background1,relief=relief2)
		shop.image = image4
		shop.place(x=100,y=100)

		#-----------------------------------boton siguiente--------------------------------------------#
		button_next=Button(self,text="NEXT",activebackground=background3,
			bg=background1,fg=foreground1,font=font2)
		button_next.place(x=356,y=420)

		#------------------------------------boton anterior--------------------------------------------#
		button_previuos=Button(self,text="PREVIOUS",activebackground=background3,
			bg=background1,fg=foreground1,font=font2)
		button_previuos.place(x=100,y=420)

		#-------------------------------------boton comprar--------------------------------------------#
		button_buy=Button(self,text="BUY",activebackground=background3,
			bg=background1,fg=foreground1,font=font2,command=lambda:self.__buy)
		button_buy.place(x=362,y=460)

		#-------------------------ventana donde se escribirán los compras------------------------------#
		Shop.item=Entry(self,bg=background1,fg=foreground1,font=font2,width=10)	
		Shop.item.bind("<Return>",self.__buy)
		Shop.item.place(x=250,y=463)

	def __buy(self,event):
		Shop.item.delete(0,"end")
		self.label=Label(self,text="+1 item",bg=background1,fg=foreground1,font=font2).place(x=100,y=463)
		sleep(0.5)
		self.label.after(1500,self.label.destroy)
		
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
	app=Application()
	app.title("Shadow's Game")
	app.resizable(0,0)
	app.bind("<Escape>",lambda x:app.destroy())
	app.mainloop()

main()
