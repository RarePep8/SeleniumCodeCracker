from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://live.hackvalley2.com/500hash')
hash_box = browser.find_element_by_id("hash-box")
submit_button = browser.find_element_by_id("get-button")
result = browser.find_element_by_id('result')






ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def combination_crack(curr_seq):
    if(len(curr_seq) < 10):
        for letter in ALPHABET:
            combination_crack(curr_seq + letter) 
    else:
        hash_box.clear()
        hash_box.send_keys(curr_seq)
        submit_button.click()
        time.sleep(0.25)
        temp = result.get_attribute("outerHTML")
        if("Hash" not in temp):
            print(temp[-12])
combination_crack("")
