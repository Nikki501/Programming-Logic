# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = 0
month = 0
day = 0

# Get the year, then the month, then the day
# housekeeping()
year = input("Enter The Year (Example 2024): ")
month = input("Enter The Month (Example 09): ")
day = input("Enter The Day (Example 26): ")

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    # Output statement
    print("month/day/year is a valid date.")
else:
    # Output statement
    print("month/day/year is an invalid date. ")
