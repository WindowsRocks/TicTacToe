from tkinter import *
from tkinter.messagebox import showinfo
import itertools

win = Tk()

avail_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_1 = [] #X
player_2 = [] #O
def click(b_num):

	if 1 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "X")
			e1["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "X")
			e2["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "X")
			e3["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "X")
			e4["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "X")
			e5["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "X")
			e6["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "X")
			e7["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "X")
			e8["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "X")
			e9["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(1)

	elif 2 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "O")
			e1["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "O")
			e2["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "O")
			e3["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "O")
			e4["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "O")
			e5["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "O")
			e6["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "O")
			e7["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "O")
			e8["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "O")
			e9["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(2)

	elif  3 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "X")
			e1["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "X")
			e2["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "X")
			e3["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "X")
			e4["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "X")
			e5["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "X")
			e6["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "X")
			e7["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "X")
			e8["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "X")
			e9["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(3)

	elif 4 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "O")
			e1["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "O")
			e2["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "O")
			e3["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "O")
			e4["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "O")
			e5["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "O")
			e6["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "O")
			e7["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "O")
			e8["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "O")
			e9["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(4)

	elif 5 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "X")
			e1["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "X")
			e2["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "X")
			e3["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "X")
			e4["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "X")
			e5["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "X")
			e6["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "X")
			e7["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "X")
			e8["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "X")
			e9["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(5)
		else:
			""



	elif  6 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "O")
			e1["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "O")
			e2["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "O")
			e3["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "O")
			e4["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "O")
			e5["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "O")
			e6["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "O")
			e7["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "O")
			e8["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "O")
			e9["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(6)

	elif 7 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "X")
			e1["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "X")
			e2["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "X")
			e3["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "X")
			e4["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "X")
			e5["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "X")
			e6["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "X")
			e7["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "X")
			e8["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "X")
			e9["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(7)	

	elif 8 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "O")
			e1["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "O")
			e2["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "O")
			e3["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "O")
			e4["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "O")
			e5["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "O")
			e6["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "O")
			e7["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "O")
			e8["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "O")
			e9["state"] = DISABLED
			player_2.append(b_num)
			avail_moves.remove(8)

	elif 9 in avail_moves:
		if b_num == 1:
			e1 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e1.grid(row=0, column=0)
			e1.insert(0, "X")
			e1["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 2:
			e2 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e2.grid(row=0, column=1)
			e2.insert(0, "X")
			e2["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 3:	
			e3 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e3.grid(row=0, column=2)
			e3.insert(0, "X")
			e3["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 4:
			e4 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e4.grid(row=1, column=0)
			e4.insert(0, "X")
			e4["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 5:
			e5 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e5.grid(row=1, column=1)
			e5.insert(0, "X")
			e5["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 6:
			e6 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e6.grid(row=1, column=2)
			e6.insert(0, "X")
			e6["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 7:
			e7 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e7.grid(row=2, column=0)
			e7.insert(0, "X")
			e7["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 8:
			e8 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e8.grid(row=2, column=1)
			e8.insert(0, "X")
			e8["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)
		elif b_num == 9:
			e9 = Entry(win, width=2, borderwidth=3, font=("Calibri 24"))
			e9.grid(row=2, column=2)
			e9.insert(0, "X")
			e9["state"] = DISABLED
			player_1.append(b_num)
			avail_moves.remove(9)

	else:
		""

	set1 = itertools.permutations([1,2,3])
	set2 = itertools.permutations([3,5,7])
	set3 = itertools.permutations([1,5,9])
	set4 = itertools.permutations([4,5,6])
	set5 = itertools.permutations([7,8,9])
	set6 = itertools.permutations([1,4,7])
	set7 = itertools.permutations([2,5,8])
	set8 = itertools.permutations([3,6,9])	

	for i in set1, set2, set3, set4, set5, set6, set7, set7, set8:
		for j in list(i):
			p_1 = all(elem in player_1 for elem in j)
			p_2 = all(elem in player_2 for elem in j)

			if p_1 == True:
				print("Player X wins!!")
				showinfo("Game Result", "Player X wins!!")
				break
			elif p_2 == True:
				print("Player O wins")
				showinfo("Game Result", "Player O wins!!")
				break
			else:
				pass	
    																	



b1 = Button(win, padx=20, pady=20, command=lambda: click(1))
b2 = Button(win, padx=20, pady=20, command=lambda: click(2))
b3 = Button(win, padx=20, pady=20, command=lambda: click(3))
b4 = Button(win, padx=20, pady=20, command=lambda: click(4))
b5 = Button(win, padx=20, pady=20, command=lambda: click(5))
b6 = Button(win, padx=20, pady=20, command=lambda: click(6))
b7 = Button(win, padx=20, pady=20, command=lambda: click(7))
b8 = Button(win, padx=20, pady=20, command=lambda: click(8))
b9 = Button(win, padx=20, pady=20, command=lambda: click(9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


win.mainloop()