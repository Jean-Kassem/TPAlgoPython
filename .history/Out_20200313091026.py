from validate import *

#Classe pour les données en sorties
#Il y a des tableau pour checker que les valeurs sont bien uniques

class Out:
    #Obligatoire
    #Alphanumérique
    #Unique
    ref_fournisseur = ""
    arr_ref_fournisseur = []

    #Obligatoire
    #Alphanumérique
    #Unique
    designation = ""
    arr_designation = []

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
    arr_code_barre = []

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
        #ref sap si pas de ref fournisseur
        out = ref_fourn if ref_fourn else ref_sap
        #Obligatoire
        is_ok = _mandatory(out)
        #Alphanumériuqe
        is_ok = isalnum(out) and is_ok

