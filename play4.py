import http.client
import time
import socket

print ('''Welcome to SenEdu's HC, please read the below details:
          There are 2 types of HC embedded in this program: TCP and HTTP
          Type 1 for TCP HC
          Type 2 for HTTP HC''')

def HTTP_HC ():
    hc = 1

    server_name = input("What is the server's ip address or dns name: ")
    server_port = input("What is the server port to health check on: ")
    path = input("What is the path you would like to send the ELB health check to: ")
    status_code = int(input("What status code should you consider when marking the response as OK: "))
    timeout_hc = int(input("What is the health check timeout: "))
    hc_threshold = int(input('How many successive health check pass till mark as healthy: '))
    hc_unhealthy_threshold = int(input('How many successive health check failure till mark as unhealthy: '))

    while True:
        try:
            conn = http.client.HTTPConnection(server_name, server_port, timeout = timeout_hc)
            conn.request("GET", path)
            r1 = conn.getresponse()
            if (r1.status == status_code) and (hc % hc_threshold != 0):
                print ('Health Check', hc, 'to', server_name, 'has passed')
                hc = hc + 1
                time.sleep(timeout_hc)
            elif (r1.status == status_code) and (hc % hc_threshold == 0):
                print('Health Check', hc, 'to', server_name, 'has passed and', server_name, 'has been marked as healthy')
                hc = 1
                time.sleep(timeout_hc)
            #hc = 0
            elif (r1.status != status_code) and (hc % hc_unhealthy_threshold != 0):
                print('Health Check', hc, 'to', server_name, 'has failed with status code', r1.status )
                hc = hc + 1
                time.sleep(timeout_hc)
            elif (r1.status != status_code) and (hc % hc_unhealthy_threshold == 0):
                print('Health Check', hc, 'to', server_name, 'has failed and', server_name, 'has been marked as unhealthy' )
                hc = 1
                time.sleep(timeout_hc)
            else:
                print ('Health Check', hc, 'to', server_name, 'has failed')
                time.sleep(timeout_hc)
                hc = hc + 1
        except Exception as e:
            print('Sorry, health check to', server_name, 'is failing with Error: ', e )
            time.sleep(timeout_hc)

def TCP_HC():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print (e)

    try:
        server_ip = input ("What is your server's ip address: ")
        server_port = int(input ('What is the health check port of your server: '))
        hc_threshold = int(input ('How many successive health check till pass: '))
        hc_sleep = int(input ('What is the health check interval: '))
    except Exception as e:
        print(e)

        hc = 0
        s.connect((server_ip, server_port))


    while True:
        try:
            print('health check to', server_ip, 'passed OK')
            s.close()
            time.sleep(hc_sleep)
            hc = hc + 1
            if hc % hc_threshold == 0 :
                print ('ELB edu.amazonaws.com has marked', server_ip, "as healthy")
            elif:
                print('Health Check', hc, 'to', server_name, 'has failed')
                time.sleep(timeout_hc)
                hc = hc + 1
        except Exception as e:
            print (e)


try:
    HC_TYPE = int(input('What type of Health Check would you like to execute ? 1 or 2: '))

    if HC_TYPE == 1:
        HTTP_HC()
    elif HC_TYPE == 2:
        TCP_HC()
    else:
        print ('Sorry, wrong input')
except Exception as e:
    print(e)
