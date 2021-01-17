def func(s, temp):
    if not s:
        print("+".join(temp))
        return

    for i in reversed(range(len(s))):
        temp.append(s[0:i + 1])
        func(s[i + 1:], temp)
        temp.pop()


s = input("Enter a string: ")
func(s, [])

