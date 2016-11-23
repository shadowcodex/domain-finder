__author__ = 'SHADOWxCODEX'
#pip install requests
#or easy_install requests
#found under python_path\Scripts\pip
#if you get an python egg related error, try 'pip install --upgrade setuptools'

import requests
import itertools

print('Author: SHADOWxCODEX')
print('Date Created: 7-24-2015')
print('Source: https://github.com/SHADOWxCODEX/pydomainfinder')

acronym = input('Please enter your company acronym : ')
acc_list = list(acronym)
matrix = [['']*2 for x in range (5)]
sec_matrix = []
count = 0

#Get the replacement names for the acronym characters
for char in acc_list:
    acc_name = input('Please tell me what ' + char + ' stands for : ')
    matrix[count][0] = char
    matrix[count][1] = acc_name
    print('Character :' + matrix[count][0])
    print('Name :' + matrix[count][1])
    sec_matrix.append(char)
    sec_matrix.append(acc_name)
    count += 1

type_of_comb = input('Would you like "1" only options in your acronym order or "2" everything?')

count2 = 0
inner_count = 0
inner_test = True
result_matrix = []
for item in itertools.combinations(sec_matrix, 4):
    if(type_of_comb == '1'):
        inner_count = 0
        result = ""
        for sub_item in item:
            #print(sub_item)
            #print("Corresponding Sec info : " + sec_matrix[inner_count])
            if((sub_item == sec_matrix[inner_count] or sub_item == sec_matrix[inner_count+1])):
                inner_test = True
                inner_count += 2
                result += sub_item
            else:
                inner_test = False
                break

        if(inner_test):
            print(item)
            print(result)
            result_matrix.append(result)
            count2 += 1
    else:
        result = ""
        for sub_item in item:
            result += sub_item
        print(item)
        print(result)
        result_matrix.append(result)
        count2 += 1



print('Total number of combinations: ' + str(count2))

def callwhois(payload_matrix, total):
    print(payload_matrix)
    print("Keep in mind you only get 500 free API Calls per month, do you want to continue with " + str(total) + " whois calls?")
    y_n_or_load = input("'1' for yes, '2' for no, '3' for write to log only")
    if(y_n_or_load == '2'):
        #do nothing and quit
        return
    elif(y_n_or_load == '1'):
        domain_available = open('domain_available.txt', 'w')
        domain_registered = open('domain_registered.txt', 'w')
        domain_whois = open('domain_whois.txt', 'w')
        #call the whois for each domain. Store info into logs.
        print("if there is an error with the program, and it exits throwing an error. You have reach your rate limit")
        for each_payload in payload_matrix:
            print("Starting request for ... " + each_payload + " ... please wait ...")
            payload = {"domain": each_payload}
            the_headers = {"Accept":"application/json","Authorization":"Token token=<API KEY>"}
            r = requests.get("https://jsonwhois.com/api/v1/whois", headers=the_headers, params=payload)
            response = r.json() #parsed json response

            #record all domain whois information
            domain_whois.write("############### domain " + each_payload + " who is ###############\n")
            domain_whois.write(str(response) + "\n")
            domain_whois.write("\n\n")

            print(str(response))
            if(response["available?"] == True):
                domain_available.write(each_payload + "\n")

            if(response["registered?"] == True):
                domain_registered.write(each_payload + "\n")

    #write domain log
    domain_log = open('domain_log.txt', 'w')
    for each_payload in payload_matrix:
        domain_log.write(each_payload + "\n")
    domain_log.close()

    print("All done!, please look for the following files in this directory. domain_available.txt, domain_registered.txt, domain_whois.txt, domain_log.txt")
    return

payload_type = input('Would you like "1" all .coms, "2" all .nets, "3" all .orgs, or "4" all three?')
if(payload_type == '1'):
    print('Total payload :' + str(count2))
    payload_matrix = []
    for res in result_matrix:
        populate = res + ".com"
        payload_matrix.append(populate)
    callwhois(payload_matrix, count2)
elif(payload_type == '2'):
    print('Total payload :' + str(count2))
    payload_matrix = []
    for res in result_matrix:
        populate = res + ".net"
        payload_matrix.append(populate)
    callwhois(payload_matrix, count2)
elif(payload_type == '3'):
    print('Total payload :' + str(count2))
    payload_matrix = []
    for res in result_matrix:
        populate = res + ".org"
        payload_matrix.append(populate)
    callwhois(payload_matrix, count2)
elif(payload_type == '4'):
    payload_total = count2*3
    print('Total payload :' + str(payload_total))
    payload_matrix = []
    for res in result_matrix:
        populate = res + ".com"
        payload_matrix.append(populate)
        populate = res + ".net"
        payload_matrix.append(populate)
        populate = res + ".org"
        payload_matrix.append(populate)
    callwhois(payload_matrix, payload_total)



