from validate import *

class Out:
    #Obligatoire
    #Alphanumérique
    #Unique
    ref_fournisseur = ""

    #Obligatoire
    #Alphanumérique
    #Unique
    designation = ""

    #Obligatoire
    #Numérique
    litrage = 0

    #Non obligatoire
    #Numérique
    conditionnement = 0

    #Obligatoire
    #Numérique
    #Unique
    #EAN13
    code_barre = 0

    #Obligatoire
    #Numérique
    prix_achat = 0

    #Obligatoire
    #Numérique
    prix_vente = 0

    #Obligatoire
    _type = ""

    #Obligatoire
    modele = ""

    #Obligatoire
    marque = ""

    def set_ref_fournisseur(self, ref_fourn, ref_sap):
