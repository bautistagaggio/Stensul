from basePage import BasePage
from config import TestData
from test_base import BaseTest
from homepage import Homepage

class Test_Items(BaseTest):

    def test_create_item(self):
        homepage = Homepage(self.driver)
        homepage.FileUpload()
        homepage.Description()
        homepage.Confirm_Item()
        self.Assert_Exitence_Item()
    
    def test_edit_item(self):
        homepage = Homepage(self.driver)
        ItemName = TestData.Text
        homepage.Edit_Item(ItemName)
        self.Assert_Exitence_Item()

    def test_delete_item(self):
        homepage = Homepage(self.driver)
        ItemName = TestData.Text
        homepage.Delete_Item(ItemName)
        self.Assert_Not_Exitence_Item()
    
    def test_check_length(self):
        homepage = Homepage(self.driver)
        homepage.Description_300()
        self.Assert_Create_300()

    def test_text_existence(self):
        self.Assert_Creators()

    """
/**
 todo  ------------------------------------ ASSERTIONS ------------------------------------------
*/"""

    def Assert_Exitence_Item(self):
        homepage = Homepage(self.driver)
        Items = homepage.Get_Items_Text()
        assert TestData.Text in str(Items)
    
    def Assert_Not_Exitence_Item(self):
        homepage = Homepage(self.driver)
        Items = homepage.Get_Items_Text()
        assert TestData.Text not in str(Items)
    
    def Assert_Create_300(self):
        assert BasePage.Wait_for_Existence(Homepage.Create_Item) != True
    
    def Assert_Creators(self):
        homepage = Homepage(self.driver)
        Items = homepage.Get_Items_Text()
        assert TestData.text2 in str(Items)

            
            
