#define a function
def leapyear(year):
    if(year %4 == 0 and year % 100 != 0 or year % 400 == 0):
        print (f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

#create a list 
year_list = ["1900", "2000", "2004", "2006"]
for year in year_list:
    int_year = int(year)
    leapyear(int_year)
