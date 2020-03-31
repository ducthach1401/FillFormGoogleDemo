from selenium import webdriver
from ThuVienTen import *

n=int(input('Nhap so lan dien form: '))
list_name=thuvienten(n)

for i in range(n):
	url="https://forms.gle/4grzQLgP1YEFQ63F7"
	browser=webdriver.Chrome()
	browser.get(url)
	fill=browser.find_element_by_name('entry.1609267383')
	fill.send_keys(list_name[i])
	fill=browser.find_element_by_name('entry.1548460402')
	fill.send_keys('Random')
	for i in browser.find_elements_by_xpath('//*[@role="radio"]'):
	     i.click()
	browser.find_elements_by_xpath('//*[@role="button"]')[0].click()
	browser.quit()
print('Done')
