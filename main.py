def f(x):
    "fonction a renseigner"
    return x**3+x+5

def convertisseur(i, n):
  return int((i * 10**n)/10**n)

def convertisseur_float(i, n):
  return int(i * 10**n) / 10**n            
             
def encadrement(n):
  """Premier et deuxième chiffre à changer en fonction des intervales"""
  cpt = -2
  while cpt <= -1:
    cpt = cpt + 10**-n
    if convertisseur(f(cpt),n) == 0:
      return convertisseur_float(cpt, n)
  return False



print(encadrement(7))