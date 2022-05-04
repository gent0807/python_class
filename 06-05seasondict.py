season={'봄':'spring', '여름':'summer', '가을':'autumn', '겨울':'wninter'}
print(season.keys())
print(season.items())
print(season.values())

for key in season.keys():
    print('%s %s   ' % (key, season[key]))

for item in season.items():
    print('{} {}   '.format(item[0], item[1]), end=' ')
print()
for item in season.items():
    print('{} {}   '.format(*item), end=' ')
print()
          
