picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# for i in picture:
#   for p in i:
#     if (p):
#       print('*', end="")
#     else:
#       print(' ', end="")
#   print('')

for item in picture: 
    line = ""
    for n_item in item:
        line +="$" if n_item else " "
    print(line)