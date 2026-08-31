---
title: Où sont stockées mes données
description: BiblioGenius est local d'abord : votre bibliothèque vit sur votre appareil, et cette page dit exactement ce qui en sort, quand, et vers où.
order: 12
group: data
---

BiblioGenius est local d'abord : votre bibliothèque vit dans une base de données sur votre appareil, et l'application fonctionne sans compte et sans connexion. Ce qui sort de l'appareil ne sort que parce que vous l'avez demandé, et cette page dit exactement quoi, quand et vers où.

## Sur votre appareil

Vos livres, étagères, collections, étiquettes, exemplaires, prêts et contacts sont stockés localement. Vous pouvez utiliser l'application entière hors ligne : ajouter des livres à la main, les organiser, suivre vos lectures.

## Ce qui quitte l'appareil, et quand

- **Les recherches dans les catalogues externes.** Quand vous scannez un ISBN ou cherchez un titre, la requête part vers les sources activées (BnF, OpenLibrary, Inventaire et d'autres). Ces sources voient donc ce que vous cherchez. Vous choisissez lesquelles interroger dans Paramètres > Sources de recherche.
- **Les couvertures et métadonnées** sont téléchargées depuis ces mêmes sources, puis conservées sur votre appareil.
- **Le partage avec vos contacts.** Quand une bibliothèque connectée consulte votre catalogue, votre appareil lui répond directement, chiffré de bout en bout. En Wi-Fi local, l'échange ne sort pas du réseau. À distance, il passe par un relais qui ne voit que des données chiffrées.
- **L'annuaire en ligne**, si vous l'activez avec « Me rendre visible auprès des autres bibliothèques ». Vous pouvez exiger votre approbation avant qu'un nouvel abonné accède à vos livres partagés. Votre ville reste une préférence locale tant que vous ne choisissez pas de la partager.
- **Le compte chiffré**, si vous en créez un. Le serveur ne stocke alors que des blocs chiffrés, illisibles pour lui. Voir [Compte chiffré et plusieurs appareils](account-sync.html).

Rien de tout cela n'est activé à votre place.
## Les permissions de l'application

Deux permissions Android sont classées « dangereuses » par le système. Voici ce qu'elles servent à faire.

**Caméra.** Le scan des codes-barres pour ajouter un livre, et la lecture des QR codes d'appairage entre bibliothèques.

**Microphone.** Une seule fonction : dicter une note de lecture ou une citation au lieu de la taper. Le bouton micro apparaît dans les champs de notes. La permission est déclarée dans le manifeste de l'application, mais elle n'est demandée qu'à la première utilisation de ce bouton : si vous ne dictez jamais, l'application ne vous la demande jamais.

L'application n'enregistre ni ne conserve aucun son. Seul le texte reconnu est inséré dans le champ de note. La conversion de la parole en texte, elle, est celle du système d'exploitation : l'application utilise la reconnaissance vocale que l'appareil fournit. Ce traitement dépend donc de votre appareil et de ses réglages, et il échappe à l'application. C'est pour cela que la dictée se désactive : la couper dans les Paramètres retire le bouton micro. Elle est active par défaut, sauf sur le profil libraire.

## Un audit indépendant

Exodus Privacy analyse les pisteurs et les permissions des applications Android. Son rapport sur BiblioGenius est public : [voir le rapport Exodus Privacy](https://reports.exodus-privacy.eu.org/fr/reports/com.bibliogenius.app/latest/).


## Choisir ce que les autres voient

Activez « Livres privés » dans les Paramètres pour débloquer l'option Privé sur chaque livre : un livre privé reste dans votre bibliothèque mais n'apparaît jamais aux autres, ni sur votre profil public, ni dans les recherches du réseau.

Pour vérifier plutôt que croire, ouvrez **« Ce que voient les autres bibliothèques »** : cette liste est la réponse exacte que votre appareil envoie à une bibliothèque qui consulte votre catalogue, produite par le même code, sans recalcul de façade.

## Sauvegardes

Vous pouvez sortir vos données à tout moment depuis **Paramètres > Sauvegarde et récupération** : export portable, export CSV lisible dans un tableur, ou archive chiffrée restaurable. Voir [Exporter et sauvegarder](export-backup.html).

## Chiffrement

Les échanges entre bibliothèques sont chiffrés de bout en bout. Le compte chiffré et les sauvegardes complètes le sont également, avec une clé dérivée de votre phrase secrète : nous n'avons aucun moyen technique de lire vos données.

## Effacer mes données

Sur l'appareil, les Paramètres permettent d'effacer vos livres ou de repartir de zéro. Pour la suppression d'un compte en ligne, suivez la procédure décrite sur la page [Suppression des données](../data-deletion.html).
