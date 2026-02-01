# import libraries
import numpy as np
import numpy_financial as npf

# get input variables
print("\nDebt vs. Investing calculator . . .")
print("This program aims to determine the likelihood and amount that investing money rather than using it to pay off debt will pay off.")
print("Please fill in the appropriate information relating to the investment.\n")

version = ""
while version not in ("1", "2"):
    version = input("Calculate for a one time payment (Enter 1) or for recurring payments (Enter 2): ")

loanAmount = float(input("Enter the loan amount, e.g. 400000: "))
loanLengthYrs = int(input("Enter the loan length in years e.g. 30: "))
loanIntRate = float(input("Enter the loan interest rate as a decimal e.g. .031: "))
periodsPerYear = 12

downPayment = 0
extraPayOrInvest = 0
if version == "1":
    downPayment = float(input("Enter the down payment amount that you are considering putting towards the loan vs investing e.g. 40000: "))
if version == "2":
    extraPayOrInvest = float(input("Enter the amount that you would pay off or invest each period (there are " + str(periodsPerYear) + " periods in a year: "))

meanYearlyReturn = float(input("Enter the average yearly return that you anticipate from your investments. The average for large cap growth stocks is .122. If you are taking a safer or more aggressive approach, feel free to enter more or less. It is suggested you enter a lower amount to be safe. "))

print("\nSelect the type of investments you plan on using:")
print("1. Large Cap Stocks")
print("2. Small Cap Stocks")
print("3. Long Term Corporate Bonds")
print("4. Long Term Government Bonds")
print("5. Intermediate Term Government Bonds")
print("6. U.S. Treasury Bills")
choice = input("\nEnter the number corresponding with your investment type (1-6): ")
investment_options = {
    "1": "Large Cap Stocks",
    "2": "Small Cap Stocks",
    "3": "Long Term Corporate Bonds",
    "4": "Long Term Government Bonds",
    "5": "Intermediate Term Government Bonds",
    "6": "U.S. Treasury Bills"
}
investmentType = investment_options.get(choice, "Invalid selection")

returnStandardDeviation = 0
if investmentType == "Large Cap Stocks":
    returnStandardDeviation = .197
elif investmentType == "Small Cap Stocks":
    returnStandardDeviation = .31
elif investmentType == "Long Term Corporate Bonds":
    returnStandardDeviation = .084
elif investmentType == "Long Term Government Bonds":
    returnStandardDeviation = .102
elif investmentType == "Intermediate Term Government Bonds":
    returnStandardDeviation = .055
elif investmentType == "U.S. Treasury Bills":
    returnStandardDeviation = .031

# creates an array of realistic sample returns with a length of loanLengthYrs
def createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation):
    returnsArray = []
    for i in range(loanLengthYrs):
        z = np.random.normal(0, 1)
        returnsArray.append(meanYearlyReturn + z*returnStandardDeviation)

    return returnsArray

# creates a test sample array where each value is equal to the meanYearlyReturn, to deterministically compare results to old program
def createTestReturnsArray(loanLengthYrs, meanYearlyReturn):
    returnsArray = []
    for i in range(loanLengthYrs):
        returnsArray.append(meanYearlyReturn)
    return returnsArray

# calculates investment account value after n years after being given an array of returns of size n
def calcAccountExpectedValue(principalInvested, returnsArray):
    return principalInvested * np.prod(1 + np.array(returnsArray))

# identical to the numpy financial fv function, but passes in an array of return rates rather than a single return rate
def fvArray(returnsArray, periodsPerYear, periodicPayment, pv):
    value = pv
    for yearly_return in returnsArray:
        period_rate = yearly_return / periodsPerYear
        for _ in range(periodsPerYear):
            value = value * (1 + period_rate)
            value += periodicPayment   
    return value

# similar to fvArray, but duration of the investment is passed in rather than assumed from the array length
def fvArray2(returnsArray, investmentLengthYrs, periodsPerYear, periodicPayment, pv):
    value = pv
    total_periods = int(round(investmentLengthYrs * periodsPerYear))
    start_year_index = len(returnsArray) - int(np.ceil(investmentLengthYrs))
    periods_used = 0
    for yearly_return in returnsArray[start_year_index:]:
        period_rate = yearly_return / periodsPerYear
        for _ in range(periodsPerYear):
            if periods_used >= total_periods:
                return value
            value *= (1 + period_rate)
            value += periodicPayment
            periods_used += 1
    return value

# calculate results for a one time down payment/initial investment amount (version 1)
def calculateOneTimeResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, downPayment, returnsArray):
    principalInvested = downPayment
    totalInvestmentAccountValue = calcAccountExpectedValue(principalInvested, returnsArray)
    payment1 = npf.pmt(loanIntRate/periodsPerYear, loanLengthYrs*periodsPerYear, loanAmount*-1)
    totalInterestOnLoan1 = loanLengthYrs*periodsPerYear*payment1 - loanAmount
    payment2 = npf.pmt(loanIntRate/periodsPerYear, loanLengthYrs*periodsPerYear, (loanAmount-downPayment)*-1)
    totalInterestOnLoan2 = loanLengthYrs*periodsPerYear*payment2 - (loanAmount-downPayment)
    extraPmt = -(payment2 - payment1)
    investBenefit = (totalInvestmentAccountValue-(fvArray(returnsArray, periodsPerYear, extraPmt, pv=0)) - (totalInterestOnLoan1-totalInterestOnLoan2))
    return investBenefit

# calculate results for periodic recurring payments/investment amounts (version 2)
def calculateRecurringResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, extraPayOrInvest, returnsArray):
    totalAmountInvested = extraPayOrInvest*loanLengthYrs*periodsPerYear
    totalInvestmentAccountValue = fvArray(returnsArray, periodsPerYear, extraPayOrInvest, pv=0)
    investmentGain = totalInvestmentAccountValue-totalAmountInvested
    payment1 = npf.pmt(loanIntRate/periodsPerYear, loanLengthYrs*periodsPerYear, loanAmount*-1)
    totalInterestOnLoan1 = loanLengthYrs*periodsPerYear*payment1 - loanAmount
    payment2 = payment1 + extraPayOrInvest
    totalInterestOnLoan2 = npf.nper(loanIntRate/periodsPerYear, payment2, loanAmount*-1)*payment2 - loanAmount
    investmentLengthYrs = loanLengthYrs - npf.nper(loanIntRate/periodsPerYear, payment2, loanAmount*-1, 0)/12
    totalInvestmentAccountValue2 = fvArray2(returnsArray, investmentLengthYrs, periodsPerYear, (payment2), pv=0)
    investBenefit = totalInvestmentAccountValue - (totalInterestOnLoan1-totalInterestOnLoan2) - totalInvestmentAccountValue2
    return investBenefit


# Test 10000 random scenarios of the recurring payment calculator
#results = []
#for i in range(10000):
#    returnsArray = createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation)
#    results.append(calculateRecurringResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, extraPayOrInvest, returnsArray))
#print(sum(results)/len(results))


# Test the static return scenario of the recurring payment calculator
#returnsArray = createTestReturnsArray(loanLengthYrs, meanYearlyReturn)
#print(calculateRecurringResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, extraPayOrInvest, returnsArray))


# Test 10000 random scenarios of the one time calculator
#results = []
#for i in range(10000):
#    returnsArray = createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation)
#    results.append(calculateOneTimeResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, downPayment, returnsArray))
#print(sum(results)/len(results))


# Test the static return scenario of the one time calculator
#returnsArray = createTestReturnsArray(loanLengthYrs, meanYearlyReturn)
#print(calculateOneTimeResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, downPayment, returnsArray))


# Generates a sample return array of size 100000 and compares it to the input mean and standard deviation
#import statistics
#loanLengthYrs = 100000
#returnsArray = createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation)
#arrayMean = sum(returnsArray)/len(returnsArray)
#arraySD = statistics.stdev(returnsArray)
#print("The average return you selected was " + str(meanYearlyReturn) + " and the typical standard deviation of return for your selected investement type is " + str(returnStandardDeviation) + ".")
#print("The mean of the randomly generated returns was " + str(arrayMean) + " and the standard deviation was " + str(arraySD) + ".")

# Generate 10 sample return arrays of length 30 and print them
#for i in range(30):
#    loanLengthYrs = 30
 #   returnsArray = createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation)
 #   print(returnsArray)



# Generate 5 samples for each version and their corresponding investBenefit
for i in range(5):
    returnsArray = createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation)
    result = calculateOneTimeResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, downPayment, returnsArray)
    for i in range(len(returnsArray)):
        returnsArray[i] = round(returnsArray[i], 3)
    print(returnsArray)
    print(result)

#for i in range(5):
#    returnsArray = createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation)
#    result = calculateRecurringResults(loanAmount, loanLengthYrs, loanIntRate, periodsPerYear, extraPayOrInvest, returnsArray)
#    for i in range(len(returnsArray)):
#        returnsArray[i] = round(returnsArray[i], 3)
#    print(returnsArray)
#    print(result)