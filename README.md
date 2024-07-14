# Basic Data Analysis: Lotofácil Lottery

## Intro

The goal of this project is to analyze and gain some insights from the results of 'Lotofácil,' a Brazilian lottery game. In this game, players choose 15 numbers between 1 and 25. They win the lowest prize if they score at least 11 points and win the highest prize if they score 15 points.

## Analysis

Analysis of previous results present in results.json.

    Total Results Analyzed: 461
    
    Each lottery's result is unique in this dataset.

    Distribution of Numbers:
    
        Even Numbers: 48.32%
        Odd Numbers: 51.68%

    Most Frequently Drawn Numbers: 10, 11, 12, 20, 25

    Least Frequently Drawn Numbers: 6, 16, 17, 19, 23

    Range of Most Frequently Drawn Numbers: 11-15

    Range of Least Frequently Drawn Numbers: 16-20

    Game with Most Numbers in Sequence:
        Numbers: 3, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25

    Game with Least Numbers in Sequence:
        Numbers: 1, 2, 4, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22, 24, 25

    Similarity to Previous Results:
        In 64.13% of the 460 games, at least 9 numbers were the same as in the prior result.

Simulation of 326,876 Games:

    Occurrences of Winning Scores:
        11 points: 28,804 times
        12 points: 5,558 times
        13 points: 467 times
        14 points: 11 times
        15 points: 0 times

Probability of winning:

    Chance of winning - one out of: 
        11 points: 11 
        12 points: 59 
        13 points: 691 
        14 points: 21,791 
        15 points: 3,268,760 


## Be advised

Lottery outcomes are typically designed to be random, and past results may not predict future outcomes. Therefore, such analysis serves as informational rather than predictive. Also, the current result of this analysis will change if more valid data are added or removed from the file results.json.

## Prerequisites

- Python

## Usage Instructions

To use this repository, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/RobisonTorres/Data_Analysis_Lottery.git

2. Navigate to the directory.

3. And execute analyzing.py.