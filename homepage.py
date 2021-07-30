
from test_base import BaseTest
from config import TestData
from basePage import BasePage
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui




"""
/**
 ?  -----------------------THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN HOME PAGE --------------------------------------------------        
*/"""


class Homepage(BasePage):

    ###############################################   OBJECT SELECTORS   #########################################

    UploadFile = (By.XPATH, "//input[@id='inputImage']")
    Text = (By.XPATH, "//textarea[@class='form-control ng-touched ng-dirty ng-valid-parse ng-valid-maxlength ng-invalid ng-invalid-required']")
    Create_Item = (By.XPATH, "//button[@class='btn pull-right btn-success']")
    Update_item =  (By.XPATH, "//button[@class='btn pull-right btn-primary']")   
    Items_text = "//p[@class='story ng-binding']"
    Delete_Confirmation = "//button[@class='btn btn-primary']"

    
    
    ###############################################   OBJECT SELECTORS   #########################################

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def FileUpload(self):
        self.do_click(self.UploadFile)
        pyautogui.write(TestData.FileDirectory, interval=0.01)
        pyautogui.press('enter')
    
    def Description(self):
        self.do_send_keys(self.Text,TestData.Text)
    
    def Description_300(self):
        self.do_send_keys(self.Text,TestData.Text300)
            
    def Confirm_Item(self):
        self.do_click(self.Create_Item)
    
    def Edit_Item(self, ItemName):
        self.do_click(self.GetItemEditSelector(ItemName))
        self.do_send_keys(self.Text,TestData.Text)
        self.do_click(self.Update_item)
    
    def Delete_Item(self, ItemName):
        self.do_click(self.GetItemDeleteSelector(ItemName))
        self.do_click(self.Delete_Confirmation)
    
    def Get_Items_Text(self):
        return self.get_elements_text(self.Items_text)

    def GetItemEditSelector(self, ItemName):
        Edit =  f"(//p[@class='story ng-binding'][contains(text(), '{ItemName}')]/parent::div/parent::div/child::div/child::button)[1]"
        return Edit
    
    def GetItemDeleteSelector(self, ItemName):
        Delete =  f"(//p[@class='story ng-binding'][contains(text(), '{ItemName}')]/parent::div/parent::div/child::div/child::button)[2]"
        return Delete
