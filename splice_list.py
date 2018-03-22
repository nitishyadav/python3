#python program to "slicing lists from end"

#we have given a list containing the balance at the end of the day for some number of days. 
#the last item in the list represents yesterday's closing balance and each previous items refers to day before

daily_balances = [107.92, 108.67, 109.86, 110.15]


#The first step in the process is to grab adjacent items in the list. To get started, we want a function that takes in our list of daily_balances and prints pairs of adjacent balances for the last 3 days: 
'''
Should print
#"slice starting 3 days ago: [108.67, 109.86]"
#"slice starting 2 days ago: [109.86, 110.15]"
'''

print(daily_balances[3])
def show_balances(daily_balances):
    n =len(daily_balances)

# do not include -1 because that slice will only have 1 balance, yesterday
    for day in range(n -3,n-1):
        
        balance_slice = daily_balances[day : day + 2]
        day_out = n - day 
        # use positive number for printing, taking only the absolute value
        print("slice starting %d days ago: %s" % (abs(day_out), balance_slice))

#calling the function        
show_balances(daily_balances)
