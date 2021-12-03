from selenium import webdriver
from time import sleep

college_name = input("College Name: ")

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get("https://www.collegesimply.com/")
sleep(2)

college_searchbar = browser.find_element_by_xpath("/html/body/header/nav/div/div[1]/form/div/div/input")
college_searchbar.send_keys(college_name)
college_searchbar.submit()
sleep(3)

browser.execute_script('window.scrollTo(0,200)')
# college_link = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a")
college_link = browser.find_element_by_css_selector('#___gcse_0 > div > div > div > div.gsc-wrapper > div.gsc-resultsbox-visible > div > div > div.gsc-expansionArea > div:nth-child(1) > div.gs-webResult.gs-result > div.gsc-thumbnail-inside > div > a > b')
college_link.click()
sleep(2)
   
# window_after = driver.window_handles[1]
# browser.switch_to_window(browser.window_handles[1])
browser.switch_to.window(browser.window_handles[1])
browser.execute_script('window.scrollTo(0,300)')
sleep(1)
overview_link = browser.find_element_by_xpath('/html/body/div[3]/div[4]/aside/div/nav/a[1]')
overview_link.click()
sleep(4)

# if len(browser.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[3]')) > 0:
#     browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[3]').click()
browser.execute_script('window.scrollTo(0,100)')
name = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/h1').text
state = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]/a[2]').text
population = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div[1]/div[1]/div').text
setting = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[4]/td[2]').text
camp_house = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[2]').text
p_type = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[2]').text
website = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[2]/a').text
# rank = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div[1]/div[2]/div').text
# graduation_rate = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[10]/div/div/div[2]/div').text
print('---------------------------------------------------------')
print('College Name: ' + name + '\nState: ' + state + '\nStudents Enrolled: ' + population + '\nCampus Setting: ' + setting + '\nOn-Campus Housing: ' +camp_house + '\nProfit Type: ' + p_type + '\nWebsite: ' + website)
sleep(1)

cost_link = browser.find_element_by_xpath('/html/body/div[3]/div[4]/aside/div/nav/a[3]')
cost_link.click()
sleep(4)

sticker_price = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div/div/div').text
net_price = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[3]/div/div[1]/div/table/tbody/tr[5]/td[2]').text
print('\nSticker Price: ' + sticker_price + '\nNet Price: ' + net_price)
sleep(1)

admissions_link = browser.find_element_by_xpath('/html/body/div[3]/div[4]/aside/div/nav/a[2]')
admissions_link.click()
sleep(2)

acceptance = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div').text
average_gpa = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[11]/div/div/div[1]/div').text

average_sat = browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[4]/div/div[2]/div[2]/table/tbody/tr[4]/td[2]').text
average_sat_math = (int(browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[4]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]').text) + int(browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[4]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]').text))/2
average_sat_english = (int(browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[4]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]').text) + int(browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[4]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]').text))/2
average_act = (int(browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[7]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]').text) + int(browser.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/div[7]/div/div[2]/div[1]/table/tbody/tr[3]/td[2]').text))/2
print('\nAcceptance Rate: ' + acceptance + '\nAverage GPA: ' + average_gpa + '\nAverage Sat: ' + average_sat + '\nAverage Sat Math: ' + str(average_sat_math) + '\nAverage Sat English: ' + str(average_sat_english) + '\nAverage ACT: ' + str(average_act))
print('---------------------------------------------------------')

browser.close()