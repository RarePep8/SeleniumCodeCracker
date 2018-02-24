from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://live.hackvalley2.com/500hash')
hash_box = browser.find_element_by_id("hash-box")
submit_button = browser.find_element_by_id("get-button")
result = browser.find_element_by_id('result')

hash_box.clear()
hash_box.send_keys("hi")
submit_button.click()


hash_box.clear()
hash_box.send_keys("fuck this shit")
submit_button.click()


print(result.get_attribute("text"))
print(submit_button.text)

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def combinations_crack(curr_seq):
    if(len(curr_seq) < 10):
        for letter in ALPHABET:
            result = combinations_crack(curr_seq.append(letter)) 
    else:
        hash_box.clear()
        hash_box.send_keys(result)
        submit_button.click()
        
    
    
