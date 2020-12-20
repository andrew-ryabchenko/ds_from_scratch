from interests import index

# Find out what topic users are most interested in

topics_rating = []

for key in index.keys():
    topics_rating.append((key, len(index[key])))

topics_rating = sorted(topics_rating, key = lambda i: i[1], reverse = True)

print(topics_rating)