import time
import tkinter as tk
from tkinter import Tk, Label, Menu, StringVar, ttk


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("700x500")
        self.title("Skyline Soaring Logsheet 2.0.0alpha")
        self.iconbitmap('favicon.ico')

        self.init_topmenu()
        self.init_primarytabs()
        self.init_secondarytabs()
        self.init_statusbar()

    def do_nothing(self):
        print("doing nothing")

    def init_topmenu(self):
        # todo: fill in menubar choices
        ### top menu bar ###
        menubar = Menu(self)
        self.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save", command=self.do_nothing)  # todo: implement file chooser
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)

        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)

        flightmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Flight", menu=flightmenu)

        paymentmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Payment", menu=paymentmenu)

    def on_primarytab_selected(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")

    def init_primarytabs(self):
        self.primary_tab_bar = ttk.Notebook(self)
        self.startup_tab = ttk.Frame(self.primary_tab_bar)
        self.members_tab = ttk.Frame(self.primary_tab_bar)
        self.operations_tab = ttk.Frame(self.primary_tab_bar)
        self.finances_tab = ttk.Frame(self.primary_tab_bar)
        self.shutdown_tab = ttk.Frame(self.primary_tab_bar)

        self.primary_tab_bar.bind("<<NotebookTabChanged>>", self.on_primarytab_selected)

        self.primary_tab_bar.add(self.startup_tab, text='Startup')
        self.primary_tab_bar.add(self.members_tab, text='Members')
        self.primary_tab_bar.add(self.operations_tab, text='Operations')
        self.primary_tab_bar.add(self.finances_tab, text='Finances')
        self.primary_tab_bar.add(self.shutdown_tab, text='Shutdown')

        self.primary_tab_bar.pack(expand=1, fill='both')

    def on_secondtab_selected(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")

    def init_secondarytabs(self):
        # Startup Tabs
        self.startuptabs = ttk.Notebook(self.startup_tab)
        self.staffsettab = ttk.Frame(self.startuptabs)
        self.tracontab = ttk.Frame(self.startuptabs)
        self.helptab = ttk.Frame(self.startuptabs)

        self.startuptabs.bind("<<NotebookTabChanged>>", self.on_secondtab_selected)
        self.startuptabs.add(self.staffsettab, text='Staff & Settings')
        self.startuptabs.add(self.tracontab, text='Potomac TRACON')
        self.startuptabs.add(self.helptab, text='Program Help')

        self.startuptabs.pack(expand=1, fill='both')

        # Members Tabs
        self.memberstabs = ttk.Notebook(self.members_tab)
        self.currenttab = ttk.Frame(self.memberstabs)
        self.introtab = ttk.Frame(self.memberstabs)
        self.specialtab = ttk.Frame(self.memberstabs)
        self.fulltab = ttk.Frame(self.memberstabs)
        self.guesttab = ttk.Frame(self.memberstabs)
        self.payertab = ttk.Frame(self.memberstabs)
        self.stafftab = ttk.Frame(self.memberstabs)

        self.memberstabs.bind("<<NotebookTabChanged>>", self.on_secondtab_selected)
        self.memberstabs.add(self.currenttab, text='Current')
        self.memberstabs.add(self.introtab, text='Intro')
        self.memberstabs.add(self.specialtab, text='Special')
        self.memberstabs.add(self.fulltab, text='Full')
        self.memberstabs.add(self.guesttab, text='Guest')
        self.memberstabs.add(self.payertab, text='Payer')
        self.memberstabs.add(self.stafftab, text='Staff')

        self.memberstabs.pack(expand=1, fill='both')

        # Operations Tabs
        self.operationstabs = ttk.Notebook(self.operations_tab)
        self.glidertab = ttk.Frame(self.operationstabs)
        self.airplanetab = ttk.Frame(self.operationstabs)
        self.pilottab = ttk.Frame(self.operationstabs)
        self.instructortab = ttk.Frame(self.operationstabs)
        self.towqueuetab = ttk.Frame(self.operationstabs)

        self.operationstabs.bind("<<NotebookTabChanged>>", self.on_secondtab_selected)
        self.operationstabs.add(self.glidertab, text='Glider Flights')
        self.operationstabs.add(self.airplanetab, text='Airplane Flights')
        self.operationstabs.add(self.pilottab, text='Pilot Summary')
        self.operationstabs.add(self.instructortab, text='Instructor Summary')
        self.operationstabs.add(self.towqueuetab, text='Tow Queue')

        self.operationstabs.pack(expand=1, fill='both')

        # Finances Tabs
        self.financestabs = ttk.Notebook(self.finances_tab)
        self.paymentstab = ttk.Frame(self.financestabs)
        self.feestab = ttk.Frame(self.financestabs)
        self.chargestab = ttk.Frame(self.financestabs)
        self.adjustmentstab = ttk.Frame(self.financestabs)
        self.expensestab = ttk.Frame(self.financestabs)

        self.financestabs.bind("<<NotebookTabChanged>>", self.on_secondtab_selected)
        self.financestabs.add(self.paymentstab, text='Payments')
        self.financestabs.add(self.feestab, text='Fees')
        self.financestabs.add(self.chargestab, text='Charges')
        self.financestabs.add(self.adjustmentstab, text='Adjustments')
        self.financestabs.add(self.expensestab, text='Expenses')

        self.financestabs.pack(expand=1, fill='both')

        # Shutdown Tabs
        # Shutdown: Tow Plane Data, Contact Info, Awards, Comment, No Operations
        self.shutdowntabs = ttk.Notebook(self.shutdown_tab)
        self.towplanetab = ttk.Frame(self.shutdowntabs)
        self.contacttab = ttk.Frame(self.shutdowntabs)
        self.awardstab = ttk.Frame(self.shutdowntabs)
        self.commentstab = ttk.Frame(self.shutdowntabs)
        self.nooperationstab = ttk.Frame(self.shutdowntabs)

        self.shutdowntabs.bind("<<NotebookTabChanged>>", self.on_secondtab_selected)
        self.shutdowntabs.add(self.towplanetab, text='Tow Plane Data')
        self.shutdowntabs.add(self.contacttab, text='Contact Info')
        self.shutdowntabs.add(self.awardstab, text='Awards')
        self.shutdowntabs.add(self.commentstab, text='Comments')
        self.shutdowntabs.add(self.nooperationstab, text='No Operations')

        self.shutdowntabs.pack(expand=1, fill='both')

    def init_statusbar(self):
        self.status_msg_base_text = 'this is the status bar!'
        self.status_msg_text = StringVar()
        self.status_label = Label(self, textvariable=self.status_msg_text,
                             relief=tk.GROOVE, padx=3, pady=3, anchor=tk.W
                             )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        self.time = ''
        self.tick()

    def tick(self):
        newtime = time.strftime('%H:%M:%S')
        if newtime != self.time:
            self.time = newtime
            self.status_msg_text.set(f'{self.status_msg_base_text} - {self.time}')
        self.status_label.after(200, self.tick)


def main():
    mw = MainWindow()
    mw.mainloop()


if __name__ == '__main__':
    main()
