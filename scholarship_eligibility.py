import argparse

def condition_a(age):
    # A: Student Age from 18 - 24
    if 18 <= age <= 24:
        print('Passed condition A')
        return 1
    else:
        print('Failed condition A')
        return 0

def condition_b(time_in_cali):
    # B: Student lived in California for last 2 years. If fails here, check if D is satisfied.
    if time_in_cali > 2:
        print('Passed condition B')
        return 1
    else:
        print('Failed condition B')
        return 0

def condition_c(relevant_work):
    # C: Has worked part time for at least 6 months in relevant field of study.
    if relevant_work >= 6:
        print('Passed condition C')
        return 1
    else:
        print('Failed condition C')
        return 0


def condition_d(parent_cali_tax):
    # D: Students Parents have paid California state tax for at least 1 year in their lifetime.
    if parent_cali_tax:
        print('Passed condition D')
        return 1
    else:
        print('Failed condition D')
        return 0


def condition_e(volunteer_work):
    # E: Has volunteered for a cause and has a valid proof of it.
    if volunteer_work:
        print('Passed condition E')
        print(volunteer_work)
        return 1
    else:
        print('Failed condition E')
        return 0


def condition_f(household_income):
    # F: If household income less then 5000$ per year then no need to satisfy criteria C. Will be redirect to "Dean for consideration".
    if household_income <= 5000:
        print('Passed condition F - "Dean for consideration"')
        return "Dean for consideration"
    else:
        print('Failed condition F')
        return 0


def check_eligibility(age, time_in_cali, relevant_work, parent_cali_tax, volunteer_work, household_income):
    # inputs: Age, Time_in_Cali, Relevant_Work, Parent_Cali_Tax, Volunteer_work, Household_Income
    # returns: 1, 0, or "Dean for consideration"

    # Calulate result_one
    result_one = condition_a(age)

    # Calculate result_two
    b = condition_b(time_in_cali)
    if b:
        # result_two is a 1!
        result_two = b
    else:
        # condition_d can substitute for condition_b with parents tax history
        result_two = condition_d(parent_cali_tax)

    # Calculate result_three.
    c = condition_c(relevant_work)
    if c:
        # result_three is a 1!
        result_three = c
    else:
        # condition_e can substitute for condition_c with volunteer work
        result_three = condition_e(volunteer_work)
        if not result_three:
            # condition_f can turn failed condition_c into 'Dean for consideration'
            result_three = condition_f(household_income)


    # Calculate eligibility result
    if 0 in [result_one, result_two, result_three]:
        # Return 0 if any result failed
        return 0
    elif 'Dean for consideration' in [result_one, result_two, result_three]:
        # Return 'Dean for consideration' if that is in results
        return 'Dean for consideration'
    else:
        # Return 1 if all results passed
        return 1


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
