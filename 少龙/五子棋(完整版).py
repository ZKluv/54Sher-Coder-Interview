n = 15
qipan = [['.'] * n for i in range(n)]
def main():
	q = 0 #计数，奇数为Player1,偶数为Player2
	print('1.PvP\n2.PvC\n3.CvC\n4.退出')
	w = int(input('请选择模式：'))
	global qipan
	while w != 4:
		qipan = [['.'] * n for i in range(n)]
		o = False
		if w == 1:
			print('选择模式1\n')
			while not o:
				print_qipan()
				q += 1
				if q == 225:
					print('棋盘被下满了！！！\n')
					break
				print('玩家1为：X   玩家2为：O   玩家1先手\n')
				f = 'X' if q % 2 > 0 else 'O'
				if q % 2 > 0:
					print('玩家1下子：\n')
				else:
					print('玩家2下子：\n')
				get_qizi(f)
				o = jiance()
			break
		if w == 2:
			print('选择模式2\n')
			print('电脑玩家加入战场。\n')
			while not o:
				print_qipan()
				q += 1
				if q == 225:
					print('棋盘被下满了！！！\n')
					break
				print('玩家1为：X   玩家2为：O   玩家1先手\n')
				f = 'X' if q % 2 > 0 else 'O'
				if q % 2 > 0:
					print('玩家1下子：\n')
					get_qizi(f)
				else:
					print('电脑下子：\n')
					cpu(f)
				o = jiance()
			break
		if w == 3:
			print('选择模式3\n')
			print('电脑玩家加入战场。\n')
			while not o:
				print_qipan()
				q += 1
				if q == 225:
					print('棋盘被下满了！！！\n')
					break
				print('玩家1为：X   玩家2为：O   玩家1先手\n')
				f = 'X' if q % 2 > 0 else 'O'
				if q % 2 > 0:
					print('电脑1下子：\n')
					cpu_1(f)
				else:
					print('电脑2下子：\n')
					cpu(f)
				o = jiance()
			break

def print_qipan():
        for m in range(1,16):
            print(m,end='\t')
        print('\n')
        for i in range(len(qipan)):
                for j in range(len(qipan[i])):
                        print(qipan[i][j],end='\t')
                        if j == 14:
                                print(i + 1)
                                print('\n')

def get_qizi(f):
	while True:
		a = input('请输入下子坐标(先行后列)（格式为x,y）(逗号为英文字符中的逗号)')
		b = []
		b = a.split(',')
		x = int(b[0]) - 1
		y = int(b[1]) - 1
		if x > 14 or y > 14:
			print('超出范围！！！\n')
			continue
		elif qipan[x][y] != '.':
			print('此处已下过\n')
			continue
		else:
			qipan[x][y] = f
			break

def jiance():
	a = []#横，玩家1
	b = []#竖
	c = []#向右斜
	d = []#向左斜
	a2 = []#横，玩家2
	b2 = []#竖
	c2 = []#向右斜
	d2 = []#向左斜
	for i in range(len(qipan)):
		for j in range(len(qipan[i])):
			a = []#横，玩家1
			b = []#竖
			c = []#向右斜
			d = []#向左斜
			a2 = []#横，玩家2
			b2 = []#竖
			c2 = []#向右斜
			d2 = []#向左斜
			if qipan[i][j] == 'X':
				a.append(qipan[i][j])
				b.append(qipan[i][j])
				c.append(qipan[i][j])
				d.append(qipan[i][j])
				for q in range(1,3):
					try:
						a.append(qipan[i][j + q])
						a.append(qipan[i][j - q])
						b.append(qipan[i + q][j])
						b.append(qipan[i - q][j])
						c.append(qipan[i + q][j + q])
						c.append(qipan[i - q][j - q])
						d.append(qipan[i - q][j + q])
						d.append(qipan[i + q][j - q])
						if a.count('X') == 5 or b.count('X') == 5 or c.count('X') == 5 or d.count('X') == 5:
							print('玩家1获胜！\n')
							print_qipan()
							return True
					except:
						continue
			elif qipan[i][j] == 'O':
				a2.append(qipan[i][j])
				b2.append(qipan[i][j])
				c2.append(qipan[i][j])
				d2.append(qipan[i][j])
				for q in range(1,3):
					try:
						a2.append(qipan[i][j + q])
						a2.append(qipan[i][j - q])
						b2.append(qipan[i + q][j])
						b2.append(qipan[i - q][j])
						c2.append(qipan[i + q][j + q])
						c2.append(qipan[i - q][j - q])
						d2.append(qipan[i - q][j + q])
						d2.append(qipan[i + q][j - q])
						if a2.count('O') == 5 or b2.count('O') == 5 or c2.count('O') == 5 or d2.count('O') == 5:
							print('玩家2获胜！\n')
							print_qipan()
							return True
					except:
						continue

def cpu(f):
	import random
	for i in range(len(qipan)):
		for j in range(len(qipan[i])):
			try:
				#插对方空位
				if qipan[i][j] != '.':
					continue
				if qipan[i+1][j+1] == 'X' and qipan[i-1][j-1] == 'X':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'X' and qipan[i+1][j-1] == 'X':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i][j+1] == 'X' and qipan[i][j-1] == 'X':#横
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'X' and qipan[i-1][j] == 'X':#竖
					qipan[i][j] = f
					return
				#拦截对手
				elif qipan[i][j+1] == 'X' and qipan[i][j+2] == 'X' and qipan[i][j+3] == 'X':#横
					qipan[i][j] = f
					return
				elif qipan[i][j-1] == 'X' and qipan[i][j-2] == 'X' and qipan[i][j-3] == 'X':
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'X' and qipan[i+2][j] == 'X' and qipan[i+3][j] == 'X':#竖
					qipan[i][j] = f
					return
				elif qipan[i-1][j] == 'X' and qipan[i-2][j] == 'X' and qipan[i-3][j] == 'X':
					qipan[i][j] = f
					return
				elif qipan[i+1][j+1] == 'X' and qipan[i+2][j+2] == 'X' and qipan[i+3][j+3] == 'X':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j-1] == 'X' and qipan[i-2][j-2] == 'X' and qipan[i-3][j-3] == 'X':
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'X' and qipan[i-2][j+2] == 'X' and qipan[i-3][j+3] == 'X':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i+1][j-1] == 'X' and qipan[i+2][j-2] == 'X' and qipan[i+3][j-3] == 'X':
					qipan[i][j] = f
					return
				#拦截对手决胜
				elif qipan[i][j+1] == 'X' and qipan[i][j+2] == 'X' and qipan[i][j+3] == 'X' and qipan[i][j+4] == 'X' and qipan[i][j+5] == 'O':#横
					qipan[i][j] = f
					return
				elif qipan[i][j-1] == 'X' and qipan[i][j-2] == 'X' and qipan[i][j-3] == 'X' and qipan[i][j-4] == 'X' and qipan[i][j-5] == 'O':
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'X' and qipan[i+2][j] == 'X' and qipan[i+3][j] == 'X' and qipan[i+4][j] == 'X' and qipan[i+5][j] == 'O':#竖
					qipan[i][j] = f
					return
				elif qipan[i-1][j] == 'X' and qipan[i-2][j] == 'X' and qipan[i-3][j] == 'X' and qipan[i-4][j] == 'X' and qipan[i-5][j] == 'O':
					qipan[i][j] = f
					return
				elif qipan[i+1][j+1] == 'X' and qipan[i+2][j+2] == 'X' and qipan[i+3][j+3] == 'X' and qipan[i+4][j+4] == 'X' and qipan[i+5][j+5] == 'O':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j-1] == 'X' and qipan[i-2][j-2] == 'X' and qipan[i-3][j-3] == 'X' and qipan[i-4][j-4] == 'X' and qipan[i-5][j-5] == 'O':
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'X' and qipan[i-2][j+2] == 'X' and qipan[i-3][j+3] == 'X' and qipan[i-4][j+4] == 'X' and qipan[i-5][j+5] == 'O':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i+1][j-1] == 'X' and qipan[i+2][j-2] == 'X' and qipan[i+3][j-3] == 'X' and qipan[i+4][j-4] == 'X' and qipan[i+5][j-5] == 'O':
					qipan[i][j] = f
					return
				#插自己空位
				elif qipan[i+1][j+1] == 'O' and qipan[i-1][j-1] == 'O':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'O' and qipan[i+1][j-1] == 'O':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i][j+1] == 'O' and qipan[i][j-1] == 'O':#横
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'O' and qipan[i-1][j] == 'O':#竖
					qipan[i][j] = f
					return
				#决胜
				elif (qipan[i][j+1] == 'O' and qipan[i][j+2] == 'O'and qipan[i][j+3] == 'O'and qipan[i][j+4] == 'O') or (qipan[i][j+1] == 'O' and qipan[i][j+2] == 'O'and qipan[i][j+3] == 'O') or (qipan[i][j+1] == 'O' and qipan[i][j+2] == 'O') or (qipan[i][j+1] == 'O'):#横
					qipan[i][j] = f
					return
				elif (qipan[i][j-1] == 'O' and qipan[i][j-2] == 'O'and qipan[i][j-3] == 'O'and qipan[i][j-4] == 'O') or (qipan[i][j-1] == 'O' and qipan[i][j-2] == 'O'and qipan[i][j-3] == 'O') or (qipan[i][j-1] == 'O' and qipan[i][j-2] == 'O') or (qipan[i][j-1] == 'O'):
					qipan[i][j] = f
					return
				elif (qipan[i+1][j] == 'O' and qipan[i+2][j] == 'O'and qipan[i+3][j] == 'O'and qipan[i+4][j] == 'O') or (qipan[i+1][j] == 'O' and qipan[i+2][j] == 'O'and qipan[i+3][j] == 'O') or (qipan[i+1][j] == 'O' and qipan[i+2][j] == 'O') or (qipan[i+1][j] == 'O'):#竖
					qipan[i][j] = f
					return
				elif (qipan[i-1][j] == 'O' and qipan[i-2][j] == 'O'and qipan[i-3][j] == 'O'and qipan[i-4][j] == 'O') or (qipan[i-1][j] == 'O' and qipan[i-2][j] == 'O'and qipan[i-3][j] == 'O') or (qipan[i-1][j] == 'O' and qipan[i-2][j] == 'O') or (qipan[i-1][j] == 'O'):
					qipan[i][j] = f
					return
				elif (qipan[i+1][j+1] == 'O' and qipan[i+2][j+2] == 'O'and qipan[i+3][j+3] == 'O'and qipan[i+4][j+4] == 'O') or (qipan[i+1][j+1] == 'O' and qipan[i+2][j+2] == 'O'and qipan[i+3][j+3] == 'O') or (qipan[i+1][j+1] == 'O' and qipan[i+2][j+2] == 'O') or (qipan[i+1][j+1] == 'O'):#向右斜
					qipan[i][j] = f
					return
				elif (qipan[i-1][j-1] == 'O' and qipan[i-2][j-2] == 'O'and qipan[i-3][j-3] == 'O'and qipan[i-4][j-4] == 'O') or (qipan[i-1][j-1] == 'O' and qipan[i-2][j-2] == 'O'and qipan[i-3][j-3] == 'O') or (qipan[i-1][j-1] == 'O' and qipan[i-2][j-2] == 'O') or (qipan[i-1][j-1] == 'O'):
					qipan[i][j] = f
					return
				elif (qipan[i+1][j-1] == 'O' and qipan[i+2][j-2] == 'O'and qipan[i+3][j-3] == 'O'and qipan[i+4][j-4] == 'O') or (qipan[i+1][j-1] == 'O' and qipan[i+2][j-2] == 'O'and qipan[i+3][j-3] == 'O') or (qipan[i+1][j-1] == 'O' and qipan[i+2][j-2] == 'O') or (qipan[i+1][j-1] == 'O'):#向左斜
					qipan[i][j] = f
					return
				elif (qipan[i-1][j+1] == 'O' and qipan[i-2][j+2] == 'O'and qipan[i-3][j+3] == 'O'and qipan[i-4][j+4] == 'O') or (qipan[i-1][j+1] == 'O' and qipan[i-2][j+2] == 'O'and qipan[i-3][j+3] == 'O') or (qipan[i-1][j+1] == 'O' and qipan[i-2][j+2] == 'O') or (qipan[i-1][j+1] == 'O'):
					qipan[i][j] = f
					return
				else:
					continue
			except:
				continue
	for o in range(0,100):
		x = random.randint(0,15)
		y = random.randint(0,15)
		if x > 14 or y > 14:
			continue
		elif qipan[x][y] != '.':
			continue
		else:
			qipan[x][y] = f
			break

def cpu_1(f):
	import random
	for i in range(len(qipan)):
		for j in range(len(qipan[i])):
			try:
				#插对方空位
				if qipan[i][j] != '.':
					continue
				if qipan[i+1][j+1] == 'O' and qipan[i-1][j-1] == 'O':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'O' and qipan[i+1][j-1] == 'O':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i][j+1] == 'O' and qipan[i][j-1] == 'O':#横
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'O' and qipan[i-1][j] == 'O':#竖
					qipan[i][j] = f
					return
				#拦截对手
				elif qipan[i][j+1] == 'O' and qipan[i][j+2] == 'O' and qipan[i][j+3] == 'O':#横
					qipan[i][j] = f
					return
				elif qipan[i][j-1] == 'O' and qipan[i][j-2] == 'O' and qipan[i][j-3] == 'O':
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'O' and qipan[i+2][j] == 'O' and qipan[i+3][j] == 'O':#竖
					qipan[i][j] = f
					return
				elif qipan[i-1][j] == 'O' and qipan[i-2][j] == 'O' and qipan[i-3][j] == 'O':
					qipan[i][j] = f
					return
				elif qipan[i+1][j+1] == 'O' and qipan[i+2][j+2] == 'O' and qipan[i+3][j+3] == 'O':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j-1] == 'O' and qipan[i-2][j-2] == 'O' and qipan[i-3][j-3] == 'O':
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'O' and qipan[i-2][j+2] == 'O' and qipan[i-3][j+3] == 'O':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i+1][j-1] == 'O' and qipan[i+2][j-2] == 'O' and qipan[i+3][j-3] == 'O':
					qipan[i][j] = f
					return
				#拦截对手决胜
				elif qipan[i][j+1] == 'O' and qipan[i][j+2] == 'O' and qipan[i][j+3] == 'O' and qipan[i][j+4] == 'O' and qipan[i][j+5] == 'X':#横
					qipan[i][j] = f
					return
				elif qipan[i][j-1] == 'O' and qipan[i][j-2] == 'O' and qipan[i][j-3] == 'O' and qipan[i][j-4] == 'O' and qipan[i][j-5] == 'X':
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'O' and qipan[i+2][j] == 'O' and qipan[i+3][j] == 'O' and qipan[i+4][j] == 'O' and qipan[i+5][j] == 'X':#竖
					qipan[i][j] = f
					return
				elif qipan[i-1][j] == 'O' and qipan[i-2][j] == 'O' and qipan[i-3][j] == 'O' and qipan[i-4][j] == 'O' and qipan[i-5][j] == 'X':
					qipan[i][j] = f
					return
				elif qipan[i+1][j+1] == 'O' and qipan[i+2][j+2] == 'O' and qipan[i+3][j+3] == 'O' and qipan[i+4][j+4] == 'O' and qipan[i+5][j+5] == 'X':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j-1] == 'O' and qipan[i-2][j-2] == 'O' and qipan[i-3][j-3] == 'O' and qipan[i-4][j-4] == 'O' and qipan[i-5][j-5] == 'X':
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'O' and qipan[i-2][j+2] == 'O' and qipan[i-3][j+3] == 'O' and qipan[i-4][j+4] == 'O' and qipan[i-5][j+5] == 'X':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i+1][j-1] == 'O' and qipan[i+2][j-2] == 'O' and qipan[i+3][j-3] == 'O' and qipan[i+4][j-4] == 'O' and qipan[i+5][j-5] == 'X':
					qipan[i][j] = f
					return
				#插自己空位
				elif qipan[i+1][j+1] == 'X' and qipan[i-1][j-1] == 'X':#向右斜
					qipan[i][j] = f
					return
				elif qipan[i-1][j+1] == 'X' and qipan[i+1][j-1] == 'X':#向左斜
					qipan[i][j] = f
					return
				elif qipan[i][j+1] == 'X' and qipan[i][j-1] == 'X':#横
					qipan[i][j] = f
					return
				elif qipan[i+1][j] == 'X' and qipan[i-1][j] == 'X':#竖
					qipan[i][j] = f
					return
				#决胜
				elif (qipan[i][j+1] == 'X' and qipan[i][j+2] == 'X'and qipan[i][j+3] == 'X'and qipan[i][j+4] == 'X') or (qipan[i][j+1] == 'X' and qipan[i][j+2] == 'X'and qipan[i][j+3] == 'X') or (qipan[i][j+1] == 'X' and qipan[i][j+2] == 'X') or (qipan[i][j+1] == 'X'):#横
					qipan[i][j] = f
					return
				elif (qipan[i][j-1] == 'X' and qipan[i][j-2] == 'X'and qipan[i][j-3] == 'X'and qipan[i][j-4] == 'X') or (qipan[i][j-1] == 'X' and qipan[i][j-2] == 'X'and qipan[i][j-3] == 'X') or (qipan[i][j-1] == 'X' and qipan[i][j-2] == 'X') or (qipan[i][j-1] == 'X'):
					qipan[i][j] = f
					return
				elif (qipan[i+1][j] == 'X' and qipan[i+2][j] == 'X'and qipan[i+3][j] == 'X'and qipan[i+4][j] == 'X') or (qipan[i+1][j] == 'X' and qipan[i+2][j] == 'X'and qipan[i+3][j] == 'X') or (qipan[i+1][j] == 'X' and qipan[i+2][j] == 'X') or (qipan[i+1][j] == 'X'):#竖
					qipan[i][j] = f
					return
				elif (qipan[i-1][j] == 'X' and qipan[i-2][j] == 'X'and qipan[i-3][j] == 'X'and qipan[i-4][j] == 'X') or (qipan[i-1][j] == 'X' and qipan[i-2][j] == 'X'and qipan[i-3][j] == 'X') or (qipan[i-1][j] == 'X' and qipan[i-2][j] == 'X') or (qipan[i-1][j] == 'X'):
					qipan[i][j] = f
					return
				elif (qipan[i+1][j+1] == 'X' and qipan[i+2][j+2] == 'X'and qipan[i+3][j+3] == 'X'and qipan[i+4][j+4] == 'X') or (qipan[i+1][j+1] == 'X' and qipan[i+2][j+2] == 'X'and qipan[i+3][j+3] == 'X') or (qipan[i+1][j+1] == 'X' and qipan[i+2][j+2] == 'X') or (qipan[i+1][j+1] == 'X'):#向右斜
					qipan[i][j] = f
					return
				elif (qipan[i-1][j-1] == 'X' and qipan[i-2][j-2] == 'X'and qipan[i-3][j-3] == 'X'and qipan[i-4][j-4] == 'X') or (qipan[i-1][j-1] == 'X' and qipan[i-2][j-2] == 'X'and qipan[i-3][j-3] == 'X') or (qipan[i-1][j-1] == 'X' and qipan[i-2][j-2] == 'X') or (qipan[i-1][j-1] == 'X'):
					qipan[i][j] = f
					return
				elif (qipan[i+1][j-1] == 'X' and qipan[i+2][j-2] == 'X'and qipan[i+3][j-3] == 'X'and qipan[i+4][j-4] == 'X') or (qipan[i+1][j-1] == 'X' and qipan[i+2][j-2] == 'X'and qipan[i+3][j-3] == 'X') or (qipan[i+1][j-1] == 'X' and qipan[i+2][j-2] == 'X') or (qipan[i+1][j-1] == 'X'):#向左斜
					qipan[i][j] = f
					return
				elif (qipan[i-1][j+1] == 'X' and qipan[i-2][j+2] == 'X'and qipan[i-3][j+3] == 'X'and qipan[i-4][j+4] == 'X') or (qipan[i-1][j+1] == 'X' and qipan[i-2][j+2] == 'X'and qipan[i-3][j+3] == 'X') or (qipan[i-1][j+1] == 'X' and qipan[i-2][j+2] == 'X') or (qipan[i-1][j+1] == 'X'):
					qipan[i][j] = f
					return
				else:
					continue
			except:
				continue
	for o in range(0,100):
		x = random.randint(0,15)
		y = random.randint(0,15)
		if x > 14 or y > 14:
			continue
		elif qipan[x][y] != '.':
			continue
		else:
			qipan[x][y] = f
			break

main()
input()
