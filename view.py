import model
import tkinter
from typing import List

class LifeView:
    def __init__(self, root, run_cb, init_cb, start_cb, stop_cb):
        self.root = root
        self.root.title("Game of Life")
        self.root.geometry('280x320')
        self.field = tkinter.Canvas(self.root, width=270,height=270)
        self.field.pack()
        self.field.place(x=10, y=5)
        #self.field.grid(row=0, column= 0)

        if run_cb == init_cb == start_cb == None:
            run_cb = init_cb = start_cb = stop_cb = self.hello
        pady_val = 5
        self.next_button = tkinter.Button(self.root, text="Next Iteration", \
                             command=lambda : run_cb(self.field))
        #self.next_button.pack(pady = pady_val)
        self.next_button.place(x=20, y=250)
        #self.next_button.grid(row=1, column=0)
        self.init_button = tkinter.Button(self.root, text="New Initialization", \
                             command=lambda : init_cb(self.field))
        #self.init_button.pack(pady = pady_val)
        self.init_button.place(x=150, y=250)
        #self.init_button.grid(row=2, column=0)
        self.start_button = tkinter.Button(self.root, text="Start Auto Iterations", \
                             command=lambda : start_cb(self.field))
        #self.start_button.pack(pady = pady_val)
        #self.start_button.grid(row=3, column=0)
        self.start_button.place(x=20, y=280)
        self.stop_button = tkinter.Button(self.root, text="Stop Auto Iterations", \
                             command=lambda : stop_cb(self.field))
        #self.stop_button.pack(pady = pady_val)
        self.stop_button.place(x=150, y=280)
        #self.stop_button.grid(row=4, column=0)

    def hello(self, f: tkinter.Canvas):
        print('hello')

    def update_field(self, board: List[List[int]]) -> None:#, f: tkinter.Canvas) -> None:
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 1:
                    self.field.create_rectangle(i*21, j*21, i*21 + 20, \
                                           j*21 + 20, fill='chartreuse2')
                else:
                    self.field.create_rectangle(i*21, j*21, i*21 + 20, j*21+20, \
                                           fill='brown4')
    def run_mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    LM = model.LifeModel(4, 7)
    LM.board_init()
    root = tkinter.Tk()
    LV = LifeView(root, None, None, None, None)
    LV.update_field(LM.get_board());
    LV.run_mainloop()


