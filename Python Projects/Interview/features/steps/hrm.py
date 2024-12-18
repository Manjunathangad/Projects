from Interview.common_imports import *



test_data_path = os.path.realpath(os.path.abspath(os.getcwd()))+ "\Test_data\login.json"


@given('launch chrome browser')
def openchrome(context):
 context.driver = webdriver.Chrome(service=Service(r"C:\Users\prash\Downloads\chromedriver-win64\chromedriver.exe"))
 context.test_data = json.load(open(test_data_path, encoding="utf-8"))
 context.driver.get("https://amazon.com") 
 context.driver.maximize_window()
 time.sleep(20)

# @given('launch firefox browser')
# def openfirefox(context):
#  options = webdriver.FirefoxOptions()s
#  context.driver = webdriver.Firefox(options=options)
#  context.test_data = json.load(open(test_data_path, encoding="utf-8"))
#  context.driver.get("http://opshub.narmada.ivpdth.in/assets/login.html")
#  context.driver.maximize_window()
    

@when('open HP')
def openhp(context):
    test_data = context.test_data
    context.driver.find_element(
        By.XPATH, "//input[@id='j_username']").send_keys(test_data['login_data'][0]['username'])
    context.driver.find_element(
        By.XPATH, "//input[@id='j_password']").send_keys(test_data['login_data'][0]['password'])
    context.driver.find_element(By.XPATH, "//button[@id='btnPrimary']").click()


@then('verify the logo and close browser')
def verifylogo(context):
   try:
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@class='w7Vu97qRRCKYOcxwmtUboA==']")))
    context.driver.find_element(By.XPATH, "//img[@class='w7Vu97qRRCKYOcxwmtUboA==']").is_displayed()
    context.driver.close()
   except:
     context.driver.close()
     assert False, "Test Failed"
   
     
   

# @then('verify the "{un}" and "{pw}"logo and close browser')
# def verifylogo(context,un,pw):


# types of writing Xpath
# d.find_element(By.XPATH, "//div[@id='username']")
# d.find_element(By.XPATH, "//span[@class='fdsds543fd123_gfd43']")
# d.find_element(By.XPATH,"//span[normalize-space()='password']")
# d.find_element(By.XPATH,"//div[contains(text(),'username')]")
# d.find_element(By.XPATH,"//tagname[@*[.='manju']"]
# d.find_elemet(By.XPATH, "//input[@id ='search']")
     

# [Success] 200: Ok, 201: created, 202: accepted
# [Redirectional] 300 : multi choice, 301: moved permenetly
# [Client] 400: bad request, 401: unauth, 402:pay req 403: Forbidden, 404: not found, 405: Method not found
# [Server] 500: internal, 501: not implemened, 502: bad gateway, 503: service unavailable, 504: gateway timeout


   
     
