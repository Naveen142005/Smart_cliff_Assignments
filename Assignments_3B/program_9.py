class StringProcessor:
    def ProcessString(self, txt , op = None):
        if op  ==" upper":
            return txt.upper()
        elif op == "reverse":
            return txt[::-1]
        elif op == "length":
            return len(txt)
        else:
            return txt

def main():
    sp = StringProcessor()

    myStr = input("Enter a string: ")

    print("Original:", sp.ProcessString(myStr))
    print("Uppercase:" ,sp.ProcessString(myStr,"upper"))
    print("Reversed:",sp.ProcessString(myStr,"reverse"))
    print("Length:" , sp.ProcessString(myStr,"length"))

if __name__=="__main__":
    main()
