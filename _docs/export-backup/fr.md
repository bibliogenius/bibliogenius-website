---
title: Exporter et sauvegarder ma bibliothèque
description: BiblioGenius exporte votre catalogue en CSV pour tableur et produit une sauvegarde complète chiffrée, restaurable telle quelle sur un autre appareil.
order: 13
group: data
---

Vos livres vous appartiennent : vous pouvez les sortir de BiblioGenius à tout moment, dans un format lisible ou dans une archive chiffrée prête à être restaurée. Tout se passe dans **Paramètres > Sauvegarde et récupération**.

## Quel fichier pour quel besoin

| Votre besoin | L'action à choisir | Ce que vous obtenez |
|---|---|---|
| Tout retrouver après une perte ou un changement d'appareil | Sauvegarde complète | Une archive chiffrée `.bgbackup` |
| Archiver vos données ou les emporter vers une autre application | Exporter mon catalogue | Un fichier portable, réimportable dans BiblioGenius |
| Consulter, trier ou inventorier vos livres dans un tableur | Exporter en CSV | Un fichier `.csv` lisible, non réimportable |

## La sauvegarde automatique

En haut de la section, une carte indique quand la dernière sauvegarde de cet appareil a été faite. Avec la sauvegarde automatique 24 h activée, BiblioGenius crée chaque jour un instantané chiffré de votre catalogue, **sur cet appareil seulement**. Vous pouvez la lancer à la main, restaurer l'une des archives présentes, ou les effacer toutes depuis cette même carte.

La sauvegarde automatique protège vos données sur l'appareil. Elle ne les transporte pas ailleurs : pour changer d'appareil, utilisez une sauvegarde complète ou un compte chiffré.

## Exporter mon catalogue

Crée un fichier portable et partageable contenant vos livres, auteurs, étiquettes, collections et contacts. C'est le format à choisir pour archiver vos données ou les reprendre dans une autre application. Il se réimporte dans BiblioGenius avec « Restaurer mon catalogue ».

Ce fichier n'est pas chiffré : rangez-le comme vous rangeriez n'importe quel document personnel.

## Exporter en CSV (tableur)

Crée un fichier avec une ligne par livre : titre, auteurs, ISBN, éditeur, année, langue, possession, statut de lecture, note, prix, étiquettes et date d'ajout. Il est pensé pour être ouvert, trié et filtré dans un tableur, par exemple pour faire un inventaire ou une liste d'assurance.

Les en-têtes et les statuts sont écrits dans votre langue. Le nom du fichier porte la date et la minute de l'export, pour qu'un second export du même jour n'écrase pas un fichier encore ouvert dans votre tableur.

**Ce fichier ne se réimporte pas.** Pour restaurer votre bibliothèque, utilisez la sauvegarde complète.

## Sauvegarde complète

Crée une archive chiffrée de toute votre bibliothèque, restaurable sur cet appareil ou sur un autre. Vous la protégez avec une phrase secrète de votre choix, ou avec votre phrase de récupération si vous avez un compte chiffré. Notez ce secret : sans lui, l'archive est illisible, y compris pour nous.

L'option **Inclure l'identité** ajoute à l'archive l'identité cryptographique de votre bibliothèque. Elle vous permet de migrer vers un nouvel appareil sans refaire l'appairage chiffré avec chacun de vos contacts.

## Restaurer

- **Restaurer une sauvegarde complète** : un assistant vous guide, et vous choisissez de fusionner l'archive avec votre bibliothèque actuelle ou de la remplacer entièrement.
- **Restaurer mon catalogue** : réimporte un fichier d'export de catalogue. Attention, cette opération remplace l'intégralité de vos données actuelles.
- **Annuler la restauration récente** : pendant 24 h après une restauration, une tuile vous propose de revenir à l'état précédent. L'application se ferme pour terminer l'opération, relancez-la ensuite.

## Bon réflexe

Faites une sauvegarde complète avant un changement de téléphone, avant une restauration, et avant toute opération de masse sur votre bibliothèque. Conservez-la ailleurs que sur l'appareil qu'elle protège.
