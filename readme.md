### 🐾 Projet QA BDD – PetClinic avec Selenium, Behave et Page Object Model

Ce projet montre comment automatiser un scénario métier critique sur l'application PetClinic (Spring Framework) en utilisant :

🧪 BDD (Gherkin + Behave) pour une meilleure lisibilité métier

⚙️ Selenium pour piloter le navigateur

🧱 Page Object Model (POM) pour organiser proprement le code

🚀 Objectifs
Rechercher un propriétaire existant (“Harold Davis”)

Vérifier son numéro de téléphone

Ajouter un nouvel animal de compagnie (“Moustique”)

Vérifier que l’animal est bien ajouté

🧩 Architecture
bash
Copier
Modifier
DUCKDUCKGO_BEHAVE_PY_BDD/
├── features/
│ ├── add_pet.feature # Scénario en Gherkin
│ ├── steps/
│ │ └── step_add_pet.py # Étapes liées au scénario
│ ├── pages/
│ │ └── add_pet_page.py # POM – page “Add Pet”
│ └── environment.py # Hooks (setup/teardown)
├── requirements.txt # Dépendances
├── README.md # Ce fichier
├── .gitignore # Fichiers à exclure
📘 Exemple de scénario BDD
gherkin
Copier
Modifier
Feature: Ajout d'un animal pour un propriétaire existant

Scenario: Ajouter un pet à Harold Davis
Given je suis sur la page d'accueil de PetClinic
When je clique sur "Find Owners"
And je saisis "Davis" comme nom de famille
And je clique sur le bouton "Find Owner"
And je clique sur le lien "Harold Davis"
Then le numéro de téléphone doit être "6085553198"
When j'ajoute un nouvel animal appelé "Moustique" de type "dog" né le "25/02/2025"
Then le nouvel animal "Moustique" est bien affiché dans la fiche du propriétaire
🛠️ Exécution des tests
📦 Installation
bash
Copier
Modifier
pip install -r requirements.txt
▶️ Lancer le test
bash
Copier
Modifier
behave features/add_pet.feature
✅ Exemple de sortie
vbnet
Copier
Modifier
Feature: Ajout d'un animal pour un propriétaire existant
Scenario: Ajouter un pet à Harold Davis
Given je suis sur la page d'accueil de PetClinic ... OK
...
Then le nouvel animal "Moustique" est bien affiché ... OK

1 feature passed, 1 scenario passed
❓ Pourquoi automatiser ce test ?
Ce scénario reflète un parcours utilisateur critique :

Utilisé quotidiennement par les vétérinaires

Manipule des données clés : propriétaire, animal, type, date

Permet de valider l'intégrité de la fiche utilisateur

C’est aussi un bon candidat pour l’automatisation car :

Il est répétable

Il a des résultats attendus clairs

Il s’intègre bien dans une suite de régression

📌 Technologies utilisées
Outil Rôle
Python Langage principal
Selenium Automatisation du navigateur
Behave Scénarios BDD (Gherkin)
POM Organisation des pages
ChromeDriver Contrôle de Chrome
✨ Améliorations futures
Ajout de cas limites (ex : champ vide, mauvais type)

Rapports HTML (behave-html-formatter, allure)

Exécution via GitHub Actions (CI/CD)

Scénarios négatifs et tests de sécurité

🔗 Lien vers l’application
https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app
