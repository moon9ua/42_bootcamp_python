languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

# print (len(languages))
# print(list(languages)[1])
# print(list(languages.values())[1])

for i in range(len(languages)):
    print("{} was created by {}"
          .format(list(languages)[i], list(languages.values())[i]))
