def pound(kilo):
    return(kilo*2.205)# function for convert Kilogram to Pound.

kilo = float(input("Enter the value in Kilogram\n"))#asking user to enter the value for convert.
pound = pound(kilo)
print(kilo,"Kilogram is = ",float(pound),"Pound")