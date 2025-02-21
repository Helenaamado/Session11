from operator import truediv

import requests

link= "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
punctuation = ",.?1;\": -=(){}"
result= requests.get(link)
print(result.text)
unique_words ={}
lines= result.text.splitlines() #same as split but we use \n
for line in lines:
    for p in punctuation:
        line= line.replace(p, " ")
    words= line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0) +1

freq= list(unique_words.values())
freq.sort(reverse= True)
freq= freq[:10]
print(freq)
print("the most 10 common words are: ")
for f in freq:
    for key, value in unique_words.items():
      if value == f:
          print(key)