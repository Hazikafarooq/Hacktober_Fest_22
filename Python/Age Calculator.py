# Enter your code here.
dob_day = int(input())
dob_month = int(input())
dob_year = int(input())
current_day = int(input())
current_month = int(input())
current_year = int(input())

def age_from_dob(dob_day, dob_month, dob_year, current_day, current_month, current_year):
    final_year = current_year - dob_year
    
    if (current_month < dob_month) or ((current_month == dob_month and current_day < dob_day)):
        final_year -= 1
    
    
    return final_year
        
print(age_from_dob(dob_day, dob_month, dob_year, current_day, current_month, current_year))