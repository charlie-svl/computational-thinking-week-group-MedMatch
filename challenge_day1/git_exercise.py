
# Import functions from different modules
import charlie
import andrey
import akanksha
import al
import hugo
import maxim


# Define an introduction function
def introduction():
    print("This is team MedMatch. We are:")
    charlie.name()
    andrey.name_andrey()
    akanksha.akanksha_c()
    al.N()
    hugo.name_hugo()
    maxim.function()
    return


def story(name_1, name_2, name_3, name_4, name_5, name_6):
    print("Act 1:")
    act_1 = charlie.par_c_1(name_1, name_2, name_3, name_4, name_5, name_6), al.par_al_1(name_1, name_2, name_3, name_4, name_5, name_6), akanksha.par_ac_1(name_1, name_2, name_3, name_4, name_5, name_6), andrey.par_an_1(name_1, name_2, name_3, name_4, name_5, name_6), hugo.par_h_1(name_1, name_2, name_3, name_4, name_5, name_6), maxim.par_m_1(name_1, name_2, name_3, name_4, name_5, name_6)
    print("Act 2:")
    act_2 = charlie.par_c_2(name_1, name_2, name_3, name_4, name_5, name_6), al.par_al_2(name_1, name_2, name_3, name_4, name_5, name_6), akanksha.par_ac_2(name_1, name_2, name_3, name_4, name_5, name_6), andrey.par_an_2(name_1, name_2, name_3, name_4, name_5, name_6), hugo.par_h_2(name_1, name_2, name_3, name_4, name_5, name_6), maxim.par_m_2(name_1, name_2, name_3, name_4, name_5, name_6)
    print("Act 3:")
    act_3 = charlie.par_c_3(name_1, name_2, name_3, name_4, name_5, name_6), al.par_al_3(name_1, name_2, name_3, name_4, name_5, name_6), akanksha.par_ac_3(name_1, name_2, name_3, name_4, name_5, name_6), andrey.par_an_3(name_1, name_2, name_3, name_4, name_5, name_6), hugo.par_h_3(name_1, name_2, name_3, name_4, name_5, name_6), maxim.par_m_3(name_1, name_2, name_3, name_4, name_5, name_6)
    return

# Call the story function with the actual names
name1 = charlie.name_story()
name2 = akanksha.name_story()
name3 = al.name_story()
name4 = andrey.name_story()
name5 = hugo.name_story()
name6 = maxim.name_story()

introduction()
story(name1, name2, name3, name4, name5, name6)
