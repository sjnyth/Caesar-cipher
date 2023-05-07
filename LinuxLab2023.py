import sys

def cipher(your_msz, cipher_key):  
  cipher_list = []
  final = ""
  your_msz = your_msz.upper()
  for i in range(0, len(your_msz)):
   if ord(your_msz[i])>=65 and ord(your_msz[i]) <=90:
     cipher_char_ord = ((ord(your_msz[i]) + cipher_key -65)) % 26 + 65    
     cipher_char= chr(cipher_char_ord )
     cipher_list.append(cipher_char)
  
  for i in range(0,len(cipher_list), 5):  
      if i == 0 :    
        final = cipher_list[i:5]
        print(("".join(final)), end = " ") 
       
      elif i % 50 != 0:       
        j = i + 5
        final = cipher_list[i:j]
        print(("".join(final)), end = " ")
        
      else: # print new line and then print the same format
        print("")
        j = i + 5
        final = cipher_list[i:j]
        print(("".join(final)), end = " ")  
  print()
  return ""

k = int(sys.argv[1])
lines = []
for line in sys.stdin:
  lines.append(line)

cipher("".join(lines),k)