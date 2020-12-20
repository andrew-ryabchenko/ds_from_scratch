from key_connectors import users, friendships
from collections import Counter

# Function that returns count of mutual friends with all his respective friends for every user passed

def mutual_friends_count(user, users):

    # Determine if the foaf is the user
    def is_not_same(user, foaf):
        return user['id']!=foaf['id']

    # Determine if user has foaf in his friends list
    def is_not_friends(user, foaf):
        return foaf['id'] not in user['friends']

    result=[]

    for id in user['friends']:
        # Pull an object representing a friend by id
        friend = users[id]
        for foaf_id in friend['friends']:
             # Pull an object representing a foaf by id
            foaf = users[foaf_id]
            if (is_not_same(user, foaf) and is_not_friends(user, foaf)):
                result.append(id)
    
    return Counter(result)

print(mutual_friends_count(users[3], users))
print(users[3])
print(users[1])
print(users[2])
print(users[4])