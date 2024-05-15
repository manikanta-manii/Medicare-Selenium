from pages.login_page import TestLoginPage
from pages.admin_page import TestAdminPage

url="http://localhost:3000/"
medicine_image="/Users/mparameswarappa/Downloads/dolo.jpg"
delay = 3

def test_scenario_1(chrome_browser):
    driver = chrome_browser
    test_login = TestLoginPage(driver)
    test_login.login("admin@gmail.com","Admin@123")
    test_add = TestAdminPage(driver)
    test_add.click_doctor_view()
    doctor1 = test_add.add_doctor("doctor1","doctor1@gmail.com","8987678987","2","1000",1)
    doctor2 = test_add.add_doctor("doctor2", "doctor2@gmail.com", "9878987678", "3", "1500",2)

    medicine1 = test_add.add_medicine(medicine_image,"DOLO","FOR FEVER AND HEADACE","10","2","10","true")
    medicine2 = test_add.add_medicine(medicine_image, "PARACETAMOL", "FOR FEVER AND HEADACE", "10", "2", "10", "false")

