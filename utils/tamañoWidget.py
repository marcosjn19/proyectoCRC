import tkinter as tk

class tam(tk.Entry):
    def __init__(self, master=None, max_len=5, **kwargs):
        self.var = tk.StringVar()
        self.max_len = max_len
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)

    def check(self, *args):
        if len(self.get()) <= self.max_len:
            self.old_value = self.get() # accept change
        else:
            self.var.set(self.old_value) # reject change
