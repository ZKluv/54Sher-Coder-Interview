def zhishu():
	o = int(input('若开始请输入数字0：'))
	while o == 0:
		n = int(input('请输入数字:'))
		print('在2到',n,'之间的质数有：')
		a = [True] * (n+1)
		for b in range(2,n+1):
			if a[b]:
				print(b,end=' ')
				for i in range(b * 2,n+1,b):
					a[i] = False
		o = int(input('\n输入非0数即可退出（输入0则继续）：'))

zhishu()
input()
