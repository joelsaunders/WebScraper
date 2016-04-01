# Utils v2
# Some utility functions for checking and manipulating input string


def create_input_list(prompt):
    """
    Creates input list then lowers it and also checks it is
    only letters

    >>> create_input_list("Japan, South Africa, pakistan")
    ["japan", "south africa", "pakistan"]
    
    """
    list_countries = input(prompt).split(", ")
    list_countries = [x.lower() for x in list_countries] 
    return list_countries

def check_country(input_list):
    """
    Checks that user inputted country is in list of accepted
    country names.
    If not, they must retry entering whole list.

    >>> check_country(["japan", "singapore", "india"])
    ['japan', 'singapore', 'india']

    >>> check_country(["space", "singapore", "india"])
    Please make sure you entered the correct country names
    Try again, each item separated by ', ':
    """

    country_list = open("countries.txt").read().splitlines()
    country_list = [x.lower() for x in country_list]
    while True:
        if not all(x in country_list for x in input_list):
            print("Please make sure you entered the correct country names")

            input_list = create_input_list("Try again, each item "
                                           "separated by ', ': ")
            continue
        else:
            break

    return input_list

        
if __name__ == "__main__":   
    in_list = create_input_list("Enter string of countries separated "
                                "by a comma then space: ")
    in_list = check_country(in_list)
    
        

    

        
