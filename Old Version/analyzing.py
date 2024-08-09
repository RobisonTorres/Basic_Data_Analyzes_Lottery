import open_save
import random

def sample_data():

    # This function determines the sample's size.
    total_rounds = len(open_save.open_file().values())
    rounds = input(f'Please choose a sample between 1 and {total_rounds} '\
                   f'or press enter to check all of them: ')
    return total_rounds if rounds == '' else int(rounds)

def organize_data(sample):
     
    # This function organizes the data.
    lottery_results = open_save.open_file().values()
    results = ''.join(lottery_results).replace('-', '') 
    numbers = [int(results[x: x+2]) for x in range(0, len(results), 2)][-sample * 15:]
    return numbers

def check_duplicate(sample):

    # This function checks the data for repeated results.
    lottery_results = open_save.open_file()
    values = list(lottery_results.values())[-sample:]
    count = [v for v in values if values.count(v) >= 2]
    repeat_keys = [k for k in lottery_results.keys() if lottery_results[k] in count]

    if count:
        return(f'Please check the data, these rounds {"-".join(repeat_keys)} '\
               f'have duplicated results.\n')
    return 'Each lottery\'s result is unique in this dataset.\n'

def even_odd(data):

    # This function returns the percentage of even and odd numbers.
    count_even = len([n for n in data if n % 2 == 0])
    even_nums = float(f'{(count_even/ len(data)*100):.2f}')
    return f'In {int(len(data)/ 15)} previous results '\
           f'{even_nums}% of the numbers are even and {100 - even_nums}% are odd.'

def frequency(data):
    
    # This function gets the frequency of each number and shows 
    # the five numbers most and least drawn.    
    fre_nums = {}
    for num in range(1, 26):
        fre_nums[num] = data.count(num)
    
    # Numbers most an least drawn.
    fre_num_sorted = sorted(fre_nums.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(fre_num_sorted).keys())    
    return f'Numbers most drawn - {sorted(numbers[0:5])}. '\
           f'Numbers least drawn - {sorted(numbers[20:])}.'     

def frequency_range(data):
    
    # This function groups the numbers in 5 different
    # ranges and shows the most and least drawn.
    fre_ranges = {}
    for x in range(1, 26, 5):
        count_numbers = str(len([n for n in data if n in range(x, x + 5)]))
        fre_ranges[f'{x}-{x + 4}'] = count_numbers
    
    # Ranges most an least drawn.
    fre_ranges_sorted = sorted(fre_ranges.items(),key=lambda x:int(x[1]))[::-1]
    ranges = list(dict(fre_ranges_sorted).keys())
    return f'Range of numbers most drawn - {[ranges[0]]}. '\
           f'Range of numbers least drawn - {[ranges[-1]]}.'

def get_sequence(data):

    # This function returns the games with more and less numbers in sequence.
    g_results = [sorted(data[x:x+15]) for x in range(0, len(data), 15)]
    sequence = []
    for x in range(0, len(g_results)):
        seq = [0]
        [seq.append(seq[-1]+1) if g_results[x][y] + 1 == g_results[x][y+1]
                               else seq.append(0) for y in range(0, 14)]
        sequence.append(max(seq))
    
    more_seq = g_results[sequence.index(max(sequence))]
    less_seq = g_results[sequence.index(min(sequence))]
    return f'Game with more numbers in sequence: {"-".join(map(str , more_seq))}'\
           f'\nGame with less numbers in sequence: {"-".join(map(str, less_seq))}\n'

def repetition(data):

    # This function calculates the frequency of repeated numbers 
    # between current result and previous one, except for the first result.
    grouped_results = [data[x:x+15] for x in range(0, len(data), 15)]
    if len(grouped_results) <= 2:
        return 'The sample must be more than 2 to find games that repeat numbers from previous results.\n'
    else:
        rep_numbers = [(15 - len(set(grouped_results[x]) - set(grouped_results[x-1])))
                        for x in range(0, len(grouped_results)) if x != 0]
    
        # Frequency of repeated numbers.
        fre_result = {}
        for num in range(6, 16):
            fre_result[num] = rep_numbers.count(num)

        # Games that repeated at least 9 numbers from previous result.
        repeated = sum(list(fre_result.values())[3:])   
        return f'Out of {len(grouped_results) - 1} games analyzed, '\
               f'{((repeated / (len(grouped_results) - 1)) * 100):.2f}% '\
            f'of them repeated at least 9 numbers from the previous result.\n'             

def simulate_games():

    # This function simulates 100,000 games and calculate scores. 
    # Each game is a selection of 15 numbers between 1 and 25.
    random_games = []
    for x in range(0, 100_000):  
        random_games.append(random.sample(range(1, 26), 15))
  
    score = []
    random_result = random.sample(range(1, 26), 15)
    for num in range(0, len(random_games)):
            score.append(15 - len(set(random_result) - set(random_games[num])))

    # Frequency of winning prizes.    
    score_prizes = {}
    for num in range(11, 16):
        score_prizes[str(num) + ' pts'] = score.count(num)
    
    chance_winning = int((list(score_prizes.values())[0] / 100_000) * 100)
    return (f"By simulating 100,000 games, "
        f"the occurrence of each score required to win prizes is:\n"
        f"{score_prizes}. It indicates\nthat the player has approximately "
        f"{chance_winning}% of chance to win at least the lowest prize per game.\n")

def main():

    print("Analyzing Previous Results.\n")
    sample = sample_data()
    data = organize_data(sample)
    print(check_duplicate(sample))
    print(even_odd(data))
    print(frequency(data))
    print(frequency_range(data))
    print(get_sequence(data))
    print(repetition(data))
    print('Simulating Games.\n')
    print(simulate_games())

main()