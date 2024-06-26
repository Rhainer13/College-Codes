# Name: Mata, Rhainer Matheuz P.
# Date: March 15, 2024
# Exercise 2

PR = float(input("Amount of loan (Principal)? ")) # principal amount
IY = float(input("Interest Rate per year (per cent)? ")) # interest per year
NY = int(input("Number of years? ")) # number of years

NM = (NY * 12) # number of months
IM = (IY / 12) / 100 # interest per month
P = (1 + IM) ** NM 
Q = (P/(P - 1))
MP = (PR * IM * Q) # monthly payment

print(f"\nThe amount of the loan (principal)  : {PR}")
print(f"Interest rate/year (percent)        : {IY}")
print(f"Interest rate/month (decimal)       : {IM:.6f}")
print(f"Number of years                     : {NY}")
print(f"Number of months                    : {NM}")
print(f"Monthly payment                     : {MP:.2f}")

print(f"\nMonth\t\tOld Balance\t\tMonthly Payment\t\tInterest Paid\t\tPrincipal Paid\t\tNew Balance")

old_balance = PR

for i in range(NM):
    interest_paid = round(old_balance * IM, 2)
    principal_paid = round(MP - interest_paid, 2)
    new_balance = round(old_balance - principal_paid, 2)

    if i == (NM - 1):
        last = old_balance - principal_paid
        MP = MP + last

        # interest_paid = round(old_balance * IM, 2)
        
        principal_paid = round(MP - interest_paid, 2)
        new_balance = round(old_balance - principal_paid, 2)
    
    print(f"{i+1}\t\t{old_balance:.02f}\t\t\t{MP:.02f}\t\t\t{interest_paid:.02f}\t\t\t{principal_paid:.02f}\t\t\t{new_balance:.02f}")
    
    old_balance = new_balance