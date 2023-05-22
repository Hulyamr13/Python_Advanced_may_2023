my_dict = {'Peter': [2, 6], 'George': [4], 'John': [6, 3]}
sorted_dict = sorted(my_dict.items(), key=lambda x: -sum(x[1]) / len(x[1]))
print(sorted_dict)


my_dict = {'Peter': [2, 6], 'George': [4], 'John': [6, 3]}
sorted_dict = sorted(my_dict.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)
print(sorted_dict)


my_dict = {'Peter': [2, 6], 'George': [4], 'John': [6, 3]}
sorted_dict = sorted(my_dict.items(), key=lambda x: -sum(x[1]) / len(x[1]), reverse=True)
print(sorted_dict)
