Feature: Recherche sur DuckDuckGo

  Scenario: Rechercher un terme et afficher les résultats
    Given J'ouvre DuckDuckGo
    When Je saisis "Panda" dans la barre de recherche
    And Je clique sur le bouton de recherche
    Then Je vois des résultats de recherche
