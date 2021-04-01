def condition_a(age):
    # A: Student Age from 18 - 24
    if 18 <= age <= 24:
        continue 1
    else:
        return 0

def condition_b(time_in_cali, parent_cali_tax):
    # B: Student lived in California for last 2 years. If fails here, check if D is satisfied.
    if time_in_cali > 2:
        return 1
    else:
        return condition_d(parent_cali_tax)

def condition_c(relevant_work, volunteer_work, household_income):
    # C: Has worked part time for at least 6 months in relevant field of study. If fails here, check if E is satisfied.
    f = condition_f(household_income)
    if f:
        return f

    if relevant_work >= 6:
        return 1
    else:
        return condition_e(volunteer_work)

def condition_d(parent_cali_tax):
    # D: Students Parents have paid California state tax for at least 1 year in their lifetime.
    if parent_cali_tax is True:
        return 1
    else:
        return 0


def condition_e(volunteer_work):
    # E: Has volunteered for a cause and has a valid proof of it.
    if volunteer_work is True:
        return 1
    else:
        return 0


def condition_f(household_income):
    # F: If household income less then 5000$ per year then no need to satisfy criteria C. Will be redirect to "Dean for consideration".
    if household_income <= 5000:
        return "Dean for consideration"
    else:
        return 0


def check_eligibility(age, time_in_cali, relevant_work, parent_cali_tax, volunteer_work, household_income):
    # inputs: Age, Time_in_Cali, Relevant_Work, Parent_Cali_Tax, Volunteer_work, Household_Income
    # returns: 1, 0, or "Dean for consideration"
    a = condition_a(age)
    b = condition_b(time_in_cali, parent_cali_tax)
    c = condition_c(relevant_work, volunteer_work, household_income)
    if 0 in [a, b, c]:
        return 0
    elif 'Dean for consideration' in [a, b, c]:
        return 'Dean for consideration'
    else:
        return 1


if __name__ "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('age')
    my_parser.add_argument('time_in_cali')
    my_parser.add_argument('relevant_work')
    my_parser.add_argument('parent_cali_tax')
    my_parser.add_argument('volunteer_work')
    my_parser.add_argument('household_income')
    args = my_parser.parse_args(age, time_in_cali, relevant_work, parent_cali_tax, volunteer_work, household_income))
    print(check_eligibility()
