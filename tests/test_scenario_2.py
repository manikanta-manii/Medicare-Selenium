import time

from pages.login_page import TestLoginPage
from pages.patient_page import TestSlotBookPage
from pages.doctor_page import TestDoctorPage
from pages.admin_page import TestAdminPage
from database.doctors import DoctorsDB
from database.medicines import MedicinesDB

url="http://localhost:3000/"
medicine_image="/Users/mparameswarappa/Downloads/dolo.jpg"
delay = 3

def test_scenario_2(chrome_browser):
    driver = chrome_browser
    test_login = TestLoginPage(driver)
    test_login.login("manikantap036@gmail.com","Abcd@123")
    time.sleep(2)

    test_slot_book = TestSlotBookPage(driver)
    test_slot_book.navigate_to_url()
    test_slot_book.select_specalization("Cardiologist")
    time.sleep(2)

    test_login.login("doctor1@gmail.com", "Doctor@123")
    time.sleep(4)

    test_prescription = TestDoctorPage(driver)
    test_prescription.navigate_to_url()
    test_prescription.click_on_view()
    test_prescription.prescribe()




