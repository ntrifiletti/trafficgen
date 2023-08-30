#! /bin/python3

import requests
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

new_ip_adds = []
urls = ["https://www.darklab.co"]
for i in range(5):
    while i < 20:
        new_ip_adds.append((str(random.randint(3,8))+str(random.randint(3,8)))+"."+
                           (str(random.randint(3,8))+str(random.randint(3,8)))+"."+
                           (str(random.randint(3,8))+str(random.randint(3,8)))+"."+
                           (str(random.randint(3,8))+str(random.randint(3,8))))
        i = i+1
        
print(new_ip_adds)
print(len(new_ip_adds))
status_codes = []

def task(ip, urls):
    print("ip is "+ ip)
    headers={"X-Forwarded-For": ip}
    req = requests.get(urls, headers=headers)
    return req.status_code

def run_traffic(new_ip_adds):
    with ThreadPoolExecutor(max_workers=5) as executor:
        task_list = {executor.submit(task,ip, urls[0]): ip for ip in new_ip_adds }
        for executed_task in as_completed(task_list):
            print(executed_task.result())
    

def main():
    start_time = time.time()
    run_traffic(new_ip_adds)
    elapsed_time = time.time()-start_time
    print(elapsed_time)

main()





