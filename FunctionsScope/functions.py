# Mini Task: Write a function is_palindrome(s) that returns True/False

def is_palindrome(s):
    v1 = True if s == s[::-1] else False

    s_copy = []
    for i in range(len(s) - 1, -1, -1):
        s_copy.append(s[i])
    v2 = (s == ''.join(s_copy))

    es = s
    es = list(es)
    es.reverse()
    v3 = ''.join(es) == s

    print(v3)

    return v1 == v2 == v3

print(is_palindrome('racecar'))