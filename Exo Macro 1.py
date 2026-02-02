#####################################""EXERCICE 1############################################"
phrase = "I Love Cheese and Wine"
nombre_caracteres = len(phrase)
print("Le nombre de caractères dans la phrase est :", nombre_caracteres)

# #############################""EXERCICE 2##############################################################"
Sentence = "You would not believe your eyes"
mots_extraits = Sentence.split()
print(mots_extraits)
####################################Exercice 3####################################################"""
texte = """Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say
que they were perfectly normal, thank you very much. They were the last people
you'd expect to be involved in anything strange or mysterious, because they
just didn't hold with such nonsense. Mr. Dursley was the director of a firm
called Grunnings, which made drills. He was a big, beefy man with hardly any
neck, although he did have a very large mustache. Mrs. Dursley was thin and
blonde and had nearly twice the usual amount of neck, which came in very
useful as she spent so much of her time craning over garden fences, spying on
the neighbors. The Dursleys had a small son called Dudley and in their
opinion there was no finer boy anywhere."""
nombre_de_e = texte.count("e")
print("Le nombre de lettre 'e' est :", nombre_de_e)
# ####################################Exercice 4####################################################"""
import pandas as pd

Df_grades = pd.DataFrame({
    "Name": ["Paul", "Arthur", "Emma", "Lisa", "Eduardo", "Ben"],
    "Grade": [87, 35, 42, 87, 65, 53]
})
note_eduardo = Df_grades.iloc[4, 1]
print(f"Note d'Eduardo : {note_eduardo}")
note_max = Df_grades["Grade"].max()
note_min = Df_grades["Grade"].min()
print(f"Note max : {note_max}, Note min : {note_min}")
df_good_students = Df_grades[Df_grades["Grade"] >= 50]
print("Étudiants avec au moins 50/100 :")
print(df_good_students)
###############################exo 5######################################################""
import pandas as pd
import matplotlib.pyplot as plt

Df_grades = pd.DataFrame({
    "Name": ["Paul", "Arthur", "Emma", "Lisa", "Edoardo", "Ben"],
    "Grade": [87, 35, 42, 87, 65, 53]
})

Df_citizenship = pd.DataFrame({
    "Name": ["Paul", "Arthur", "Emma", "Lisa", "Edoardo", "Hector"],
    "Citizenship": ["French", "English", "French", "Italian", "Italian", "Polish"]
})


df_merged = pd.merge(Df_grades, Df_citizenship, on="Name", how="outer")
print("Base fusionnée :")
print(df_merged)


moyenne_italiens = df_merged[df_merged["Citizenship"] == "Italian"]["Grade"].mean()
print(f"\nMoyenne des étudiants italiens : {moyenne_italiens}")


df_merged["rank"] = df_merged["Grade"].rank(ascending=False, method='min')

df_merged["Grade"].hist(bins=10)
plt.title("Distribution des notes")
plt.xlabel("Notes")
plt.ylabel("Nombre d'étudiants")
plt.show()


df_merged.to_csv("Data_my_first_exercise.csv", index=False)
print("\nFichier sauvegardé avec succès sous le nom 'Data_my_first_exercise.csv'")
########################exercice 6 ###########################################################""
String = "Olympic Games"
def dernier(arg):
    arg = String[-1]
    return arg

last=dernier(String)
print(last)

########################exercice 7 ###########################################################""

String = "To strive, to seek, to find, and not to yield"


voyelles = "aeiouyAEIOUY"


compteur = 0


for lettre in String:

    if lettre in voyelles:

        compteur = compteur + 1


print(compteur)
########################exercice 8 ###########################################################""

def additionner(chiffre1, chiffre2):

    resultat = chiffre1 + chiffre2

    return resultat


somme = additionner(5, 10)
print(f"La somme est : {somme}")

###########################exercice 9 ###############################""""

try:
    for i in range(101):
        print(i)
except KeyboardInterrupt:
    print("Interrompu")


####################exercice 10###############################""
list_students = ["Tom : A", "Elena : C", "Bruno : B", "Etienne : A"]
dictionary = {}

for item in list_students:
    nom, note = item.split(" : ")
    dictionary[nom] = note

print(dictionary)

###########################exercice 10########################""""
numbers = [500, 10, 20, 50, 350, 10000, 55, 1.2]

maximum = max(numbers)
minimum = min(numbers)

print(maximum)
print(minimum)

##################exercice 12 ###################"
from numpy.random import uniform

def tirage_binomial(nb_essais, proba):
    nb_succes = 0
    for i in range(nb_essais):
        if uniform(0, 1) < proba:
            nb_succes = nb_succes + 1
    return nb_succes

print(tirage_binomial(10, 0.5))