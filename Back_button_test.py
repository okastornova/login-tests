from selenium.webdriver import Opera

browser = Opera(executable_path="/Users/macbook/webdriver/operadriver")
browser.get('https://mail.ru')
browser.find_element_by_name("login").send_keys('ttesterski@mail.ru')
browser.find_element_by_id("mailbox:submit").click()
browser.implicitly_wait(5)
browser.find_element_by_id("mailbox:password").send_keys('O+ryrpoAOY24')
browser.find_element_by_id("mailbox:submit").click()
browser.implicitly_wait(7)
browser.find_element_by_link_text("sign out").click()
browser.back()
print(browser.title)