"""
---- GET INPUT AND SELECTION ----
Give user instructions to select either Investment or Bond based on what \
    they calculating.
Store their input in variable named selection and convert to lowercase using \
    .lower()

---- CHECK CONDITIONS FOR INVESTMENT ----
If user enters "I" or "Investment" then ask user for deposit amount, store \
    input in variable named deposit and cast input into float.
Ask user for interest rate, store input in variable named interest_rate and \
    cast input into float.
Ask user for term (in years) for how long they plan to invest, store in a \
    variable name term and cast input value into a float
Ask user which type of interest they would like to calculate, Simple(S) or \
    Compound(C), convert input value to lowercase (using .lower())

If user enters "Simple" or "S" then
    calculate their total by using formula: \
        total = deposit * (1 + (interest_rate / 100) *  term)
    print their total Simple Investment and round to two decimals

else if user enters "Compound" or "C" then
    calculate their total by using formula: \
        total = deposit * math.pow((1 + (interest_rate / 100)), term)

    print their total Compound Investment and round to two decimals

---- CHECK CONDITIONS FOR BOND ----
If user entered "B" or "Bond" then
    Ask user for the value of the house, store in a variable and cast their \
        input into a float
Ask user for interest rate, store input in variable named interest_rate and \
    cast input into float
Calculate and store monthly interest rate by diving interest rate by 12 ask \
    user for term (in months) for how long their bond payment will be, store \
        in a variable name term and cast input value into a float
Calculate their repayment by using formula:
            (monthly_interest_rate * value_of_house) / \
                (1 - (1 + monthly_interest_rate) ** (-term))
"""

import math

# give user information about two options available
print("\nInvestment / i - to calculate the amount of interest you'll earn on" +
      " your investment\n" +
      "Bond / b       - to calculate the amount you'll have to pay on a home"
      + " loan\n")

# get selection from user to calculate either Investment or Bond
selection = input("Good day, please enter either 'Investment' or 'Bond' from" +
                  " the menu above to proceed: ").lower()

#   ---------- INVESTMENT CALCULATOR ----------
if (selection == "investment") or (selection == "i"):
    print("\nGreat, you have selected Investment.\n")

    # declare variables and get input from user
    deposit = float(input("Enter the amount you are depositing: R"))
    interest_rate = float(input("Now enter the amount of interest (%): "))
    term = float(input("Great, now enter the amount of years you plan on" +
                       " investing: "))
    interest = input("Finally, enter either 'Simple' or 'Compound' for the" +
                     " interest you are calculating: ").lower()

    # check condition to calculate either Simple or Compound interest
    if (interest == "simple") or (interest == "s"):

        # calculate total simple investment
        total = deposit * (1 + (interest_rate / 100) * term)
        print(f"\nYour total simple investment would be: R{total:.2f}\n")

    elif (interest == "compound") or (interest == "c"):
        # calculate total compound investment
        total = deposit * math.pow((1 + interest_rate / 100), term)
        print(f"\nYour total compound investment would be: R{total:.2f}\n")

    else:
        print("Invalid selection, please try again.")

#   ---------- BOND CALCULATOR ----------
elif (selection == "bond") or (selection == "b"):
    print("\nYou have selected Bond.\n")

    # declare variables and get input from user
    value_of_house = float(input("To get started, please enter the value of" +
                                 " the house: R"))
    annual_interest_rate = float(input("Great, now please enter the" +
                                       " percentage of annual interest (%): "))
    term = float(input("Lastly, enter the number of months you plan to" +
                       " repay: "))

    # calculate monthly interest by dividing annual interest by 100 (percent) \
    # and then 12 (months)
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # calculate total repayment
    repayment = (monthly_interest_rate * value_of_house) / \
        (1 - (1 + monthly_interest_rate) ** (-term))
    print(f"\nYour total monthly repayment is R{repayment:.2f}\n")

else:
    print("\nInvalid selection, please run again and enter either Investment" +
          " or Bond.\n")
