import time

from pages.login_page import TestLoginPage
from pages.medicine_page import TestBuyMedicinePage
from pages.patient_page import TestSlotBookPage
from pages.doctor_page import TestDoctorPage
from pages.admin_page import TestAdminPage
from database.doctors import DoctorsDB
from database.medicines import MedicinesDB

url="http://localhost:3000/"
medicine_image="/Users/mparameswarappa/Downloads/dolo.jpg"
delay = 3

def test_scenario_3(chrome_browser):
    driver = chrome_browser
    test_login = TestLoginPage(driver)
    test_login.login("manikantap036@gmail.com","Abcd@123")
    time.sleep(2)

    test_medicine = TestBuyMedicinePage(driver)
    test_medicine.navigate_to_url()

    medicines_table = MedicinesDB()
    time.sleep(2)
    total_medicines = medicines_table.get_medicines_count()
    test_medicine.add_to_cart(total_medicines)








