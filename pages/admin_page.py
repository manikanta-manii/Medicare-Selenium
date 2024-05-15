
import time
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass


class TestAdminPage:

    # VIEW_BUTTON =
    # ADD_BUTTON = (By.ID, 'myInput')
    # NAME_FIELD = By.ID, 'name'
    # EMAIL_FIELD = By.ID, 'email'
    # PHONE_NUMBER = By.ID, 'phone_number'
    # YOE = By.ID, 'years_of_experiance'
    # CONSULTATION_FEE = By.ID, 'consultation_fee'
    # SELECT_BUTTON = By.ID ,'specialization_id'
    # SUBMIT_BUTTON = (By.ID, 'submit-btn')
    #
    # IMAGE_FIELD = By.ID, 'image'
    # DESCRIPTION_FIELD = By.ID, 'description'
    # PRICE = By.ID, 'price'
    # DOSAGE = By.ID, 'dosage'
    # QUANTITY = By.ID, 'quantity'
    # NEED_PRESCRIPTION = (By.ID ,'need_prescription')


    def __init__(self, driver):
        self.driver = driver

    def click_doctor_view(self):
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'doctor-view-btn'))
        print("2 .Entered Doctors Index Path")

    def add_doctor(self,name,email,phone,yoe,fee,sid):
        self.driver.get("http://localhost:3000/doctors")
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'myInput'))
        print("3. Click on Add Button")
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'name'),name)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'email'), email)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'phone_number'), phone)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'years_of_experiance'), yoe)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'consultation_fee'), fee)
        BaseClass(self.driver, 3).wait_and_click((By.ID ,'specialization_id'))
        BaseClass(self.driver,3).wait_and_click((By.XPATH, f'//select[@id="specialization_id"]//option[@value="{sid}"]'))
        BaseClass(self.driver,3).wait_and_click((By.ID, 'submit-btn'))
        print(f"DOCTOR ADDED SUCCESFULLY-{name}")

    def add_medicine(self,image,name,description,price,dosage,quantity,pid):
        self.driver.get("http://localhost:3000/medicines")
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'myInput'))
        print("3. Click on Add Button")
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'image'), image)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'name'), name)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'description'), description)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'price'), price)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'dosage'), dosage)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'quantity'), quantity)
        BaseClass(self.driver, 3).wait_and_click((By.ID ,'need_prescription'))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, f'//select[@id="need_prescription"]//option[@value="{pid}"]'))
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'submit-btn'))
        print(f"MEDICINE ADDED SUCCESFULLY-{name}")







