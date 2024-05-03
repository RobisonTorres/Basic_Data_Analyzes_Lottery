import requests, bs4, re
import open_save

# Not working anymore because they've changed the site's structure.
def web_search(round):

    # This function accesses the lottery's page and takes the html.
    url = f'https://www.intersena.com.br/lotofacil/resultados/{round}'  # Site's changed.
    source = requests.get(url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    return soup

def extract_search(round):

    # This function extracts only the lottery result from 
    # the web_search, and gives a proper format to the result.
    previous_results = open_save.open_file()
        
    if str(round) in previous_results.keys():
        return [round, previous_results[str(round)]]

    else:    
        target = web_search(round)
        round_found = target.find('h1', class_='col-md-6 col-sm-6 col-xs-12')  
        lottery_numbers = target.find('div', class_='resultado-individual-sorteio')  

        # Only numbers.
        round_found = re.sub('[^0-9]', '', round_found.text)
        lottery_numbers = re.sub('[^0-9]', '', lottery_numbers.text)

        if str(round) != round_found: 
            return f'Round: {round} - Result not found.'

        else:
            lottery_result = '-'.join([lottery_numbers[x:x+2] for x in range(0, len(lottery_numbers), 2)])
        
            # Save new results.
            previous_results[round] = lottery_result
            previous_results = dict(sorted(previous_results.items(),key=lambda x:int(x[0])))
            open_save.save_file(previous_results)   
            return [round, lottery_result]
