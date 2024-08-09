# Data Analyzes Lottery

## Intro

The goal of this project is to analyze and get some insights from lottery's previous results called 'Lotofácil' a brazilian lottery game.

## Features 

 - ```analyzing.py``` - This script executes a series of analyzes on previous results present in pre_results.json file. And simulates 100,000 games to find the occurrence of each score required to win prizes.
 - ```open_save.py``` - This function opens and loads pre_results.json file, and saves new retrieved results. 
 - ```pre_results.json``` - The file stores all the previous result from the lottery.
 - ```previous_results.py``` - This script retrieves 20 previous results through web scraping and saves new result on pre_results.json file.
 - ```web_scraper.py``` - This function do the web scraping.
 
## Prerequisites

- Python
- Required Python packages: `requests`, `bs4`, `re`, `json`, `random`

## Usage Instructions

To use this repository, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/RobisonTorres/Data_Analysis_Lottery.git

2. Install required Python packages.

3. Navigate to the directory.

4. Choose a function and execute.

## Example

After running the analyzing.py on all previous results you should get this outcome:

```
Each lottery's result is unique in this dataset.

In 460 previous results 48.3% of the numbers are even and 51.7% are odd.
Numbers most drawn - [10, 11, 12, 20, 25]. Numbers least drawn - [6, 16, 17, 19, 23].
Range of numbers most drawn - ['11-15']. Range of numbers least drawn - ['16-20'].
Game with more numbers in sequence: 3-5-12-13-14-15-16-17-18-19-20-21-22-23-25
Game with less numbers in sequence: 1-2-4-7-8-10-12-13-15-17-19-20-22-24-25

Out of 459 games analyzed, 64.05% of them repeated at least 9 numbers from the previous result.      

Simulating Games.

By simulating 100,000 games, the occurrence of each score required to win prizes is:
{'11 pts': 8647, '12 pts': 1599, '13 pts': 137, '14 pts': 4, '15 pts': 0}. It indicates
that the player has approximately 8% of chance to win at least the lowest prize per game.
```

- Note:

The current result of this analyze will change if more data are put in pre_results.json.

Lottery outcomes are typically designed to be random, and past results may not predict future outcomes. Therefore, users should approach such analyze with caution and consider them as informational rather than predictive.