def capitalize_list(words):
    for i in range(len(words)):
        words[i]=words[i].capitalize()
        print(words[i])
    return


fruits = ["banana","apple","cherry","plum","kiwi"]
print(fruits)
capitalize_list(fruits)
print(fruits)
