import matplotlib.pyplot as pl
import pandas as pd
import numpy as np


#### Prétraitement
   #PRE 1
       #client
def filtrage_client(A,B):
    import csv
    with open(A) as TD:
        TD=csv.reader(TD,delimiter=',')
        emp=open(B,'w')
        line_count=0
        for ligne in TD:
            if ligne[1]=='' :
                line_count+=0
            else:
                emp.write(f'{ligne[0]},{ligne[1]},{ligne[2]},{ligne[3]},{ligne[4]},{ligne[5]},{ligne[6]},{ligne[7]},{ligne[8]},{ligne[9]},{ligne[10]},{ligne[11]},{ligne[12]} \n')
        emp.close()
    return(0)
filtrage_client('clients.csv','clients_new.csv')
    #employee
def filtrage_employe(A,B):
    import csv
    with open(A) as TD:
        TD=csv.reader(TD,delimiter=',')
        emp=open(B,'w')
        line_count=0
        for ligne in TD:
            if ligne[1]=='' :
                line_count+=0
            else:
                emp.write(f'{ligne[0]},{ligne[1]},{ligne[2]},{ligne[3]},{ligne[4]},{ligne[5]},{ligne[6]},{ligne[7]} \n')
        emp.close()
    return(0)
filtrage_employe('emplyes.csv','employes_new.csv')

#PRE 2
def poste(A):
    import csv
    with open(A) as TD:
        TD=csv.reader(TD,delimiter=',')
        ficha=open('client_null.csv','w')
        for ligne in TD:
            if ligne[9]=='NULL' :
                ligne[9]='00000'
                ficha.write(f'{ligne[0]},{ligne[1]},{ligne[2]},{ligne[3]},{ligne[4]},{ligne[5]},{ligne[6]},{ligne[7]},{ligne[8]},{ligne[9]},{ligne[10]},{ligne[11]},{ligne[12]} \n')
            else:
                ficha.write(f'{ligne[0]},{ligne[1]},{ligne[2]},{ligne[3]},{ligne[4]},{ligne[5]},{ligne[6]},{ligne[7]},{ligne[8]},{ligne[9]},{ligne[10]},{ligne[11]},{ligne[12]} \n')
    return(0)
poste('clients.csv')


##statistique
def num_missing(x):
    return sum(x.isnull())
def stats(colonne, b):
    #b = int(input("Entrer 0 pour les clients_employes et 1 pour les employée "))
    if b==0:
        clients_employes= pd.read_csv('client_new.csv')
    elif b==1:
        clients_employes=pd.read_csv('employes_new.csv')
    else:
        print("erreur aucune table correspondante")
    print(clients_employes.info())
    #colonne = input("Choisir une colonne de notre du dataframe:  ")
    if clients_employes[colonne].dtype == 'object':
        print(clients_employes[colonne].value_counts())
        print('Valeurs manquantes')
        print(num_missing(clients_employes[colonne]))
        clients_employes[colonne].value_counts().plot(kind='bar')
        pl.show()
    if clients_employes[colonne].dtype == 'float64':
        print("la moyenne est: " ,clients_employes[colonne].mean())
        print("la min est: ", clients_employes[colonne].min())
        print("la max est: ", clients_employes[colonne].max())
        print('Valeurs manquantes: ',num_missing(clients_employes[colonne]))
        clients_employes[colonne].plot.hist(bins=20)
        pl.show()


#STAT 2
def sup(a):
    TD=open('employes_new.csv','r')
    import csv
    TD=csv.reader(TD,delimiter=',')
    l=[]
    n=0
    for ligne in TD:
        if ligne[6]==str(a):
            l.append(ligne[0])
            n+=1
    while l!=[]:
        k=[]
        for x in l:
            TD=open('employes_new.csv','r')
            import csv
            TD=csv.reader(TD,delimiter=',')
            for ligne in TD:
                if ligne[6]==x:
                    k.append(ligne[0])
                    n+=1
        l=k
    print('lemployee numero',a,'est le superieur de',n,'employes\n')
    return(n)

def tosup():
    TD = open('employes_new.csv', 'r')
    import csv
    
    TD = csv.reader(TD, delimiter=',')
    num_employe = []
    nbe_subordonnes = []
    for ligne in TD:
        num_employe.append(ligne[0])
    num_employe.remove('employeeNumber')
    for x in num_employe:
        nbe_subordonnes.append(sup(x))
    import matplotlib.pyplot as pl
    
    pl.plot(num_employe, nbe_subordonnes)
    pl.title('NOMBRE DEMPLOYEE INFERIEUR')
    pl.xticks(rotation=90)
    pl.xlabel('NUM EMPLOYEE')
    pl.ylabel('NBRE DEMPLOYEE INFERIERUR')
    pl.show


#STATS 3
def nbre_client(a):
    import csv
    n = 0
    TD = open('clients.csv', 'r')
    TD = csv.reader(TD, delimiter=',')
    for ligne in TD:
        if ligne[11] == str(a):
            n += 1
    print('le nombre de clients de lemployee', a, 'est', n)
    return (n)

def tnbre_client():
    import csv
    num_employe = []
    TD = open('employes_new.csv', 'r')
    TD = csv.reader(TD, delimiter=',')
    for ligne in TD:
        num_employe.append(ligne[0])
    del num_employe[0]
    nbe_clients = []
    for i in num_employe:
        nbre_client(i)
        nbe_clients.append(nbre_client(i))
    import matplotlib.pyplot as pl
    pl.plot(num_employe, nbe_clients)
    pl.title('NOMBRE DE CLIENTS DE CHAQUE EMPLOYEE')
    pl.xlabel('NUM EMPLOYEE')
    pl.xticks(rotation=90)
    pl.ylabel('NBRE DE CLIENTS')
    pl.show
    

# CDD 1
def nbre_credit(a):
    TD = open('clients.csv', 'r')
    import csv
    TD = csv.reader(TD, delimiter=',')
    s = 0
    for ligne in TD:
        if ligne[11] == str(a):
            print(ligne[12])
            s += float(ligne[12])
    print('le total de credit de lemployee', a, 'est', s, '\n')
    return ('le nombre total de credit de lemployee', a, 'est', s)


# CCD 2
def empcredit():
    ficha = open('emp_credit.tnum_employet', 'w')
    TD = open('employes_new.csv', 'r')
    import csv
    TD = csv.reader(TD, delimiter=',')
    num_employe = []

    for ligne in TD:
        num_employe.append(ligne[0])
    num_employe.remove('employeeNumber')
    for i in num_employe:
        nbre_credit(int(i))
        ficha.write(f' {nbre_credit(int(i))}\n')

    import matplotlib.pyplot as pl
    total_credit = 0
    total_credit_par_employe = []

    for a in num_employe:
        print(a)
        TD = open('clients.csv', 'r')
        import csv
        TD = csv.reader(TD, delimiter=',')
        for ligne in TD:
            if ligne[11] == str(a):
                print(ligne[12])
                total_credit += float(ligne[12])
        print('le total de credit de lemployee', a, 'est', total_credit, '\n')
        total_credit_par_employe.append(total_credit)

    pl.plot(num_employe, total_credit_par_employe, fillstyle='top')
    pl.title('CREDIT PAR EMPLOYES')
    pl.num_employeticks(rotation=90)
    pl.num_employelabel('NUMERO EMPLOYE')
    pl.ylabel('CREDIT')
    pl.show


# CCD 3
def ville():
    ficha = open('ville.txt', 'w')
    TD = open('client_new.csv', 'r')
    import csv
    TD = csv.reader(TD, delimiter=',')
    h = []
    total_credit_par_ville = []
    for ligne in TD:
        h.append(ligne[7])
    ville = list(set(h))
    ville.remove('city')
    for i in ville:
        s = 0
        TD = open('client_new.csv', 'r')
        TD = csv.reader(TD, delimiter=',')
        for ligne in TD:
            if ligne[7] == i:
                s += float(ligne[12])
            else:
                s += 0
        total_credit_par_ville.append(s)
        ficha.write(f' le total de credit de la ville de {i} est {s} \n')
    import matplotlib.pyplot as pl
    pl.plot(ville, total_credit_par_ville)
    pl.title('CREDIT PAR VILLE')
    pl.xticks(rotation=90)
    pl.xlabel('VILLE')
    pl.ylabel('CREDIT')
    pl.show()


# CDD 4
def pays():
    ficha = open('pays.txt', 'w')
    TD = open('Client_new.csv', 'r')
    import csv
    TD = csv.reader(TD, delimiter=',')
    h = []
    total_credit_par_pays = []
    for ligne in TD:
        h.append(ligne[10])
    print(h)
    pays = list(set(h))
    pays.remove('country')
    for i in pays:
        s = 0
        print(i)
        TD = open('client_new.csv', 'r')
        TD = csv.reader(TD, delimiter=',')
        for ligne in TD:
            if ligne[10] == i:
                s += float(ligne[12])
            else:
                s += 0
        total_credit_par_pays.append(s)
        ficha.write(f'le total de credit du pays {i} est {s} \n')
    import matplotlib.pyplot as pl
    pl.plot(pays, total_credit_par_pays)
    pl.xticks(rotation=90)
    pl.title('CREDIT PAR PAYS')
    pl.xlabel('PAYS')
    pl.ylabel('CREDIT')
    pl.show()


# Programme principal
def main():
    while True:
        print("\nVISUALISATION DES DONNEES")
        print("\t1. Statistiques")
        print("\t2. Croisement des données")
        print('\t. 0 pour quitter')
        choix = int(input("Choix : "))
    
        if choix == 1:
            print("\t1. Statistique Colonne")
            print("\t2. Statistique Employées")
            choix1 = int(input("Choix : "))
            if choix1 == 1:
                colonne = input("colonne: ")
                b= int(input("b: "))
                stats(colonne, b)
            if choix1 == 2:
                print("\t1. Nombre d'employé inferieur pour un employé donnée ")
                print("\t2. Nombre d'employees superieur pour tout les employees")
                print("\t3. Nombre de clients  d'un un employé")
                print("\t4. Nombre de clients pour tout les employees")
                choix11 = int(input("Choix : "))
                if choix11 == 1:
                    a=int(input("Entrer le numero d'un employé: "))
                    sup(a)
                if choix11 == 2:
                    tosup()   
                if choix11 == 3:
                    a = input("Entree le numero d'un employee: ") 
                    nbre_client(a)
                if choix11 ==   4:
                    tnbre_client()
    
        if choix == 2:
            print("\t1. Nombre de credit d'un employe")
            print("\t2. Fichier relation employé crédit des clients")
            print("\t3. Fichier relation ville montant des clients basés ")
            print("\t4. Fichier relation pays montants des clients basés")
            choix21 = int(input("Choix : "))
            if choix21 == 1:
                a = input("Entree le numero d'un employee: ")
                nbre_credit(a)
            if choix21 == 2:
                empcredit()
            if choix21 == 3:
                ville()
            if choix21 == 4:
                pays()
        if choix == 0:
            break
        else:
            print('aucune action correspondante')


            
            

main()

    
    