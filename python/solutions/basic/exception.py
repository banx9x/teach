try:
    with open("solutions/python/demo.txt") as file:
        lines = file.readlines()

        for line in lines:
            print(line.strip())  # remove newline
except IOError as e:
    print(e)
