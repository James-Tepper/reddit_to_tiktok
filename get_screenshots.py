from selenium import webdriver

driver = webdriver.Firefox()
driver.get(post.url)


def take_title_screenshot(driver, wait):
    handle = 


def take_comment_screenshot(driver, wait, comment_id):
    handle = By.ID
    id = f"t1_{comment_id}"
    search = wait.until(EC.presence_of_element_located((handle, id)))
    
    screenshot_name = f"{screenshot_directory}/{handle}.png"
    file = open(screenshot_name, "wb")
    file.write(search.get_screenshot_as_png())
    file.close()
    return screenshot_name
