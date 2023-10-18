import tkinter

canvas = tkinter.Canvas(width=800,height=600)
canvas.pack()

#Pismeno C
canvas.create_line(50,50,50,150,50,50,100,50,fill="red",width= 3)
canvas.create_line(50,150,100,150, fill="red",width= 3)
#Pis H
canvas.create_line(150,50,150,150,150,100,200,100,200,50,200,150,fill="blue",width= 5)
#pis R
canvas.create_line(235,50,235,150)
canvas.create_arc(200 ,50,270,100,start = 270, extent = 180)
canvas.create_line(235,100,270,150)
               

#pis I
canvas.create_line (290,50,290,150,fill="red",width=10)
# pis S
canvas.create_arc(255,50,305,150,start = 270, extent = 180)




#pis T
canvas.create_line (380,50,380,150)
canvas.create_line (350,50,410,50)


#pis I
canvas.create_line (440,50,440,150,fill="red",width=10)

#pis A
canvas.create_line (500,50,480,150)
canvas.create_line (500,50,520,150)
canvas.create_line (490,100,510,100)

#pis N
canvas.create_line (550,50,550,150,550,50,590,150,590,50,590,150)


#pis K
canvas.create_line (50,200,50,300,50,250,100,200)
canvas.create_line (50,250,100,300)

# pis O
canvas.create_oval (120,200,190,300)

#pis P
canvas.create_line(220,200,220,300)
canvas.create_arc(185,200,255,250,start = 270, extent = 180)

#pis P
canvas.create_line(280,200,280,300)
canvas.create_arc(255,200,305,250,start = 270, extent = 180)

#pis E

canvas.create_line(330,200,330,300,330,200,365,200)
canvas.create_line (330,250,365,250)
canvas.create_line (330,300,365,300)

#pis R
canvas.create_line(400,200,400,300)
canvas.create_arc(365,200,435,250,start = 270, extent = 180)
canvas.create_line(400,250,435,300)
        
                   
