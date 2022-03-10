from model import *
from view import *
import tkinter
from typing import List

class LifeControl:
    def __init__(self, root):
        self.Start_flag = False
        self.End_flag = False
        self.LM = LifeModel(10, 10)
        self.LM.board_init()
        self.LV = LifeView(root, self.run_cb, self.init_cb,\
                           self.start_cb, self.stop_cb)
        self.LV.update_field(self.LM.get_board())
        self.root = root
        self.task()
        self.LV.run_mainloop()

    def run_cb(self, f: tkinter.Canvas) -> None:
        if not self.End_flag:
            self.End_flag = self.LM.board_next()
            self.LV.update_field(self.LM.get_board())

    def init_cb(self, f: tkinter.Canvas) -> None:
        self.Start_flag = self.End_flag = False
        self.LM.board_init()
        self.LV.update_field(self.LM.get_board())

    def start_cb(self, f: tkinter.Canvas) -> None:
        self.Start_flag = True

    def stop_cb(self, f: tkinter.Canvas) -> None:
        self.Start_flag = False
        
    def task(self):
        if self.Start_flag and not self.End_flag:
            self.End_flag = self.LM.board_next()
            self.LV.update_field(self.LM.get_board())
        self.root.after(1000, self.task)
        
root = tkinter.Tk()
LC = LifeControl(root)