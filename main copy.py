from Question import Questions






question = [
    "How old are you?\n\n",
    "What is your fitness goal?\n(a)weight loss\n(b)aesthetic appearence\n(c)strength gain\n\n",
    "What is your gender?\n(a)M\n(b)F\n\n"
]

questions = [
    Questions(question[0]),
    Questions(question[1]),
    Questions(question[2]),
]


def get_routine(questions):
    range1 = range(0, 13)
    range2 = range(70, 121)
    range3 = range(13, 18)
    range4 = range(50, 69)
    range5 = range(18, 25)
    range6 = range(35, 49)
    range7 = range(25, 34)

    answer1 = input(questions[0].prompt)
    intensity1 = False
    intensity2 = False
    intensity3 = False
    wl = False
    a = False
    s = False
    m = False
    f = False

    if int(answer1) in range1 or int(answer1) in range2:
        print("You are not of age to workout.")
        return
    elif int(answer1) in range3 or int(answer1) in range4:
        intensity1 = True
    elif int(answer1) in range5 or int(answer1) in range6:
        intensity2 = True
    elif int(answer1) in range7:
        intensity3 = True
    else:
        print("Accurate age not given")
        return
    answer2 = input(questions[1].prompt)
    answer2 = answer2.upper()
    if answer2 == "A":
        wl = True
    elif answer2 == "B":
        a = True
    elif answer2 == "C":
        s = True
    else:
        print("Valid goal not given.")
        return
    answer3 = input(questions[2].prompt)
    answer3 = answer3.upper()
    if answer3 == "A":
        m = True
    elif answer3 == "B":
        f = True
    else:
        print("Valid gender not given")
        return
    if intensity1 and wl and m:
        print('Jog for 30 minutes a day, each day, and diet.')
        return
    elif intensity1 and a and m:
        print('Do pushups, situps, and squats, 2 sets of reps to failure, every other day.')
    elif intensity1 and s and m:
        print('Do 2 sets of reps to failure, curls, shoulder presses, and dumbbell benchpress every other day.')
    elif intensity1 and wl and f:
        print('Jog for 20 minutes a day, each day, and diet.')
    elif intensity1 and a and f:
        print('Do girl pushups, situps, and squats, 2 sets of reps to failure, each day.')
    elif intensity1 and s and f:
        print('Do very light curls and shoulder presses for 2 sets of 10 every other day')
    elif intensity2 and wl and m:
        print('Jog for 1 hr and 30 minutes each day and diet.')
    elif intensity2 and a and m:
        print('Do 3 sets of reps to failure of pushups, situps, squats, and chinups eachday')
    elif intensity2 and s and m:
        print('Do 3 sets of 15 of curls, shoulder presses, and benchpress one day. The next day rest. The following 3 '
              'sets of 15 squats and lunges')
    elif intensity2 and wl and f:
        print('Jog for 1 hour and 10 minutes each day, and diet.')
    elif intensity2 and a and f:
        print('Run at least 3 miles a day, and do 5 sets of reps to failure of squats and situps.')
    elif intensity2 and s and f:
        print('Do benchpress, curls, and deadlifts one day, rest for 2 day, and do shoulder presses and squats the '
              'following day.')
    elif intensity3 and wl and m:
        print('Run for 8 miles a day minimum.')
    elif intensity3 and a and m:
        print('5 sets of reps to failure, pushups, situps, pullups, squats, and dips, everyday.')
    elif intensity3 and s and m:
        print('5 sets of reps to failure, benchpress, shoulder press, curls, and dumbbell squats each day.')
    elif intensity3 and wl and f:
        print('Run for 5 miles a day minimum')
    elif intensity3 and a and f:
        print('5 sets of reps to failure, squats, lunges, and situps.')
    elif intensity3 and s and f:
        print('5 sets of reps to failure, squats, lunges, and situps')
    return

get_routine(questions)


