from selenium import webdriver

#open up a Chrome browser and navigate web page
#initialize a variable to extract data from a website 
driver = webdriver.Chrome()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

#extract list of "buyers" and "prices" based on xpath

buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
print(buyers)
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

#print out all buyers and prices

num_page_item = len(buyers)

for i in range(num_page_item):
    print(buyers[i].text + " : " princes[i].text)

driver.close()