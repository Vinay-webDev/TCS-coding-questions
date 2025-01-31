s1 = "hello world "
s2 = "who are you?"
def reverseSentence(s):
    N = len(s)
    def countWord(s):
        N, count = len(s), 0 if s[0] != " " else -1
        for i in range(1, N + 1):
            if s[i - 1] == " " and s[i] != " ":
                count += 1
        return count + 1
    t, arr = "", [0] * countWord(s)
    for i in range(N):
        if s[i] != " ":
            t += s[i]
        else:
            arr.append(t)
            t = ""
    res = ""
    for j in range(len(arr) - 1, -1, -1):
        res += arr[j] + " "
    return res
print(reverseSentence(s1))  #world hello
print(reverseSentence(s2))  #world hello
    