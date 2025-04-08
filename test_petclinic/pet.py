from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC

# Démarrer le navigateur
driver = webdriver.Chrome()

# Ouvrir la page principale
driver.get("https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/")

# 🟢  Cliquer sur "Find Owners"
button_find_owner = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/owners/find']"))
)
button_find_owner.click()

# 🟢  Saisir "Davis" dans le champ "Last Name"
input_last_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='lastName' and @name='lastName' and @type='text']"))
)
input_last_name.send_keys("Davis")

# 🟢  Cliquer sur le bouton "Find Owner"
find_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
find_button.click()

# 🟢  Cliquer sur "Harold Davis"
harold_davis = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Harold Davis"))
)
harold_davis.click()

# 🟢  Récupérer le numéro de téléphone de Harold Davis
telephone_element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH,"//td[@headers='telephone']" ))
)
telephone_number = telephone_element.text

# 🟢  Vérifier si le numéro est correct
expected_number = "6085553198"
if telephone_number == expected_number:
    print("✅ Le numéro de Harold Davis est correct :", telephone_number)
else:
    print("❌ Le numéro est incorrect :", telephone_number)

add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Add New Pet']"))
)
add_button.click()

name_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='name' and @class='form-control']"))
)
pet_name = "Moustique"
name_field.send_keys(pet_name)

# 🟢  Remplir "Birth Date"
birth_date_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "birthDate"))
)
birth_date_field.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "flatpickr-calendar"))
)
print("✅ Le calendrier s'affiche bien")

date_to_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'flatpickr-day') and @aria-label='February 25, 2025']"))
)
date_to_select.click()
print("✅ Date sélectionnée : 25 Février 2025")


selected_date = birth_date_field.get_attribute("value")
print("✅ Date sélectionnée :", selected_date)

# 🟢  Sélectionner "dog" dans la liste déroulante
type_dropdown = Select(driver.find_element(By.ID, "type"))
type_dropdown.select_by_visible_text("dog")

# 🟢  Cliquer sur le bouton "Add Pet"
add_pet_button = driver.find_element(By.XPATH, "//button[text()='Add Pet']")
add_pet_button.click()

# 🟢  Vérifier que le pet a été ajouté (redirigé sur la page de Harold Davis)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h2[text()='Pets and Visits']"))
)

# 🟢  Vérifier que le pet "Moustique" est bien dans la liste
try:
    added_pet = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//dd[text()='{pet_name}']"))
    )

    print(f"✅ Le pet '{pet_name}' a été ajouté avec succès.")
except:
    print(f"❌ Erreur : le pet '{pet_name}' n'a pas été ajouté.")


# Fermer le navigateur
driver.quit()


