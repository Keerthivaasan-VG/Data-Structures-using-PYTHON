from collections import deque  

def is_palindrome(word):
    n = len(word)
    dq = deque()
    for ch in word:
        dq.append(ch)
    while len(dq) > 1:   
        front = dq.popleft()   
        rear = dq.pop()       
        if front != rear:
            return False
    return True

print("PALINDROME CHECKER USING QUEUE")
text = input("Enter a word: ")
if is_palindrome(text):
    print("Result:", text, "IS a Palindrome")
else:
    print("Result:", text, "is NOT a Palindrome")
