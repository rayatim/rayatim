a = []
b = []
c = []
print("veuiller saisir  les element de la matrcie a :")
for i in range(4):
    ligne = []
    for j in range(5):
        print('a[', i+1, '][', j+1, ']=', end = ' ')
        ligne.append(int(input()))
    a.append(ligne)

print("veuiller saisir  les element de la matrcie b :")
for i in range(4):
    ligne = []
    for j in range(5):
        print('b[', i+1, '][', j+1, ']=', end = ' ')
        ligne.append(int(input()))
    b.append(ligne)

for lignea, ligneb in zip(a,b):
    ligne =[]
    for ea, eb in zip(lignea, ligneb):
        ligne.append(ea + eb)
    c.append(ligne)

"...affichage des resultats"
print('Afficher la matrice a :')
for i in a:
    for e in i:
        print(e, end = '\t')
    print()

print('Afficher la matrice b :')
for i in b:
    for e in i:
        print(e, end = '\t')
    print()

print("Afficher l'addition des matrices a et b :")
for i in c:
    for e in i:
        print(e, end = '\t')
    print()