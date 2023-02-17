def calculate_minimum_coins(change, denominations):
    denominations = sorted(denominations, reverse=True)
    result = []
    for i in denominations:
        while change >= i:
            result.append(i)
            change -= i
    return result

if __name__ == "__main__":
    print("\n Enter coin denomination(space seperated): ", end="")
    denominations = list(map(int, input().split()))

    change = int(input("\n Enter the amount for which you want change: "))

    result = calculate_minimum_coins(change, set(denominations))

    print("\n The minimum number of coins required to make up the change of", change, "is:", len(result))

    print("\n Array with each coin to be given as change is:", result)
