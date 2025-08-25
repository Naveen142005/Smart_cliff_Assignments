
def create_file():
    #Read from file
    with open("data.txt", "r") as file_1:
        lines = file_1.readlines()
        cleaned_line = []

        for i in lines:
            cleaned_line.append(i.strip('\n').strip())

        #Clean the redundant content
        cleaned_line = '\n'.join(set(cleaned_line))

    #Write into another file
    with open("cleaned.txt", "w+") as file_2:
        file_2.write(cleaned_line)

def main():
    create_file()
if __name__ == "__main__":
    main()
