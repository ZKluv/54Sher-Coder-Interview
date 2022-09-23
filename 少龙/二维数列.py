def main():
   n = int(input('请输入二位数列的边长：'))
   num = [[' '] * n for i in range(1,n+1)]
   z = 1
   o = 0
   space = 0
   for y in range(0,n):
      for x in range(0,n):
         num[y][x] = z
         z += 1
   print('交换位置前：')
   for value in num:
      print(value)
   for y in range(0,n):
      for x in range(o,n):
         space = num[y][x]
         num[y][x] = num[x][y]
         num[x][y] = space
      o += 1
   print('交换位置后：')
   for value in num:
      print(value)
main()
input()