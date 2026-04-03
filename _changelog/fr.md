---
title: Changelog
meta_description: "Historique des versions de BiblioGenius : nouvelles fonctionnalités, corrections et améliorations."
hero_title: Changelog
hero_subtitle: Historique des versions et des changements
nav_home: Accueil
nav_story: Notre histoire
nav_docs: Documentation
nav_contribute: Contribuer
nav_blog: Blog
nav_changelog: Changelog
lang_label: Choisir la langue
lang_name: Français
footer_text: "BiblioGenius &mdash; Open Source, local, chiffré."
---

## 0.8.9 <small>2 avril 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.8-beta.6...v0.8.9-beta.8" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.9-beta.8" class="changelog-link">release</a>

- **Nombre de pages** : champ nombre de pages dans les fiches, formulaires d'ajout/modification et recherche
- **Durée de prêt configurable** : personnalisation de la durée de prêt dans les paramètres
- **Formulaires livre** : refonte UX des formulaires d'ajout et de modification
- **Sync multi-appareils** : correction de la synchronisation des auteurs, notes, copies et métadonnées entre appareils liés
- **Recherche** : fiabilité améliorée des sources externes, scoring de pertinence, protection contre les recherches concurrentes
- **Stabilité** : correction de la désérialisation Inventaire, correction du nom de bibliothèque par défaut localisé

## 0.8.8 <small>23 mars 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.7-beta.3...v0.8.8-beta.6" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.8-beta.6" class="changelog-link">release</a>

- **Sync multi-appareils (E2EE)** : synchronisation chiffrée de bout en bout entre appareils liés, appairage bidirectionnel, backfill et déduplication
- **Notes de lecture** : ajout de notes sur les livres avec dictée vocale
- **Livres privés** : possibilité de masquer des livres aux pairs du réseau
- **Descriptions de livres** : récupération automatique depuis OpenLibrary et SUDOC
- **Jeu du pendu** : nouveau mini-jeu ajouté au hub de jeux
- **Onboarding** : messages flash séquencés et refonte du design d'accueil
- **Stabilité** : correction de crashs au premier lancement et au premier scan, récupération du Keystore Android

## 0.8.7 <small>17 mars 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.6-alpha.6...v0.8.7-beta.3" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.7-beta.3" class="changelog-link">release</a>

- **macOS DMG** : distribution via DMG avec runtime sécurisé et repli Keychain résilient
- **Empreinte appareil** : enregistrement du modèle et fingerprint de l'appareil sur le hub
- **Stabilité pairs** : rafraîchissement catalogue, cache hors-ligne, persistance du nom des pairs
- **Notifications** : refonte UX complète, filtre emprunts, correction nom des pairs
- **Compatibilité** : correction `ClipRect` pour Flutter 3.38

## 0.8.6 <small>13 mars 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.5-beta.6...v0.8.6-alpha.6" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.6-alpha.3" class="changelog-link">release</a>

- **Catalogue hub unifié** : rendu uniforme et chargement plus rapide des bibliothèques pair
- **Scan en masse** : fonctionnalité de scan par lot avec redirection vers l'étagère scannée
- **Statistiques** : quantité et qualité enrichies, couleurs harmonisées avec le profil
- **Localisation** : ajout de l'italien, corrections turques, nettoyage i18n
- **UI** : logo, barre de recherche, bordure nav basse, dates du journal d'opérations

## 0.8.5 <small>7 mars 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.4-alpha.4...v0.8.5-beta.6" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.5-beta.6" class="changelog-link">tag</a>

- **Fil d'activité** : nouveau flux d'activité avec badges "nouveau"
- **Gestion des emprunts** : demandes d'emprunt, UX notifications, badge statut de lecture modifiable au tap
- **Découverte réseau** : cross-référence noms mDNS avec les pairs sauvegardés, repli 5G
- **UI** : option barre de navigation basse, rafraîchissement instantané des couvertures, quick action partage

## 0.8.4 <small>4 mars 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.2-alpha.3...v0.8.4-alpha.4" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.4-alpha.4" class="changelog-link">tag</a>

- **Annuaire hub** : écran Explore, suivi/désabonnement de bibliothèques, requêtes entrantes
- **Collections** : refactorisation vers FFI direct, regroupement dans la bibliothèque
- **Navigation web** : connexion et navigation des bibliothèques pair via navigateur web
- **Sync appareil** : module de sécurité sync avec écran de revue
- **Couvertures** : prise de photo via caméra de l'appareil

## 0.8.2 <small>26 février 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.1-alpha.2...v0.8.2-alpha.3" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.2-alpha.3" class="changelog-link">tag</a>

- **Liens d'invitation courts** : partage de profil simplifié avec URL courte via le hub
- **Bouton partage** : nouveau bouton de partage de profil
- **Accessibilité** : prérequis d'accessibilité ajoutés (travail en cours)

## 0.8.1 <small>25 février 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.0-alpha.2...v0.8.1-alpha.2" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.1-alpha.2" class="changelog-link">tag</a>

- **Jeu de mémoire** : nouveau mini-jeu avec les couvertures de votre bibliothèque, tableau des scores et animations
- **Puzzle glissant** : jeu de puzzle avec les couvertures, écran dédié et hub de jeux
- **Aide** : section d'aide enrichie
- **Traductions** : ajout du portugais et du turc

## 0.8.0 <small>20 février 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.7.2-alpha.2...v0.8.0-alpha.2" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.0-alpha.2" class="changelog-link">tag</a>

- **Chiffrement de bout en bout (E2EE)** : échange de clés par QR code v2, indicateur E2EE dans l'interface, chiffrement des requêtes de prêt
- **Hub relais** : interface de configuration du hub relais dans les paramètres
- **Licence AGPL-3.0** : passage du projet sous licence AGPL-3.0
- **Support CJK** : polices de repli pour japonais, chinois et coréen, squelettes .po
- **Langues** : ajout du bulgare, support des variantes régionales (pt-BR, zh-TW...)
- **Prêts** : approbation automatique configurable, compteur de requêtes en attente

## 0.7.2 <small>13 février 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.7.1-alpha.7...v0.7.2-alpha.2" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.7.2-alpha.2" class="changelog-link">tag</a>

- **Internationalisation** : migration des traductions vers des fichiers .po, recherche multilingue
- **Thème** : personnalisation du thème dans les paramètres, optimisation du thème par défaut
- **Audit UX** : corrections basées sur des personas, déduplication de recherche, résolution de 4 frictions majeures
- **Classement** : corrections de l'affichage du leaderboard sur le profil et entre pairs

## 0.7.1 <small>10 février 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.7.0-alpha.1...v0.7.1-alpha.7" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.7.1-alpha.7" class="changelog-link">tag</a>

- **Module Classement** : leaderboard de gamification entre bibliothèques connectées

## 0.7.0 <small>6 février 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.6.6-alpha.4...v0.7.0-alpha.1" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.7.0-alpha.1" class="changelog-link">tag</a>

- **Découverte P2P** : repli mDNS via hostname.local, suppression du fallback 127.0.0.1
- **Architecture propre** : migration des écrans Flutter vers le pattern Repository
- **Chemin base de données** : migration du dossier d'installation
- **Optimisations** : statut de lecture, recherche en ligne, import, cache pair

## 0.6.6 <small>25 janvier 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.6.5-alpha.21...v0.6.6-alpha.4" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.6.6-alpha.4" class="changelog-link">tag</a>

- **Emprunts et prêts** : corrections et améliorations de la fonctionnalité d'emprunt
- **UX/UI** : amélioration des états vides, gestion de la visibilité de l'avatar, amélioration de la recherche
- **Statistiques** : page de statistiques et affichage du tableau de bord améliorés
- **Actions rapides** : nouveau bouton d'actions rapides dans la bannière
- **Installation simplifiée** : suppression de l'assistant de configuration, auto-initialisation, support ES/DE

## 0.6.5 <small>12 janvier 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.6.5-alpha.21" class="changelog-link">tag</a>

- **Version initiale alpha** : gestion de bibliothèque personnelle, ajout/scan de livres, recherche en ligne
- **Réseau local** : découverte de pairs via mDNS, navigation dans les bibliothèques voisines
- **Interface** : tableau de bord, collections, étagères, profil avec badges de gamification
