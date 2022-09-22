
def main():
   n = int(input('请输入行数：'))
   m = (n + 1) / 2
   x = 1 #列
   y = 1 #行
   z = m - 1 #每行前的空格数
   while y <= m:
      while z >= 0:
         print(' ', end='')
         z -= 1
      z = m - 1 - y
      while x <= y*2-1:
         print('*',end = '')
         x += 1
      print('\n')
      x = 1
      y += 1
   while y >= 1:
      while z >= 0:
         print(' ', end='')
         z -= 1
      z = m - y + 1
      while x <= y*2-1:
         print('*',end = '')
         x += 1
      print('\n')
      x = 1
      y -= 1

main()
input()