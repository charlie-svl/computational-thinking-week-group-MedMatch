def name():
    print("Charlie Smit")
    return

def name_story():
    name = "Alice"
    return name

name_1=name_story()


def par_c_1(name_1, name_2, name_3, name_4, name_5, name_6):
    paragraph = f"This is a story about 6 friends who take the journey through their life together. The {name_1}, {name_2}, and {name_3} have grown up together, as their moms were best friends and decided to have babies at the same time. They met the boys: {name_4}, {name_5}, and {name_6} a couple years later when they entered kindergarten. Together they have a lot of stories to share."
    print(paragraph)
    return

def par_c_2(name_1, name_2, name_3, name_4, name_5, name_6):
    paragraph = f"After {name_4}, {name_5}, and {name_6} started listening to some controversial podcasts, mainly about women, {name_3}, {name_2}, and {name_1} decided to hold an intervention. They saw the path they were going on and were just in time before their brain was permanently altered."
    print(paragraph)
    return

def par_c_3(name_1, name_2, name_3, name_4, name_5, name_6):
    paragraph = f"{name_3} proclaims this will be her last summer at the country house as her now husband, {name_5}, had passed away a few months back. {name_1} and {name_6} are very understanding. {name_2} and {name_4} were very sad to hear it and started crying."
    print(paragraph)
    return


name()
par_c_1("Alice", "Brianna", "Ella", "Juan", "Igor", "Theo")
par_c_2("Alice", "Brianna", "Ella", "Juan", "Igor", "Theo")
par_c_3("Alice", "Brianna", "Ella", "Juan", "Igor", "Theo")

