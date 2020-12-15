
import random

while(1):
  num = random.randint(0,1000)
  cube = num * num * num
  print(cube)
  key = input('Press Enter to continue, input \'q\' to quit.')
  print(num)
  print('')
  if key == 'q' or key == 'Q':
    break
  