import decisions

#prompt the user for options (float)
options_var = input('Enter option: ')

totals_var = input('Enter your total: ')

options = float(options_var)
totals = int(totals_var)

ratio = decisions.get_options_ratio(options, totals)

rating = decisions.get_faculty_rating(ratio)

print(rating)
