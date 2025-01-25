num=''
while not num == 'q':
  num = int(input('please input your number: '))
  if (num % 5 == 0 and num % 3 == 0):
    print('FIZZBUZZ')
  elif (num % 3 == 0):
      print("FIZZ")
  elif (num % 5 == 0):
      print("BUZZ")
  else:
    print(num)