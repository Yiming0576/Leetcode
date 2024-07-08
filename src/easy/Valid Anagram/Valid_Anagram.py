from collections import defaultdict

def is_Anagram(s, t):
    sorted_t = sorted(t)
    sorted_s = sorted(s)

    return sorted_t == sorted_s



result = is_Anagram("cat", "tac")
print(f"result:  {result}")


def isAnagram(s, t):

    count = defaultdict(int)


    for x in s:
        count[x] +=1

    
    for x in t:
        count[x] -= 1


    for val in count.values():
        if val != 0:
            return False
        
    return True


def is_anagram(s, t):
    
    count = [0] * 26


    for x in s:
        count[ord(x) - ord('a')] += 1

    for x in t:
        count[ord(x) - ord('a')] -= 1
    
    for val in count:
        if val != 0:
            return False
        
    return True