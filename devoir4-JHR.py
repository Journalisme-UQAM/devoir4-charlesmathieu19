# coding : utf-8

### BONJOUR!
### MES CORRECTIONS SONT DANS DES COMMENTAIRES PRÉCÉDÉS DE 3#

# Mise en place des bibliothèques nécessaires et du CNN (pas sûr que ça s'appelle de même, mais pas grave.)

import csv
import spacy
from collections import Counter

tal = spacy.load("fr_core_news_md")

# J'ajoute ici les "y" dans les stop_words et j'enlève le mot "gens" des stop_words.

tal.Defaults.stop_words.add("y")
tal.Defaults.stop_words.remove("gens")

# Ici, je crée un lien entre le document CSV qui contient les chroniques de Richard Martineau que je vais analyser. 

# martineau = "martino.csv"
martineau = "../martino.csv" ### MODIFICATION POUR PERMETTRE QUE ÇA FONCTIONNE SUR MON ORDI
f = open(martineau)
chroniques = csv.reader(f)
next(chroniques)

# Création de la liste qui sera utilisée plus tard. 

bigramsliste = []

for chronique in chroniques:
    textes = chronique[3]
    doc = tal(textes)
    lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    
    # Création des bigrams. Je ne les ai pas tout de suite ajoutés à la liste, pour être en mesure de créer une condition. 

    for x, y in enumerate(lemmes[:-1]):
        bigrams = "{} {}".format(lemmes[x],lemmes[x + 1])

        # Création de la condition pour aller chercher sulement les deux expressions dans les bigrams générés précédemments. 

        if "islam" in bigrams or "musulm" in bigrams: ### EXCELLENTE SOLUTION, ENCORE PLUS SIMPLE QUE CELLE QUE JE PROPOSE DANS LE SYLLABUS!
            bigramsliste.append(bigrams)

# Mise en place du "Counter" pour générer les 50 combinaisons de mots les plus souvent répétées par Richard Martineau. 

freq = Counter(bigramsliste)
print(freq.most_common(50))

### PARFAIT! RIEN À REDIRE! :)