

from datetime import datetime

words = open('C:/Users/No Name/OneDrive/Desktop/vezba/dict_datetime.txt', 'r', encoding='utf_8')
words = words.read()

wordlist = words.split()
print(wordlist)


test_keys = wordlist[::2]
wordlist.insert(0, 0)

test_values = wordlist[::2]
#print(test_keys)
test_values.pop(0)
#print(test_values)

res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break
#print(res)

from collections import OrderedDict

ordered_data = OrderedDict(sorted(res.items(), key = lambda x:datetime.strptime(x[0], '%d-%m-%Y')) )

#print(ordered_data)

ordered_data1 = str(ordered_data)
#print(ordered_data1)

ordered_data_string = ordered_data1.replace("),", "\n")
ordered_data_string = ordered_data_string.replace("'", "")
ordered_data_string = ordered_data_string.replace("(", "")
ordered_data_string = ordered_data_string.replace("]", "")
ordered_data_string = ordered_data_string.replace("]", "")
ordered_data_string = ordered_data_string.replace(")", "")
print(ordered_data_string)

with open("C:/Users/No Name/OneDrive/Desktop/vezba/visual_analysis.txt", "a", encoding="utf_8") as f:
    f.write(ordered_data_string)
