# Namn: Armin
# Klass: IT22
# Uppgift:  Månatliga avbetalningar


def calculate_monthly_payment(principal, annual_rate, years):
    # beräknar räntan
    # beräknar år
    # avbetalningen
    
    #9%
    rate = annual_rate / 12 / 100
    months = years * 12
    payment = (principal * rate) / (1 - (1 + rate) ** -months)
    return payment
   


    
    
                            


principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")
