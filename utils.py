# Country Checker v1
# Check countries code that checks if entries in a list are countries.


def create_input_list(prompt):
    """ Create input list then lower it and also check it is
    only letters
    """
    
    list_countries = input(prompt).split(", ")
    list_countries = [x.lower() for x in list_countries]
        
    return list_countries

def check_country(input_list):
    print(input_list)
    country_list = open("countries.txt").read().splitlines()
    country_list = [x.lower() for x in country_list]
    while True:
        if not all(x in country_list for x in input_list):
            print("Please make sure you entered the correct country names")

            input_list = create_input_list("Try again, each item \
separated by ', '")
            continue
        else:
            break

    return input_list

        
if __name__ == "__main__":
    in_list = create_input_list("Enter string of countries separated \
by a comma then space: ")
    in_list = check_country(in_list)
        

    

        
