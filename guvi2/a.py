from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_Locators import locators
from Test_Data import data
import pytest

class Dhanush():
 
    @pytest.fixture
    def booting_function(self):
          self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
          self.driver.get(data.data_Dhanush().url)
          self.driver.maximize_window()
          self.driver.implicitly_wait(10)
    def login(self, booting_function):
         
            self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
            self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_upper)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Admin).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_lower)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Admin).click()

            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_PIM)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().PIM).click()

            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_pim)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().PIM).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_LEAVE)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Leave).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_leave)
            sleep(5)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Leave).click()

            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_TIME)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Time).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_time)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Time).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_RECRUITMENT)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Recruitment).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_recruitment)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Recruitment).click()
 
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_MYINFO)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().My_info).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_myinfo)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().My_info).click()

            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_PERFORMANCE)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Performance).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_performance)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Performance).click()

            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_DASHBOARD)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Dashboard).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_dashboard)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Dashboard).click()

            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_DIRECTORY)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Directory).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_directory)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Directory).click()
            
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_MAINTAINANCE)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Maintenance).click()
      
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().main_password).send_keys(data.data_Dhanush().maintenance_password)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().conform_button).click() 
       
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_Maintainace)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Maintenance).click()
   
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_BUZZ)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Buzz).click()
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_box).send_keys(data.data_Dhanush().search_buzz)
            self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Buzz).click()

            assert self.driver.title == 'Management Application'
            print("Success")

#Testcase 2:
    def Adminpage(self, booting_function):
          # website login functions and loging function
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Admin).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().user_management).click() 
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().user_management).click()  
           self.driver.execute_script("window.stop();");  
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().user_name).send_keys(data.data_Dhanush().user_name)                
           userrole1=self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().userrole)
           userrole1.click()
           d1=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           
           if d1.__contains__("Admin"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Admin'",userrole1)
           num1=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().value_status)
           num1.click()
           d2=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d2.__contains__("Enabled"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Enabled'",num1)
           sleep(5)      
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().Admin).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().user_management).click() 
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().user).click()   
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().user_name).send_keys(data.data_Dhanush().user_name)                
           userrole2=self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().userrole)
           userrole2.click()
           d3=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d3.__contains__("ESS"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='ESS'",userrole2)
           status2=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().status)
           status2.click()
           d4=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d4.__contains__("Disabled"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Disabled'",status2)
        
           assert self.driver.title == 'Management Application'
           print("Success")
        
     #test case 3 
    def employee(self,booting_function):
          #Orange HRM website login functions and loging function
          self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
          self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().add_module).click() 
          self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().employee_firstname).send_keys(data.data_Dhanush().first_name)
          self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().employee_lastname).send_keys(data.data_Dhanush().last_name)
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().create_login).click()
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().login_name).send_keys(data.data_Dhanush().login_username)           
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().login_password).send_keys(data.data_Dhanush().login_password)
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().login_cformpword).send_keys(data.data_Dhanush().confirm_password)                                 
          self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button).click() 
          assert self.driver.title == 'Management Application'
          print("success")
#test case 4 
    def search_employee(self,booting_function):
           #Orange HRM website login functions and loging function
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click()                              
           assert self.driver.title == 'Management Application'
           print("success")

#test case 5 
    def personal_employee(self, booting_function):
           #Orange HRM website login functions and loging function
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click() 
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().otherid).send_keys(data.data_Dhanush().other_id)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().licence_number).send_keys(data.data_Dhanush().dlicense_number)           
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().expiry_date).send_keys(data.data_Dhanush().license_edate)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().ssnnumber).send_keys(data.data_Dhanush().ssn_number)          
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().sinnumber).send_keys(data.data_Dhanush().sin_number)                                    
           value=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().nationality)
           value.click()
           d_downvalue0=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down2).text
           if d_downvalue0.__contains__("Canadian"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian'",value)
           value2=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().marital_status)
           value2.click()  
           d_downvalue1=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down2).text
           if d_downvalue1.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",value2)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().date_ofbirth).send_keys(data.data_Dhanush().dob)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().gender).click()                         
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().military_s).send_keys(data.data_Dhanush().military_service)    
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button1).click()                                                                                                                       
           assert self.driver.title == "Management Application"
           print("success")

#test case 6 
    def contact_detail(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click()
           self .driver.find_element(by=By.LINK_TEXT, value=locators.locators_Dhanush().contact_detail).click() 
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().street).send_keys(data.data_Dhanush().street)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().street_n).send_keys(data.data_Dhanush().state_name)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().city).send_keys(data.data_Dhanush().city_name)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().state).send_keys(data.data_Dhanush().state_name)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().zcode).send_keys(data.data_Dhanush().zip_code)
           place=self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().country)
           place.click()
           d2=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down3).text
           if d2.__contains__("Canadian"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian'",place)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().home).send_keys(data.data_Dhanush().home_number)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().moblie).send_keys(data.data_Dhanush().mobile_number)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().work).send_keys(data.data_Dhanush().work_name)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().work_mail).send_keys(data.data_Dhanush().work_mailid)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().other_mailid).send_keys(data.data_Dhanush().other_mail)        
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button2).click()        
           assert self.driver.title == 'Management Application'
           print("success")

#test case 7 
    def emergency_details(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click() 
           self.driver.find_element(by=By.LINK_TEXT, value=locators.locators_Dhanush().emergency_contact).click()  
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().emergency_addbutton).click()  
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().name).send_keys(data.data_Dhanush().name)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().relationship).send_keys(data.data_Dhanush().relationship)                      
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().home_number).send_keys(data.data_Dhanush().home_telephone)           
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().mobile_number).send_keys(data.data_Dhanush().mobile_number1)           
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().work_number).send_keys(data.data_Dhanush().work_telephone)           
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button3).click()           
           assert self.driver.title == 'Management Application'
           print("success")

#test case 8 
    def dependents_details(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().dependent_b).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().dependents_add).click()  
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().dependents_n).send_keys(data.data_Dhanush().dependent_name)
           relative = self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().relationship_button)
           relative.click()
           d3=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d3.__contains__("Child"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Child'",relative)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().relation_dob).send_keys(data.data_Dhanush().realtion_dob)
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button4).click()     
           assert self.driver.title == "Management Application"
           print("success")

#test case 9 
    def job_detail(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().job).click()
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().joined).send_keys(data.data_Dhanush().joined_date) 
           sleep(2)
           job_name=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().job_title)
           job_name.click()
           d4=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d4.__contains__("Software Engineer"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Software Engineer'",job_name)
           job_role=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().job_category)
           job_role.click()
           d5=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d5.__contains__("Professionals"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Professionals'",job_role)
                   
           sub_name=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().sub_unit)
           sub_name.click()
           d6=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d6.__contains__("Engineering"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Engineering'",sub_name)    
     
           area=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().location)
           area.click()
           d7=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d7.__contains__("Canadian Regional HQ"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian Regional HQ'",area)    
               
           employee_position=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_status)
           employee_position.click()
           d8=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d8.__contains__("Full-Time Contract"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Full-Time Contract'",employee_position)
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button5).click()
           assert self.driver.title == 'Management Application'
           print("success")

#test case 10 
    def terminate_employee(self, booting_function):      
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().job).click()       
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush.terminate_button).click()
           sleep(2)  
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().terminate_de).send_keys(data.data_Dhanush().termination_date)
           Terminate=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush.terminate_reason)
           Terminate.click()
           d9=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush.drop_down).text
           if d9.__contains__("Other"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Other'",Terminate)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush.note).send_keys(data.data_Dhanush().terminate_note)    
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush.save_button6).click()
           assert self.driver.title == 'Management Application'
           print("success")

#test case 11 
    def activate_employee(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().job).click()       
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush.activation).click()  
           assert self.driver.title == 'Management Application'
           print("success")

#test case 12 
    def salarydetails(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click()  
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().salary).click()
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().salary_add).click()           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().salary_com).send_keys(data.data_Dhanush().salary_component)
           value=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pay_grade)
           value.click()
           d10=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d10.__contains__("Grade 1"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Grade 1'",value)
           name=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pay_frequency)
           name.click()
           d11=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d11.__contains__("Monthly"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Monthly'",name)     
           money=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().currency)
           money.click()
           d12=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d12.__contains__("Canadian Dollar"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian Dollar'",money)          
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush.salary_amount).send_keys(data.data_Dhanush().salary_amount)                     
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().toggle_on).click()     
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().account_no).send_keys(data.data_Dhanush().account_number)                      
           account=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().account_type)
           account.click()
           d13=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d13.__contains__("Savings"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Savings'",account) 
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().routing_no).send_keys(data.data_Dhanush().routing_number) 
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().routing_amount).send_keys(data.data_Dhanush().r_amount) 
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button7).click()
           assert self.driver.title == 'Management Application'
           print("success")

#test case 13 
    def tax (self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().username_locator).send_keys(data.data_Dhanush().username)
           self.driver.find_element(by=By.NAME, value=locators.locators_Dhanush().password_locator).send_keys(data.data_Dhanush().password)
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().loginButtonLocator).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().employee_name).send_keys(data.data_Dhanush().employee_name)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().click_button).click()          
           self .driver.find_element(by=By.LINK_TEXT, value=locators.locators_Dhanush().tax).click() 
           sleep(2)
           status=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().federal_status)
           status.click()
           d14=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d14.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",status) 
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().fendral_exemptions).send_keys(data.data_Dhanush().fit_exemption)
           state=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().state_income)
           state.click()
           d15=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d15.__contains__("New York"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='New York'",state)
           tax=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().state_status)
           tax.click()
           d16=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d16.__contains__("Single"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Single'",tax)
           self .driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().tax_exemptions).send_keys(data.data_Dhanush().sit_exemption)
           unemployee=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().unemployee)
           unemployee.click()
           d17=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d17.__contains__("California"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Hawaii'",unemployee)
           work=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().work_state)
           work.click()
           d18=self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().drop_down).text
           if d18.__contains__("Florida"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Texas'",work)  
           self.driver.find_element(by=By.XPATH, value=locators.locators_Dhanush().save_button8).click()           
           assert self.driver.title == 'Management Application'        
           print("success")       




