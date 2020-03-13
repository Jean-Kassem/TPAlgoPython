import re

#Il y a une somme de contrôle pour l'EAN 13. Les 12 premiers chiffres sont le code et le dernier permet de faire un contrôle
def is_ean13(_str):
    _str = str(_str)
    #check du format (13 chiffres)
    if not re.search("[0-9]{13}", _str):
        return False
    
    #calcul de la somme de controle
    ponderations = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    _sum = 0
    key = 0

    for i in range(len(ponderations)):
        _sum = _sum + int(_str[i]) * ponderations[i]
    
    rest = _sum % 10

    if rest != 0:
        key = 10 - rest
    
    return int(_str[12]) == key

#on peut mettre un nombre indeterminé d'arguments, il faut qu'il y ait un moins un des parametres existants
def _mandatory(*_str):
    for _s in _str:
        if _s:
            return True
    return False

def _is_duplicate(_array, _str):
    exist = _str in _array
    _array.append(_str)
    return exist

#On lui envoi en premier argument le prix de vente et en deuxième le prix d'achat, 
# il retourne true si le prix de vente est bon et supérieur au prix d'achat
def _check_price(sell_price, buy_price):

  try:

    if(isinstance(int(sell_price), int) and int(sell_price) > 0 and buy_price < sell_price):
      flag = True    
    else:
      flag = False
  except:
    flag = False

  return flag

#Check if l'argument passé est bien un entier 
def _check_int(value):
  try:
    if(isinstance(int(value), int)):
      flag = True 
  except:
    flag = False

  return flag