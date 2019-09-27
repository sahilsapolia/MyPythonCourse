with open('friends.txt') as friends_file:
    friend_list = []
    for friend in friends_file:
        friend_list.append(friend.rstrip())
    print(friend_list)

friends_file.close()