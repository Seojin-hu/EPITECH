
'''
#task1.1
list = ["a", "b", "s", "g", "w"]
print(list[0])
'''

'''
#task1.2
list = ["a", "b", "c", "d", "e"]
print(list[-1])
'''


'''
#task1.3
list = ["a", "b", "c", "d", "e"]
list.append("42")
list.append("forty-two")
print(list)
'''


'''
#task1.4
list = ["a", "b", "c", "d", "e"]
for element in list:
    print(element)
'''


'''
#task1.5
list = ["a", "b", "c", "d", "e"]
list.pop()
print(list)
'''


'''
#task1.6
list = ["a", "b", "c", "d", "e"]
list[0] = "z"
print(list)
'''


'''
#task1.7
list = ["a", "b", "c", "d", "e"]
print(list[1:4])
'''


'''
#task1.8
list = ["a", "b", "c", "d", "e"]
reversed_list = list[::-1]
print(reversed_list)
'''


'''
#task1.9
list = ["a", "b", "c", "d", "e"]
list.extend(range(11, 21))
print(list)
'''


'''
#task1.10
my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
print(my_first_list)
'''


'''
#task1.11
list = ["1", "2", "3", "4", "5"]

result = 1
for n in list:
    result *= int(n)

print(result)
'''


'''
#task1.12
print([x + 10 for x in [3, 2, 6, 7, 1, 4]])
'''


'''
#task1.13
numbers = [8, 3, 15, 1, 10]
print(min(numbers))
print(max(numbers))
'''


'''
#task1.14
numbers = [8, 3, 15, 1, 10]
numbers.sort(reverse=True)
print(numbers)
'''


'''
#task1.15
print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
'''


'''
#task1.16
print(list(set([1, 1, 1, 1, 2, 2, 2, 2, 2])))
print(list(set([42, '42', 42.0, 21 + 21, 42 * 10 / 10])))
'''



'''
#CHALLENGE
import random

numbers = [random.randint(0, 100) for _ in range(1000000)]
numbers.sort()
print(numbers)
'''


'''
#task2.1
pokemons = {
    "Pikachu": "Electric",
    "Bulbasaur": "Grass",
    "Charmander": "Fire"
}

print(pokemons)
'''



'''
#task2.2
pokemons = {
    "Pikachu": "Electric",
    "Bulbasaur": "Grass",
    "Charmander": "Fire"
}
pokemons["Blaziken"] = "Fire"
print(pokemons)
'''



'''
#task2.3
pokemons = {
    "Pikachu": "Electric",
    "Bulbasaur": "Grass",
    "Charmander": "Fire"
}
pokemons["Pikachu"] = ["Pichu", "Raichu"]
print(pokemons)
'''


'''
#task2.4
types = {
    "Electric": [],
    "Grass": [],
    "Fire": []
}
print(types)
'''



'''
#task2.6
pokemons = {
    "Pikachu": "Electric",
    "Bulbasaur": "Grass",
    "Charmander": "Fire"
}
for key in pokemons:
    print(key)
'''



'''
#task2.7
pokemons = {
    "Pikachu": "Electric",
    "Bulbasaur": "Grass",
    "Charmander": "Fire"
}
print(pokemons["Pikachu"])
'''



'''
#task2.8
superheroes = {
    "Batman": {
        "id": 1,
        "aliases": ["Bruce Wayne", "Dark knight"],
        "location": {
            "number": 1007,
            "street": "Mountain Drive",
            "city": "Gotham"
        }
    },
    "Superman": {
        "id": 2,
        "aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
        "location": {
            "number": 344,
            "street": "Clinton Street",
            "apartment": "3D",
            "city": "Metropolis"
        }
    }
}

print(superheroes["Superman"]["location"]["city"])
'''


'''
#task2.9
superheroes = {
    "Batman": {
        "id": 1,
        "aliases": ["Bruce Wayne", "Dark knight"],
        "location": {
            "number": 1007,
            "street": "Mountain Drive",
            "city": "Gotham"
        }
    },
    "Superman": {
        "id": 2,
        "aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
        "location": {
            "number": 344,
            "street": "Clinton Street",
            "apartment": "3D",
            "city": "Metropolis"
        }
    }
}


superheroes["Batman"]["aliases"].append("Caped Crusader")

superheroes["Wolverine"] = {
    "id": 3,
    "aliases": [],
    "location": {}
}

print(superheroes["Batman"]["aliases"])
print(superheroes["Wolverine"])
'''



'''
#task2.10
for name, info in superheroes.items():
    print(name + ":")
    aliases = info.get("aliases", [])
    if aliases:
        for alias in aliases:
            print(alias)
    else:
        print("No aliases found.")
    print()

#task2.11
numbers = {
    "dalmatians": 101,
    "pi": 3.14,
    "beast": 666,
    "life": 42,
    "googol": 10**100,
    "jordan": 23,
    "life, the universe and everything": 42,
    "emergency": 911,
    "euler": 2.71828
}

print(max(numbers, key=numbers.get))
'''


#CHALLENGE
def scrabble_score(word):
    score = 0
    for letter in word.upper():
        if letter in "AEIOULNSTR":
            score += 1
        elif letter in "DG":
            score += 2
        elif letter in "BCMP":
            score += 3
        elif letter in "FHVWY":
            score += 4
        elif letter == "K":
            score += 5
        elif letter in "JX":
            score += 8
        elif letter in "QZ":
            score += 10
    return score

word = input("Enter a word: ")
print(scrabble_score(word))