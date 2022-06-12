from mylib import check

IN = input('').split()

gr = [False]*(2**4)
char = []
isprint=gr[0];isinput=gr[1];iserror=gr[2];isnumer=gr[3]
isalpha=gr[4]

for tok in IN:
  if   tok == '0001': 
    for attr in gr:
        attr = False
    isprint = True
  elif tok == '0010':
    for attr in gr:
        attr = False
    isinput = True
  elif tok == '0011': 
    for attr in gr:
        attr = False
    iserror = True
  elif tok == '0100':
    for attr in gr[2:]:
        attr = False
    isnumer = True
  elif tok == '0101':
    for attr in gr[2:]:
        attr = False
    isalpha = True
  elif check(tok[2:],'01') and tok[:2] == "s'":
    char.append(tok[2:])
  else: print('Invalid value.')

if not isnumer:
  char = [chr(int(i,2)) for i in char]
else:
  char = [str(int(i,2)) for i in char]

if isprint:
    print(''.join(char))
elif isinput:
    input(''.join(char)+' ')
elif iserror:
    raise Exception(''.join(char)+'.')
