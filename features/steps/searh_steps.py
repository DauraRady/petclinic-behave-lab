from behave import given, when, then
from selenium import webdriver
from pages.duckduckgo_page import DuckDuckGoPage

@given("J'ouvre DuckDuckGo")
def open_duckduckgo(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.page = DuckDuckGoPage(context.driver) 
    context.page.open()

@when('Je saisis "{query}" dans la barre de recherche')
def enter_search_query(context, query):
    context.page.enter_search(query)

@when("Je clique sur le bouton de recherche")
def click_search_button(context):
    context.page.click_search()

@then("Je vois des résultats de recherche")
def verify_results(context):
    results = context.page.get_results()
    assert len(results) > 0, "❌ Aucun résultat affiché sur DuckDuckGo !"
    print("✅ Test réussi : Les résultats sont bien affichés.")
    context.driver.quit()