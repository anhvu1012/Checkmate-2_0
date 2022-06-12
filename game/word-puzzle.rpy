screen solving_word_puzzle:
    image "Items Pop Up/word-puzzle-unsolved-pop-up.png" align (0.8, 0.4) at half_size

screen wp_solved:
    image "Items Pop Up/word-puzzle-solved-pop-up.png" align (0.8, 0.4) at half_size

screen choose_question:
    frame:
        #background "#FFFFFF40"
        xpos 5 ypos 5
        hbox:
            textbutton "Back to livingroom" action [Return(True), Jump("back_to_livingroom")]

    imagebutton auto "images/wp_setup/questions/q1_%s.png" xpos 676 ypos 194 action Jump("question1") sensitive answ1 == False
    imagebutton auto "images/wp_setup/questions/q2_%s.png" xpos 645 ypos 228 action Jump("question2") sensitive answ2 == False
    imagebutton auto "images/wp_setup/questions/q3_%s.png" xpos 645 ypos 261 action Jump("question3") sensitive answ3 == False
    imagebutton auto "images/wp_setup/questions/q4_%s.png" xpos 651 ypos 303 action Jump("question4") sensitive answ4 == False
    imagebutton auto "images/wp_setup/questions/q5_%s.png" xpos 513 ypos 339 action Jump("question5") sensitive answ5 == False
    imagebutton auto "images/wp_setup/questions/q6_%s.png" xpos 596 ypos 383 action Jump("question6") sensitive answ6 == False

    imagebutton auto "images/wp_setup/keyword_%s.png" xpos 528 ypos 435 action Jump("keyword_answ")

    if answ1 == True:
        image "images/wp_setup/answers/a1.png" xpos 710 ypos 192
    if answ2 == True:
        image "images/wp_setup/answers/a2.png" xpos 677 ypos 228
    if answ3 == True:
        image "images/wp_setup/answers/a3.png" xpos 680 ypos 261
    if answ4 == True:
        image "images/wp_setup/answers/a4.png" xpos 709 ypos 303
    if answ5 == True:
        image "images/wp_setup/answers/a5.png" xpos 539 ypos 339
    if answ6 == True:
        image "images/wp_setup/answers/a6.png" xpos 660 ypos 379

label keyword_answ:
    a_left "You got the keyword already?"

    $keyword = renpy.input("Keyword: (ALL IN UPPERCASE)", length = 6)
    $keyword = keyword.strip()
    if keyword == "FLOWER":
        a_left "Wow! You are good at this!"
        jump wp_solved
    else:
        a_left "Hmm.. Take your time and try again."
        call screen choose_question

label question1:
    a_left "\"When I eat, I live, but when I drink, I die. What am I?\""
    $answer = renpy.input("Your answer: (all in lowercase)", length = 4)
    $answer = answer.strip()

    if answer == "fire":
        a_left "Yes, I think so too! Let's move on!"
        $answ1 = True
        $answ_count += 1
        call screen choose_question
    else:
        a_left "I don't think it's correct. Do you want to choose an another question?"
        menu:
            extend ''
            "Yes":
                call screen choose_question
            "No":
                jump question1

label question2:
    a_left "\"What has three hands but only one face?\""
    $answer = renpy.input("Your answer: (all in lowercase)", length = 5)
    $answer = answer.strip()

    if answer == "clock":
        a_left "Yes, I think so too! Let's move on!"
        $answ2 = True
        $answ_count += 1
        call screen choose_question
    else:
        a_left "I don't think it's correct. Do you want to choose an another question?"
        menu:
            extend ''
            "Yes":
                call screen choose_question
            "No":
                jump question2

label question3:
    a_left "\"What is it that was the past of tomorrow and the future of yesterday?\""
    $answer = renpy.input("Your answer: (all in lowercase)", length = 5)
    $answer = answer.strip()

    if answer == "today":
        a_left "Yes, I think so too! Let's move on!"
        $answ3 = True
        $answ_count += 1
        call screen choose_question
    else:
        a_left "I don't think it's correct. Do you want to choose an another question?"
        menu:
            extend ''
            "Yes":
                call screen choose_question
            "No":
                jump question3

label question4:
    a_left "\"If there are three apples and you take away two. How many apples do you have?\""
    $answer = renpy.input("Your answer: (all in lowercase)", length = 3)
    $answer = answer.strip()

    if answer == "two":
        a_left "Yes, I think so too! Let's move on!"
        $answ4 = True
        $answ_count += 1
        call screen choose_question
    else:
        a_left "I don't think it's correct. Do you want to choose an another question?"
        menu:
            extend ''
            "Yes":
                call screen choose_question
            "No":
                jump question4

label question5:
    a_left "\"Which word contains 26 letters but only syllables?\""
    $answer = renpy.input("Your answer: (all in lowercase)", length = 8)
    $answer = answer.strip()

    if answer == "alphabet":
        a_left "Yes, I think so too! Let's move on!"
        $answ5 = True
        $answ_count += 1
        call screen choose_question
    else:
        a_left "I don't think it's correct. Do you want to choose an another question?"
        menu:
            extend ''
            "Yes":
                call screen choose_question
            "No":
                jump question5

label question6:
    a_left "\"If drop me, I'm sure to crack but if you give me a smile, I'll always smile back. What am I?\""
    $answer = renpy.input("Your answer: (all in lowercase)", length = 6)
    $answer = answer.strip()

    if answer == "mirror":
        a_left "Yes, I think so too! Let's move on!"
        $answ6 = True
        $answ_count += 1
        call screen choose_question
    else:
        a_left "I don't think it's correct. Do you want to choose an another question?"
        menu:
            extend ''
            "Yes":
                call screen choose_question
            "No":
                jump question6

label back_to_livingroom:
    hide screen solving_word_puzzle
    hide athena
    show screen UI
    call screen scene1
