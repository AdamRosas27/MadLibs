
# Method that takes in a parameter and chooses a story based on the input
def choose_story(choice):
    # Match case statement that acts as a switch statement and the output is based on the users input
    match choice:
        case 1:
            # Prints the story out
            print("You chose the Farm Animal ad-lib:\nThere are many kinds of (adjective) animals that (verb) on a farm. For example, (plural noun; animals) and (plural noun; animals) (verb) eggs, and (noun; food) comes from farm-raised (plural noun; animals). On a dairy farm, (plural noun; animals) and (plural noun; animals) make (noun;beverage) that people drink and also use to make (noun; food) and (noun; food). Some farm animals like (plural noun; animals) and (plural noun; animals) have soft (noun), which is used to make (plural noun; article of clothing) and (plural noun).")
            # Asks the user to enter an input for the types of words
            fa_adj_1, fa_verb_1, fa_pn_1, fa_pn_2, fa_verb_1, fa_n_1, fa_pn_3, fa_pn_4, fa_pn_5, fa_n_2, fa_n_3, fa_n_4, fa_pn_6, fa_pn_7, fa_n_5, fa_pn_8, fa_pn_9 = input(
                "Enter your desired adjectives, pronouns, nouns, and verbs to complete the story").split()
            # Prints out the story with the words that the user chose
            print("You chose the Farm Animal ad-lib:\nThere are many kinds of {} animals that {} on a farm. For example, {} and {} {} eggs, and {} comes from farm-raised {}. On a dairy farm, {} and {} make {} that people drink and also use to make {} and {}. Some farm animals like {} and {} have soft {}, which is used to make {} and {}.".format(
                fa_adj_1, fa_verb_1, fa_pn_1, fa_pn_2, fa_verb_1, fa_n_1, fa_pn_3, fa_pn_4, fa_pn_5, fa_n_2, fa_n_3, fa_n_4, fa_pn_6, fa_pn_7, fa_n_5, fa_pn_8, fa_pn_9))
        case 2:
            return None
        case 3:
            return None
        case 4:
            return None


# Choice variable is set to the input that the user gives
choice = int(input(
    "Enter 1 for Farm Animals\nEnter 2 for Spooky Story\nEnter 3 for Birthday Party\nEnter 4 for Love Story"))

# Choose story method is called with the choice variable as the argument
choose_story(choice)
