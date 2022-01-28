from itertools import combinations
from input import input, test
from utils import timeit

def sort_input(input):
    return input.sort(key=lambda a: a['cost'])

def sort_sub_five_hundred_portfolios(sub_five_hundred_portfolios):
    return sub_five_hundred_portfolios.sort(key= lambda a: a['total_roi'], reverse=True)


def get_all_combinations(input):
    all_combinations = []
    for i in range(1, len(input) +1):     
        combination = list(combinations(input, i))
        all_combinations.append(combination)
    return all_combinations

def get_sub_five_hundred_portfolios(combinations):
    sub_five_hundred_combinations = []
    for i in range(len(combinations)):
        for j in range(len(combinations[i])):
            sum = 0
            roi = 0
            for k in range(len(combinations[i][j])):
                    sum += combinations[i][j][k]['cost']
                    roi += combinations[i][j][k]['cost'] * combinations[i][j][k]['roi']
            if sum <= 500:
                sub_five_hundred_combinations.append({'total_roi': roi, 'total_investment': sum, 'combination': combinations[i][j]})
    return sub_five_hundred_combinations
                
@timeit
def get_best_five_portfolios():
    all_combinations = get_all_combinations(input)
    sub_five_hundred_portfolios = get_sub_five_hundred_portfolios(all_combinations)
    sort_sub_five_hundred_portfolios(sub_five_hundred_portfolios)
    for i in range(5):
        print(sub_five_hundred_portfolios[i])

get_best_five_portfolios()