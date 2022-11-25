from django.contrib.auth.models import User
from profilepage.testing_tools import SeleniumTestCase
from selenium.webdriver.common.by import By


import time

class AuthenticationFormTest(SeleniumTestCase):
    def test_authentication_form(self):
        # Create a user to login with
        user = User.objects.create_user(
            username="test@user.com", password="12345"
        )

        # Go to the login page
        self.driver.get(self.live_server_url + "/login/")

        # Find HTML elements
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "btn-login")

        # Type in an username that doesn't exist
        username_input.send_keys("wrong@user.com")

        # Type in a password
        password_input.send_keys("wrongpassword")
        login_button.click()

        # Wait for request
        time.sleep(0.5)

        # Check that the error message is displayed
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".error")
        self.assertEqual(error_message.text, "Your username and password didn't match. Please try again.")

        # Type in the correct username and password
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "btn-login")
        username_input.clear()
        username_input.send_keys(user.username)
        password_input.send_keys("12345")
        login_button.click()

        # Wait for request
        time.sleep(0.5)

        # Check that the user is logged in
        self.assertEqual(self.driver.current_url, self.live_server_url + '/profile/'+ str(user.profile.id) +"/")

        # Check that the username, edit button and map are displayed
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, "a").text, 'Portfolio Map')
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, "h2").text, user.username)
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".bi-pencil-fill").is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".leaflet-container").is_displayed(),True)
