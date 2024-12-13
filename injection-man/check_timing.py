from selenium import webdriver
import speedtest

def time_avareging(target_url):
    sql_payloads = ['1','\'']
    st = speedtest.Speedtest()
    driver = webdriver.Chrome()
    list_of_time = []
    for payload in sql_payloads:
        replace_url = target_url + payload
        driver.get(replace_url)
        src = driver.page_source
        html_size = len(src.encode('utf-8'))
        download_speed = st.download()
        timing = html_size / download_speed

        print("HTML Size:", html_size, "bits")
        print("Download Speed:", download_speed, "s")
        print("timing average:", timing, "s")
        print("URL:", replace_url,)


        list_of_time.append(timing)
    finished = True
    list_of_time = sorted(list_of_time)
    print(list_of_time)
    print("The last item in the list is: ", list_of_time[-1])
    return list_of_time[-1], finished
