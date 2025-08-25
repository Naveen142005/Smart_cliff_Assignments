
def create_file():
    #Create the file
    with open("sample.txt", "w+") as file:
        print('Enter something to store in a file:')
        input_string = input()

        # Move the file pointer to start
        file.seek(0)

        #Write into the files
        file.write(input_string)

        #Force fully write into the disk instead of buffer
        file.flush()

        #Reading the input
        print('For changing...')
        print('Enter old text:')
        old_text = input()

        print('Enter new text:')
        new_text = input()

        # Move the file pointer to start
        file.seek(0)

        #Read and replace the words
        text = file.read()
        text = text.replace(old_text, new_text)
        print(text)

        # Move the file pointer to start
        file.seek(0)

        #Write into the file
        file.write(text)

def main():
    create_file()
if __name__ == "__main__":
    main()
