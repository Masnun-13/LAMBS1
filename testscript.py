from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\\Programming3\\LAMBS1\\WebDrivers\\chromedriver.exe")

report = Report()

report.setup(
	report_folder=r'D:\Programming3\LAMBS1\Reports',
	module_name='Report',
	release_name='Release 1',
	selenium_driver=driver
)
driver.get(url="http://127.0.0.1:8000/")
time.sleep(3.0)

# Test 1
try:
    report.write_step(
    	'Testing Login Page functionality',
    	status=report.status.Start,
    	test_number=1
    )
    driver.find_element_by_link_text("Log in").click()
    time.sleep(3.0)
    report.write_step(
    	'Entered Login',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )


# Test 2
try:
    report.write_step(
    	'Testing Login functionality',
    	status=report.status.Start,
    	test_number=2
    )
    driver.find_element_by_name("username").send_keys("Masnun")
    time.sleep(2.0)
    driver.find_element_by_name("password").send_keys("dummypass")
    time.sleep(2.0)
    driver.find_element_by_name("loginbutton").click()
    time.sleep(2.0)
    report.write_step(
    	'Logged in',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )


# Test 3
try:
    report.write_step(
    	'Testing Home Page functionality',
    	status=report.status.Start,
    	test_number=3
    )
    driver.find_element_by_link_text("Home").click()
    time.sleep(3.0)
    report.write_step(
    	'Entered Home Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )


# Test 4
try:
    report.write_step(
    	'Testing Profile Page functionality',
    	status=report.status.Start,
    	test_number=4
    )
    driver.find_element_by_link_text("Profile").click()
    time.sleep(3.0)
    report.write_step(
    	'Entered Profile Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )


# Test 5
try:
    report.write_step(
    	'Testing Routines Page functionality',
    	status=report.status.Start,
    	test_number=5
    )
    driver.find_element_by_link_text("Routines").click()
    time.sleep(3.0)
    report.write_step(
    	'Entered Routines Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 6
try:
    report.write_step(
    	'Testing User Info functionality',
    	status=report.status.Start,
    	test_number=6
    )
    driver.find_element_by_link_text("User Info").click()
    time.sleep(3.0)
    report.write_step(
    	'Entered User Info Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 7
try:
    report.write_step(
    	'Testing Create User functionality',
    	status=report.status.Start,
    	test_number=7
    )
    driver.find_element_by_link_text("Enter New User Info").click()
    time.sleep(4.0)
    driver.find_element_by_name("submitbutton").click()
    time.sleep(2.0)
    report.write_step(
    	'Created new user in User Info table with default values',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 8
try:
    report.write_step(
    	'Testing Update User functionality',
    	status=report.status.Start,
    	test_number=8
    )
    driver.find_element_by_link_text("Update").click()
    time.sleep(2.0)
    driver.find_element_by_name("user_age").send_keys("2")
    time.sleep(2.0)
    driver.find_element_by_name("submitbutton").click()
    time.sleep(2.0)
    report.write_step(
    	'Updated user age value',
    	status=report.status.Pass,
    	screenshot=True
    )


except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 9
try:
    report.write_step(
    	'Testing Delete User functionality',
    	status=report.status.Start,
    	test_number=9
    )
    driver.find_element_by_link_text("Delete").click()
    time.sleep(2.0)
    driver.find_element_by_name("confirmbutton").click()
    time.sleep(2.0)
    report.write_step(
    	'Deleted user from User Info table',
    	status=report.status.Pass,
    	screenshot=True
    )


except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 10
try:
    report.write_step(
    	'Testing Log Out functionality',
    	status=report.status.Start,
    	test_number=10
    )
    driver.find_element_by_link_text("Log out").click()
    time.sleep(3.0)
    report.write_step(
    	'Logged out',
    	status=report.status.Pass,
    	screenshot=True
    )


except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )


finally:
    report.generate_report()
    driver.quit()