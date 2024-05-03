import web_scraper
print('Gathering Previous Results.')
print()

# Not working anymore because they've changed the site's structure.
def gathering_data():

    # This function retrieves twenty previous results from the lottery, 
    # through web scraping or local file, and saves new results for future use.
    round = int(input('Type in the lottery round: '))
    for num in range((round - 19), round + 1):
        if num <=0: continue
            
        else:
            lottery_result = web_scraper.extract_search(num)                       
            if type(lottery_result) == str:
                print(f'{lottery_result}')
                
            else: 
                numbers_result = lottery_result[1]
                print(f'Round: {num} - Result: {numbers_result}') 

    return '\nNews results have been saved.'

print(gathering_data())
