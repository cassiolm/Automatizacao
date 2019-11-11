import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

chromeOps = webdriver.ChromeOptions()
chromeOps._binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe"
chromeOps._arguments = ["--enable-internal-flash"]

browser = webdriver.Chrome("C:\\Applications\\Browser\\chromedriver.exe", port=4445, options=chromeOps)
time.sleep(3)
browser.set_window_size(1024, 600)
browser.maximize_window()
time.sleep(3)
browser.get("http://191.255.219.184:4000/extrator/pmix")

browser.find_element_by_xpath("//input[@placeholder='Usuário']").click();
browser.find_element_by_xpath("//input[@placeholder='Usuário']").send_keys("seu login");   
browser.find_element_by_xpath("//input[@placeholder='Senha']").click();
browser.find_element_by_xpath("//input[@placeholder='Senha']").send_keys("sua senha);  
browser.find_element_by_id("button-login").click();
time.sleep(4)

# browser.get("http://191.255.219.184:4000/extrator/pmix")
# time.sleep(5)

# browser.execute_script('document.getElementsByName("data-v-0121dc7b")[0].removeAttribute("readonly")')
periodo = browser.find_element_by_class_name("input-period")
periodo.click()
periodo.send_keys("10")
periodo.send_keys("01")
periodo.send_keys("2019")
#periodo2 = browser.find_element_by_class_name('["input-period"][div=2]')
periodo2 = browser.find_element_by_xpath('(//input[@class="input-period"])[2]')
periodo2.click()
time.sleep(2)
periodo2.send_keys("10")
periodo2.send_keys("08")
periodo2.send_keys("2019")
time.sleep(2)
desativar = browser.find_element_by_xpath('(//input[@id="select-all"])[2]')
desativar.click()
# desativar = 
# desativar.click()
# desativar = browser.find_elements_by_xpath('(//span[@id="select-all"])[1]')
# desativar.click()
# browser.find_element_by_id("btn-extract").click();
# time.sleep(3)
# browser.find_element_by_id("btn-confirm").click();

# # browser.find_element_by_xpath("//label[text()='Fev']").click()
# browser.find_element_by_xpath("//li[text(),'Jan')]").click()
# time.sleep(4)
# browser.find_element_by_id("btn-extract").click();
# time.sleep(2)
# browser.find_element_by_id("btn-ok").click();
# time.sleep(2)

# browser.find_element_by_xpath("//input[@type='date'").removeAttribute("readonly").send_keys("01/01/2018"); 
# browser.find_element_by_xpath("//input[@type='date'").send_keys("01/01/2018");

# browser.get("http://191.255.219.184:4000/extrator/pmix")
# time.sleep(5)
# browser.find_element_by_id("btn-extract").click();
# time.sleep(2)
# browser.find_element_by_id("btn-confirm").click();
# time.sleep(2)
# browser.find_element_by_id("btn-ok").click();
# time.sleep(5)

# browser.get("http://191.255.219.184:4000/extrator/gc")
# time.sleep(5)
# browser.find_element_by_id("btn-extract").click();
# time.sleep(2)
# browser.find_element_by_id("btn-confirm").click();
# time.sleep(2)
# browser.find_element_by_id("btn-ok").click();
# time.sleep(5)

# browser.get("http://191.255.219.184:4000/extrator/pmix")
# time.sleep(5)
# browser.find_element_by_id("btn-extract").click();
# time.sleep(2)
# browser.find_element_by_id("btn-confirm").click();
# time.sleep(2)
# browser.find_element_by_id("btn-ok").click();
# time.sleep(5)


# browser.get("http://191.255.219.184:4000/extrator/gc")
# time.sleep(5)
# browser.find_element_by_id("btn-extract").click();
# time.sleep(2)
# browser.find_element_by_id("btn-confirm").click();
# time.sleep(2)
# browser.find_element_by_id("btn-ok").click();



# time.sleep(5)
# browser.find_elements_by_css_selector("input[type='radio'][value='2']").click();


# browser.get("http://191.255.219.184:4000/extrator/extracoes")


# browser.find_elements_by_partial_link_text('http://191.255.219.184:4000/extrator/pmix')click();


# webdriver.ActionChains(browser).click(on_element='//button[text()="Some text"]')

#driver.find_element_by_css_selector('.button .c_button .s_button').click()