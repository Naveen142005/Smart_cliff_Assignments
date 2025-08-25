def main():
    #Read from files
    with open("document.txt", "r") as f:
        lines = f.readlines()

    #Read input
    keyword = input()
    keyword = keyword.lower()

    print("Lines: ", end= ' ')

    #Finding the keywords
    for i in range(0 , len(lines)):
        #Convert to lower for avoid cases-sensitive
        lines[i] = lines[i].lower()

        #Check the word exists or not
        if lines[i].find(keyword) != -1:
            print(i + 1, end= ',')

if __name__ == "__main__":
    main()
