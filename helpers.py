# Create a random family tree of dogs using dictionaries.

from random import choice

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
        if not \
         family_tree_structure[0][0][0]['Name'] == maternal_grandmother['Name'] and \
         family_tree_structure[0][0][1]['Name'] == maternal_grandfather['Name'] and \
         family_tree_structure[0][1][0]['Name'] == fraternal_grandmother['Name'] and \
         family_tree_structure[0][1][1]['Name'] == fraternal_grandfather['Name'] and \
         family_tree_structure[1][0][0]['Name'] == mother['Name'] and \
         family_tree_structure[1][0][1]['Name'] == father['Name'] and \
         family_tree_structure[2][0]['Name'] == offspring_1['Name'] and \
         family_tree_structure[2][1]['Name'] == offspring_2['Name']:
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
        elif sorted(family_tree_structure[1][0][0]['Parents']) != sorted(maternal_grandmother['Name'], maternal_grandfather['Name']):
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the mother")
            print("Ensure the mother's parents are the maternal grandmother and maternal grandfather")
            return
        elif sorted(family_tree_structure[1][0][1]['Parents']) != sorted(fraternal_grandmother['Name'], fraternal_grandfather['Name']):
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the mother")
            print("Ensure the mother's parents are the maternal grandmother and maternal grandfather")
            return
        elif sorted(family_tree_structure[2][0]['Parents']) != sorted(mother['Name'], father['Name']):
            print("Family tree structure is incorrect")
            print("Failed when checking the parents of the offspring")
            print("Ensure the offspring's parents are the mother and father")
            return
        elif sorted(family_tree_structure[2][1]['Parents']) != sorted(mother['Name'], father['Name']):
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
        elif family_tree_structure[0][0][0]['Tricks'] - maternal_grandmother['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the maternal grandmother")
            print("Ensure the maternal grandmother's tricks are correct")
            return
        elif family_tree_structure[0][0][1]['Tricks'] - maternal_grandfather['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the maternal grandfather")
            print("Ensure the maternal grandfather's tricks are correct")
            return
        elif family_tree_structure[0][1][0]['Tricks'] - fraternal_grandmother['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the fraternal grandmother")
            print("Ensure the fraternal grandmother's tricks are correct")
            return
        elif family_tree_structure[0][1][1]['Tricks'] - fraternal_grandfather['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the fraternal grandfather")
            print("Ensure the fraternal grandfather's tricks are correct")
            return
        elif family_tree_structure[1][0][0]['Tricks'] - mother['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the mother")
            print("Ensure the mother's tricks are correct")
            return
        elif family_tree_structure[1][0][1]['Tricks'] - father['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the father")
            print("Ensure the father's tricks are correct")
            return
        elif family_tree_structure[2][0]['Tricks'] - offspring_1['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are correct")
            return
        elif family_tree_structure[2][1]['Tricks'] - offspring_2['Tricks'] != set():
            print("Family tree structure is incorrect")
            print("Failed when checking the tricks of the offspring")
            print("Ensure the offspring's tricks are correct")
            return
        else:
            print("Tricks fields are correct")
    except KeyError:
        print("Ensure your dict uses `Tricks` as the key for the dog's tricks")
        return
