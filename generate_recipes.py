import markovify

# function to delete any duplicate ingredients in a recipe
def delete_duplicates(recipe):
    words = recipe.split(" ")
    no_dups = []
    [no_dups.append(word) for word in words if word not in no_dups]
    r = ""
    for w in no_dups:
        r = r + w
        if w != no_dups[-1]:
            r = r + " "
    return r

# Get raw text as string.
with open("SampleRecipes.txt") as file:
    text = file.read()

# Build the model.
text_model = markovify.NewlineText(text)

cocktail_list = list()
# Add the 100 generated recipes to the cocktail list
for i in range(20):
    #print(text_model.make_sentence(test_output=False))
    # the defaults: max_overlap_ratio=0.7, max_overlap_total=15, tries = 10
    recipe = text_model.make_sentence(tries=100)
    cocktail_list.append(delete_duplicates(recipe))

# Add the recipes to file that contains all the recipes
file = open('generated_recipes.txt', 'w')
for drink in cocktail_list:
    file.write(drink + '\n')
file.close()
