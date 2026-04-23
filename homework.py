# Program to find all substrings of a user-input string
while True:
    s = input("Enter a string: ")
    substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    print("All substrings:")
    for sub in substrings:
        print(sub)