#!/bin/python3
# Import Libraries
import getopt
import sys
from time import sleep
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains as AC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BROWSER=webdriver.Chrome('chromedriver_win32/chromedriver.exe');
BROWSER.maximize_window()
USERNAME="username"
PASSWORD="password"

def login():
    BROWSER.get("https://github.com/login");
    assert "Sign in to GitHub" in BROWSER.title;
    user_field=BROWSER.find_element_by_xpath("//*[@id='login_field']");
    user_field.clear();
    user_field.send_keys(USERNAME);
    pass_field=BROWSER.find_element_by_xpath("//*[@id='password']");
    pass_field.clear();
    pass_field.send_keys(PASSWORD);
    login_botton=BROWSER.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]");
    login_botton.click();
    assert "No results found." not in BROWSER.page_source;

def createRepo(repoName):
    BROWSER.get("https://github.com/new");
    assert "New Repository" in BROWSER.title;
    repo_name_field=BROWSER.find_element_by_xpath("//*[@id='repository_name']");
    repo_name_field.clear();
    repo_name_field.send_keys(repoName);
    readme_checkbox=BROWSER.find_element_by_xpath("//*[@id='repository_auto_init']");
    readme_checkbox.click();
    create_repository=BROWSER.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button");
    sleep(1);
    create_repository.send_keys(Keys.RETURN);

def deleteRepo(repo):
    BROWSER.get("https://github.com/" + USERNAME + "/" + repo + "/settings");
    reject_cookies=BROWSER.find_element_by_xpath("/html/body/div[9]/div/div/div/div[1]/div/div/button[2]");
    reject_cookies.click()
    delete_button=BROWSER.find_element_by_xpath("//*[@id='options_bucket']/div[10]/ul/li[4]/details/summary");
    sleep(1);
    delete_button.click()
    text_box=BROWSER.find_element_by_xpath("//*[@id='options_bucket']/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input");
    text_box.clear()
    text_box.send_keys(USERNAME + "/" + repo)
    #sleep(2)
    confirm=BROWSER.find_element_by_xpath("//*[@id='options_bucket']/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button/span[1]");
    #cursor= AC(BROWSER).move_to_element(confirm)
    sleep(1)
    #cursor.perform()
    confirm.click()


def parseOpts():
    try: 
        opts, args = getopt.getopt(sys.argv[1:], "c:d:", ["create=","delete="])
    except(err):
        print("Error : " + err)
    for opt, arg in opts:
        if opt in ("-c", "--create"):
            createRepo(arg)
        if opt in ("-d", "--delete"):
            deleteRepo(arg)

def main():
    login()
    sleep(1)
    parseOpts()
    BROWSER.close()

    







if __name__ == "__main__":
    main()





# Todo
# * 
# * 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

