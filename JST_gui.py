# Albert Kingston Wang 231012000079

#sel 1 net v
#sel 0 net w
from tkinter import*
from JST_proses import *
global inp
import time
inp   = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]
root = Tk()
root.geometry('700x500')
root.resizable(width=False,height=False)
root.title('Albert Kingston Wang/231012000079')
root.configure(bg= 'mint cream')


l1 = Label(root, text  = 'Nama : ')
l2 = Label(root, text  = 'NIM : ')
l1.grid(column = 0,row = 0,padx = 5,pady = 3, sticky = E+W+N+S)
l2.grid(column = 0,row = 1,padx = 5,pady = 3, sticky = E+W+N+S)

l3 = Label(root, text  = 'Albert Kingston Wang ')
l4 = Label(root, text  = '231012000079 ')
l3.grid(column = 1,row = 0,padx = 5,pady = 3, sticky = E+W+N+S)
l4.grid(column = 1,row = 1,padx = 5,pady = 3, sticky = E+W+N+S)

l1 = Label(root, text  = '')
l2 = Label(root, text  = '')
l1.grid(column = 2,row = 0,padx = 5,pady = 3, sticky = E+W+N+S)
l2.grid(column = 2,row = 1,padx = 5,pady = 3, sticky = E+W+N+S)

l3 = Label(root, text  = '')
l4 = Label(root, text  = ' ')
l3.grid(column = 3,row = 0,padx = 5,pady = 3, sticky = E+W+N+S)
l4.grid(column = 3,row = 1,padx = 5,pady = 3, sticky = E+W+N+S)

f1 = Frame(root, bg = 'spring green', width = 500, height = 420)
f1.grid(column = 0,row = 2,padx = 5,pady =5,columnspan=6, sticky = E+W+N+S)

c1 = Canvas(f1, bg = 'white', width = 300, height = 400)
c1.grid(column = 1,row = 0,padx = 5,pady =5,rowspan=9, sticky = E+W+N+S)

c2 = Canvas(f1, bg = 'spring green', width = 200, height = 200)
c2.grid(column = 0,row = 4,padx = 5,pady =5, sticky = E+W+N+S)

c3 = Canvas(root, bg = 'pink', width = 190, height = 100)
c3.grid(column = 7,row = 2,padx = 5,pady =5,rowspan=6, sticky = E+W+N+S)

offset = 10
def klik(n):
    if n%7 == 0:
        baris = int(n/7)-1
        kolom = 6
    else:
        test = n/7
        baris = int(test)
        kolom = int(round((test-baris)*7))-1
    if(inp[baris][kolom] == 0):
        c1.itemconfigure(n,fill = 'black')
        inp[baris][kolom] = 1
    elif(inp[baris][kolom] == 1):
        c1.itemconfigure(n,fill = 'white')
        inp[baris][kolom] = 0
##    print(baris,kolom)
def proses_val():
    global v,w
    v = []
    w = []
    wak = 0
    v,w,wak = proses()
    tchat.insert(END,'proses selama :'+str(wak)+'\n')
    tchat.insert(END,'proses selesai\n')
    
def Clear():
    global inp
    tchat.delete('1.0',END)
    for i in range (64):
        c1.itemconfigure(i,fill = 'white')
    inp =[[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]
def tentu ():
    global v,w,inp
    inpu = []
    for i in range (len(inp)):
        inpu = inpu+inp[i]
    z = bobot(net(v,inpu,1),1)
    a_list = (bobot(net(w,z,0),0))
    round_to_whole = [round(num) for num in a_list]
    if (round_to_whole[0] == 1):
        tchat.insert(END,'Huruf A\n')
    elif (round_to_whole[1] == 1):
        tchat.insert(END,'Huruf B\n')
    elif (round_to_whole[2] == 1):
        tchat.insert(END,'Huruf H\n')
    else :
        tchat.insert(END,str(a_list)+'\n')
        
data = []
data=(('1',lambda:klik(1)),('2',lambda:klik(2)),('3',lambda:klik(3)),('4',lambda:klik(4)),
      ('5',lambda:klik(5)),('6',lambda:klik(6)),('7',lambda:klik(7)),('8',lambda:klik(8)),
      ('9',lambda:klik(9)),('10',lambda:klik(10)),('11',lambda:klik(11)),('12',lambda:klik(12)),
      ('13',lambda:klik(13)),('14',lambda:klik(14)),('15',lambda:klik(15)),('16',lambda:klik(16)),
      ('17',lambda:klik(17)),('18',lambda:klik(18)),('19',lambda:klik(19)),('20',lambda:klik(20)),
      ('21',lambda:klik(21)),('22',lambda:klik(22)),('23',lambda:klik(23)),('24',lambda:klik(24)),
      ('25',lambda:klik(25)),('26',lambda:klik(26)),('27',lambda:klik(27)),('28',lambda:klik(28)),
      ('29',lambda:klik(29)),('30',lambda:klik(30)),('31',lambda:klik(31)),('32',lambda:klik(32)),
      ('33',lambda:klik(33)),('34',lambda:klik(34)),('35',lambda:klik(35)),('36',lambda:klik(36)),
      ('37',lambda:klik(37)),('38',lambda:klik(38)),('39',lambda:klik(39)),('40',lambda:klik(40)),
      ('41',lambda:klik(41)),('42',lambda:klik(42)),('43',lambda:klik(43)),('44',lambda:klik(44)),
      ('45',lambda:klik(45)),('46',lambda:klik(46)),('47',lambda:klik(47)),('48',lambda:klik(48)),
      ('49',lambda:klik(49)),('50',lambda:klik(50)),('51',lambda:klik(51)),('52',lambda:klik(52)),
      ('53',lambda:klik(53)),('54',lambda:klik(54)),('55',lambda:klik(55)),('56',lambda:klik(56)),
      ('57',lambda:klik(57)),('58',lambda:klik(58)),('59',lambda:klik(59)),('60',lambda:klik(60)),
      ('61',lambda:klik(61)),('62',lambda:klik(62)),('63',lambda:klik(63)))
button = []
col = 0
row = 0
for i,(nama,fungsi) in enumerate(data):
    button.append(Button(c2,text=nama,command = fungsi))
    button[i].grid(column = col,row = row, sticky = E+W+N+S)
    
    col = col + 1
    if (col == 7):
        col = 0
        row = row + 1
for i in range (9):
    for j in range (7):
        c1.create_rectangle(offset+(40*j),offset+(40*i),offset+(40*(j+1)),offset+(40*(i+1)),tag = (j+1)+(7*i))
for i in range (9):
    for j in range (7):
        c1.create_text(offset+20+(40*j),offset+20+(40*i),text = str((j+1)+(7*i)),fill = 'magenta')    

text = tchat = Text(c3, bg = 'cyan', width = 20 , height = 12)
tchat.grid(column = 0,row=1,padx = 5,pady = 5,sticky = E+W+N+S)

b1 = Button(c3,width = 10, height = 1,text = 'proses',bg = 'lime',command = proses_val)
b1.grid(column= 0,row = 2 ,padx = 3,pady = 5,sticky = E+W+N+S)
b2 = Button(c3,width = 10, height = 1,text = 'Clear',bg = 'lime',command = Clear)
b2.grid(column= 0,row = 4,padx = 3,pady = 5,sticky = E+W+N+S)
b3 = Button(c3,width = 10, height = 1,text = 'Tentukan',bg = 'lime',command = tentu)
b3.grid(column= 0,row = 3,padx = 3,pady = 5,sticky = E+W+N+S)

