### Convertir des secondes ###
"""
AIDE
Année = 60 x 60 x 24 x 365
Mois  = 60 x 60 x 24 x (365/12)
Jour  = 60 x 60 x 24
Heure = 60 x 60
Min   = 60
"""

def conversion():
    s = int(input("Entrez votre nombre entier de seconde : "))
                            ## Année
    an = 60*60*24*365
    if s % an != 0:
        year = s // an # il faut stocker la variable dans une autre pour la retenir
        s = s % an
    else:
        year = s / an
        s = s % an

                                ## Mois
    m = 60*60*24*(365/12) 
    if s % m != 0:
        mois = s // m 
        s = s % m
    else:
        mois = s / m
        s = s % m

                                    ## Jour
    j = 60*60*24
    if s % j != 0:
        day = s // j
        s = s % j
    else:
        day = s / j
        s = s % j

                                        ## Heure
    h = 60*60
    if s % h != 0:
        heure = s // h
        s = s % h
    else:
        heure = s / h
        s = s % h

                                            ## Minute
    mi = 60
    if s % mi != 0:
        minute = s // mi
        s = s % mi
    else:
        minute = s / mi
        s = s % mi

                                                ## Total
        
    return(print(year ,"année(s)", mois , "mois", day ,"jour(s)", heure ,"heure(s)", minute , "minute(s)", s , "seconde(s)."))

conversion()
