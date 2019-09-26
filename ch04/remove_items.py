sample_list = ['Red','Green','White','Black','Pink','Yellow']
remove_list = [0,3,4]
for x in remove_list:
    print(x)
    sample_list.pop(x)

print(sample_list)
