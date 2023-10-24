import tkinter

canvas = tkinter.Canvas(width=800,height=600)
canvas.pack()

#Pismeno C
canvas.create_line(50,50,50,150,50,50,100,50,fill="red",width= 3)
canvas.create_line(50,150,100,150, fill="red",width= 3)
#Pis H
canvas.create_line(150,50,150,150,150,100,200,100,200,50,200,150,fill="blue",width= 5)
#pis R
canvas.create_line(235,50,235,150,fill="yellow",width= 2)
canvas.create_arc(200 ,50,270,100,outline="yellow",width= 2,start = 270, extent = 180)
canvas.create_line(235,100,270,150,fill="yellow",width= 2)
               

#pis I
canvas.create_line (290,50,290,150,fill="red",width=10)
# pis S
canvas.create_arc(310,50,390,100,start=70, extent=180,style=tkinter.ARC,width= 5)
canvas.create_arc(370,96,270,150,start=255, extent=180,style=tkinter.ARC,width= 5)



#pis T
canvas.create_line (395,50,395,150,fill="green",width= 2)
canvas.create_line (370,50,420,50,fill="green",width= 2)


#pis I
canvas.create_line (440,50,440,150,fill="red",width=10)

#pis A
canvas.create_line (500,50,480,150,fill="pink",width= 4)
canvas.create_line (500,50,520,150,fill="pink",width= 4)
canvas.create_line (490,100,510,100,fill="pink",width= 4)

#pis N
canvas.create_line (550,50,550,150,550,50,590,150,590,50,590,150,fill="blue",width= 6)


#pis K
canvas.create_line (50,200,50,300,50,250,100,200,fill="green",width= 5)
canvas.create_line (50,250,100,300,fill="green",width= 5)

# pis O
canvas.create_oval (120,200,190,300,outline="orange",width= 8)

#pis P
canvas.create_line(220,200,220,300,fill="aqua",width= 2)
canvas.create_arc(185,200,255,250,start = 270, extent = 180,outline="aqua",width= 2)

#pis P
canvas.create_line(280,200,280,300,fill="aqua",width= 2)
canvas.create_arc(255,200,305,250,start = 270, extent = 180,outline="aqua",width= 3)

#pis E

canvas.create_line(330,200,330,300,330,200,365,200,fill="brown",width= 7)
canvas.create_line (330,250,365,250,fill="brown",width= 7)
canvas.create_line (330,300,365,300,fill="brown",width= 7)

#pis R
canvas.create_line(400,200,400,300,fill="yellow",width= 5)
canvas.create_arc(365,200,435,250,start = 270, extent = 180,outline="yellow",width= 5)
canvas.create_line(400,250,435,300,fill="yellow",width= 5)
        
                   
