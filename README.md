# Spécifications fonctionnelles

#### Module 1 : Authentification et Tableau de Bord (Dashboard)

- **SF 1.1 - Connexion :** Le système doit permettre à l'utilisateur de s'authentifier via un couple Email / Mot de passe.
    
- **SF 1.2 - Gestion des erreurs :** Le système doit afficher un message clair en cas d'identifiants incorrects et bloquer l'accès.
    
- **SF 1.3 - Dashboard Accueil :** Une fois connecté, l'utilisateur accède à un tableau de bord affichant :
    
    - Le volume de cours prévus pour la journée/semaine en cours.
        
    - Le statut de la dernière synchronisation avec Google Agenda.
        
    - Les 3 dernières notifications envoyées.
        
- **SF 1.4 - Déconnexion :** L'utilisateur doit pouvoir se déconnecter de la plateforme depuis n'importe quel écran principal.
    

#### Module 2 : Gestion du Calendrier Pédagogique

- **SF 2.1 - Importation de masse (Drag & Drop) :** L'application doit permettre l'importation d'un fichier `.csv` ou `.xlsx` via une zone de glisser-déposer ou un bouton de parcours classique.
    
- **SF 2.2 - Prévisualisation des données :** Avant l'insertion en base, le système doit afficher un extrait du fichier (les 5 premières lignes) pour permettre à l'utilisateur de vérifier la correspondance des colonnes (Mapping).
    
- **SF 2.3 - Visualisation Graphique :** Les évènements doivent être affichés sous forme de calendrier (vues Mois, Semaine, Jour) et sous forme de liste de données tabulaires.
    
- **SF 2.4 - Opérations CRUD :** L'utilisateur doit pouvoir :
    
    - _Créer_ un nouvel évènement manuellement.
        
    - _Modifier_ un évènement (nom, date, heure, salle) via un formulaire ou par Drag & Drop sur le calendrier.
        
    - _Supprimer_ un évènement avec une demande de confirmation préalable.
        
    - _Rechercher_ un évènement via une barre de recherche textuelle.
        

#### Module 3 : Interopérabilité Google Agenda

- **SF 3.1 - Authentification OAuth :** L'application doit permettre de lier et de délier un compte Google de manière sécurisée.
    
- **SF 3.2 - Exportation avec Filtres :** L'utilisateur doit pouvoir exporter des évènements locaux vers Google Agenda. Le système doit proposer des filtres rapides (ex: "Tous les TP", "La semaine prochaine") pour faciliter la sélection.
    
- **SF 3.3 - Suivi de Synchronisation :** L'interface doit afficher un indicateur visuel (badge ou icône colorée) pour chaque évènement, indiquant s'il est parfaitement synchronisé avec Google, non synchronisé, ou s'il a subi une modification locale nécessitant une mise à jour.
    

#### Module 4 : Système de Notifications

- **SF 4.1 - Envoi ciblé :** Lors de l'ajout, la modification ou la suppression d'un évènement, l'utilisateur doit pouvoir envoyer une notification (email ou alerte système).
    
- **SF 4.2 - Sélection des destinataires :** L'interface doit proposer des cases à cocher pour cibler les destinataires : Étudiants, Enseignants, Responsables.
    
- **SF 4.3 - Historique :** Le système doit conserver et afficher l'historique complet des notifications envoyées, la date, l'évènement concerné et les cibles.
