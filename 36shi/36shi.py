def enc(text):
  abc = {"","","","","","","","","","","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," ",".","?","!",",","'","-","_","+","=","/","(",")","[","]","{","}"}
  out = ""
  for c in range(len(text)):
    tx = text[c]
    for i in abc:
      if i == tx:
        kk = abc.index(i)
        kk = kk + 1
        out = out + str(kk)

  return out


def dec(num):
  abc = {"","","","","","","","","","","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," ",".","?","!",",","'","-","_","+","=","/","(",")","[","]","{","}"}
  num = str(num)
  x = 0
  r = len(str(num)) / 2 + 1
  out2 = ""
  while r > x:
    i = num[x]
    x = x + 1
    ii = num[x]
    i = i + ii
    i = int(i)
    o = abc[i - 1]
    out2 = out2 + o
    x = x + 1

  return out2
