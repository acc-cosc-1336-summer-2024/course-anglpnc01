def get_options_ratio(option, total):
    ratio = option / total
    return ratio
    
def get_faculty_rating(ratio):
    
    
    result = ''


    if (ratio >= .9 and ratio <= 1):
        result = 'Excellent'
    elif (ratio >= .8 and ratio <= .9):
        result = 'Very Good'
    elif (ratio >= .7 and ratio <= .8):
        result = 'Good'    
    elif (ratio >= .6 and ratio <= .7):
        result = 'Needs Improvement'
    elif (ratio >= 0 and ratio <= .6):
        result = 'Unacceptable'

    else:
        result = 'Invalid Option'

    return result
        