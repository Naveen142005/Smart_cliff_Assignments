
def create_file():
    #Read from file
    with open("input.txt", "r") as file_1:
        lines = file_1.readlines()
        reversed_line = []

        for i in lines:
            reversed_line.append(i.strip('\n')[::-1])

        #Reverse the lines
        reversed_line = '\n'.join(reversed_line)

    #Write into another file
    with open("reversed.txt", "w+") as file_2:
        file_2.write(reversed_line)

def main():
    create_file()
if __name__ == "__main__":
    main()
