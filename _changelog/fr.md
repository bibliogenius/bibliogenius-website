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

## 1.1.4 <small>24 août 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.1.3-beta.2...v1.1.4-beta.1" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.1.4-beta.1" class="changelog-link">release</a>

- **Suggestions de lecture** : un moteur local propose des livres à partir de ce que votre bibliothèque contient déjà, sur le tableau de bord, sur la fiche d'un livre, au moment où vous en terminez un, et dans un écran dédié ; chaque carte dit pourquoi elle est là, et « Ça ne m'intéresse pas » l'écarte partout d'un geste
- **Onglet « À découvrir »** : en haut de la bibliothèque, un bandeau partage sa place entre votre activité récente et les suggestions, sans jamais basculer tout seul, et une action de la barre du haut ouvre la liste complète
- **Compléter une série, compléter un auteur** : le tome manquant d'une série que vous possédez et les livres d'un auteur que vous lisez déjà sont retrouvés par une recherche anonyme, et proposés avec leur raison en clair
- **Page d'un auteur** : le nom de l'auteur s'ouvre désormais sur ses livres présents dans votre bibliothèque, puis sur ceux qui n'y sont pas
- **Emprunter plutôt qu'acheter** : dans l'aperçu d'un livre suggéré, les bibliothèques de votre réseau qui le possèdent sont listées, et la demande d'emprunt part de là
- **Favoris** : un marque-page étoile sur la fiche du livre, une collection Favoris qui se remplit toute seule, et un poids double dans les suggestions ; une collection que vous teniez déjà à la main peut être adoptée telle quelle
- **Possession** : un filtre « Possession » sépare enfin ce que vous avez de ce que vous cherchez, la recherche couvre tout le catalogue quel que soit le filtre en cours, les livres non possédés portent partout le même repère, et les compteurs d'étagères comme les statistiques s'accordent avec ce qu'ils affichent
- **Partager une liste** : une collection s'envoie par fichier ou par copier-coller, avec un récapitulatif de ce qui part ; à la réception, un aperçu montre la liste et son expéditeur, et rien n'entre dans la bibliothèque avant confirmation
- **Sélections toutes prêtes** : les listes relues qui recoupent votre bibliothèque vous sont proposées avec leurs livres en commun, une carte se déplie sur la liste complète avec ses notes, la catégorie « Rentrée des classes » couvre CM1-CM2, la 6e et la 5e, et le corpus a été relu (cinq ISBN corrigés, seize notes remises à l'endroit)
- **Carte de contact** : e-mail, téléphone et précisions se saisissent dans un formulaire, ne partent chiffrés qu'aux bibliothèques que vous avez acceptées, et une action « Contacter » ouvre un message déjà écrit depuis un livre ou depuis la page d'une bibliothèque
- **Export** : le catalogue s'exporte en CSV lisible dans un tableur, avec la date et la minute dans le nom du fichier
- **Vie privée** : un aperçu montre votre bibliothèque telle qu'une autre bibliothèque la reçoit, et votre ville devient une préférence locale, publiée seulement si vous choisissez de la partager
- **Annuaire** : le catalogue d'une bibliothèque reste consultable un an après la dernière connexion de son propriétaire, au lieu de disparaître au bout d'une semaine
- **Import** : un livre déjà complet n'est plus renvoyé vers une recherche de métadonnées, et une valeur de notice qui contenait un séparateur n'est plus tronquée
- **Interface** : les actions des messages de confirmation redeviennent lisibles sur leur propre fond, les cartes de livres similaires s'alignent, et l'espacement des icônes de l'en-tête est corrigé

## 1.1.3 <small>19 août 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.1.2-beta.5...v1.1.3-beta.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.1.3-beta.2" class="changelog-link">release</a>

- **Liste d'envies** : les livres que vous recherchez sont repérés dans les catalogues des bibliothèques connectées, avec une demande d'emprunt directe depuis la fiche du livre, et vos propres livres signalent discrètement qui les recherche
- **Couvertures** : fin du re-téléchargement périodique qui faisait disparaître les couvertures toutes les trois heures, et récupération de l'espace de cache qui fuyait
- **Prêts** : les listes de prêts et d'emprunts s'affichent du plus récent au plus ancien, et une proposition de prêt émise par le prêteur est désormais notifiée comme une proposition, et non comme une demande
- **Interface** : des cartes de la liste d'envies, badges et jalons de lecture masqués par un blocage silencieux au démarrage s'affichent de nouveau, correction de la barre de défilement de la bibliothèque sur ordinateur, et retour de l'avatar généré sur les cartes des bibliothèques
- **Données** : assainissement automatique des catalogues des contacts en cache (identifiants distants corrigés, doublons hérités supprimés)

## 1.1.2 <small>21 juillet 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.1.1-beta.1...v1.1.2-beta.5" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.1.2-beta.5" class="changelog-link">release</a>

- **Séries** : frise de lecture sur la fiche livre, où les tomes d'une série s'affichent dans l'ordre, les volumes non lus estompés et ceux que vous ne possédez pas signalés ; l'ordre se règle par glisser-déposer ou en saisissant le numéro de tome, depuis la fiche livre comme depuis la collection
- **Genres** : liste fermée de genres proposée à la saisie d'un livre, rangés comme des étagères sous un parent « Genre », avec le même filtrage, le même renommage et la même synchronisation que vos autres étagères
- **Bibliothèque** : les livres lus mais non possédés, gardés après un prêt terminé, réapparaissent dans les filtres avec un badge dédié, et leur suppression est proposée après un retour au lieu d'être silencieuse
- **Prêts** : l'état de prêt ne se confond plus avec le statut de lecture (deux pastilles distinctes), une demande d'emprunt qui n'a pas pu partir affiche un échec d'envoi au lieu de rester en attente indéfiniment, et un retour que le prêteur n'a jamais reçu déclenche un avertissement au lieu d'un faux succès
- **Emprunts à un contact** : ils apparaissent désormais dans la liste des livres empruntés et dans son compteur, avec l'identité du prêteur enregistrée durablement
- **Réseau** : les contacts appairés se suivent automatiquement pour que leur catalogue reste consultable quand ils sont hors ligne, l'écran d'un contact explique pourquoi un catalogue est indisponible (approbation requise, cache expiré) au lieu d'afficher une liste vide, et les livres affichés ne s'effacent plus une seconde après le chargement
- **Bibliothèques connues** : les contacts appairés depuis un autre appareil de votre compte sont désormais listés à part, avec la marche à suivre pour les réappairer sur cet appareil
- **Assistants IA (MCP)** : nouveau contrat d'outils en lecture seule sur votre bibliothèque, servi par l'application en cours d'exécution, protégé par un jeton et limité à votre vue de propriétaire
- **Sécurité** : l'API propriétaire n'est plus joignable depuis le réseau local, les échanges de prêt non chiffrés authentifient l'expéditeur, et les catalogues partagés ne laissent plus fuiter les livres que vous ne possédez pas
- **Collections** : l'onglet ne se bloque plus sur une date d'ajout invalide venue d'un contact ou d'une ancienne sauvegarde
- **Compte chiffré** : reconnexion automatique quand le hub expire la session
- **Réseau local** : avertissement au démarrage quand le port habituel de l'application est déjà occupé, vos contacts pouvant alors joindre un autre service à sa place
- **Bureau** : les paquets Windows et l'AppImage Linux embarquent désormais le moteur de synchronisation, comme sur macOS
- **Interface** : espacement des icônes de l'en-tête corrigé sur ordinateur et champ de recherche plus lisible

## 1.1.1 <small>3 juillet 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.1.0...v1.1.1-beta.1" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.1.1-beta.1" class="changelog-link">release</a>

- **Réseau** : le catalogue en cache d'un contact en ligne n'est plus perdu lors du rafraîchissement de l'annuaire

## 1.1.0 <small>3 juillet 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.0.2...v1.1.0" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.1.0" class="changelog-link">release</a>

- **Compte chiffré** : le compte devient le pilier sauvegarde et récupération de votre bibliothèque, avec une section Compte repensée dans les réglages, des explications guidées et un partage d'invitation
- **Multi-appareils (fondations)** : moteur de synchronisation de la bibliothèque entre les appareils d'un même compte (fusion cr-sqlite, registre d'appareils signé, enrôlement par QR code, retrait d'un appareil, déclenchement automatique, transport chiffré des couvertures personnalisées, ADR-046) ; livré désactivé dans cette version, activation prévue prochainement
- **Identifiants pérennes** : les livres, contacts, étagères, exemplaires et prêts passent sur des identifiants universels (UUID), avec une migration validée sur des copies de bibliothèques réelles et des garde-fous d'intégrité
- **Restauration** : choix explicite de l'identité de bibliothèque lors d'une restauration sur un autre appareil
- **Réseau** : reconnexion plus rapide des contacts en local après une coupure, catalogues des contacts lisibles entre versions différentes de l'app, rafraîchissement du catalogue en ligne calé sur la forme canonique ISBN-13
- **Exemplaires** : auto-réparation d'un identifiant de bibliothèque périmé qui pouvait faire échouer la création d'exemplaires
- **Réglages** : retrait du mot de passe local de l'application, redondant avec la phrase secrète du compte chiffré
- **Jeux** : sélecteur de difficulté du memory repensé avec des cartes colorées dépliables
- **Interface** : marges latérales harmonisées sur grand écran, en-tête et fiche livre affinés
- **Langues** : catalogues chinois, japonais et coréen complétés à 100 %

## 1.0.2 <small>24 juin 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.0.1-beta.3...v1.0.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.0.2" class="changelog-link">release</a>

- **Scan QR sur macOS** : caméra du scanner corrigée pour l'appairage et l'ajout de contacts
- **Identité macOS** : correction d'un cas où l'identité de votre bibliothèque pouvait se désynchroniser sur Mac et rompre les connexions avec vos pairs
- **Recherche** : message clair sur le quota Google Books, et vos sources de recherche préférées sont désormais conservées
- **Statistiques** : classement des auteurs plus lisible sur mobile
- **Tableau de bord** : les contacts connectés sont désormais comptés dans la statistique Contacts
- **Réglages** : écran de partage en ligne plus clair, champ de contact corrigé, retrait d'un compteur de bibliothèques trompeur
- **Réseau** : l'écran de chargement des contacts défile correctement en mode paysage
- **Activité** : icône de la section affichée dans la bannière d'activité
- **Thème** : barre supérieure aux couleurs de la marque, plus lumineuse
- **Couvertures iOS** : les photos de couverture ajoutées manuellement ne disparaissent plus après une mise à jour de l'app
- **Compléter ma bibliothèque** : sélection par lots, avec pourcentage en direct et progression par lot
- **Sauvegarde** : redémarrage systématique de l'app après une restauration avec retour arrière
- **Appareils liés** : retrait de l'ancien appairage direct entre appareils, remplacé à terme par la synchronisation par compte
- **Réglages** : tuiles d'accès rapide en pleine largeur sur mobile

## 1.0.1 <small>18 juin 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.0.0-beta.9...v1.0.1-beta.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.0.1-beta.3" class="changelog-link">release</a>

- **Compléter ma bibliothèque** : nouvel écran et carte sur le tableau de bord pour remplir en une fois les données manquantes de vos livres (résumé, éditeur, pages, couverture)
- **Réglages** : réorganisation plus claire et orientée usage, réglages plus faciles à trouver via la recherche
- **Appairage** : messages d'erreur plus clairs, vérification que l'autre appareil est joignable, écran qui reste allumé pendant l'opération, appairage par QR code
- **Réseau** : catalogues de vos contacts plus à jour et plus fiables, avec un retour de synchronisation honnête
- **Appareils liés** : fonctionnement clarifié dans l'interface
- **Recherche** : les résumés tiennent compte de vos langues de lecture
- **Statistiques** : blocs plus lisibles et mieux adaptés au mobile
- **Tableau de bord** : nouvelle section « Pour aller plus loin »
- **Nettoyage** : retrait d'un ancien écran d'import devenu inutile

## 1.0.0 <small>4 mai 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.9.2-beta.3...v1.0.0-beta.1" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.0.0-beta.1" class="changelog-link">release</a>

- **Sauvegarde locale (ADR-037)** : nouveau format `.bgbackup` chiffré, assistant de restauration avec carte de rollback, planificateur de sauvegarde automatique avec carte d'état, garde-fous bloquant toutes les sorties après une restauration réussie, teaser de sauvegarde complète, traductions FR/EN/DE/ES
- **Réglages** : sauvegarde promue au niveau racine, aplatissement de la section Contenu, suppression de l'accordéon Système, intégration de l'annuaire dans la section appropriée
- **Réseau** : les demandes d'abonnement entrantes s'affichent même quand l'annuaire est désactivé
- **Robustesse** : écran d'erreur de production sobre en remplacement du red screen de dev
- **Permissions iOS** : description d'utilisation du micro corrigée, chaînes de permissions localisées, périmètre clarifié pour `NSPhotoLibraryUsageDescription`
- **Permissions Android** : déclaration de `RECORD_AUDIO` et de la requête `RecognitionService` pour la dictée vocale

## 0.9.2 <small>29 avril 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.9.1-beta.4...v0.9.2-beta.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.9.2-beta.3" class="changelog-link">release</a>

- **Partage de ville (ADR-035 Phase 1+2)** : sélecteur de ville, synchronisation, affichage et filtre annuaire par puce/bouton, hydratation au démarrage, sémantique d'accessibilité sur les puces tap-to-filter
- **CityRepository durci** : validation, isolate, cache LRU, consommation des enregistrements enrichis (admin1 + admin2) issus de l'ADR-036
- **Annuaire V1** : bannière de mise en avant des bibliothèques de la même ville
- **Prêts** : module scindé en deux bascules indépendantes (prêter / emprunter), sous-onglets Reçues/Envoyées indépendants par module, prêt désactivé par défaut sur le preset libraire
- **Récupération d'identité E2EE** : dialog de récupération au lieu d'une rupture silencieuse avec les pairs, liste des pairs et appareils à re-appairer après un wipe
- **Carrousel d'activité** : plafond relevé à 20 items, complétés par les derniers livres ajoutés
- **Recherche** : bascule Google Books persistante, garde-fous UX en l'absence de clé API, clé i18n générique `search` ajoutée
- **Annuaire hub** : auto-configuration du relais et cache négatif sur 404
- **Profil** : suppression de `profileType` et `simplifiedMode` au profit d'un pilotage par mode
- **Collections** : navigation null-safe depuis la fiche livre, rafraîchissement automatique de la liste
- **Stabilité** : badge d'exemplaire rafraîchi sur la fiche livre au retour de la gestion d'exemplaires, validation de la composition IME avant lecture du contrôleur auteur dans les formulaires
- **i18n** : 22 chaînes manquantes traduites en espagnol et allemand, déduplication de la clé `badge_new` sur fr/en/es/de
- **Hub** : push automatique du pays de localisation lors du changement dans les réglages

## 0.9.1 <small>25 avril 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.9.0-beta.6...v0.9.1-beta.4" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.9.1-beta.4" class="changelog-link">release</a>

- **Découverte internationale v1.0** : refonte complète des listes curées en préparation de l'international
- **Carrousel "Activité"** : rebaptisé depuis "derniers ajouts", tri orienté lecture, badge "nouveau" masqué quand un statut est déjà affiché, propagation ES/DE
- **Bibliothèque** : tri persistant dans une pilule unique avec popup (auteurs vides en bas), regroupement par collections piloté depuis les réglages, barre de progression corrigée
- **Fiche pair** : feuille de livre pair draggable avec en-tête épinglé et CTA d'emprunt fixe
- **Couvertures** : isolation du cache pair avec plafond utilisateur, badge d'avertissement quand l'upload hub est en attente, unification de la résolution d'URL via `CoverUrlResolver`
- **Prêts (ADR-034)** : métadonnées typées, helper d'extraction de lecteur, lecture corrigée du payload `/api/copies/borrowed`
- **Statistiques** : prise en compte des livres lus sans date de fin, correction des cartes prêts et pages-lues bloquées à 0
- **Détail livre** : suppression bloquée sur prêt actif, préservation `addedAt`/`hubCoverUploadFailedAt`, coercition `DateTime` &rarr; ISO en FFI
- **Réseau** : badge connexion obsolète sur les cartes de pairs (ADR-032)
- **Collections** : option de supprimer les livres associés lors de la suppression d'une collection
- **i18n** : "Gamification" renommé "Accomplissements" (FR), chaînes carrousel et nouveaux badges propagés en ES et DE
- **Stabilité** : marquage des notifications au tap dans la popover, confirmation localisée de suppression d'étagère, replay du renommage de bibliothèque si la config n'est pas encore hydratée

## 0.9.0 <small>17 avril 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.9-beta.17...v0.9.0-beta.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.9.0-beta.6" class="changelog-link">release</a>

- **Synchronisation delta des pairs (ADR-028 / ADR-029)** : les rafraîchissements de catalogue pair se font désormais par deltas (ajouts, modifications, suppressions) au lieu d'un pull complet, ce qui réduit drastiquement la bande passante et accélère la découverte des nouveautés chez les pairs
- **Fallback transparent** : repli automatique sur le pull complet legacy si le pair ne supporte pas encore le protocole delta
- **État local préservé** : `firstSeenAt` et l'état "en ligne" sont conservés lors d'un refresh delta (le badge "nouveau" reste cohérent)
- **Sync avatar multi-appareils (ADR-025)** : les avatars de profil se propagent désormais aux appareils liés via `profile_changed`
- **Auto-réparation bibliothèque pair (ADR-030)** : récupération du UUID de bibliothèque via manifeste E2EE, curseur delta préservé après une reset-recovery
- **Carrousel d'activité récente** : nouveau carrousel des derniers ajouts dans la bibliothèque perso et pair, variante repliable pilotée par le scroll, masquage automatique sur petites bibliothèques
- **En-tête collant** : header rétractable avec onglets stickés sur Bibliothèque et Prêts
- **Annuaire Discover** : ouverture sans gate avec CTA de publication dans l'onglet, vue grille de couvertures, badge "nouveau" fiabilisé, demandes d'abonnement entrantes remontées sur la carte Discover, snackbars de confirmation, déverrouillage des bascules approbation et emprunt avec valeurs par défaut prudentes
- **Accessibilité** : tooltips sur 13 IconButtons, libellés sémantiques pour lecteurs d'écran, en-têtes `Semantics` sur la fiche livre
- **Réglages** : regroupement visuel des modules en 4 sections, langage neutralisé, confirmations explicites sur les actions destructives réseau
- **Classement** : synchronisation au démarrage et harmonisation visuelle, timeout côté client avec feedback utilisateur
- **Hub de jeux** : ajout du lien vers le pendu depuis le tableau de bord
- **UI bibliothèque pair** : grille de couvertures par défaut avec RAM bornée, variété de couleurs restaurée sur les placeholders de livres, badge "nouveau" piloté par `added_at` fourni par le propriétaire
- **Annuaire hub** : les clients remontent désormais leur version d'app au hub à l'enregistrement
- **Couverture de livre** : évitement du placeholder gris d'OpenLibrary pour les ISBN inconnus
- **i18n** : 24 chaînes manquantes traduites en espagnol et allemand

## 0.8.9 <small>13 avril 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.8-beta.6...v0.8.9-beta.17" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.9-beta.17" class="changelog-link">release</a>

- **Annuaire hub public** : activation de l'annuaire public avec garde-fous UX et demandes d'emprunt directes depuis les bibliothèques suivies
- **Classement en temps réel (ADR-023)** : push live du leaderboard, affichage cache-first, pré-chauffage au démarrage, bouton de réinitialisation des scores, saut du direct en cellulaire
- **Rappels de prêt** : notifications de rappel d'échéance, deep-links corrigés pour les évènements prêt/retour
- **Fiche livre enrichie** : statut de prêt actif (emprunteur, date d'échéance, badge retard), notes de contact, stepper exemplaires, bouton emprunter désactivé si livre déjà prêté
- **Catalogue pair en direct** : abonnement aux changements des pairs pour rafraîchir la bibliothèque sans action manuelle, re-vérification de connectivité avant sync
- **Couvertures maîtrisées** : plafonnement 300&times;450, ré-encodage JPEG à l'upload, cache ETag, éviction sur 404, proxy hub pour les couvertures des pairs, propagation des couvertures personnalisées au hub
- **Nombre de pages** : champ nombre de pages dans les fiches, formulaires d'ajout/modification et recherche
- **Durée de prêt configurable** : personnalisation de la durée de prêt dans les paramètres, sélection du pair emprunteur dans la boîte de dialogue
- **Formulaires livre** : refonte UX des formulaires d'ajout et de modification
- **Pairs réseau** : avatars des pairs (LAN et relais via hub), ouverture directe de la bibliothèque au tap, polish liste pairs (statut, skeleton, QR plein écran), bouton de partage d'invitation dans la feuille "ajouter une connexion"
- **Robustesse relais (5G/4G)** : republication fiable des credentials à la reconnexion, sync non bloquante, fallback hors-ligne, circuit breaker sur 502, refresh nodeId, timeout de sync
- **Profil hub** : code de récupération de profil, récupération automatique sur 401 (retry avec recovery code avant purge), sauvegarde Keychain renforcée, back-off sur 401 d'enregistrement, URL du hub masquée en release, garde-fous contre le verrouillage permanent du profil
- **Sync multi-appareils** : correction de la synchronisation des auteurs, notes, copies et métadonnées entre appareils liés, propagation du renommage de bibliothèque vers le hub
- **Recherche** : fiabilité améliorée des sources externes, scoring de pertinence, protection contre les recherches concurrentes
- **i18n** : traductions ES/DE complétées (couverture, prêts, notes, récupération), renommage "Copies" en "Exemplaires" (fr)
- **Sécurité & stabilité** : logs sensibles gated en mode debug et identifiants redactés, désérialisation Inventaire, nom de bibliothèque par défaut localisé

## 0.8.8 <small>23 mars 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.7-beta.3...v0.8.8-beta.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.8-beta.6" class="changelog-link">release</a>

- **Sync multi-appareils (E2EE)** : synchronisation chiffrée de bout en bout entre appareils liés, appairage bidirectionnel, backfill et déduplication
- **Notes de lecture** : ajout de notes sur les livres avec dictée vocale
- **Livres privés** : possibilité de masquer des livres aux pairs du réseau
- **Descriptions de livres** : récupération automatique depuis OpenLibrary et SUDOC
- **Jeu du pendu** : nouveau mini-jeu ajouté au hub de jeux
- **Onboarding** : messages flash séquencés et refonte du design d'accueil
- **Stabilité** : correction de crashs au premier lancement et au premier scan, récupération du Keystore Android

## 0.8.7 <small>17 mars 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.6-alpha.6...v0.8.7-beta.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.7-beta.3" class="changelog-link">release</a>

- **macOS DMG** : distribution via DMG avec runtime sécurisé et repli Keychain résilient
- **Empreinte appareil** : enregistrement du modèle et fingerprint de l'appareil sur le hub
- **Stabilité pairs** : rafraîchissement catalogue, cache hors-ligne, persistance du nom des pairs
- **Notifications** : refonte UX complète, filtre emprunts, correction nom des pairs
- **Compatibilité** : correction `ClipRect` pour Flutter 3.38

## 0.8.6 <small>13 mars 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.5-beta.6...v0.8.6-alpha.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.6-alpha.3" class="changelog-link">release</a>

- **Catalogue hub unifié** : rendu uniforme et chargement plus rapide des bibliothèques pair
- **Scan en masse** : fonctionnalité de scan par lot avec redirection vers l'étagère scannée
- **Statistiques** : quantité et qualité enrichies, couleurs harmonisées avec le profil
- **Localisation** : ajout de l'italien, corrections turques, nettoyage i18n
- **UI** : logo, barre de recherche, bordure nav basse, dates du journal d'opérations

## 0.8.5 <small>7 mars 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.4-alpha.4...v0.8.5-beta.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.5-beta.6" class="changelog-link">tag</a>

- **Fil d'activité** : nouveau flux d'activité avec badges "nouveau"
- **Gestion des emprunts** : demandes d'emprunt, UX notifications, badge statut de lecture modifiable au tap
- **Découverte réseau** : cross-référence noms mDNS avec les pairs sauvegardés, repli 5G
- **UI** : option barre de navigation basse, rafraîchissement instantané des couvertures, quick action partage

## 0.8.4 <small>4 mars 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.2-alpha.3...v0.8.4-alpha.4" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.4-alpha.4" class="changelog-link">tag</a>

- **Annuaire hub** : écran Explore, suivi/désabonnement de bibliothèques, requêtes entrantes
- **Collections** : refactorisation vers FFI direct, regroupement dans la bibliothèque
- **Navigation web** : connexion et navigation des bibliothèques pair via navigateur web
- **Sync appareil** : module de sécurité sync avec écran de revue
- **Couvertures** : prise de photo via caméra de l'appareil

## 0.8.2 <small>26 février 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.1-alpha.2...v0.8.2-alpha.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.2-alpha.3" class="changelog-link">tag</a>

- **Liens d'invitation courts** : partage de profil simplifié avec URL courte via le hub
- **Bouton partage** : nouveau bouton de partage de profil
- **Accessibilité** : prérequis d'accessibilité ajoutés (travail en cours)

## 0.8.1 <small>25 février 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.0-alpha.2...v0.8.1-alpha.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.1-alpha.2" class="changelog-link">tag</a>

- **Jeu de mémoire** : nouveau mini-jeu avec les couvertures de votre bibliothèque, tableau des scores et animations
- **Puzzle glissant** : jeu de puzzle avec les couvertures, écran dédié et hub de jeux
- **Aide** : section d'aide enrichie
- **Traductions** : ajout du portugais et du turc

## 0.8.0 <small>20 février 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.7.2-alpha.2...v0.8.0-alpha.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.0-alpha.2" class="changelog-link">tag</a>

- **Chiffrement de bout en bout (E2EE)** : échange de clés par QR code v2, indicateur E2EE dans l'interface, chiffrement des requêtes de prêt
- **Hub relais** : interface de configuration du hub relais dans les paramètres
- **Licence AGPL-3.0** : passage du projet sous licence AGPL-3.0
- **Support CJK** : polices de repli pour japonais, chinois et coréen, squelettes .po
- **Langues** : ajout du bulgare, support des variantes régionales (pt-BR, zh-TW...)
- **Prêts** : approbation automatique configurable, compteur de requêtes en attente

## 0.7.2 <small>13 février 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.7.1-alpha.7...v0.7.2-alpha.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.7.2-alpha.2" class="changelog-link">tag</a>

- **Internationalisation** : migration des traductions vers des fichiers .po, recherche multilingue
- **Thème** : personnalisation du thème dans les paramètres, optimisation du thème par défaut
- **Audit UX** : corrections basées sur des personas, déduplication de recherche, résolution de 4 frictions majeures
- **Classement** : corrections de l'affichage du leaderboard sur le profil et entre pairs

## 0.7.1 <small>10 février 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.7.0-alpha.1...v0.7.1-alpha.7" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.7.1-alpha.7" class="changelog-link">tag</a>

- **Module Classement** : leaderboard de gamification entre bibliothèques connectées

## 0.7.0 <small>6 février 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.6.6-alpha.4...v0.7.0-alpha.1" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.7.0-alpha.1" class="changelog-link">tag</a>

- **Découverte P2P** : repli mDNS via hostname.local, suppression du fallback 127.0.0.1
- **Architecture propre** : migration des écrans Flutter vers le pattern Repository
- **Chemin base de données** : migration du dossier d'installation
- **Optimisations** : statut de lecture, recherche en ligne, import, cache pair

## 0.6.6 <small>25 janvier 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.6.5-alpha.21...v0.6.6-alpha.4" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.6.6-alpha.4" class="changelog-link">tag</a>

- **Emprunts et prêts** : corrections et améliorations de la fonctionnalité d'emprunt
- **UX/UI** : amélioration des états vides, gestion de la visibilité de l'avatar, amélioration de la recherche
- **Statistiques** : page de statistiques et affichage du tableau de bord améliorés
- **Actions rapides** : nouveau bouton d'actions rapides dans la bannière
- **Installation simplifiée** : suppression de l'assistant de configuration, auto-initialisation, support ES/DE

## 0.6.5 <small>12 janvier 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.6.5-alpha.21" class="changelog-link">tag</a>

- **Version initiale alpha** : gestion de bibliothèque personnelle, ajout/scan de livres, recherche en ligne
- **Réseau local** : découverte de pairs via mDNS, navigation dans les bibliothèques voisines
- **Interface** : tableau de bord, collections, étagères, profil avec badges de gamification
