def main():
    #Read the number n
    n = int(input())

    #Read all lines from file
    with open("bigfile.txt","r") as f:
        line = f.readlines()

    file_count = 0

    #traversing the file content
    for i in range(0,len(line) , n):
        #Count the file's count
        file_count += 1
        j = i
        end = n
        lines_to_write= ""

        #Extract n lines from all lines
        while j < len(line) and end:
            lines_to_write += line[j]
            j += 1
            end -= 1

        #Create new files
        file_name = f"part{file_count}.txt"

        #Write n lines into the created file
        with open(file_name, "w+") as file:
            file.write(lines_to_write)


if __name__ == "__main__":
    main()
