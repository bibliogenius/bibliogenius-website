---
title: Compte chiffré et plusieurs appareils
description: Le compte chiffré de BiblioGenius garde une copie de votre bibliothèque que vous seul pouvez lire, pour ne rien perdre et la retrouver sur chacun de vos appareils.
order: 14
group: data
---

BiblioGenius fonctionne d'abord sur votre appareil, sans compte. Le compte chiffré est une option : il garde une copie chiffrée de votre bibliothèque, que vous seul pouvez lire. Il sert à trois choses : ne rien perdre, retrouver votre bibliothèque sur un nouvel appareil, et l'utiliser à plusieurs.

Vous le trouvez dans **Paramètres > Sauvegarde et récupération > Compte chiffré**.

## Ce que le serveur voit

Rien de lisible. Vos livres sont chiffrés sur votre appareil avant d'être envoyés, avec une clé dérivée de votre phrase secrète. Le serveur ne stocke que des blocs chiffrés : ni nous, ni un hébergeur, ni quelqu'un qui obtiendrait la base ne peut lire vos titres, vos notes ou vos contacts.

La contrepartie est directe : personne ne peut vous redonner accès à vos données si vous perdez vos secrets.

## Créer un compte

Il vous faut une adresse e-mail, une phrase secrète, et un nom pour cet appareil.

**Votre phrase secrète ne peut pas être réinitialisée.** À la création, l'application affiche une **phrase de récupération de 24 mots** : c'est le seul moyen de récupérer le compte si vous oubliez la phrase secrète. Elle n'est affichée qu'une seule fois et n'est jamais stockée. Notez-la dans l'ordre, sur papier ou dans un gestionnaire de mots de passe.

Cette même phrase de récupération peut servir de secret pour vos sauvegardes complètes, voir [Exporter et sauvegarder](export-backup.html).

## Ce qui se synchronise, et ce qui ne se synchronise pas

Se synchronise : vos livres, auteurs, étiquettes, collections, exemplaires, prêts, contacts et couvertures personnalisées.

Ne se synchronise pas : les réglages propres à l'appareil, et les **appairages chiffrés avec vos contacts**. L'appairage se fait appareil par appareil, par conception : la clé qui vous relie à une autre bibliothèque ne quitte pas l'appareil qui l'a créée.

C'est pourquoi vos contacts peuvent apparaître, sur un nouvel appareil, dans une section « Bibliothèques connues » avec la mention « Non appairée sur cet appareil ». Pour vous connecter à elles depuis ce nouvel appareil, refaites un appairage : partagez votre lien d'invitation ou acceptez le leur.

## Ajouter un appareil

1. Sur le nouvel appareil, choisissez « Ajouter cet appareil via un autre appareil » : il affiche un code QR.
2. Sur un appareil déjà connecté, ouvrez **Compte chiffré > Ajouter un appareil** et scannez ce code.
3. L'appareil existant affiche en retour un code d'autorisation, que le nouvel appareil scanne à son tour.

Ne scannez ces codes qu'en personne, directement entre vos deux appareils. Ne les transmettez jamais par message ni en photo.

Si vos deux appareils ne sont pas côte à côte, l'option « Rejoindre un compte existant » fait la même chose avec votre e-mail et votre phrase secrète.

## Synchroniser

La synchronisation se fait toute seule, périodiquement et au retour dans l'application. Le bouton **Synchroniser maintenant** force un cycle immédiat.

Si le message indique une synchronisation partielle, c'est que certains éléments n'ont pas pu être appliqués sur cet appareil, en général parce qu'un de vos appareils tourne sur une version plus ancienne. Mettez-les à jour, puis relancez la synchronisation.

## Partager l'accès à plusieurs personnes

Depuis le même écran, « Partager l'accès à ma bibliothèque » permet à une autre personne de rejoindre le compte depuis son appareil, avec votre e-mail et votre phrase secrète. Elle apparaît ensuite comme un appareil autorisé.

Sachez ce que cela implique : **toute personne qui partage ce compte y a un accès complet**, et retirer durablement un accès n'est pas encore possible. C'est un usage de confiance, pensé pour un foyer.

## Retirer un appareil, se déconnecter

Retirer un appareil l'empêche de continuer à se synchroniser, mais il conserve les données déjà téléchargées : ce n'est pas un verrouillage de sécurité. Vous pourrez le rajouter plus tard.

Se déconnecter sur un appareil arrête sa synchronisation sans toucher au compte ni aux autres appareils. Vous le reconnectez plus tard avec votre phrase secrète.

## Si vous perdez tout

Avec la phrase de récupération, vous retrouvez le compte. Sans la phrase secrète ni la phrase de récupération, les données du compte sont définitivement illisibles, y compris pour nous. C'est le prix du chiffrement de bout en bout, et c'est aussi pourquoi une sauvegarde complète locale reste une bonne idée.
