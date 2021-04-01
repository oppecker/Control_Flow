import argparse

def condition_a(age):
    # A: Student Age from 18 - 24
    if 18 <= age <= 24:
        return 1
    else:
        return 0

def condition_b(time_in_cali):
    # B: Student lived in California for last 2 years. If fails here, check if D is satisfied.
    if time_in_cali > 2:
        return 1
    else:
        return 0

def condition_c(relevant_work):
    # C: Has worked part time for at least 6 months in relevant field of study.
    if relevant_work >= 6:
        return 1
    else:
        return 0


def condition_d(parent_cali_tax):
    # D: Students Parents have paid California state tax for at least 1 year in their lifetime.
    if parent_cali_tax:
        return 1
    else:
        return 0


def condition_e(volunteer_work):
    # E: Has volunteered for a cause and has a valid proof of it.
    if volunteer_work:
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

    # Calulate condition a:
    in_age_range = condition_a(age)
    # If it is 0, not eligibile so return 0
    if in_age_range == 0:
        return 0

    # Calculate condition b
    lived_in_cali = condition_b(time_in_cali)
    if lived_in_cali == 0:
        # condition_d can substitute for condition_b with parents tax history
        parents_paid_tax = condition_d(parent_cali_tax)
        # If it is 0, not eligibile so return 0
        if parents_paid_tax == 0:
            return 0

    # Calculate condition c
    has_work_experience = condition_c(relevant_work)
    # if it is 1, return 1 for eligible!
    if has_work_experience == 1:
        return 1
    # condition_e can substitute for condition_c with volunteer work
    has_volunteer_work = condition_e(volunteer_work)
    # if it is 1, return 1 for eligible!
    if has_volunteer_work == 1:
        return 1
    # Finally return either 0 or 'Dean for consideration'
    return condition_f(household_income)


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-a', '--age', type=int, help='In Years')
    my_parser.add_argument('-b', '--time_in_cali', type=int, help='In Years')
    my_parser.add_argument('-c', '--relevant_work', type=int, help='In Months')
    my_parser.add_argument('-d', '--parent_cali_tax', type=int, help='In Years')
    my_parser.add_argument('-e', '--volunteer_work', type=int, help='1 for Yes, 0 for No')
    my_parser.add_argument('-f', '--household_income', type=int, help='In Dollars')
    args = my_parser.parse_args()
    print(check_eligibility(args.age, args.time_in_cali, args.relevant_work, args.parent_cali_tax, args.volunteer_work, args.household_income))
