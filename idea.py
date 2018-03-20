s = "betty bought a bit of butter but the butter was bitter"
n = 3

list_0 = s.split()#word
list_1 = []#times

for i in range(len(list_0)):
    list_1.append(list_0.count(list_0[i]))#count the number of the words
    
list_2 = list(sorted(set(list_0)))#sort words；remove repeated words
list_3 = []#sort the times of word by list_2

for i in range(len(list_2)):
    list_3.append(list_1[list_0.index(list_2[i])])#sort the times of word by list_2

data = [(word,times) for word, times in zip(list_2,list_3)]
data.sort(reverse = True)
data_s = sorted(data, key = lambda x: (-x[1],x[0]))

top_n = data_s[0:n]
print(top_n)
