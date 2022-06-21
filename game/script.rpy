# The script of the game goes in this file.

default grey = 0
default black = 0
default white = 0
default athena_friendliness = 0
default su_friendliness = 0
default title = None
default non_b = False

# In Game musics
define op = "audio/myuu-unspoken.mp3"
define teashop = "audio/Circus Marcus_Aux_puces_n4_Noctambule.mp3"
define investigation_scene = "audio/myuu_God_Rest_Ye_Merry_Gentlemen_Dark_Piano_Version.mp3"

# The game starts here.
label opening_scene:
    play music op
    scene bg black with fade
    centered "\"Do you know the principle of sufficient reason?\"" with dissolve
    centered "\"Leibniz states that everything must have a reason or a cause.\"" with dissolve

    play sound "audio/chess_sound_longer.mp3"
    show chess board with fade
    $ renpy.pause(3)
    hide chess board with fade
    centered "\"So I wonder why I have this unshakeable obsession.\"" with dissolve
    centered "\"Do you believe in free will?\"" with dissolve
    play sound "audio/chess_sound_longer.mp3"

    window hide
    show mc eyes with fade
    $ renpy.pause(3)
    hide mc eyes with fade
    play sound "audio/chess_sound_longer.mp3"
    centered "\"May God truly exist then is it all God’s will?\"" with dissolve

    show anta eyes with fade
    $ renpy.pause(3)
    hide anta eyes with fade
    play sound "audio/chess_sound_longer.mp3"
    centered "\"May God be nothing but our conviction then shall it be my will?\"" with dissolve

    centered "\"Oh dear little Arborvitae..\"" with dissolve
    scene bg black
    centered "\"Would you know the answer?\"" with dissolve

    "They all kept rambling the same things to torture my little brain"
    "Yet I still tagged along with them"
    "In hopes of discovering the truth if I witness their story 'till the very end"
    stop music fadeout 3.0
    pause 1.5
    jump scene_red_district

label scene_red_district:
    show text "{=chap}Chapter I{/=chap}"
    with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text

    show crow with fade
    play sound "audio/crow.mp3"
    $ renpy.pause(2.5)
    scene red district with fade
    "Another day in Red District again"
    "As it should always be, the street’s crowded with lecherous customers or people who’ve lost their sense of reality."
    "Oh my..."
    "What a lovely child!"
    "It isn’t abnormal for a little girl to appear in this kind of place, and it’s also never safe wandering around here."
    "Oh, the direction to which she's heading...."
    "Could it be that eccentric shop?"
    "The shop’s name itself is quite boring. I mean… Who would name a tea shop “Tea Shop”?"
    "And why a tea shop but not a bar or something that sells alcohol? Would it be more suitable in Red District?"
    "Honestly I’ve never seen anyone visit the shop just for a cup of tea."
    jump scene_teashop

label scene_teashop:
    show black with dissolve
    play sound "audio/bellring.mp3"
    $ renpy.pause(1.6, hard=True)
    scene tea shop
    play music teashop volume 0.3 fadein 2.0
    show athena neutral at right
    unk1 "Welcome to the Tea Shop! If you’re here for the tea then we don’t sell them."
    show su neutral at left
    kid "Ah oh, sorry Miss, I come here for another reason."
    # show athena smile at right (maybe)
    athena "Then you must be looking for the owner?"
    kid "Y-yes! They told me that I can find help here."
    hide athena
    hide su
    unk2 "It depends on which kind of help you want from me, little one."

    show su surprise at left
    kid "Ah!"

    # show mc neutral at right
    unk2"Oh my, did I startle you?"

    show su quest at left
    kid "W-who are you? Sir... umh, Miss?"
    show su neutral at left

    label choice_gender:
        menu:
            extend ''
            "Sir":
                 $ title = "Sir"
                 unk2 "It's Sir."
                 jump after_choice_gender
            "Miss":
                 $ title = "Miss"
                 unk2 "It's Miss."
                 jump after_choice_gender
            "Either way or none of that. I'm nonbinary":
                 $ non_b = True
                 unk2 "Either Sir or Miss or none of them."
                 jump after_choice_gender

label after_choice_gender:
    unk2 "However, to make it less complicating for you, just call me by my name."

    show su quest at left
    kid "O-kay! But… Uhm, what’s your name?"
    show su neutral at left
    unk2 "Ah right..."

    $ mc_name = renpy.input("What's your name?", length = 10)
    $ mc_name = mc_name.strip()

    if non_b == True:
        $ title = mc_name

    mc "[mc_name], I'm the owner of this shop."
    mc "Shall we have a seat first and talk later?"

    kid "Yes, [mc_name]!"

    mc "Shouldn't you tell me who you are now?"
    kid "Ah! My name is Sully Cornwell, but my dad usually calls me Su."
    # hide mc
    # play sound tea spoon
    show athena neutral at right
    athena "[mc_name], here is your tea."
    show athena smile at right
    athena "Su, would you like to drink something too?"

    show su neutral at left
    su "No Miss, thank you very much."

    athena "Don’t call me \"Miss\", I’m Athena."
    hide athena
    # show mc neutral at right
    mc "You aren’t a resident of Red District, are you?"

    show su surprise at left
    su "Wow, how could you tell?"
    show su neutral at left
    mc "It’s just a guess but with such a reaction of yours..."
    # show mc smile at right
    mc "I'm not wrong after all."

    show su sad at left
    su "So you trick me? That’s unfair!"
    # show mc smile at right
    show su neutral at left
    mc "If you say so."
    mc "But how lucky it may seem, actually I wasn’t blindly guessing at all."

    show su quest at left
    su "Really? How come?"

    # scene mc drinking tea at right
    show su neutral at left
    mc "There are three social classes in this district, the owners and the prostitutes."
    mc "And the third one, Master of Red District, you’re probably not him so we only have two possibilities left."
    mc "But you’re pretty young, too young to become an owner which means you must be otherwise."
    show su quest at left
    su "Is it the prostitutes you’ve spoken about? Who are they?"
    show su neutral at left
    mc "Have you seen those beautiful men and women displaying themself behind the bars?"

    show su sad at left
    su "Yes, did they do something bad so that they’re being locked up? I feel bad for them."

    # scene mc smirk at right
    mc "Humph, \"did something bad\" you say. Well... they're all prostitutes who sell their bodies to survive."

    show su surprise at left
    su "I don’t quite get it but I am definitely not a prostitute either!"

    mc "Of course you aren’t but I am hypothesizing that you were to prove that you aren’t."

    show su quest at left
    su "H-huh?"

    # show mc smile at right
    mc "Oh my, it isn't my intention to confuse you more."

    show su neutral at left
    su "Haha, it's ok."
    show su quest at left
    su "So how do you know that I'm not?"
    show su neutral at left
    mc "Well, let me see.."
    mc "Your skin is soft and nice with no traces of being abused."
    mc "You also have an exceptionally cute face."
    mc "With all those traits it should be a high chance that you attract a lot of pedophiles."
    show su quest at left
    su "What does pedophiles mean?"

    mc "It’s those who want to fu..."
    hide su
    # sound hit on the head
    show athena frown at left
    a_left "Stop right there! You don’t think it’s inappropriate to talk about adult stuff in front of an innocent child?"

    mc "Huh? But I thought ignorance isn’t the best way to protect a child?"

    a_left "Yes, even though... could you be more considerate?"

    # show mc smile at right
    mc "Sure."
    hide athena

    label choice_explain:
        menu:
            extend ''
            "Continue explaining but in a subtle way":
                $ grey += 1
                jump explain1
            "Still explain directly with other choices of words":
                $ black += 1
                jump explain2
            "Change the topic":
                $ white += 1
                $ athena_friendliness += 1
                jump c_t

        label explain1:
            # show mc neutral at right
            mc "Well, they’re adults who have ill-intention towards children."

            show athena neutral at left
            a_left "So if you meet someone who looks super suspicious, just try to avoid them at any cost and call for help as soon as you can."
            hide athena
            show su neutral at left
            su "Uhm, uhm, I got it!"

            mc "Should I continue?"

            su "Yes, please!"
            hide su
            show athena surprise at left
            a_left "You still want to listen to all of that? What a weird kid."
            hide athena
            mc "Alright then..."
            jump explain_all

        label explain2:
            # show mc neutral at right
            mc "To put it simply, they are adults who’re sexually attracted towards prepubescent children."
            hide su
            show athena frown at left
            a_left "You… That doesn’t make things better!"

            # show mc surprise at right
            mc "Huh? Why? I didn’t use those \"f\" words or \"paedophile\" as you wish."

            a_left "Ughhh... That's even not human language!"

            mc "Heh? Is that so?"
            #show mc smile at right
            mc "But it’s all written in books, I’ve just literally repeated what I read."
            hide athena
            show su neutral at left
            su "Hahah, it's ok, I understand what [mc_name]'s saying, though."
            hide su
            show athena surprise at left
            a_left "You do?"
            hide athena
            show su neutral at left
            su "Ah... uhm, at least half of it?"
            su "But don't mind me, please continue, I'm really curious what comes next."
            # show mc neutral at right
            mc "You sure?"
            mc "Alright then..."
            hide su
            jump explain_all

        label c_t:
            # show mc neutral at right
            mc "Nevermind."
            jump about_dad

    label explain_all:
        # show mc neutral at right
        mc "As I said, you should have a lot of customers."
        mc "No way would your owner let such fine goods run around without any supervisors."
        mc "Furthermore, your way of speaking is too well mannered."
        mc "You could come from either a well-educated \"normal\" family or a high-quality brothel."
        mc "If it was the second case, it'd be more illogical to see you being here alone."
        mc "But for the counter-argument..."
        mc "You might be a deserter, somehow managing to come here asking for help."

        if black < 2:
            mc "Or you may be abandoned by your owner because..."
            mc "Uhm... reasons."
        else:
            mc "Or you may be abandoned by your owner because either you have sexually transmitted disease or you’re incredibly bad at serving your customers."

        show athena frown at left
        a_left "Ok, that's enough."
        a_left "This little girl seems confused as hell and what’s the point in explaining things to a person who’s already at a loss?"

        mc "Ehmm... It’s because she asked me in the first place?"
        hide athena
        show su neutral at left
        su "Haha, but it’s truly fun to listen to you, [title]."

        # show mc smile at right
        mc "Be my guest."

        jump about_dad

label about_dad:
    # show mc neutral at right
    mc "By the way, should I remind you about your purpose being here?"
    show su sad at left
    su "Oh right, I need you to find my dad! It’s been weeks and I'm worried about him."
    hide su
    show athena neutral at left
    a_left "You don’t seem to be in an emergency."
    hide athena
    mc "So I suppose that it's normal for him to be absent from home for such a long time?"
    show su neutral at left
    su "Yes, sometimes my dad stays overnight at his workplace."

    mc "Oh, what is his job?"

    su "He’s a professor in AASO."
    hide su
    show athena surprise at left
    a_left "AASO? Is it that famous academy in the Old? It’s pretty far from here, isn’t it?"

    mc "Yeah."

    show athena neutral at left
    a_left "So he must be very talented right?"

    mc "If he didn't bribe for his current position then sure he is."

    a_left "Yeah."

    mc "Su, have you checked out his office yet?"
    hide athena
    show su sad at left
    su "I did but I couldn't find him anywhere."
    su "And whenever I try to make a phone call, there's no answer."

    mc "I see... in which major does he specialize then?"

    show su quest at left
    su "Hmmm..."
    show su neutral at left
    su "Ah yeah, I think it’s something about medicine!"

    mc "Could you remember when and where was the last time you saw him?"

    su "It was in the Sunday morning at our apartment and he said that he had some business at the academy."
    #hide mc
    show athena neutral at right
    athena "Why don't you report this to the police? It'd be better than coming here all the way alone."

    su "Vincent said that I shouldn't or else my dad and I would be in danger and..."
    hide athena
    #show mc neutral at right
    mc "Vicent you say... Who's that?"

    show su neutral at left
    su "Oh, he's my dad's friend."

    mc "Do you know how close he is to your father?"

    su "I don't know, it's my first time meeting him."
    #hide mc
    show athena surprise at right
    athena "Your what?!"
    show su surprise at left
    su "My first time!"
    su "Oh right! He's also the one leading me to this tea shop."
    show su neutral at left
    su "He said its owner could help me find my dad."

    show athena frown at right
    athena "Young lady, you know nothing about him but still follow him eagerly?"

    su "But he is really nice and gentle!"

    athena "Oh fuck me! I'm speechless, say something [mc_name]!"

    label choice_say:
        menu:
            extend ''
            "You are stupid.":
                $ black += 1
                jump choice_say_1
            "You are a \"masterpiece\".":
                $ grey += 1
                jump choice_say_2
            "At least she's still alive.":
                $ white += 1
                jump choice_say_3

        label choice_say_1:
            # hide athena
            # show mc neutral at right
            mc "For such a long time I haven't met anyone as stupid as you."
            hide su
            show athena frown at right
            athena "[mc_name]! That won't help at all!"
            hide athena
            jump after_choice_say

        label choice_say_2:
            # hide athena
            # show mc smile at right
            mc "Wow.. Su, you're indeed a masterpiece, trusting strangers like breathing air!"
            hide su
            show athena frown at right
            athena "Wow..[mc_name], with that annoying attidute, why're you still breathing?"

            mc "It's God's wills I suppose."
            hide athena
            jump after_choice_say

        label choice_say_3:
            # hide athena
            # show mc smile at right
            mc "Hahah, don't be too harsh, Athena. At least she's still alive."

            jump after_choice_say

label after_choice_say:
    #hide mc
    show athena frown at right
    athena "Whatever, why do I even count on you in the first place."
    show athena neutral at right
    athena "Listen carefully Su, you shouldn’t trust anyone but yourself."
    show athena smile at right
    athena "But you can trust us for now!"
    show su neutral at left
    su "Yes, Athena!"
    hide athena
    hide su
    # show mc neutral at right
    mc "Done with your life lesson?"
    mc "Alright then..."

    menu:
        extend ''
        "What does Vincent look like?":
            $ grey += 1
            jump choice_last_question_1
        "How much do you pay us?":
            $ black += 1
            jump choice_last_question_2
        "Let's begin to look for your dad.":
            $ white += 1
            jump choice_last_question_3

label choice_last_question_1:
    mc "Can you describe that \"Vincent\" you’ve mentioned earlier?"
    show su neutral at left
    su "Oh? I’ve never seen his full face because he always puts on his mask. But... hmm... he has azure eyes and black hair."

    mc "Do you happen to notice his scent as well?"

    show su quest at left
    su "His scent?"
    show su neutral at left
    su "He smells pretty... woody and warm? Hope that makes sense to you."

    mc "Did he... leave any message to you?"
    show su surprise at left
    su "Right, now you mention that... when we parted, he told me to give you this if you ask about him."
    hide su

    show letter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide letter with dissolve

    $ addToInventory(["letter-from-vincent"])
    $ got_letter = True

    hide su
    show athena surprise at left
    a_left "Is it him?"
    hide athena

    # show player smirked at right

    mc "Yes, it’s the black king himself."
    jump end_chap_1

label choice_last_question_2:
    mc "How much are you going to pay for our service?"

    show su quest at left
    su "P-pardon?"

    mc "Oh, are you thinking this shop is a charity or something?"

    hide su
    show athena frown at left
    a_left "[mc_name], she’s just a child, could we just help her for free?"

    menu:
        extend ''
        "Still ask for payment":
            jump payment
        "Let it go":
            $ athena_friendliness += 1
            jump let_it_go

    label payment:
        hide athena
        mc "A child or not, that’s irrelevant."
        mc "Her father works as a professor in AASO, he’ll be able to pay us on behalf of his daughter."

        show su surprise at left
        su "Please, I want to see my dad! I’m willing to pay you with all I have!"
        play sound "audio/metal-coin-sound-effect.mp3"
        $ renpy.pause(1.3, hard=True)

        mc "That’s enough for now, we’ll take the rest once we find your father."
        hide su
        show athena neutral at left
        a_left "Such a simple reason and she goes so far for that..."
        mc "Her choices and reasons are none of our business so don’t be bothered by that, Athena."
        hide athena
        jump end_chap_1

    label let_it_go:
        mc "..."
        mc "Fine, I will let it pass this time."
        show su neutral at left
        su "Yay, thank you very much, [title]!"
        hide su
        jump end_chap_1

label choice_last_question_3:
    mc "Well then..."
    mc "Let's solve this missing case, shall we?"
    jump end_chap_1

label end_chap_1:
    show text "{=chap}End chapter I.{/=chap}"
    with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve
    stop music fadeout 1.5
    jump scene_before_investigation

# Anfang Kap. 2
label scene_before_investigation:
    scene black
    show tea shop with dissolve
    show text "{=chap}Chapter II{/=chap}"
    with dissolve
    $ renpy.pause(2.5, hard=True)
    play music investigation_scene volume 0.3 fadein 2.0
    hide text with dissolve
    show athena neutral at left
    a_left "Where's your little suitcase?"
    mc "Why do you ask?"
    show athena frown at left
    a_left "You don't take it with you? What if you find something in that house? Where would you put it huh?"
    if got_letter == True:
        mc "You're at nagging again."
        a_left "So what?"
        a_left "I've also put the letter from earlier in it. Here, take it!"
    else:
        mc "You're at nagging again. Can you just pass me the suitcase?"
        a_left "Gosh.. Here, take it!"
    hide athena
    show screen UI
    $ renpy.pause(1.5, hard=True)
    show athena frown at left
    a_left "Now go! Su is waiting!"
    hide athena
    hide tea shop with dissolve
    $ renpy.pause(1.5, hard=True)
    show su neutral at left
    su "We've arrived. Just give me a moment. I'm going to open the door."
    play sound "audio/stuck-key-38228.mp3" volume 1.0
    $ renpy.pause(1, hard=True)
    su "There! Welcome in!"
    su "You can look around all you want, [title]!"

    jump setupScene1

label choice_what_to_talk_with_Su:
    hide screen UI
    hide screen inventory2
    show su neutral at left
    if family_pic_examined == False and drawing_examined == False:
        su "Have you found something?"
        menu:
            extend ''
            "Not yet.":
                jump continue_investigate
            "I want to leave this room.":
                jump want_to_leave
    else:
        su "What do you want to talk about?"
        menu:
            extend ''
            "About the family picture..." if family_pic_examined == True and talked_with_Su_about_famPic == False:
                hide su
                jump talk_about_famPic
            "About the drawing on the table..." if drawing_examined == True and talked_with_Su_about_drawing == False:
                hide su
                jump talk_about_drawing
            "Nothing":
                hide su
                show screen UI
                call screen scene1
            "I want to leave this room.":
                jump want_to_leave

label continue_investigate:
    su "Come to me again if you find something!"
    hide su
    show screen UI
    call screen scene1

label talk_about_drawing:
    $talked_with_Su_about_drawing = True

    if wordpuzzle_taken == True:
        show livingroom
        $livingroom_on_screen = True
    else:
        show livingroom_with_wp
        $livingroom_with_wp_on_screen = True

    show athena neutral at left
    a_left "”Mom and Lu”? That reminds me, you’ve never mentioned your mother, haven’t you?"
    show su sad at right
    su "Ah... She left us and went to heaven 2 years ago."
    a_left "Oh... I'm so sorry kid..."
    show su neutral at right
    su "It’s ok... I just hope she’ll have a great time up there."
    su "..."
    a_left "What's wrong?"
    show su sad at right
    su "Dad used to love her so much. He’ll do anything for mom. When she was so sick and couldn’t get out of bed. He quitted his job for years to stay home and took care of her the whole time."
    su "But I don’t know why after mom’s death, dad burnt all the stuff that relates to mom, he also forbids us to talk about or mention her ever again."
    su "And there’s one time when we tried to make a portrait of mom as his birthday gift, he suddenly got super upset and yelled at us."
    show athena frown at left
    a_left "What short-tempered guys!"
    su "No don’t say that! It’s our fault for not listening to him! He must hate mom so much..."
    su "But we just tried to make him love mom again... We shouldn’t have done that, right?"
    show athena sad at left
    a_left "Oh Su..."
    hide athena
    hide su


    menu:
        extend ''
        "Remain silent":
            jump return_investigation
        "Say something":
            menu:
                extend ''
                "He must have his reasons":
                    $ grey += 1
                    $ su_friendliness += 1
                    jump his_reasons
                "Don’t meddle in others' business":
                    $ black += 1
                    jump others_business
                "You did the right thing but chose the wrong time":
                    $ white += 1
                    $ su_friendliness =+ 1
                    $ athena_friendliness += 1
                    jump wrong_time

    label his_reasons:
        mc "There must be some reasons behind one’s action. Ask him when we find him, okey?"
        show su neutral at left
        su "Uhm, you’re right! Let’s find dad first!"
        hide su
        jump return_investigation

    label others_business:
        mc "It’s his own problem and you shouldn’t meddle in like that, little girl."
        mc "Being pushy just makes him more on edge and may feel annoying."
        show athena frown at left
        a_left "Can something nice come from your mouth?"
        mc "I thought I was being nice enough?"
        a_left "Try harder."
        hide athena
        mc "Well... just let him have some space, when he feels ready to talk, then he’ll talk."
        show su sad at left
        su "Alright..."
        hide su
        jump return_investigation

    label wrong_time:
        mc "You acted out of noble causes and there’s nothing wrong about that."
        mc "But maybe you should consider when would be the right moment to express your intention, little girl."
        show athena neutral at left
        a_left "So it seems he can’t bear the fact that his wife is gone. It hurts him so much that he tries to avoid everything related to her?"
        mc "The man has his own way to deal with loss and pain. Time is what he needs."
        a_left "Even so he has no right to make the child suffer with his issues. A good father won’t do that. It isn’t only him who is sad here, is it?"
        mc "How can you ask one to forget its own pain so as to recognize the other’s?"
        a_left "You can’t but you can share the pain and surpass it together!"
        a_left "Would it be better than endure it in loneliness?" # with mc_name
        mc "That... sounds nice, indeed."
        hide athena
        show su sad at left
        su "I don’t want to leave dad alone!"
        hide su
        $renpy.pause(1.5, hard=True)
        jump return_investigation

    label return_investigation:
        $ renpy.pause(0.5, hard=True)
        if talked_with_Su_about_famPic == False:
            show athena neutral at right
            a_left "So who is Lu standing next to your mom? Your sister?"
            show su neutral at left
            su "Yes, she is my younger twin, we also have a photo just the two of us."
            su "Over there, on the TV cabinet!"
            hide athena
            hide su
        else:
            show athena sad at left
            a_left "Oh Lu, poor child, I hope she’ll get better soon"
            hide athena

        if livingroom_on_screen == True:
            hide livingroom
        if livingroom_with_wp_on_screen == True:
            hide livingroom_with_wp

        show screen UI
        call screen scene1

label talk_about_famPic:
    if wordpuzzle_taken == True:
        show livingroom
        $livingroom_on_screen = True
    else:
        show livingroom_with_wp
        $livingroom_with_wp_on_screen = True

    $talked_with_Su_about_famPic = True

    show su neutral at left
    su "We took it on a summer vacation years ago. It was so fun!"
    show athena neutral at right
    athena "The little girl on the right just looks exactly like you."
    su "She's my twin sister. Her name is Lunally."
    athena "Where is she right now?"
    su "She’s sickbed and in the hospital. I haven’t visited her for a while since dad doesn’t allow me."
    athena "Huh? Why so?"
    su "He said Lu is under special treatment. I can’t come to visit her till the treatment is over."
    hide su
    hide athena
    show screen UI

    if livingroom_on_screen == True:
        hide livingroom
    if livingroom_with_wp_on_screen == True:
        hide livingroom_with_wp

    call screen scene1

label solve_word_puzzle:
    hide screen Su_appear
    hide screen Su_appear2
    show screen solving_word_puzzle
    show athena neutral at left
    a_left "It will take some time to solve this."
    a_left "I know for a fact you hate it when you have to read such small handwriting"
    a_left "Just pick a number and I'll read its question out for you."
    a_left "And when you think you know the keyword, just give me a sign by clicking on it."
    call screen choose_question

label wp_solved:
    $ wordpuzzle_SOLVED = True
    $ addToInventory(["word-puzzle-solved"])
    hide screen solving_word_puzzle
    show screen wp_solved
    a_left "Now that you have solved the word puzzle, should we go somewhere else or do you still want to look around more?"
    menu:
        extend ''
        "Go to the next location":
            jump leave
        "Stay here":
            hide screen wp_solved
            hide athena
            show screen UI
            call screen scene1

# label ask_about_wordpuzzle:
#     show su surprise
#     su "Oh yeah, you found a word puzzle right?"
#     su "Have you solved it yet?"
#     menu:
#         extend ''
#         ""

label start:

    # remove rollback function
    $config.rollback_enabled = False
    #$quick_menu = False

    # SpriteManager (trigger when SM updates, trigger when event happens)
    $environment_SM = SpriteManager(event = environmentEvents)
    $inventory_SM = SpriteManager(update = inventoryUpdate, event = inventoryEvents)

    # 2 Lists, keep references to sprites, help access the sprites to make changes to them
    $environment_sprites = []
    $inventory_sprites = []

    # lists for all file name of images
    $environment_items = []
    $inventory_items = []

    # lists for all items name (in game)
    $environment_items_name = []
    $inventory_items_name = ["Word Puzzle Unsolved", "Word Puzzle Solved", "Letter From Vincent", "Empty Piece Of Paper"]

    # keep track of what current scene we are in
    $current_scene = "scene1"

    # right and left inventory buttons to reveal more items if gathered more items than available slots
    $inventory_ub_enabled = False
    $inventory_db_enabled = False

    # Global attributes (width, height), padding between the slots, position of first slot in inventory
    $inventory_slot_size = (110, 92)
    $inventory_slot_pad_down = 2
    $inventory_first_slot_y = 228

    $dialogue = {}
    $char_talked = False
    $talked_with_Su_about_drawing = False
    $talked_with_Su_about_famPic = False
    $talked_with_Su = False
    $clock_examined = False
    $drawing_examined = False
    $family_pic_examined = False
    $wordpuzzle_taken = False
    $wordpuzzle_SOLVED = False
    $flower_pot_examined = False
    $got_letter = False

    $livingroom_on_screen = False
    $livingroom_with_wp_on_screen = False

    $answ1 = False
    $answ2 = False
    $answ3 = False
    $answ4 = False
    $answ5 = False
    $answ6 = False
    $answ_count = 0
    $keyword = False

    jump opening_scene

label want_to_leave:
    if clock_examined == True and drawing_examined == True and family_pic_examined == True and wordpuzzle_taken == True and flower_pot_examined == True:
        show su surprise at left
        su "You are done with everything here? How fast!"
        show su neutral at left
        su "Then I will show you my father's study room. Follow me!"
        hide su
        jump leave
    else:
        show su surprise at left
        su "You haven't looked at everything... Are you sure you want to leave?"
        menu:
            extend ''
            "Yes":
                hide su
                jump leave
            "I changed my mind.":
                jump continue_investigate

label leave:
    show text "{=chap}End chapter II.{/=chap}"
    with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve
    stop music fadeout 3.0
    return
