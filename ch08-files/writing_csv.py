employee_list=[{'name':'sahil','email':'sdahikk@hbgfgj','employee_id':'234523'},
           {'name':'sourabh','email':'sdahikk@hbgfgj','employee_id':'256523'},
           {'name':'sam','email':'sdahikk@hbgfgj','employee_id':'243523'}]

handle = open("employee.txt","w")
for employee in employee_list:
    for x in employee.values():
        handle.write(x + ',')
    handle.write('\n')

handle.close()

