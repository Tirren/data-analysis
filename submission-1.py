import re
import numpy as np
from scipy.spatial import distance

with open('sentences.txt', mode='r') as f:
    file = f.readlines()
    data = [[word for word in re.split('[^a-z]', line.lower()) if word != ''] for line in file]

i = 0
word_index = dict()
for line in data:
    for word in line:
        if word not in word_index:
            word_index[word] = i
            i += 1

matrix = np.array([[0 for x in word_index] for i in range(len(data))])
for i in range(len(data)):
    for word in data[i]:
        j = word_index[word]
        matrix[i, j] += 1

distances = [[distance.cosine(matrix[0], matrix[i])] for i in range(len(data))]
sorted_list = sorted(distances)
print(distances.index(sorted_list[1]), distances.index(sorted_list[2]))

# matrix = np.zeros((num_lines, num))
# for i in range(num_lines):
#     for j in table:
#         matrix[i, table[j]] = original[i].count(j)

