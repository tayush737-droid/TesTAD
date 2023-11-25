from selenium import webdriver
import time
import unittest

class AdNabuTestStoreAutomation(unittest.TestCase):

    def setUp(self):
        # You can choose the browser you want to use (Chrome, Firefox, etc.)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_product(self):
        driver = self.driver
        driver.get("https://adnabu-arjun.myshopify.com")

        # Perform the search
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Product Name")
        search_box.submit()

        # Wait for search results
        time.sleep(3)

        # Verify the search results
        search_results = driver.find_elements_by_class_name("product-title")
        self.assertTrue(any("Product Name" in result.text for result in search_results))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
