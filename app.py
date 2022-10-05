from game_pkg.main_functions import menu, new_story2, new_story4

while True:
    menu()
    choice = input("Select an option: 1-5.\n")
    #Manual Input - Relationship Drama
    if choice == "1": 
        names = [] 
        sing_nouns = []  
        number = []
        adj = []
        plural_nouns = []
        adverb = []

        plural_nouns.append(input("Type a capitalized plural noun: "))
        names.append(input("Type a woman's first name: "))
        number.append(input("Type a number: "))
        adj.append(input("Type an adjective (Adjectives describe nouns): "))
        adj.append(input("Type another adjective: "))
        sing_nouns.append(input("Type a singular noun: "))
        plural_nouns.append(input("Type a plural noun: "))
        plural_nouns.append(input("Type another plural noun: "))
        sing_nouns.append(input("Type a singular noun: "))
        sing_nouns.append(input("Type another singular noun: "))
        adverb.append(input("Type an adverb (Adverbs describe verbs): "))

        text_1 = "I'll make it right this time."
        italic_text_1 = "\x1B[3m" + text_1 + "\x1B[0m"
        text_2 = "Am I really doing this?"
        italic_text_2 = "\x1B[3m" + text_2 + "\x1B[0m"
        print()
        print("Relationship Drama: \n")
        print(plural_nouns[0], "threatened to splatter down Shane's cheeks. He held his head back and sniffed. \nIt's been " + number[0] +  " months since he's laid eyes on " + names[0] + ".")
        print("The emails between them have been getting " + adj[0] + " and " + adj[1] + " lately. \nShane took a deep breath and leaned against the steering wheel.")
        print("Remembering how they last parted ways always made a small block of " + sing_nouns[0] + " form in his chest.\n\n")
        
        print(italic_text_1 + "\n\n")
       
        print("He caught sight of " + names[0] + " through his side mirror, dragging " + plural_nouns[1] + " behind her as she typed into her phone.")
        print("Shane listened as she passed by his parked car as her " + plural_nouns[1] + " clicked against the pavement. \nHis heart beat in rhythm with the constant noise. He could feel himself starting to sweat.\n\n")
        print(italic_text_2 + "\n\n")
    
        print("Shane reached into the back seat for the " + sing_nouns[1] + " he'd bought earlier. He then fingered the ring in his pocket. \nIt was just there to spur him on- he had no intention of having it thrown back in his " + sing_nouns[2] + ".")
        print("He " + adverb[0] + " emerged from the car and smoothed the wrinkles out of his shirt. It was now or never, and he wouldn't make the same mistake again.")
        print("\nThe End.\n")    
   
    #Computer Generated - Relationship Drama
    elif choice == "2": 
        print("Relationship Drama: \n")
        print(new_story2())
        print()
        
    #Manual Input - Career Drama    
    elif choice == "3":  
        names = []
        careers = []
        sing_nouns = []
        cities = []
        number = []
        relative = []
        colleges = []
        verb = []
        names.append(input("Type a woman's first name: "))
        careers.append(input("Name a career: "))
        careers.append(input("Name another career: "))
        sing_nouns.append(input("Type a singular noun: "))
        cities.append(input("Name a city: "))
        cities.append(input("Name another city: "))
        number.append(input("Type a number: "))
        relative.append(input("Type of family member: "))
        colleges.append(input("Name a college: "))
        colleges.append(input("Name another college: "))
        verb.append(input("Type a verb: "))
        c_text_1 = names[0] + ", " + colleges[0] + " and " + colleges[1] + " have good " + careers[0] + " programs. If you are an intern, you'll be running errands and getting coffee. It will take a long time before you have some real responsibilities. \nA Master's degree will make a huge difference.\n\n"
        c_italic_text_1 = "\x1B[3m" + c_text_1 + "\x1B[0m"

        print("Career Drama: \n")
        print(names[0] + " is planning to start a new career in " + careers[0] + " and " + careers[1] + " by attending graduate school. Her best friends fill her "  + sing_nouns[0] + " with doubts about getting a good return on investment from the degree.\n\n")
        print("They talked her into interning for a(an) " + cities[0] + "-based Youtube channel called Your Channel.")
        print("Since it can take " + number[0] + " hour(s) to get to " + cities[0] + " from " + cities[1] + ", where " + names[0] + " lives, she decides to look for roommates in the " + cities[0]+ " area.")
        print("Her friends suggest she use the money she saved up for tuition to pay rent since the internship pays very little.\n\n")
        print(names[0] + " runs the ideas by her " + relative[0] + ", who quickly disagrees.")
        print(c_italic_text_1)
        print(names[0] + " isn't sure what to do. After a few hours, she decides to " + verb[0] +  " her friend's advice.")
        print("\nThe End.")
 
    #Computer Generated - Career Drama      
    elif choice == "4": 
        print("Career Drama: \n")
        print(new_story4())
        print()
    
    elif choice == "5":
        print("Thank you for playing. Goodbye.")
        break
    
    else:
        print("Invalid response. Please choose 1-5.")
 

        
    
    
