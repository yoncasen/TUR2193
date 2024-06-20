import random

def parola_yarat(parola_uzunlugu):
  karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

  parola = ""

  for i in range(parola_uzunlugu):
    parola += random.choice(karakterler)

  return parola

#print(parola_yarat(5))