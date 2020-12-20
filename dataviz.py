import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

def plot():
    plt.plot(years, gdp, color='red', marker='x', linestyle='dashed', linewidth=0.5)
    plt.title('Nominal GDP')
    plt.ylabel('Billions of $')
    plt.show()

# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]
# # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# # so that each bar is centered
# xs = [i+1 for i, _ in enumerate(movies)]

# # plot bars with left x-coordinates [xs], heights [num_oscars]
# plt.bar(xs, num_oscars, color='g', align='center')
# plt.bar(xs, num_oscars, color='r', align='edge', width=0.4)

# # Biased picture as it doesnt show a full magnitude of a values but rather zooms only the magnitude of difference
# plt.axis([3,6,7.8,11.5])

# plt.show()

# Scatter plot with annotations

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Stretch goal. 
# Order 'friends' and synchronously shuffle 'minutes' preserving original correspondence of values.

# Zip values of both
# zipper = list(zip(friends, minutes))
# # Sort zipper by 'friends' value
# zipper = sorted(zipper, key = lambda item: item[0], reverse=False)
# # Unpack sorted zipper to two lists
# friends = [f for f,_ in zipper]
# minutes = [m for _,m in zipper]
#____________________________________________________________________

# Plot scatter plot with annotations

plt.scatter(friends, minutes)
for f,m,l in zip(friends,minutes,labels):
    plt.annotate(l,(f,m), textcoords='offset pixels', xytext=(5,5))
#plt.axis('equal')
plt.show()
