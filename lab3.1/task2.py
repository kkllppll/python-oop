import datetime

class Calendar:
    def __init__(self, today_date=datetime.date.today()):
        self.date = today_date
        self.month_last = None

    def subtracting(self, days=0, months=0, years=0):
        start_day = self.date.day
        start_year = self.date.year

        if self.date.month - months > 0: self.month_last = self.date.month - months
        else:
            self.month_last = 12 - abs((self.date.month - months))

        while (self.date.month != self.month_last) or (self.date.year != (start_year - years)):
            self.date -= datetime.timedelta(days=1)

        last_month_day = self.date.day
        self.date -= datetime.timedelta(days=last_month_day-start_day+days)

        return self.date


    def adding(self, days=0, months=0, years=0):
        if (self.date.month + (months % 12)) % 12 != 0: self.month_last = (self.date.month + (months % 12)) % 12
        else:
            self.month_last = 12

        start_day = self.date.day
        start_year = self.date.year
        while (self.date.month != self.month_last) or (self.date.year != (start_year + years)):
            self.date += datetime.timedelta(days=1)

        for i in range(start_day+days-1): 
            self.date += datetime.timedelta(days=1)

        return self.date

   

def change_date():
    number_day = input("Since you want to change the date you need to enter some information\n \
        enter the number of days, months, years for which you want to change the date.\n Enter the days --> ")
    number_month = input("Month --> ")
    number_years = input("Years --> ")

    if number == "1":
        return 1, number_day, number_month, number_years
    elif number == "2":
        return 2, number_day, number_month, number_years
    else:
        print("Error!")





calendar = Calendar()
number = input("Date: Today`s date (press 1), Your own date (press 2)")
if number in ["1", "2"]:
        if number == "1": print("Today", calendar.date)
        elif number == "2":
            day = input("Enter:\n day --> ")
            month = input("month --> ")
            year = input("year -->")
            datetime.datetime.strptime(day + "/" + month + "/" + year, "%d/%m/%Y").date()
            print("Your date:", calendar.date)
        else:
            calendar = Calendar()

        func = change_date()
        change_day = int(func[1]) 
        change_month = int(func[2])
        change_year = int(func[3])
        print("For adding days to the date press --> 1, for subtracting press --> 2?")
        number = input("Your choice -->")
        if func[0] == 1:
                print(f"After {change_day} day(s), {change_month} month(s), {change_year} year(s) will be:",
                  calendar.adding(days=change_day, months=change_month, years=change_year))
                if calendar.date !=  calendar.adding(days=change_day, months=change_month, years=change_year):
                    if  calendar.date >  calendar.adding(days=change_day, months=change_month, years=change_year):
                        print(f'\t\tthe start date is bigger than the end date')
                    if  calendar.date <  calendar.adding(days=change_day, months=change_month, years=change_year):
                        print(f'\t\tthe start date is less than the end date')
                elif calendar.date ==  calendar.adding(days=change_day, months=change_month, years=change_year):
                    print(f'\t\tthe start date is the same as the end date')
                else: 
                    print(f'false')
        elif func[0] == 2:
            print(f"{change_day} day(s), {change_month} month(s), {change_year} year(s) before was:",
                calendar.subtracting(days=change_day, months=change_month, years=change_year))
            if calendar.date !=  calendar.adding(days=change_day, months=change_month, years=change_year):
                if  calendar.date >  calendar.adding(days=change_day, months=change_month, years=change_year):
                        print(f'\t\tthe start date is bigger than the end date')
                if  calendar.date <  calendar.adding(days=change_day, months=change_month, years=change_year):
                        print(f'\t\tthe start date is less than the end date')
                elif calendar.date ==  calendar.adding(days=change_day, months=change_month, years=change_year):
                    print(f'\t\tThe start date is the same as the end date')

else:
        print("Error, check your choice and try again!")





