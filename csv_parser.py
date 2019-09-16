# William Liu
#3/2/2018
#Description: Automobile Sorting

def function_all(option):
    #Parameter is needed for the extra credit
    #I made a lists for car type, car name, car line, and car MPG
    list_1 = []
    list_2 = []
    list_3 = []

    while True:
        ans = input("What year would you like to view data for? (2008 or 2009):")

        if ans == "2008":
            fileIn = open("epaVehicleData2008.csv", "r")
            break
        elif ans == "2009":
            fileIn = open("epaVehicleData2009.csv", "r")
            break
        else:
            print("*Invalid input, please try again!")
            continue

    ans1 = input("Enter the filename to save results to:")
    #These variables are to determine the highest MPG and lowest MPG
    highNum = 0
    lowNum = 0
    for line in fileIn:
        line = line.split(",")
        #Split is used to turn line into a list

        if option != "All":
            if option in line[0]:
                if str(line[9]) == 'HWY MPG (GUIDE)':
                    continue
                else:
                    list_1.append(line[9])
                    list_2.append(line[1])
                    list_3.append(line[2])
                    if int(line[9]) > int(highNum):
                        lowNum = highNum
                        highNum = line[9]

                    elif int(line[9]) < int(highNum) and int(line[9]) < int(lowNum):
                        lowNum = line[9]

            else:
                continue
        elif option == "All":
            if "PICKUP" in line[0]:
                continue
            elif "VANS" in line[0]:
                continue
            elif "MINIVAN" in line[0]:
                continue
            else:
                if str(line[9]) == 'HWY MPG (GUIDE)':
                    continue
                else:
                    #this will take the specified column and add it to their specific list
                    list_1.append(line[9])
                    list_2.append(line[1])
                    list_3.append(line[2])
                    if int(line[9]) > int(highNum):
                        lowNum = highNum
                        highNum = line[9]

                    elif int(line[9]) < int(highNum) and int(line[9]) < int(lowNum):
                        lowNum = line[9]
    #Counters are needed in order for the for loop, so that the index will increase by one
    counter1 = 0
    counter2 = 0
    fileOut = open(ans1, "w")

    if ans == "2008":
        print("EPA Highway MPG Calculator (2008)\n", file = fileOut)

    elif ans == "2009":
        print("EPA Highway MPG Calculator (2009)\n", file = fileOut)

    print("Maximum Mileage (highway):" + str(highNum), file=fileOut)
    for word in list_1:
        if int(word) == int(highNum):
            print(list_2[0 + counter1] + " " + list_3[0 + counter1], file=fileOut)
        counter1 += 1

    print("\nMinimum Mileage (highway):" + str(lowNum), file=fileOut)
    for word in list_1:
        if int(word) == int(lowNum):
            print(list_2[0 + counter2] + " " + list_3[0 + counter2], file=fileOut)
        counter2 += 1

    fileOut.close()
    print("Operation Success! Mileage data has been saved to " + ans1)
    print("Thanks, and have a great day!")

def main():
    print("Welcome to EPA Mileage Calculator")

    while True:
        user_ans = input("What vehicle type would you like to view?\n"
                        "Two Seater(1), Compact(2), Midsized(3), Large(4), Station Wagons(5), Pickup(6), Vans(7), SUV(8), All Cars(9):")
        #The parameter is what is used to select certain car types
        if user_ans == "1":
            function_all("TWO SEATER")
            break
        elif user_ans == "2":
            function_all("COMPACT")
            break
        elif user_ans == "3":
            function_all("MIDSIZED CARS")
            break
        elif user_ans == "4":
            function_all("LARGE CARS")
            break
        elif user_ans == "5":
            function_all("STATION WAGON")
            break
        elif user_ans == "6":
            function_all("PICKUP")
            break
        elif user_ans == "7":
            function_all("VAN")
            break
        elif user_ans == "8":
            function_all("S.U.V")
            break
        elif user_ans == "9":
            function_all("All")
            break
        else:
            print("*Invalid input, please try again!")
            continue
main()