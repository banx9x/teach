def binary_search(l, id):
    if len(l) == 1:
        return l[0] == id
    
    mid = len(l) // 2

    if l[mid] == id:
        return True
    else:
        return binary_search(l[0:mid], id) if id < l[mid] else binary_search(l[mid:], id)


s = input("Enter the top participant's ID: ")

try:
    winner_ID = list(map(lambda i: int(i), s.split(sep=" ")))
    winner_ID.sort()

    print(f"Sorted top participant's ID: {winner_ID}")

    id = int(input("Enter participant's ID: "))

    if binary_search(winner_ID, id):
        print("Congratulations! You have been shortlisted in the Top 10 \"Best Programmer 2020\".")
    else:
        print("Unsuccessful!")
except ValueError:
    print("Invalid Participant's ID!!!")
