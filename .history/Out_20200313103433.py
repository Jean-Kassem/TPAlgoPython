from validate import _mandatory
from validate import _is_duplicate
from validate import _check_price
from validate import is_ean13

#Classe pour les données en sorties
#Il y a des tableau pour checker que les valeurs sont bien uniques

class Out:
    #1
    #Obligatoire
    #Alphanumérique
    #Unique
    ref_fournisseur = ""
    arr_ref_fournisseur = []

    #2
    #Obligatoire
    #Alphanumérique
    #Unique
    designation = ""
    arr_designation = []

    #3
    #Obligatoire
    #Numérique
    litrage = 0

    #4
    #Non obligatoire
    #Numérique
    conditionnement = 0

    #5
    #Obligatoire
    #Numérique
    #Unique
    #EAN13
    code_barre = 0
    arr_code_barre = []

    #6
    #Obligatoire
    #Numérique
    prix_achat = 0

    #7
    #Obligatoire
    #Numérique
    prix_vente = 0

    #8
    #Obligatoire
    _type = ""

    #9
    #Obligatoire
    modele = ""

    #10
    #Obligatoire
    marque = ""

    def __init__(self, ref_fournisseur, ref_sap, designation, litrage, conditionnement, code_barre, prix_achat, prix_vente, _type, modele, marque):
        self.set_ref_fournisseur(ref_fournisseur, ref_sap)
        self.set_designation(designation)
        self.set_litrage(litrage)
        self.set_conditionnement(conditionnement)
        self.set_code_barre(code_barre)
        self.set_prix(prix_achat, prix_vente)
        self.set_type(_type)
        self.set_modele(modele)
        self.set_marque(marque)

    #1
    def set_ref_fournisseur(self, ref_fourn, ref_sap):
        #ref sap si pas de ref fournisseur
        out = ref_fourn if ref_fourn else ref_sap
        #Obligatoire
        is_ok = _mandatory(out)
        #Alphanumériuqe
        is_ok = out.isalnum() and is_ok
        #Unique
        is_ok = not _is_duplicate(Out.arr_ref_fournisseur, out) and is_ok

        if is_ok:
            self.ref_fournisseur = out
        
        return is_ok

    #2
    def set_designation(self, designation):
        out = designation
        #Obligatoire
        is_ok = _mandatory(out)
        #Alphanumérique
        is_ok = out.isalnum() and is_ok
        #Unique
        is_ok = not _is_duplicate(Out.arr_designation, out) and is_ok

        if is_ok:
            self.designation = out
        
        return is_ok
    
    #3
    def set_litrage(self, litrage):
        out = litrage
        #Obligatoire
        is_ok = _mandatory(out)
        #Numerique
        is_ok = str(out).isnumeric() and is_ok

        if is_ok:
            self.litrage = out
        
        return is_ok
    
    #4
    def set_conditionnement(self, conditionnement):
        out = conditionnement
        #Numérique
        is_ok = str(out).isnumeric()

        if is_ok:
            self.conditionnement = out
        
        return is_ok

    #5
    def set_code_barre(self, code_barre):
        out = code_barre
        #Obligatoire
        is_ok = _mandatory(out)
        #Unique
        is_ok = not _is_duplicate(Out.arr_code_barre, out) and is_ok
        #EAN-13
        is_ok = is_ean13(out) and is_ok

        if is_ok:
            self.code_barre = code_barre
        
        return is_ok
    
    #6-7
    def set_prix(self, prix_achat, prix_vente):
        out_achat = prix_achat
        out_vente = prix_vente
        #Obligatoire
        is_ok = _mandatory(out_achat)
        is_ok = _mandatory(out_vente) and is_ok 
        #numérique
        is_ok = str(out_achat).isnumeric() and is_ok
        is_ok = str(out_vente).isnumeric() and is_ok
        #prix de vente au dessus du prix d'achat
        is_ok = _check_price(prix_vente, prix_achat) and is_ok

        if is_ok:
            self.prix_achat = prix_achat
            self.prix_vente = prix_vente
        
        return is_ok
    
    #8
    def set_type(self, _type):
        out = _type

        is_ok = _mandatory(_type)

        if is_ok:
            self._type = out

        return is_ok

    #9
    def set_modele(self, modele):
        out = modele

        is_ok = _mandatory(modele)

        if is_ok:
            self.modele = modele

        return is_ok

    #10
    def set_marque(self, marque):
        out = marque

        is_ok = _mandatory(out)

        if is_ok:
            self.marque = out
        
        return is_ok
    
    def __str__(self):
        return (
            self.ref_fournisseur + "," +
            self.designation + "," +
            self.litrage + "," +
            self.conditionnement + "," +
            self.code_barre + "," +
            self.prix_achat + "," +
            self.prix_vente + "," +
            self._type + "," +
            self.modele + "," +
            self.marque
        )