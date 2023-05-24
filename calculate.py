import datetime

def calculate_age(birth_year, birth_month, birth_day):
    current_date = datetime.date.today()
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    age = (current_date - birth_date).days // 365
    return age

def calculate_remaining_time(age, category):
    current_date = datetime.date.today()
    cutoff_date = datetime.date(2023, 8, 1)

    general_age_limit = 32
    obc_age_limit = 35
    sc_st_age_limit = 37

    if category.lower() == "general":
        age_limit = general_age_limit
    elif category.lower() == "obc":
        age_limit = obc_age_limit
    elif category.lower() == "sc" or category.lower() == "st":
        age_limit = sc_st_age_limit
    else:
        return None, None, None

    if age <= age_limit:
        remaining_years = age_limit - age
        remaining_months = (cutoff_date.year - current_date.year) * 12 + cutoff_date.month - current_date.month
        remaining_days = (cutoff_date - current_date).days % 30

        if remaining_days >= 30:
            remaining_months += 1
            remaining_days = 0

        if remaining_months >= 12:
            remaining_years += remaining_months // 12
            remaining_months = remaining_months % 12

        return remaining_years, remaining_months, remaining_days
    else:
        return None, None, None
