def convert_to_words(num):
    l = len(num)
    if (l == 0):
        print("\nEmpty string")
        return

    if (l > 4):
        print("\n Length of the number is more than 4. It is not supported.")
        return

    single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    two_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    tens_power = ["hundred", "thousand"]

    print("\n The number", num, "in words is:", end=" ")

    if (l == 1):
        print(single_digits[ord(num[0]) - 48])
        return

    x = 0
    while (x < len(num)):
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                print(single_digits[ord(num[x]) - 48], end=" ")
                print(tens_power[l - 3], end=" ")
            l -= 1
        else:
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 + ord(num[x+1]) - 48)
                print(two_digits[sum], end=" ")
                return

            elif (ord(num[x]) - 48 == 2 and ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return

            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(tens_multiple[i], end="-")
                else:
                    print("", end="")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(single_digits[ord(num[x]) - 48], end=" ")
        x += 1


if __name__ == "__main__":
    number = str(input("\n Enter the number: "))

    if len(number) == 4 and  number[-2:] == "00" and number[-3:] != "000":
        result = convert_to_words(number[:2])
        print("hundred")
    else:
        result = convert_to_words(number)
