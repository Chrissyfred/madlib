from random import randint
import copy

word_bank = { #12 of each
    'names' : ['Tammy', 'Chrissy', 'Donna', 'Megan', 'Sarah', 'Nasreen', 'Renee', 'Harriet', 'Ruth', 'Amelia', 'Ella', 'Elsa'], 
    'sing_nouns' : ['phone', 'coffee', 'tree', 'door', 'TV', 'school', 'bed', 'rose', 'machine', 'tent', 'furniture', 'napkin'],
    'number' : ['six', 'twenty', 'five', 'ten', 'fifteen', 'three', 'three', 'eight', 'thirteen', 'twenty-one', 'two', 'seventeen'],
    'adj' : ['stupid', 'small', 'dull', 'funny', 'annoying', 'happy', 'brave', 'busy', 'cautious', 'doubtful', 'glorious', 'itchy'],
    'cap_plural_nouns' : ['Juice', 'Tea', 'Custard', 'Gasoline', 'Tears', 'Makeup', 'Water', 'Oils', 'Grease', 'Broth', 'Mud', 'Snow'],
    'plural_nouns' : ['feet', 'lamps', 'planets', 'jobs', 'rope', 'flowers', 'staff', 'data', 'food', 'games', 'problems', 'things'],
    'adverb' : ['boldly', 'victoriously', 'finally', 'bravely', 'gleefully', 'faithfully', 'safely', 'miserably', 'lazily', 'joylessly', 'painfully', 'wearily'],
    'colleges' : ['Northwestern University', 'University of Rochester', 'Stanford University', 'University of Notre Dame', 'Emory University', 'Rice University', 'Huntingdon College', 'Lyon College', 'Arizona State University', 'Argosy University', 'Humphreys College', 'Urbana University'],
    'cities' : ['Sacramento', 'Chicago', 'Flagstaff', 'El Dorado', 'Davis', 'Miliford', 'Boise', 'Augusta', 'Providence', 'Olympia', 'Lincoln', 'Phoenix'],
    'careers' : ['journalism', 'production', 'psychology', 'data science', 'counseling', 'theatre', 'programming', ' engineering', 'law', 'finance', 'human resources', 'public health'],
    'relative' : ['aunt', 'cousin', 'uncle', 'mother', 'brother', 'father', 'sister', 'step-mother', 'step-father', 'grand-father', 'grand-mother', 'great aunt'],
    'verb' : ['cook', 'accept', 'take', 'drive', 'steal', 'buy', 'argue', 'beg', 'earn', 'cry', 'paint', 'use'] 
}  

def menu():
    print("")
    print("             === Mad Libs! ===              ")
    print("------------------------------------------------")
    print("| 1. Manual Input - Relationship Drama          |")
    print("| 2. Computer-Generated - Relationship Drama    |")
    print("| 3. Manual Input - Career Drama                |")
    print("| 4. Computer-Generated - Career Drama          |")
    print("| 5. Exit                                       |")
    print("------------------------------------------------")

def random_word(type, copy_dict):
    words = copy_dict[type]
    length = len(words) - 1 #subtracting 1 since the index starts with 0
    index = randint(0, length)
    return copy_dict[type].pop(index) #use and remove a word from the dict

text_1 = "I'll make it right this time.\n\n"
italic_text_1 = "\x1B[3m" + text_1 + "\x1B[0m"
text_2 = "Am I really doing this?\n\n"
italic_text_2 = "\x1B[3m" + text_2 + "\x1B[0m" 

story_2 = (
    "{} threatened to splatter down Shane's cheeks. He held his head back and sniffed. \nIt's been {} months since he's laid eyes on {}.\n\n" +
    "The emails between them have been getting {} and {} lately. \nShane took a deep breath and leaned against the steering wheel.\n\n" + 
    "Remembering how they last parted ways always made a small block of {} form in his chest.\n\n" +
    italic_text_1 +
    "He caught sight of her through his side mirror, dragging {} behind her as she typed into her phone.\n" +
    "Shane listened as she passed by his parked car as her {} clicked against the pavement. \n\nHis heart beat in rhythm with the constant noise. He could feel himself starting to sweat.\n\n" +
    italic_text_2 +
    "Shane reached into the back seat for the {} he'd bought earlier. He then fingered the ring in his pocket. \n\nIt was just there to spur him on- he had no intention of having it thrown back in his {}.\n" +
    "He {} emerged from the car and smoothed the wrinkles out of his shirt. It was now or never, and he wouldn't make the same mistake again.\n" +
    "\nThe End.\n"
) 

def new_story2():
    copy_dict = copy.deepcopy(word_bank) #making a copy of the word bank keeps it in tact while words are used and removed in the local version.
    return story_2.format(
        random_word('cap_plural_nouns', copy_dict),
        random_word('number', copy_dict),
        random_word('names', copy_dict),
        random_word('adj', copy_dict),
        random_word('adj', copy_dict),
        random_word('sing_nouns', copy_dict),
        random_word('plural_nouns', copy_dict),
        random_word('plural_nouns', copy_dict),
        random_word('sing_nouns', copy_dict),
        random_word('sing_nouns', copy_dict),
        random_word('adverb', copy_dict)
    )
    
c_text_1 =  "\n{} and {} have good {} programs. If you are an intern, you'll be running errands and getting coffee.\nIt will take a long time before you have some real responsibilities.\nA Master's degree will make a huge difference.\n\n"
c_italic_text_1 = "\x1B[3m" + c_text_1 + "\x1B[0m"

story_4 = (
    "{} is planning to start a new career in {} and {} by attending graduate school. Her best friends fill her {} " + 
    "with doubts about getting a good return on investment from the degree.\n\n" +
    "They talked her into interning for a(an) {}-based Youtube channel called {} Channel.\n" +
    "Since it can take {} hours to get there from {}, where she lives, she decides to look for roommates that work at the Youtube channel.\n\n" +
    "Her friends suggest she use the money she saved up for tuition to pay rent since the internship pays very little.\n\n" +
    "She ran the ideas by her {}, who quickly disagreed.\n" +
    c_italic_text_1 +
    "After a few hours, she decides to {} her friend's advice.\n" +
    "\nThe End."
) 

def new_story4():
    copy_dict = copy.deepcopy(word_bank) #making a copy of the word bank keeps it in tact while words are used and removed in the local version.
    return story_4.format(
    random_word('names', copy_dict),
    random_word('careers', copy_dict),
    random_word('careers', copy_dict),
    random_word('sing_nouns', copy_dict),
    random_word('cities', copy_dict),
    random_word('cap_plural_nouns', copy_dict),
    random_word('number', copy_dict),
    random_word('cities', copy_dict),   
    random_word('relative', copy_dict),
    random_word('colleges', copy_dict),
    random_word('colleges', copy_dict),
    random_word('careers', copy_dict),       
    random_word('verb', copy_dict)
)