# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class TestEditarperfil():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editarperfil(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(1936, 1056)
    WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "username").send_keys("Manuvele")
    self.driver.find_element(By.ID, "password").send_keys("pepe")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-custom").click()
    self.driver.find_element(By.LINK_TEXT, "Manuvele").click()
    self.driver.find_element(By.ID, "id_first_name").click()
    self.driver.find_element(By.ID, "id_first_name").send_keys("mani")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-custom").click()
  
