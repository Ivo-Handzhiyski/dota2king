from matches import get_match_history

data = get_match_history(matches_requested=100)

print('-------------')
print(data)


file = open('match_data', "w")

file.write(data)