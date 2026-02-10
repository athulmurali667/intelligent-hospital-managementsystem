from datetime import datetime, timedelta


def find_day(date_string):
    # Convert the date string to a datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    # Get the day of the week (e.g., Monday, Tuesday)
    return date_object.strftime('%A')

def list_days_between(start_date_string, end_date_string):
    # Convert the date strings to datetime objects
    start_date = datetime.strptime(start_date_string, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_string, '%Y-%m-%d')

    # Initialize a list to hold all the dates
    date_list = []

    # Iterate through the range of dates
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return date_list

# Example usage
start_date_string = '2024-08-15'
end_date_string = '2024-08-20'
days_list = list_days_between(start_date_string, end_date_string)
print('All days between {start_date_string} and {end_date_string}:')
for day in days_list:
    print(day,find_day(day))
