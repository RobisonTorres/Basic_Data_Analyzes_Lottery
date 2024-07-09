# Basic Data Analysis: Lotofácil Lottery

## Intro

The goal of this project is to analyze and gain some insights from the results of 'Lotofácil,' a Brazilian lottery game.

In this game, players choose 15 numbers between 1 and 25. They win the lowest prize if they score at least 11 points and win the highest prize if they score 15 points.

## Be advised:

Lottery outcomes are typically designed to be random, and past results may not predict future outcomes. Therefore, such analysis serves as informational rather than predictive. Also, the current result of this analysis will change if more valid data are added or removed from the file results.json.

## Features 

 ```analyzing.py```
- This script executes a series of analyses on past results present in results.json.
- By creating one random result, it simulates 100,000 games to find the occurrence of each score required to win prizes. For example, it shows that {'11 pts': 8647} means 8647 out of 100,000 tickets scored 11 points.
 
## Prerequisites

- Python
- Required Python packages: `json`, `random`

## Usage Instructions

To use this repository, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/RobisonTorres/Data_Analysis_Lottery.git

2. Install required Python packages.

3. Navigate to the directory.

4. And execute analyzing.py.

## Examples

After running the analyzing.py on 50 previous results you should get this outcome:

```
Each lottery's result is unique in this dataset.

In 50 previous results 47.87% of the numbers are even and 52.13% are odd.
Numbers most drawn - [1, 7, 9, 12, 22]. Numbers least drawn - [3, 4, 11, 13, 24].
Range of numbers most drawn - ['6-10']. Range of numbers least drawn - ['11-15'].
Game with more numbers in sequence: 3-4-5-6-7-8-9-10-11-15-16-17-19-22-23
Game with less numbers in sequence: 1-2-4-7-8-10-12-13-15-17-19-20-22-24-25

Out of 49 games, in 59.18% of cases a new result had at least 9 numbers the same as the prior result.
```

After running the analyzing.py on all previous results you should get this outcome:

```
Each lottery's result is unique in this dataset.

In 461 previous results 48.32% of the numbers are even and 51.68% are odd.
Numbers most drawn - [10, 11, 12, 20, 25]. Numbers least drawn - [6, 16, 17, 19, 23].
Range of numbers most drawn - ['11-15']. Range of numbers least drawn - ['16-20'].
Game with more numbers in sequence: 3-5-12-13-14-15-16-17-18-19-20-21-22-23-25
Game with less numbers in sequence: 1-2-4-7-8-10-12-13-15-17-19-20-22-24-25

Out of 460 games, in 64.13% of cases a new result had at least 9 numbers the same as the prior result.        
```

## Simulating Games.

```
By simulating 100,000 games, the occurrence of each score required to win prizes is:
{'11 pts': 8789, '12 pts': 1605, '13 pts': 147, '14 pts': 6, '15 pts': 0}.
```
