# Exercise 1: Sliding window technique using heapq to reduce time complexity. 
import heapq
def max_sliding_window(num_list: list, k) -> list:
    results = []
    heap = []
    for i in range(k):
        # Adding item into heap, containing number and its index
        # Heapq is a min heap, so use opposite number to get create max heap-> generate max number in a window
        heapq.heappush(heap, (-num_list[i], i))
    
    results.append(-heap[0][0])
    for i in range(k, len(num_list)):
        heapq.heappush(heap, (-num_list[i], i))

        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        results.append(-heap[0][0])
    return results


# Exercise 2: Dictionary creation

def count_char(word: str) -> dict:
    results = {}
    for char in word:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
    return results

# Exercise 3: Read txt file and check occurences.
def count_words(file_path: str) -> dict:
    word_dict = {}
    with open(file_path, 'r') as file:
         content = file.read()
    text = content.lower().split()
    for word in text:
        word = word.strip()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict

# Exercise 4: Levenshtein distance
def levenshtein_dist(word1, word2):
    m = len(word1)
    n = len(word2)
    mattrix = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        mattrix[i][0] = i
    for j in range(n+1):
        mattrix[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            del_cost= mattrix[i-1][j] 
            insert_cost = mattrix[i][j-1] 
            sub_cost = mattrix[i-1][j-1]
            if word1[i-1] == word2[j-1]:
                mattrix[i][j] = sub_cost
            else: 
                mattrix[i][j] = min(del_cost, insert_cost, sub_cost) + 1
    
    return mattrix[m][n]


def My_function(integers, number=1):
    return [x == number for x in integers]
my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2)) 

    
     
    
