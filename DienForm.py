from selenium import webdriver

dem=0
while dem!=20:
	dem+=1
	url="https://forms.gle/4grzQLgP1YEFQ63F7"
	browser=webdriver.Chrome()
	browser.get(url)
	fill=browser.find_element_by_name('entry.1609267383')
	fill.send_keys('Thach5')
	fill=browser.find_element_by_name('entry.1548460402')
	fill.send_keys('Thach5')
	for i in browser.find_elements_by_xpath('//*[@role="radio"]'):
	     i.click()
	browser.find_elements_by_xpath('//*[@role="button"]')[0].click()
	browser.quit()
