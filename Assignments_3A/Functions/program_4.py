""" 4. Write a function number_to_words(num) to convert a non-negative integer to its
 English words representation."""

# dictionary for number to word mapping
def number_to_words(num):
    d = {
        "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
        "8": "Eight", "9": "Nine", "10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen",
        "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen", "20": "Twenty",
        "30": "Thirty", "40": "Forty", "50": "Fifty", "60": "Sixty", "70": "Seventy", "80": "Eighty", "90": "Ninety",
    }

    def convert(amount):
        word = ""
        len_amount = len(amount)

        # check if number directly there in dictionary
        if amount in d:
            return d[amount] + " "

        # handle 2-digit numbers
        if len_amount == 2:
            return d[amount[0] + "0"] + " " + d[amount[1]] + " "

        # handle 3-digit numbers
        if len_amount == 3:
            if amount[1] + amount[2] in d:
                return d[amount[0]] + " Hundred " + d[amount[1] + amount[2]] + " "

            if amount[0] != "0":
                word += d[amount[0]] + " Hundred "

            if len(amount) > 1 and amount[1] != "0":
                word += d[amount[1] + "0"] + " "

            if len(amount) > 2 and amount[2] != "0":
                word += d[amount[2]] + " "

        return word

    # format number with commas
    s = format(num, ",")
    separated = s.count(",")
    amounts = []
    temp = ""

    for i in range(len(s)):
        if s[i] == ",":
            temp = temp + ((len(s) - (i + separated)) * "")
            amounts.append(temp.lstrip("0"))
            temp = ""
            separated -= 1
            continue

        temp += s[i]

    amounts.append(temp.lstrip("0"))
    amounts.reverse()

    s1 = s2 = s3 = s4 = ""

    # convert units place
    len_amounts = len(amounts)
    if len_amounts >= 1:
        s1 = convert(amounts[0])

    # convert thousands place
    if len_amounts >= 2:
        s2 = convert(amounts[1])
        if s2 != "":
            s2 += "Thousand "

    # convert millions place
    if len_amounts >= 3:
        s3 = convert(amounts[2])
        if s3 != "":
            s3 += "Million "

    # convert billions place
    if len_amounts >= 4:
        s4 = convert(amounts[3])
        if s4 != "":
            s4 += "Billion "

    if 0 == len((s4 + s3 + s2 + s1).strip()):
        return "Zero"
    return (s4 + s3 + s2 + s1).strip()


# main function starts here
def main():
    # take input number from user
    num = int(input())

    # call number to words function
    res = number_to_words(num)

    # print final result
    print(res)


if __name__ == "__main__":
    main()
