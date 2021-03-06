# queue
qu = []
qu.append("queue1")
qu.append("queue2")
qu.pop(0)
# print(qu)

# stack
st = []
st.append("stack1")
st.append("stack2")
st.pop()
# print(st)


def palindrome(s):
    qu = []
    st = []
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        print("qu: ", qu)
        print("st: ", st)
        if qu.pop(0) != st.pop():
            return False
    return True


# print(palindrome("Wow"))

def palindrome_2(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


print(palindrome_2("wow"))
