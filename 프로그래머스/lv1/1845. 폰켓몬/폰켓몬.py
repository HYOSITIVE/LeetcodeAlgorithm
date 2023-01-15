import collections

def solution(nums):
    counter = len(nums) / 2
    pokemons = collections.Counter(nums)
    types = list(pokemons.keys())
    mytypes = []
    
    for type in types:
        if type not in mytypes and counter > 0:
            mytypes.append(type)
            counter -= 1
    
    answer = len(mytypes)
    return answer