import inspect
from functools import partial
from random import choice

import numpy as np
from python_scripts.n_poly_solution import n_poly
from python_scripts.fun_solver_solution import fun_solver
from time import time
from numba import jit, float64
from numba.core.errors import NumbaWarning
import warnings

# Create a random family tree of dogs using dictionaries.
# Create a dictionary of dog names and their Parents.
# We are going to go with an hourglass shape for the family tree.
# MM-GP-1   MM-GP-2     MF-GP-1    MF-GP-2    FM-GP-1   FM-GP-2    FF-GP-1    FF-GP-2
#   |         |             |         |          |         |          |         |
#   -----M-----             -----F-----          -----M-----          -----F-----
#        |                       |                   |                     |
#         -----------D-----------                    -----------B-----------
#                    |                                          |
#                    --------------------------------------------
#                    |            |                |            |
#                   P-1          P-2              P-3          P-4
# This is the structure we want to generate random names and attributes for.

# A set of  dog names to choose from.
dog_names = {
    "m": {
        "Buddy",
        "Max",
        "Charlie",
        "Jack",
        "Cooper",
        "Rocky",
        "Toby",
        "Tucker",
        "Jake",
        "Bear",
        "Duke",
        "Teddy",
        "Oliver",
        "Riley",
        "Bailey",
        "Bentley",
        "Milo",
        "Buster",
        "Cody",
        "Dexter",
        "Winston",
        "Murphy",
        "Leo",
    },
    "f": {
        "Bella",
        "Lucy",
        "Luna",
        "Daisy",
        "Lola",
        "Sadie",
        "Molly",
        "Maggie",
        "Bailey",
        "Sophie",
        "Chloe",
        "Stella",
        "Lily",
        "Penny",
        "Zoey",
        "Coco",
        "Roxy",
        "Gracie",
        "Mia",
        "Nala",
        "Ruby",
        "Rosie",
        "Ellie",
    },
}
# A set of dog Breeds to choose from.
dog_Breeds = {
    "Labrador Retriever",
    "German Shepherd",
    "Golden Retriever",
    "French Bulldog",
    "Bulldog",
    "Beagle",
    "Poodle",
    "Rottweiler",
    "Yorkshire Terrier",
    "German Shorthaired Pointer",
    "Boxer",
    "Siberian Husky",
    "Dachshund",
    "Great Dane",
    "Doberman Pinscher",
    "Australian Shepherd",
    "Miniature Schnauzer",
    "Pembroke Welsh Corgi",
    "Cavalier King Charles Spaniel",
    "Shih Tzu",
    "Boston Terrier",
    "Pomeranian",
    "Havanese",
    "Shetland Sheepdog",
    "Brittany",
    "English Springer Spaniel",
    "Bernese Mountain Dog",
    "Lhasa Apso",
    "Cane Corso",
    "Collie",
    "Basset Hound",
    "Newfoundland",
    "Border Collie",
    "Bullmastiff",
    "Bichon Frise",
    "Rhodesian Ridgeback",
    "West Highland White Terrier",
    "Shiba Inu",
    "Airedale Terrier",
    "Belgian Malinois",
    "Maltese",
    "Weimaraner",
    "Cocker Spaniel",
    "Soft Coated Wheaten Terrier",
    "Dalmatian",
    "Mastiff",
    "Pug",
    "Vizsla",
    "Irish Setter",
    "Miniature American Shepherd",
    "St. Bernard",
    "Bull Terrier",
    "Chinese Shar-Pei",
    "Wirehaired Pointing Griffon",
    "Cardigan Welsh Corgi",
    "Chihuahua",
    "Great Pyrenees",
    "Schipperke",
    "Papillon",
    "Italian Greyhound",
    "Pekingese",
    "Basenji",
    "Scottish Terrier",
    "Pembroke Welsh Corgi",
    "Whippet",
    "Bloodhound",
    "Borzoi",
    "Alaskan Malamute",
    "Bull Terrier",
    "Chinese Crested",
    "Pointer",
    "Chesapeake Bay Retriever",
    "Bull Terrier",
}
# A set of dog colors to choose from.
dog_colors = {
    "Black",
    "White",
    "Brown",
    "Red",
    "Golden",
    "Yellow",
    "Cream",
    "Gray",
    "Blue",
    "Silver",
    "Fawn",
    "Brindle",
    "Spotted",
    "Merle",
    "Sable",
    "Tan",
    "Blonde",
    "Chocolate",
    "Liver",
    "Orange",
    "Buff",
    "Tricolor",
    "Bicolor",
}

# Create a set of dog Tricks to choose from.
dog_Tricks = {
    "Sit",
    "Stay",
    "Lay Down",
    "Roll Over",
    "Shake",
    "Fetch",
    "Play Dead",
    "Speak",
    "Spin",
    "High Five",
    "Beg",
    "Jump",
    "Crawl",
    "Bow",
    "Back Up",
    "Wave",
    "Take a Bow",
    "Kiss",
    "Spin",
    "Rollover",
    "Paw",
    "Touch",
}

# Create a set of Human names male and female to choose from.
names = {
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Joseph",
    "Thomas",
    "Charles",
    "Christopher",
    "Mary",
    "Patricia",
    "Jennifer",
    "Linda",
    "Elizabeth",
    "Barbara",
    "Susan",
    "Jessica",
    "Sarah",
    "Karen",
    "Nancy",
    "Alex",
    "Andy",
    "Angel",
    "Ariel",
    "Ash",
    "Aspen",
    "Avery",
    "Bailey",
    "Bobbie",
    "Brett",
    "Brook",
    "Cameron",
}


def make_random_dog(sex=None, parent_m=None, parent_f=None):
    """Creates a random dog dictionary with random attributes."""
    if sex is None:
        sex = choice(["m", "f"])
    assert sex in ["m", "f"], 'sex must be either "m" or "f"'

    # Create a new dog dictionary.
    dog = {}
    # Set the dog's name.
    dog["Name"] = choice(list(dog_names[sex]))
    # Set the owner's name.
    dog["Owner"] = choice(list(names))
    # Set the dogs age
    dog["Age"] = choice(list(range(1, 15)))
    # Set the dogs sex
    dog["Sex"] = "Dog" if sex == "m" else "Bitch"
    # Set the dog's Breed.
    if parent_f and parent_m:
        if (parent_f['Breed'] == parent_m['Breed']) and (parent_m['Breed'] != 'Cross'):
            dog['Breed'] = parent_m['Breed']
        else:
            dog['Breed'] = 'Cross'
            dog['Breed_mix'] = set()
            if parent_f['Breed'] == 'Cross':
                dog["Breed_mix"] = dog['Breed_mix'] | parent_f['Breed_mix']
            else:
                dog['Breed_mix'].add(parent_f['Breed'])
            if parent_m['Breed'] == 'Cross':
                dog['Breed_mix'] = dog["Breed_mix"] | parent_m['Breed_mix']
            else:
                dog['Breed_mix'].add(parent_m['Breed'])
    else:
        dog["Breed"] = choice(list(dog_Breeds))
    # Set the dog's Color.
    dog["Color"] = choice(list(dog_colors))
    # Set the dog's Tricks.
    dog["Tricks"] = {choice(list(dog_Tricks)) for i in range(1, 5)}
    # Set the dog's Parents.
    if parent_f and parent_m:
        dog["Parents"] = (parent_m['Name'], parent_f['Name'])
        # Add the dog as the parent's child.
        parent_m["Children"].append(dog["Name"])
        parent_f["Children"].append(dog["Name"])
    else:
        dog["Parents"] = (None, None)
    # Set the dog's Children.
    dog["Children"] = []
    # Return the dog dictionary.
    return dog


def make_family_tree_structure(generations=3, offspring=2):
    # Generations - 1 great grandParents in pairs:

    # do the decision to pairs by going from generations-1 to generations-2
    gen_dict = {}
    for gen in range(generations):
        if gen == 0:
            gen_dict[gen] = [
                [make_random_dog(sex="m"), make_random_dog(sex="f")]
                for i in range(2 ** (generations - 2))
            ]
        elif gen == generations - 1:
            gen_dict[gen] = [
                make_random_dog(
                    sex=choice(['m', 'f']),
                    parent_m=gen_dict[gen - 1][0][0],
                    parent_f=gen_dict[gen - 1][0][1]
                )
                for i in range(0, offspring)
            ]
        else:
            gen_dict[gen] = [
                [
                    make_random_dog(
                        sex="m",
                        parent_m=gen_dict[gen - 1][i - 1][0],
                        parent_f=gen_dict[gen - 1][i - 1][1],
                    ),
                    make_random_dog(
                        sex="f",
                        parent_m=gen_dict[gen - 1][i][0],
                        parent_f=gen_dict[gen - 1][i][1],
                    ),
                ]
                for i in range(1, 2 ** (generations - 1 - gen), 2)
            ]
    return gen_dict


def print_family_tree_structure(gen_dict, full=False):
    for gen in gen_dict:
        print(f"Generation {gen}")
        if gen < len(gen_dict) - 1:
            for pair in gen_dict[gen]:
                for dog in pair:
                    print_dog(dog, full)
        else:
            for dog in gen_dict[gen]:
                print_dog(dog, full)


def print_dog(dog, full=False):
    print(f"    {dog['Name']}")
    print(f"      Sex: {dog['Sex']}")
    if full:
        print(f"      Owner: {dog['Owner']}")
        print(f"      Age: {dog['Age']}")
        print(f"      Breed: {dog['Breed']}")
        if dog['Breed'] == 'Cross':
            print(f"      Breed Mix: {', '.join(dog['Breed_mix'])}")
        print(f"      Color: {dog['Color']}")
    if not any(elem is None for elem in dog['Parents']):
        print(f"      Parents: {', '.join(dog['Parents'])}")
    if dog['Children'] != []:
        print(f"      Children: {', '.join(dog['Children'])}")
    print(f"      Tricks: {', '.join(dog['Tricks'])}")


def test_family_tree_structure(family_tree_structure,
                               maternal_grandmother, maternal_grandfather,
                               fraternal_grandmother, fraternal_grandfather,
                               mother, father,
                               offspring_1, offspring_2):
    try:
        if any((family_tree_structure[0][1][1]['Name'] != maternal_grandmother['Name'],
         family_tree_structure[0][1][0]['Name'] != maternal_grandfather['Name'],
         family_tree_structure[0][0][1]['Name'] != fraternal_grandmother['Name'],
         family_tree_structure[0][0][0]['Name'] != fraternal_grandfather['Name'],
         family_tree_structure[1][0][1]['Name'] != mother['Name'],
         family_tree_structure[1][0][0]['Name'] != father['Name'],
         sorted([family_tree_structure[2][0]['Name'], family_tree_structure[2][1]['Name']]) != sorted([offspring_1['Name'], offspring_2['Name']])
         )):
            print("Family tree structure is incorrect")
            print("Failed when checking the names of the dogs")
            return
        else:
            print("Names are correct")
    except KeyError:
        print("Ensure your dict uses `Name` as the key for the dog's name")
        return

    try:
        if type(mother['Parents']) is not tuple:
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the mother")
            print("Ensure the mother's parents are stored in a tuple")
            return
        elif type(father['Parents']) is not tuple:
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the father")
            print("Ensure the father's parents are stored in a tuple")
            return
        elif type(offspring_1['Parents']) is not tuple:
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the offspring")
            print("Ensure the offspring's parents are stored in a tuple")
            return
        elif type(offspring_2['Parents']) is not tuple:
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the offspring")
            print("Ensure the offspring's parents are stored in a tuple")
            return
        elif sorted(family_tree_structure[1][0][1]['Parents']) != sorted((maternal_grandmother['Name'], maternal_grandfather['Name'])):
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the mother")
            print("Ensure the mother's parents are the maternal grandmother and maternal grandfather")
            return
        elif sorted(family_tree_structure[1][0][0]['Parents']) != sorted((fraternal_grandmother['Name'], fraternal_grandfather['Name'])):
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the mother")
            print("Ensure the mother's parents are the maternal grandmother and maternal grandfather")
            return
        elif sorted(family_tree_structure[2][0]['Parents']) != sorted(offspring_1['Parents']):
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the offspring")
            print("Ensure the offspring's parents are the mother and father")
            return
        elif sorted(family_tree_structure[2][1]['Parents']) != sorted(offspring_2['Parents']):
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the offspring")
            print("Ensure the offspring's parents are the mother and father")
            return
        else:
            print("Parents fields are correct")
    except KeyError:
        print("Ensure your dict uses `Parents` as the key for the dog's parents")
        return

    try:
        if type(fraternal_grandfather['Children']) is not list:
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the fraternal grandfather")
            print("Ensure the fraternal grandfather's children are stored in a list")
            return
        elif type(fraternal_grandmother['Children']) is not list:
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the fraternal grandmother")
            print("Ensure the fraternal grandmother's children are stored in a list")
            return
        elif type(maternal_grandfather['Children']) is not list:
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the maternal grandfather")
            print("Ensure the maternal grandfather's children are stored in a list")
            return
        elif type(maternal_grandmother['Children']) is not list:
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the maternal grandmother")
            print("Ensure the maternal grandmother's children are stored in a list")
            return
        elif type(mother['Children']) is not list:
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the mother")
            print("Ensure the mother's children are stored in a list")
            return
        elif type(father['Children']) is not list:
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the father")
            print("Ensure the father's children are stored in a list")
            return
        elif sorted(fraternal_grandfather['Children']) != sorted([father['Name']]):
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the fraternal grandfather")
            print("Ensure the fraternal grandfather's children are the father")
            return
        elif sorted(fraternal_grandmother['Children']) != sorted([father['Name']]):
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the fraternal grandmother")
            print("Ensure the fraternal grandmother's children are the father")
            return
        elif sorted(maternal_grandfather['Children']) != sorted([mother['Name']]):
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the maternal grandfather")
            print("Ensure the maternal grandfather's children are the mother")
            return
        elif sorted(maternal_grandmother['Children']) != sorted([mother['Name']]):
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the maternal grandmother")
            print("Ensure the maternal grandmother's children are the mother")
            return
        elif sorted(mother['Children']) != sorted([offspring_1['Name'], offspring_2['Name']]):
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the mother")
            print("Ensure the mother's children are the offspring")
            return
        elif sorted(father['Children']) != sorted([offspring_1['Name'], offspring_2['Name']]):
            print("Family tree structure is incorrect")
            print("Failed when checking the children of the father")
            print("Ensure the father's children are the offspring")
            return
        else:
            print("Children fields are correct")
    except KeyError:
        print("Ensure your dict uses `Children` as the key for the dog's children")
        return

    try:
        if type(maternal_grandmother['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the maternal grandmother")
            print("Ensure the maternal grandmother's tricks are stored in a set")
            return
        elif type(maternal_grandfather['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the maternal grandfather")
            print("Ensure the maternal grandfather's tricks are stored in a set")
            return
        elif type(fraternal_grandmother['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the fraternal grandmother")
            print("Ensure the fraternal grandmother's tricks are stored in a set")
            return
        elif type(fraternal_grandfather['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the fraternal grandfather")
            print("Ensure the fraternal grandfather's tricks are stored in a set")
            return
        elif type(mother['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the mother")
            print("Ensure the mother's tricks are stored in a set")
            return
        elif type(father['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the father")
            print("Ensure the father's tricks are stored in a set")
            return
        elif type(offspring_1['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are stored in a set")
            return
        elif type(offspring_2['Tricks']) is not set:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are stored in a set")
            return
        elif family_tree_structure[0][1][1]['Tricks'] - maternal_grandmother['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the maternal grandmother")
            print("Ensure the maternal grandmother's tricks are correct")
            return
        elif family_tree_structure[0][1][0]['Tricks'] - maternal_grandfather['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the maternal grandfather")
            print("Ensure the maternal grandfather's tricks are correct")
            return
        elif family_tree_structure[0][0][1]['Tricks'] - fraternal_grandmother['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the fraternal grandmother")
            print("Ensure the fraternal grandmother's tricks are correct")
            return
        elif family_tree_structure[0][0][0]['Tricks'] - fraternal_grandfather['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the fraternal grandfather")
            print("Ensure the fraternal grandfather's tricks are correct")
            return
        elif family_tree_structure[1][0][1]['Tricks'] - mother['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the mother")
            print("Ensure the mother's tricks are correct")
            return
        elif family_tree_structure[1][0][0]['Tricks'] - father['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the father")
            print("Ensure the father's tricks are correct")
            return
        elif offspring_1['Tricks'] == offspring_2['Tricks'] and family_tree_structure[2][0] != family_tree_structure[2][1]:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are correct")
            return
        elif offspring_1['Tricks'] != offspring_2['Tricks'] and family_tree_structure[2][0] == family_tree_structure[2][1]:
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are correct")
            return
        elif not any((family_tree_structure[2][0]['Tricks'] - offspring_1['Tricks'] == set(), family_tree_structure[2][1]['Tricks'] - offspring_1['Tricks'] == set())):
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are correct")
            return
        elif not any((family_tree_structure[2][1]['Tricks'] - offspring_2['Tricks'] == set(), family_tree_structure[2][0]['Tricks'] - offspring_2['Tricks'] == set())):
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are correct")
            return
        else:
            print("Tricks fields are correct")
    except KeyError:
        print("Ensure your dict uses `Tricks` as the key for the dog's tricks")
        return
    print("All tests passed!")


def test_arg_kwarg_fun(arg_kwarg_fun):
    try:
        arg_kwarg_fun(1, 2)
    except ValueError as e:
        assert str(e) == str(ValueError('c must be set')), 'Test 1 failed'
        print('Test 1 passed')

    assert arg_kwarg_fun(1, 2, c=3) == 10, 'Test 2 failed'
    print('Test 2 passed')

    assert arg_kwarg_fun(1, 2, c=3, d=5) == 11, 'Test 3 failed'
    print('Test 3 passed')


def args_and_kwargs_fun(*args, **kwargs):
    print(args)
    print(kwargs)
    

def challenging_call(function):
    f_spec = inspect.getfullargspec(function)

    if len(f_spec.args) != 2 or f_spec.kwonlyargs != ['x', 'y']:
        print('Only 2 positional arguments and 2 keyword arguments are allowed')
        print('Try Again')
        return

    try:
        function(1, 2, 3, 4, x=5, y=6, z=7)
    except TypeError as e:
        print(e)
        if e.args[0] == "challenge_function() got multiple values for argument 'x'":
            print('Test 1 failed')
            print('You have \'unconsumed\' positional arguments')
        if e.args[0] == "challenge_function() got an unexpected keyword argument 'z'":
            print('Test 2 failed')
            print('You have \'unconsumed\' keyword arguments')

    print('All Tests passed!')


def test_quadratics(q_p3_p3_n6, q_p2_n2_n1, q_generic, partial_q_p3_p3_n6, partial_q_p2_n2_n1):
    # Define a generic quadratic function and partial it to use for solutions
    def q_generic(x, a, b, c):
        return a * x ** 2 + b * x + c
    _q_p3_p3_n6 = partial(q_generic, a=3, b=3, c=-6)
    _q_p2_n2_n1 = partial(q_generic, a=2, b=-2, c=-1)
    _q_p1_n1_n1 = partial(q_generic, a=1, b=-1, c=-1)

    # Assert that the last two arguments are partialled
    assert type(partial_q_p3_p3_n6) == partial, 'partial_q_p3_p3_n6 is not a partial function'
    assert type(partial_q_p2_n2_n1) == partial, 'partial_q_p2_n2_n1 is not a partial function'

    for i in range(-10, 10):
        assert q_p3_p3_n6(i) == _q_p3_p3_n6(i), f'q_p3_p3_n6 failed for input {i}'
        assert q_p2_n2_n1(i) == _q_p2_n2_n1(i), f'q_p2_n2_n1 failed for input {i}'
        assert q_generic(i, 1, -1, -1) == _q_p1_n1_n1(i), f'q_generic failed for input {i}'
        assert partial_q_p3_p3_n6(i) == _q_p3_p3_n6(i), f'partial_q_p3_p3_n6 failed for input {i}'
        assert partial_q_p2_n2_n1(i) == _q_p2_n2_n1(i), f'partial_q_p2_n2_n1 failed for input {i}'

    print('All tests passed!')


from io import StringIO 
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def test_wrappers(echo_name, echo_greeting_name, echo_greeting_name_signoff, greeting_wrapper, signoff_wrapper):

    def dummy(*args, **kwargs):
        pass
    with Capturing() as output:
        greeting_wrapper(dummy())
    assert output == [], 'greeting_wrapper should not print anything when wrapping a function'

    with Capturing() as output:
        signoff_wrapper(dummy())
    assert output == [], 'signoff_wrapper should not print anything when wrapping a function'

    with Capturing() as output:
        echo_name('John')
    assert output == ['John'], 'echo_name failed for input \'John\''
    print('echo_name passed!')

    with Capturing() as output:
        echo_greeting_name('John', 'Hi')
    assert output == ['Hi, John'], 'echo_greeting_name failed for input \'Hi\' and \'John\''
    print('echo_greeting_name passed!')

    with Capturing() as output:
        echo_greeting_name_signoff('John', 'Hi', 'Bye')
    assert output == ['Hi, John', 'Bye'], 'echo_greeting_name_signoff failed for input \'Hi\', \'John\' and \'Bye\''
    print('echo_greeting_name_signoff passed!')

    with Capturing() as output:
        echo_greeting_name('John')
    assert output == ['Hello, John'], 'echo_greeting_name failed for input \'John\', check your default args'
    print('echo_greeting_name passed default arg check!')

    with Capturing() as output:
        echo_greeting_name_signoff('John')
    assert output == ['Hello, John', 'Goodbye'], 'echo_greeting_name_signoff failed for input \'John\', check your default args'
    print('echo_greeting_name_signoff passed default arg check!')

    print('All tests passed!')


def test_wrappers_refac(echo_name, echo_greeting_name, echo_greeting_name_signoff, greeting_wrapper, signoff_wrapper):

    def dummy(*args, **kwargs):
        pass
    with Capturing() as output:
        greeting_wrapper(dummy())
    assert output == [], 'greeting_wrapper should not print anything when wrapping a function'

    with Capturing() as output:
        signoff_wrapper(dummy())
    assert output == [], 'signoff_wrapper should not print anything when wrapping a function'

    with Capturing() as output:
        echo_name('John')
    assert output == ['John'], 'echo_name failed for input \'John\''
    print('echo_name passed!')

    with Capturing() as output:
        echo_greeting_name('Hi','John')
    assert output == ['Hi, John'], 'echo_greeting_name failed for input \'Hi\' and \'John\''
    print('echo_greeting_name passed!')

    with Capturing() as output:
        echo_greeting_name_signoff('Hi', 'John', 'Bye')
    assert output == ['Hi, John', 'Bye'], 'echo_greeting_name_signoff failed for input \'Hi\', \'John\' and \'Bye\''
    print('echo_greeting_name_signoff passed!')

    with Capturing() as output:
        echo_greeting_name('John')
    assert output == ['Hello, John'], 'echo_greeting_name failed for input \'John\', check your default args'
    print('echo_greeting_name passed default arg check!')

    with Capturing() as output:
        echo_greeting_name_signoff('John')
    assert output == ['Hello, John', 'Goodbye'], 'echo_greeting_name_signoff failed for input \'John\', check your default args'
    print('echo_greeting_name_signoff passed default arg check!')

    print('All tests passed!')


def check_n_poly(func):

    # Test 5 orders from 1st to 5th evaluating at x=[-1, 0, 1]
    test_args = [
        [-1, 1, 1],
        [0, 1, 1],
        [1, 1, 1],  # 1st order
        [-1, 3, 3, -6],
        [0, 3, 3, -6],
        [1, 3, 3, -6],  # 2nd order
        [-1, -5, 2, -1],
        [0, -5, 2, -1],
        [1, -5, 2, -1],  # 3rd order
        [-1, -2, 2, 0, 2],
        [0, -2, 2, 0, 2],
        [1, -2, 2, 0, 2],  # 4th order
        [-1, -5, 1, 3, 2, -2],
        [0, -5, 1, 3, 2, -2],
        [1, -5, 1, 3, 2, -2]  # 5th order
    ]

    def apply_args(func, args):
        for i in args:
            assert func(*i) == n_poly(*i), f'Failed at order {len(i) - 2}\
                  for input {i}'

    apply_args(func, test_args)

    print('All tests passed!')


# Define some functions to test the fun_solver function

warnings.simplefilter('ignore', category=NumbaWarning)
# Two quadratic functions one with single root one with two roots
@jit((float64(float64)), nopython=True)
def a_quad_jit(x):
    return x**2 - 1


def a_quad(x):
    return x**2 - 1


@jit((float64(float64)), nopython=True)
def b_quad_jit(x):
    return x**2 - 2*x + 1


def b_quad(x):
    return x**2 - 2*x + 1


# A cubic function with three roots
@jit((float64(float64)), nopython=True)
def a_cubic_jit(x):
    return x**3 - 2*x**2 + x - 1


def a_cubic(x):
    return x**3 - 2*x**2 + x - 1


# A pentagonal function with five roots
@jit((float64(float64)), nopython=True)
def a_pent_jit(x):
    return x**5 - 2*x**4 + x**3 - 2*x**2 + x - 1


def a_pent(x):
    return x**5 - 2*x**4 + x**3 - 2*x**2 + x - 1


warnings.simplefilter('default', category=NumbaWarning)
# put all the functions in a list for easy access
jitted_funs = [a_quad_jit, b_quad_jit, a_cubic_jit, a_pent_jit]
funs = [a_quad, b_quad, a_cubic, a_pent]


def check_fun_solver(func):
    user_sols = []
    test_time1 = time()
    for i in jitted_funs:
        user_sols.append(func(i, 0.000001))
    test_time2 = time()

    sol_sols = []
    time1 = time()
    for i in jitted_funs:
        sol_sols.append(fun_solver(i, 0.000001))
    time2 = time()

    # Check the solutions are correct
    for i in range(len(user_sols)):
        assert np.allclose(user_sols[i], sol_sols[i]), f'Failed \
            for function {i}'

    print("Time taken for jit-ed functions:\n" +
          f"Your Code: {test_time2 - test_time1}" +
          f"seconds.\nSolution code: {time2 - time1} seconds.")

    # disable numba warnings to make the output cleaner
    warnings.simplefilter('ignore', category=NumbaWarning)
    user_sols = []
    test_time1 = time()
    for i in funs:
        user_sols.append(func(i, 0.000001))
    test_time2 = time()

    sol_sols = []
    time1 = time()
    for i in funs:
        sol_sols.append(fun_solver(i, 0.000001))
    time2 = time()

    # Check the solutions are correct
    for i in range(len(user_sols)):
        assert np.allclose(user_sols[i], sol_sols[i]), f'Failed \
            for function {i}'
    warnings.simplefilter('default', category=NumbaWarning)

    print("Time taken for non-jit functions:\n" +
          f"Your Code: {test_time2 - test_time1}" +
          f"seconds.\nSolution code: {time2 - time1} seconds.")

    print('All tests passed!')


# numbered class test functions that build on each other to test the Dog class learners 
# build in 04

def test_class_constructor_1(Dog):
    try:
        dog_class = Dog(name="Milo", owner="Cassandra", age=4, sex="Dog", color="Brown")
    except TypeError as e:
        error_list = str(e).split()
        print(f"Your class is missing {error_list[6]}")
        # Now throw the error
        raise e
    print('Constructor test 1 passed')
    return dog_class


def test_class_attrs_1(dog_class):
    assert dog_class.name == "Milo", 'Name attribute is incorrect'
    assert dog_class.owner == "Cassandra", 'Owner attribute is incorrect'
    assert dog_class.age == 4, 'Age attribute is incorrect'
    assert dog_class.sex == "Dog", "Sex attribute is incorrect"
    assert dog_class.color == "Brown", 'Color attribute is incorrect'

    print('Attributes test 1 passed')


def test_class_attrs_2(dog_class):
    test_class_attrs_1(dog_class)
    try:
        dog_class.sex = "Female"
    except AttributeError:
        print("Your class correctly rejected updating the read only attribute 'Sex'")
    else:
        raise AttributeError("Your class allowed updating the read only attribute 'Sex'")
    try:
        dog_class.color = "Black"
    except AttributeError:
        print("Your class correctly rejected updating the read only attribute 'Color'")
    else:
        raise AttributeError("Your class allowed updating the read only attribute 'Color'")

    print('Attributes test 2 passed')


def test_class_constructor_2(Dog):

    try:
        Dog(
            name="Milo", owner="Cassandra", age=4, sex="Dog", color="Brown",
            tricks = 'Sit'
            )
    except:
        print("Your class threw an error when a string was passed to the tricks argument")
        raise e 

    try:
        dog_class = Dog(
            name="Milo", owner="Cassandra", age=4, sex="Dog", color="Brown",
            tricks=['Sit', 'Paw']
            )
    except TypeError as e:
        print("Your class threw an error when a list was passed to the tricks argument")
        raise e

    print('Constructor test 1 passed')
    return dog_class 


def test_class_attrs_3(dog_class):
    test_class_attrs_2(dog_class)
    assert dog_class.tricks == {'Sit', 'Paw'}, 'Tricks attribute is incorrect'

    dog_class.tricks = {'Beg', 'Stay'}
    assert dog_class.tricks == {'Sit', 'Paw', 'Beg', 'Stay'}, 'Tricks attribute is incorrect'
    dog_class.tricks = ['Beg', 'Stay']
    assert dog_class.tricks == {'Sit', 'Paw', 'Beg', 'Stay'}, 'Tricks attribute is incorrect'
    dog_class.tricks = 'Beg'
    assert dog_class.tricks == {'Sit', 'Paw', 'Beg', 'Stay'}, 'Tricks attribute is incorrect'

    print('Attributes test 3 passed')
