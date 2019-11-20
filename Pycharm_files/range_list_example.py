#range and list use


def inputdata(): #Define input data and computation (Tried to seperate)
    print('Welcome to the personal budget program!') #Print Header
    needs = ['Rent', 'Food', 'Transport', 'Other'] #Defining needs variables
    costs =[] #Empty list
    total = 0 #Total zeroed for monthly output

    for index in range(len(needs)): #Loop to get need amounts
        costCounter = 0 #Cost counter zeroed
        print(f'How much do you spend for {needs[index]}?') #ask for user input
        costCounter = getPosint() #run getPosint function
        costCounter = int(costCounter) #define cost counter as int
        costs.append(costCounter) #Add costs to list
        total += costCounter #Adds up costs for total
    return needs, costs, costCounter, total