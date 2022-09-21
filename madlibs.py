def choose_story(choice):
    match choice:
        case 1:
            print("You chose the Farm Animal ad-lib:\nThere are many kinds of (adjective) animals that (verb) on a farm. For example, (plural noun; animals) and (plural noun; animals) (verb) eggs, and (noun; food) comes from farm-raised (plural noun; animals). On a dairy farm, (plural noun; animals) and (plural noun; animals) make (noun;beverage) that people drink and also use to make (noun; food) and (noun; food). Some farm animals like (plural noun; animals) and (plural noun; animals) have soft (noun), which is used to make (plural noun; article of clothing) and (plural noun).")
        case 2:
            return None
        case 3:
            return None
        case 4:
            return None


choice = int(input(
    "Enter 1 for Farm Animals, 2 for Spooky Story, 3 for Birthday Party, or 4 for Love Story."))

choose_story(choice)
