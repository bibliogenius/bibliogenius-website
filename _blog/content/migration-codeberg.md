+++
title = "BiblioGenius quitte GitHub pour Codeberg"
description = "Notre compte GitHub a été suspendu du jour au lendemain, sans préavis. Le code du projet vit désormais sur Codeberg, une plateforme associative et open source. Voici ce qui s'est passé, et ce que ça change (ou non) pour toi."
date = 2026-05-20
updated = 2026-05-20
template = "blog/page.html"

[extra]
tags = ["annonce"]
+++

BiblioGenius répète une idée simple depuis le premier jour : tes livres t'appartiennent, tes données restent chez toi. Le 4 mai, on a reçu un rappel très concret de la raison pour laquelle ce principe compte.

## L'essentiel d'abord : ton application ne bouge pas

Si tu utilises BiblioGenius pour gérer ta bibliothèque, **tout va bien, tu peux t'arrêter là**. Cette histoire concerne uniquement l'endroit où est rangé le *code source* du projet : la « recette » de l'application, celle que les développeurs lisent et améliorent. L'application, tes livres, tes prêts, tes données : rien n'est touché, rien n'est perdu, tu n'as rien à faire.

La suite intéressera surtout les curieux, et les personnes qui contribuent au projet.

## Ce qui s'est passé

Jusqu'ici, le code de BiblioGenius était hébergé sur **GitHub**, la plateforme la plus connue au monde pour stocker du code et collaborer dessus. Un service gratuit, pratique, utilisé par des millions de développeurs.

Le 4 mai, **notre compte GitHub a été suspendu**. Sans préavis, sans explication, sans e-mail d'avertissement. Du jour au lendemain, tout le code du projet et son historique sont devenus inaccessibles, pour nous comme pour les contributeurs.

La cause la plus probable tient à une ligne des conditions d'utilisation : GitHub n'autorise **qu'un seul compte gratuit par personne**. Pas de mise en garde, pas de délai pour régulariser : juste un interrupteur coupé.

Conséquence : les **tickets** (la liste des bugs connus et des tâches à faire) ont disparu avec le compte. C'était avant tout une liste de travail interne ; elle est en cours de reconstitution sur la nouvelle plateforme.

## La leçon

Il y a une petite ironie, là-dedans. BiblioGenius est un projet qui défend la souveraineté numérique : ne pas dépendre d'une plateforme unique, capable de changer ses règles, de t'enfermer ou de te couper l'accès sans rendre de comptes. Et on vient d'en faire l'expérience, pour de vrai, sur notre propre code.

Une seule porte d'entrée, contrôlée par une seule entreprise, c'est un point de fragilité. La bonne réponse n'est pas de râler : c'est de choisir un hébergement cohérent avec les valeurs du projet.

## Le nouveau foyer : Codeberg

BiblioGenius vit désormais sur **Codeberg**.

Codeberg, c'est l'équivalent de GitHub (un endroit pour héberger du code et collaborer), mais avec une différence de fond : c'est géré par une **association à but non lucratif**, basée en Allemagne, et non par une multinationale. Le logiciel qui fait tourner Codeberg, *Forgejo*, est lui-même open source : on peut l'inspecter, le copier, l'installer ailleurs.

Autrement dit : BiblioGenius est open source, et la plateforme qui héberge désormais son code l'est aussi. C'est plus cohérent, et c'est même ce qu'on aurait dû faire plus tôt.

Le projet est ici :

- **Organisation** : <https://codeberg.org/bibliogenius>
- **Serveur** (Rust) : <https://codeberg.org/bibliogenius/bibliogenius>
- **Application** (Flutter) : <https://codeberg.org/bibliogenius/bibliogenius-app>
- **Hub** : <https://codeberg.org/bibliogenius/bibliogenius-hub>
- **Environnement de dev** : <https://codeberg.org/bibliogenius/bibliogenius-env>

## Tu contribues au projet ? (partie technique)

Si tu as un clone local d'un dépôt, il suffit de le faire pointer vers la nouvelle adresse. Depuis le dossier du dépôt :

```
git remote set-url origin https://codeberg.org/bibliogenius/<dépôt>.git
```

Par exemple, pour l'application :

```
git remote set-url origin https://codeberg.org/bibliogenius/bibliogenius-app.git
```

Pour ouvrir un ticket ou une *pull request*, il te faudra un **compte Codeberg** (gratuit), et rien de plus. Pas besoin d'être ajouté à l'organisation : tu forkes le dépôt, tu pousses sur ton fork, tu ouvres une pull request. Le déroulé open source classique.

## Tu as contribué, et on s'est perdus de vue ?

C'est le point le plus délicat de cette migration. Comme le compte GitHub a sauté sans prévenir, **on a perdu le moyen de recontacter certaines personnes**, des traducteurs surtout.

Si tu nous as un jour envoyé une traduction, signalé un bug, proposé un correctif ou une idée, et que tu lis ces lignes : **écris-nous**. On aimerait sincèrement renouer le contact, et s'assurer que ta contribution n'a pas été oubliée dans le déménagement.

Un seul point de contact : [contact@bibliogenius.org](mailto:contact@bibliogenius.org).

## Et les téléchargements ?

Les versions à installer pour **Linux et Windows** étaient distribuées via GitHub. Elles sont donc momentanément indisponibles, le temps de remettre en place un canal de téléchargement. Les applications iOS, Android et macOS, elles, passent par l'App Store et le Play Store, et ne sont pas concernées. Besoin d'une version en attendant ? Écris-nous, on te dépanne.

La migration est terminée : BiblioGenius tourne désormais entièrement sur Codeberg. C'est là que le développement continue, et que tu peux suivre le projet.
