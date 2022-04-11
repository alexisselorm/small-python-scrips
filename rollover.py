def rollover():
    userchoices=[1,2]
    slips = int(input("How many days: "))
    amount = float(input("Enter your stake amount: "))
    slip = 1
    won = 0
    userchoice = int(
        input("Do you want \n 1. odds or \n 2. percentage\n (Please enter 1 or 2):"))
    while userchoice not in userchoices:
        print('Please type "1" or "2"')
        userchoice = int(
            input("Do you want \n 1. odds or \n 2. percentage\n (Please enter 1 or 2):"))
    if userchoice == 1:
        odds = float(input("How many odds: "))
        while slip <= slips:
            won = amount * odds
            amount = won
            print("Day {} is Gh¢{:.2f}".format(slip,won))
            slip += 1
    elif userchoice==2:
        percentage= float(input("what percentage are you looking for: "))
        while slip <= slips:
            won = amount * (percentage/100)
            amount += won
            print("Day {} is Gh¢{:.2f} and total money is Ghc {:.2f}".format(slip,won,amount))
            slip += 1


rollover()
