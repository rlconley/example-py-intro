halloween_costumes = [
    'The Bear',
    'Witch',
    'Cow',
    'Mr. Clean',
    'Cheshire Cat',
    'Bumblebee'
]

# add to list with append()
halloween_costumes.append('Dinosaur')
print(halloween_costumes)

# remove with pop()
removed_costume = halloween_costumes.pop()
print(removed_costume)
print(halloween_costumes)

print(len(halloween_costumes))
print(halloween_costumes[2:5])

next_year_costumes = []
for costume in halloween_costumes:
    if costume != "The Bear":
        next_year_costumes.append(costume)
        
print("The costumes we are keeping for next year are: ", next_year_costumes)

# tuples are like lists but are immutable, cannot be changed

colors = ('red', 'blue', 'green', 'yellow')
print(colors)

hween_costumes_dict = {
    "Freddie": "The Bear",
    'Kelsey': 'Witch',
    'Maria': 'Cow',
    'Rebecca': 'Cheshire Cat',
    'Jon': ('Mr. Clean', 'Charlie Brown'),
    'Loki': 'Bumblebee',
}

# iterable means you can loop through it and perform actions on each item
for name, costume in hween_costumes_dict.items():
    # f strings allow us to interject variable names in with text
    print(f"{name}'s costume is {costume}")

# print(hween_costumes_dict["Rebecca"])
# hween_costumes_dict["Rebecca"] = "ladybug"
# print(hween_costumes_dict["Rebecca"])
hween_costumes_dict["Jon"] = ('Mr. Clean', 'Charlie Brown', 'Gru')
print(hween_costumes_dict['Jon'] + ('Test',))
