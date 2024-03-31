from tkinter import *

window = Tk()
window.minsize(width=360, height=360)
window.title('Sudoko Solver')
window.config(padx=40, pady=40)
canvas = Canvas(width=362, height=362, highlightthickness=0)


rows, cols, box_size = 9, 9, 40

def draw_grid():
    for row in range(rows+1):
        y = row * box_size
        canvas.create_line(0, y, cols*box_size, y, fill="black")
    for col in range(cols+1):
        x = col * box_size
        canvas.create_line(x, 0, x, rows*box_size, fill="black")



def fill_values(values):
    for i in range(len(values)):
        for j in range(len(values[i])):
            value = values[i][j]




board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]









draw_grid()
canvas.pack()




























window.mainloop()
