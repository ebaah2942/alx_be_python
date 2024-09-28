import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

display_current_datetime()



def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    formated_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formated_date}")


    


calculate_future_date()



