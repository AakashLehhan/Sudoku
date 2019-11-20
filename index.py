def reset():
    for i in range(0,rows,1):
        for j in range(0,cols,1):
            col[i][j].delete(0, "end")
            col[i][j].config(bg = 'lightgray')

def check():
    for i in range(0,rows):
        for j in range(0,cols):
            temp = col[i][j].get()
            if len(temp) > 1 or temp == '' or temp == ' ':
                col[i][j].config(highlightbackground = 'Red')
            else:
                col[i][j].config(bg = 'Lightgray')
                

from tkinter import Tk, Canvas, Entry, Button, CENTER, IntVar

root = Tk()

screen = Canvas(root, height = 430, width = 460)
screen.pack()

screen.create_text(215, 15, text = 'SUDOKU', font = 'calibri 20 bold')

#vertical lines
screen.create_line(127, 54, 127, 408)
screen.create_line(232, 54, 232, 408)
#horizontal lines
screen.create_line(24, 170, 336, 170)
screen.create_line(24, 290, 336, 290)

x, y, n = 0, 0, 0

cols, rows = 9, 9

col = []
val = []

for i in range(0,rows,1): 
    x = 0
    if i == 0:
        y += 70 
    else:
        y += 40
    rowc = []
    rowv = []
    for j in range(0,cols,1):
        x += 40
        v = IntVar()
        ent = Entry(root, width = 2, textvariable = v, font = 'Calibri 20', bd = 1, justify = CENTER, bg = 'lightgray')
        screen.create_window(x, y, window = ent)
        rowc.append(ent)
        rowv.append(v)
        x -= 5
    col.append(rowc)
    val.append(rowv)

check_button = Button(root, text = 'Check', font = 'Calibri 10 bold', bd = 0, bg = 'Green', fg = 'white', padx = 10, pady = 5, command = check)
screen.create_window(400, 70, window = check_button)

reset_button = Button(root, text = 'Reset', font = 'Calibri 10 bold', bd = 0, bg = 'Red', fg = 'white', padx = 10, pady = 5, command = reset)
screen.create_window(400, 110, window = reset_button)


root.mainloop()
