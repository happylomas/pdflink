print('Using reading through a file and analizing it ')

print('')


with open("life-expectancy.csv") as life_expectant_file:
    next(life_expectant_file)

    years = []
    country = []
    codes = []
    life_expectances = []
    sum = 0
    data = []

    for line in life_expectant_file:
        remove_space = line.strip()
        parts = remove_space.split(",")

        #append to the parts of the file
        country_data = [parts[0], parts[1], parts[2], parts[3]]
        data.append(country_data)
        country.append(parts[0])
        codes.append(parts[1])
        years.append(int(parts[2]))
        life_expectances.append(parts[3])
    #for x in life_expectances:
        #if x == max(life_expectances):
    indy = life_expectances.index(max(life_expectances))
    print(f'The highest life expentancies is: {max(life_expectances)} in the country {country[indy]} in {years[indy]}')
    indy = life_expectances.index(min(life_expectances))
    print(f'The lowest life expentancies is: {min(life_expectances)} in the country {country[indy]} in {years[indy]}')

    year_of_interest = int(input('Enter the year of interest: '))


    max_country = ""
    max_life = 0
    min_country = ""
    min_life = 200
    count = 0
    for country in data:
        if int(country[2]) == year_of_interest:
            if float(country[3]) > max_life:
                max_life = float(country[3])
                max_country = country[0]
            if float(country[3]) < min_life:
                min_life = float(country[3])
                min_country = country[0]
    # for i in range(len(life_expectances)):
            sum += float(country[3])
            count += 1
            average = sum / count
            # average = sum / len(life_expectances)
            average = float(average)
# average = sum(life_expectances) / len(life_expectances)
print(f'The average life expectancy across all countries was {average:.2f}')
print(f'The highest life expentancies is: {max_life} in the country {max_country} in {year_of_interest}')
print(f'The lowest life expentancies is: {min_life} in the country {min_country} in {year_of_interest}')


    # search_year = []
    # search_country = []
    # search_codes = []
    # search_life_expectances = []

    # if year_of_interest in years:
    #     for x in years:
    #         if year_of_interest == x:
    #             search_indy = years.index(year_of_interest)
    #             search_year.append(years[search_indy])
    #             search_country.append(country[search_indy])
    #             search_codes.append(codes[search_indy])
    #             search_life_expectances.append(life_expectances[search_indy])
    
    # search_indy = search_life_expectances.index(max(search_life_expectances))
    # print(f'The highest life expentancies is: {max(search_life_expectances)} in the country {search_country[search_indy]} in {search_year[search_indy]}')
    # indy = search_life_expectances.index(min(search_life_expectances))
    # print(f'The lowest life expentancies is: {min(search_life_expectances)} in the country {search_country[search_indy]} in {search_year[search_indy]}')
    # print(search_indy)
    # print(search_country)
        
