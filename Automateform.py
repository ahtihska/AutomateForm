from selenium import webdriver
webdriver.Chrome()
driver = webdriver.Chrome()
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")


#inner nested
driver.switch_to.default_content()  
driver.switch_to.frame(1)
driver.switch_to.frame(0)
driver.switch_to.frame(0)
#filling Name
Name  = driver.find_element_by_xpath('//*[@id="fname"]')
Name.send_keys('Akshitha')
#filling Last Name
LastName = driver.find_element_by_xpath('//*[@id="lname"]')
LastName.send_keys('Chamala')
#Mobile No
Mobile = driver.find_element_by_xpath('//*[@id="mobile"]')
Mobile.send_keys('7396036423')
#Date of Birth
dob = driver.find_element_by_xpath('//*[@id="dob"]')
dob.send_keys('1999-11-11')
#Email
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('ahtihska@gmail.com')
#Country
country = driver.find_element_by_xpath('//*[@id="country"]')
country.send_keys('India')
#Gender
gender=driver.find_element_by_id("female")
gender.click()
#Hobbies
Hobbies=["Dance","Reading","Cricket"]
Hobby=[driver.find_elements_by_id(i) for i in Hobbies]
Hobby[0][0].click()
Hobby[1][0].click()
Hobby[2][0].click()
#Country dropdown
from selenium.webdriver.support.select import Select
sel = Select(driver.find_element_by_xpath('//*[@id="state"]'))
sel.select_by_visible_text("India")
#About
About  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[1]/div[11]/textarea')
About.send_keys('Akshitha')
#Des
Des  = driver.find_element_by_xpath('/html')
Des.send_keys('Akshitha')
#Authentication
username  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[1]/div/div/input')
username.send_keys('Akshitha')
pwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[2]/div/div/input')
pwd.send_keys('akshitha')
conpwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[3]/div/div/input')
conpwd.send_keys('akshitha')
#T&C
agree=driver.find_element_by_id("Agree")
agree.click()
#image upload
img = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[2]/input')
img.send_keys('/home/zoe/Downloads/bgg.jpeg')
# Form Submission
btn2 = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[4]/button[1]') 
btn2.click()

# nested
driver.switch_to.default_content()  
driver.switch_to.frame(1)
driver.switch_to.frame(0)
Name  = driver.find_element_by_xpath('//*[@id="fname"]')
Name.send_keys('Akshitha')
LastName = driver.find_element_by_xpath('//*[@id="lname"]')
LastName.send_keys('Chamala')
Mobile = driver.find_element_by_xpath('//*[@id="mobile"]')
Mobile.send_keys('7396036423')
dob = driver.find_element_by_xpath('//*[@id="dob"]')
dob.send_keys('1999-11-11')
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('ahtihska@gmail.com')
country = driver.find_element_by_xpath('//*[@id="country"]')
country.send_keys('India')
gender=driver.find_element_by_id("female")
gender.click()
Hobbies=["Dance","Reading","Cricket"]
Hobby=[driver.find_elements_by_id(i) for i in Hobbies]
Hobby[0][0].click()
Hobby[1][0].click()
Hobby[2][0].click()
from selenium.webdriver.support.select import Select
sel = Select(driver.find_element_by_xpath('//*[@id="state"]'))
sel.select_by_visible_text("India")
About  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[1]/div[11]/textarea')
About.send_keys('Akshitha')
Des  = driver.find_element_by_xpath('/html')
Des.send_keys('Akshitha')
username  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[1]/div/div/input')
username.send_keys('Akshitha')
pwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[2]/div/div/input')
pwd.send_keys('akshitha')
conpwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[3]/div/div/input')
conpwd.send_keys('akshitha')
agree=driver.find_element_by_id("Agree")
agree.click()
img = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[2]/input')
img.send_keys('/home/zoe/Downloads/bgg.jpeg')
btn1 = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[4]/button[1]') 
btn1.click()


#iframe without ID
driver.switch_to.default_content() 
driver.switch_to.frame(1)
Name  = driver.find_element_by_xpath('//*[@id="fname"]')
Name.send_keys('Akshitha')
LastName = driver.find_element_by_xpath('//*[@id="lname"]')
LastName.send_keys('Chamala')
Mobile = driver.find_element_by_xpath('//*[@id="mobile"]')
Mobile.send_keys('7396036423')
dob = driver.find_element_by_xpath('//*[@id="dob"]')
dob.send_keys('1999-11-11')
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('ahtihska@gmail.com')
country = driver.find_element_by_xpath('//*[@id="country"]')
country.send_keys('India')
gender=driver.find_element_by_id("female")
gender.click()
Hobbies=["Dance","Reading","Cricket"]
Hobby=[driver.find_elements_by_id(i) for i in Hobbies]
Hobby[0][0].click()
Hobby[1][0].click()
Hobby[2][0].click()
from selenium.webdriver.support.select import Select
sel = Select(driver.find_element_by_xpath('//*[@id="state"]'))
sel.select_by_visible_text("India")
About  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[1]/div[11]/textarea')
About.send_keys('Akshitha')
Des  = driver.find_element_by_xpath('/html')
Des.send_keys('Akshitha')
username  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[1]/div/div/input')
username.send_keys('Akshitha')
pwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[2]/div/div/input')
pwd.send_keys('akshitha')
conpwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[3]/div/div/input')
conpwd.send_keys('akshitha')
agree=driver.find_element_by_id("Agree")
agree.click()
img = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[2]/input')
img.send_keys('/home/zoe/Downloads/bgg.jpeg')
btn0 = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[4]/button[1]')
btn0.click()

#iframe with ID
driver.switch_to.default_content() 
driver.switch_to.frame("iframeId") 
Name  = driver.find_element_by_xpath('//*[@id="fname"]')
Name.send_keys('Akshitha')
LastName = driver.find_element_by_xpath('//*[@id="lname"]')
LastName.send_keys('Chamala')
Mobile = driver.find_element_by_xpath('//*[@id="mobile"]')
Mobile.send_keys('7396036423')
dob = driver.find_element_by_xpath('//*[@id="dob"]')
dob.send_keys('1999-11-11')
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('ahtihska@gmail.com')
country = driver.find_element_by_xpath('//*[@id="country"]')
country.send_keys('India')
gender=driver.find_element_by_id("female")
gender.click()
Hobbies=["Dance","Reading","Cricket"]
Hobby=[driver.find_elements_by_id(i) for i in Hobbies]
Hobby[0][0].click()
Hobby[1][0].click()
Hobby[2][0].click()
from selenium.webdriver.support.select import Select
sel = Select(driver.find_element_by_xpath('//*[@id="state"]'))
sel.select_by_visible_text("India")
About  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[1]/div[11]/textarea')
About.send_keys('Akshitha')
Des  = driver.find_element_by_xpath('/html')
Des.send_keys('Akshitha')
username  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[1]/div/div/input')
username.send_keys('Akshitha')
pwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[2]/div/div/input')
pwd.send_keys('akshitha')
conpwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[3]/div/div/input')
conpwd.send_keys('akshitha')
agree=driver.find_element_by_id("Agree")
agree.click()
img = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[2]/input')
img.send_keys('/home/zoe/Downloads/bgg.jpeg')
btn = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[4]/button[1]')
btn.click()


#form
driver.switch_to.default_content() 
Name  = driver.find_element_by_xpath('//*[@id="fname"]')
Name.send_keys('Akshitha')
LastName = driver.find_element_by_xpath('//*[@id="lname"]')
LastName.send_keys('Chamala')
Mobile = driver.find_element_by_xpath('//*[@id="mobile"]')
Mobile.send_keys('7396036423')
dob = driver.find_element_by_xpath('//*[@id="dob"]')
dob.send_keys('1999-11-11')
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('ahtihska@gmail.com')
country = driver.find_element_by_xpath('//*[@id="country"]')
country.send_keys('India')
gender=driver.find_element_by_id("female")
gender.click()
Hobbies=["Dance","Reading","Cricket"]
Hobby=[driver.find_elements_by_id(i) for i in Hobbies]
Hobby[0][0].click()
Hobby[1][0].click()
Hobby[2][0].click()
from selenium.webdriver.support.select import Select
sel = Select(driver.find_element_by_xpath('//*[@id="state"]'))
sel.select_by_visible_text("India")
About  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[1]/div[11]/textarea')
About.send_keys('Akshitha')
Des  = driver.find_element_by_xpath('/html')
Des.send_keys("Akshitha")
username  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[1]/div/div/input')
username.send_keys('Akshitha')
pwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[2]/div/div/input')
pwd.send_keys('akshitha')
conpwd  = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[3]/div/div/input')
conpwd.send_keys('akshitha')
agree=driver.find_element_by_id("Agree")
agree.click()
img = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[2]/div[1]/div/div[2]/input')
img.send_keys('/home/zoe/Downloads/bgg.jpeg')
btnmain = driver.find_element_by_xpath('//*[@id="automationtestform"]/div[4]/button[1]') 
btnmain.click()
