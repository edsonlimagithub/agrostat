
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Agrostat():
    
    def get_driver(self, driver):
        self.driver = driver

    def initial_page(self, url):
        self.driver.get(url)

    def get_iframe(self, xpath):
        iframe = self.driver.find_element_by_xpath(xpath)
        self.driver.switch_to_frame(iframe)

    def click_xpath(self, xpath):
        #Clicar na aba "Exportação Importação"
        #aba_exportacao_importacao_xpath = '/html/body/div[5]/div/div[181]/div[2]/table/tbody/tr/td'
        element = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def get_elements(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        elements = element.find_elements_by_xpath('*')
        return elements

    def action_scroll(self, Keys, xpath):
        scroll = self.driver.find_element_by_xpath(xpath)
        scroll.send_keys(Keys.END)

    def inner_html_by_id(self, id):
        e = self.driver.find_element_by_id(id)
        return e.get_attribute('innerHTML')

    def product_optional_list(self):
        product_optional_xpath = '//*[text()="Produto"]/../../../div[2]/div/div/div[@class="QvOptional_LED_CHECK_363636"]/div[2]/div[1]'
        elements = self.driver.find_elements_by_xpath(product_optional_xpath) 
        return elements

    def product_excluded_list(self):
        product_excluded_xpath = '//*[text()="Produto"]/../../../div[2]/div/div/div[@class="QvExcluded_LED_CHECK_363636"]/div[2]/div[1]'
        elements = self.driver.find_elements_by_xpath(product_excluded_xpath) 
        return elements

    def product_scroll_down(self):
        xpath = '//*[text()="Produto"]/../../../div[2]/*/div[@class="TouchScrollbar"][3]'
        element = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def page_down(self, times = 1):
        body_xpath = '/html/body'
        body = self.driver.find_element_by_xpath(body_xpath)
        body.click()
        for i in range(1, times):
            self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)

    def select_all_produts(self):
        product_title_xpath = '//div[text()="Produto"]/../../../../div[@class="QvFrame Document_LB525"]'
        product_title = self.driver.find_element_by_xpath(product_title_xpath)
        ActionChains(self.driver).context_click(product_title).perform()
        time.sleep(1)

        opcao_selecionar_tudo_xpath = '//*[text()="Selecionar Tudo"]'
        opcao_selecionar_tudo = self.driver.find_element_by_xpath(opcao_selecionar_tudo_xpath)
        ActionChains(self.driver).move_to_element(opcao_selecionar_tudo).click().perform()



    

        


