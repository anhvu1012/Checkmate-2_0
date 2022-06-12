init python:
    def inventoryUpdate(st):
        pass
    def inventoryEvents(event, x, y, at):
        if event.type == renpy.pygame_sdl2.MOUSEMOTION:
            for item in inventory_sprites:
                # check position of mouse
                if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                    renpy.show_screen("inventoryItemMenu", item = item)
                    renpy.restart_interaction()
                    break
                else:
                    renpy.hide_screen("inventoryItemMenu")
                    renpy.restart_interaction()

    def environmentEvents(event, x, y, at):
        global char_talked
        global talked_with_Su
        global drawing_examined
        global wordpuzzle_taken
        #if current event is cursor being on item -> show hover image
        if event.type == renpy.pygame_sdl2.MOUSEMOTION:
            for item in environment_sprites:
                # check position of mouse
                if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                    #swap idle image of current item to hover image
                    t = Transform(child = item.hover_image) # resize to half, access hover image
                    # add this transform as a child to current item in for loop
                    item.set_child(t)
                    # redraw environment SM in order for this change to take place
                    environment_SM.redraw(0) # run once now

                # resetting image to idle if cursor not on item
                else:
                    t = Transform(child = item.idle_image)
                    item.set_child(t)
                    environment_SM.redraw(0)

        # if current event is item being clicked on
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            # down click -> loop through environment sprite to find item that got clicked on
            if event.button == 1:
                for item in environment_sprites:
                    if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                        # check current type and what to do with it
                        if item.type == "word-puzzle":
                            if char_talked == False:
                                characterSay(who = "Athena", what = ["Hmm, these look like some drawings from Su.", "Oh, I think there is something underneath as well." , "Let's pick it up and take a closer look in the inventory!"])
                                char_talked = True
                            else:
                                addToInventory(["word-puzzle"])
                                wordpuzzle_taken = True
                                char_talked = False

                        elif item.type == "drawing":
                            if char_talked == False and talked_with_Su == False:
                                renpy.show_screen("drawing")
                                characterSay(who = "Athena", what = ["It's a drawing.", "Su must have drawn it.", "Let's talk to her!"])
                                char_talked = True
                                drawing_examined = True
                            else:
                                renpy.show_screen("drawing")
                                characterSay(who = "Athena", what = ["It's a drawing of Su and her mother."])
                            char_talked = False

                        elif item.type == "flower-pot":
                            if char_talked == False:
                                renpy.show_screen("flower_pot")
                                characterSay(who = "Athena", what = ["I don't think there's something wrong about that flower pot."])
                                char_talked = True
                            char_talked = False

                        elif item.type == "sun-clock":
                            if char_talked == False:
                                renpy.show_screen("sun_clock")
                                characterSay(who = "Athena", what = ["It's a clock.", "What time is it actually?"])
                                char_talked = True
                            char_talked = False

                        elif item.type == "family-pic":
                            if char_talked == False:
                                renpy.show_screen("family_pic")
                                characterSay(who = "Athena", what = ["Look! It's Su's family.", "They look so happy."])
                                char_talked = True
                            char_talked = False

    def characterSay(who, what):
        # check for type of what parameter
        if isinstance(what, str): # if it's a text -> call screen
            renpy.call_screen("characterSay", who = who, what = what)
        elif isinstance(what, list): # if it's a list of obj -> show screen
            global dialogue # global variable contains characters and what they say
            dialogue = {"who" : who, "what" : what}
            renpy.show_screen("characterSay") # show screen can't take parameter, doesn't know what text to show
            renpy.restart_interaction()

    def inventoryArrows(button):
        pass

    def repositionInventoryItems():
        for i, item in enumerate(inventory_sprites): # enumerate to get index value
            if i == 0: # first item in inventory list is in the first slot
                item.y = inventory_first_slot_y
                inventory_sprites[-1].original_y = item.y

            else:
                # y iteration = y + 1 slot
                item.y = (inventory_first_slot_y + inventory_slot_size[0] * i) + (inventory_slot_pad_down * i)
                inventory_sprites[-1].original_y = item.y


    def addToInventory(items):
        for item in items:
            inventory_items.append(item)
            #check for correct state of item to add to list
            if item == "word-puzzle":
                item_image = Image("Inventory Items/inventory-word-puzzle-unsolved.png")
            else:
                item_image = Image("Inventory Items/inventory-{}.png".format(item))

            # adding the sprite as a reference to inventory sprites, using inventory SM to create sprite
            t = Transform(child = item_image, zoom = 0.5)
            inventory_sprites.append(inventory_SM.create(t))
            #same size as inventory slots
            inventory_sprites[-1].width = inventory_slot_size[0]
            inventory_sprites[-1].height = inventory_slot_size[1]
            inventory_sprites[-1].type = item
            inventory_sprites[-1].item_image = item_image
            #position this inventory item on screen
            inventory_sprites[-1].x = 1162
            inventory_sprites[-1].original_x = 1162 # item being dragged around, if released then back to its original position
            inventory_sprites[-1].original_y = 0

            # keep track of different states of an item
            if item == "word-puzzle":
                inventory_sprites[-1].state = "unsolved"
            else:
                inventory_sprites[-1].state = "default"

            for envitem in environment_sprites:
                # if an item is picked up and added to inventory, remove from screen
                if envitem.type == item:
                    removeEnvironmentItem(item = envitem)
                    break

            #to position item on x-axis when item being put in inventory, no gap between, added in correct slot
            repositionInventoryItems()

            # redraw SM and refresh screen to make sure changes are reflected on screen
            inventory_SM.redraw(0)
            environment_SM.redraw(0)
            renpy.restart_interaction()

    # item that was picked up will be remove from screen
    def removeEnvironmentItem(item):
        item.destroy() # SM deletes this item
        environment_sprites.pop(environment_sprites.index(item)) # remove item from sprites list by findind its correct index in the list
        environment_items.pop(environment_items.index(item.type)) # remove item from name list by finding its type (name) in the list

screen UI:
    zorder 1 # controls the order of showing screen (screen with greater number above screen with lesser number)
    #image "images/UI/inventory-icon-bg.png" xpos 1000 ypos 50 at half_size
    imagebutton auto "images/UI/inventory-icon-%s.png" action If(renpy.get_screen("inventory2")==None, true = Show("inventory2"), false= Hide("inventory2")) xpos 1142 ypos 5 at smaller_size

screen inventory2:
    image "images/UI/inventory-bg.png" xpos 1142 ypos 117
    image "images/UI/inventory_slot.png" xpos 1148 ypos 216
    ## up and down inventory buttons to reveal more items if gathered more items than available slots
    imagebutton idle If(inventory_ub_enabled == True, true= "images/UI/inventory-arrow-up-enabled-idle.png", false= "images/UI/inventory-arrow-up-disabled.png") hover If(inventory_ub_enabled == True, true= "images/UI/inventory-arrow-up-enabled-hover.png", false= "images/UI/inventory-arrow-up-disabled.png") action Function(inventoryArrows, button = "up") xpos 1167 ypos 140 at half_size
    imagebutton idle If(inventory_db_enabled == True, true= "images/UI/inventory-arrow-down-enabled-idle.png", false= "images/UI/inventory-arrow-down-disabled.png") hover If(inventory_db_enabled == True, true= "images/UI/inventory-arrow-down-enabled-hover.png", false= "images/UI/inventory-arrow-down-disabled.png") action Function(inventoryArrows, button = "down") xpos 1167 ypos 565 at half_size

    add inventory_SM

# overlay menu on top of inventory item when hovering mouse over it
# 1 button for inspect items
screen inventoryItemMenu(item):
    zorder 8
    imagebutton:
        # position wherever the item is
        xpos item.x - 6
        ypos item.y - 4
        idle "images/UI/inventory-item-inspect-idle.png"
        hover "images/UI/inventory-item-inspect-hover.png"
        action [Show("inspectItem", items = [item.type]), Hide("inventoryItemMenu")]

screen inspectItem(items):
    modal True
    zorder 4
    button:
        imagebutton auto "images/UI/close-button-%s.png" action Hide("inspectItem") xpos 910 ypos 92
        xfill True
        yfill True
        # check if one or more items and what to do
        action If(len(items) > 1, true = RemoveFromSet(items, items[0]), false = [If(len(dialogue) > 0, true= Show("characterSay"), false= NullAction())])
        #image "Items Pop Up/items-pop-up-bg.png" align(0.5, 0.5)

        python:
            item_name = ""
            for name in inventory_items_name:
                temp_name = name.replace(" ", "-") # format to find matches, actual name with spaces replaced with file name with dashes
                # now check if this name is matching current inspected item
                if temp_name.lower() == items[0]:
                    item_name = name
        text "{}".format(item_name) size 30 align(0.5, 0.15) # text with name to show on screen
        if items[0] == "word-puzzle":
            $wordpuzzle_state = inventory_sprites[inventory_items.index("word-puzzle")].state # looking for index of word puzzle inside of inventory and pass it to inv sprites
            frame:
                align (0.5, 0.75)
                textbutton "Click here if you want to solve this world puzzle" action [Hide("inspectItem"), Hide("UI"), Hide("inventory2"), Jump("solve_word_puzzle")]
            image "Items Pop Up/{}-{}-pop-up.png".format("word-puzzle", wordpuzzle_state) align (0.5, 0.4) at half_size
        else:
            image "Items Pop Up/{}-pop-up.png".format(items[0]) align (0.5, 0.4) at half_size

screen characterSay(who = None, what = None):
    modal True
    zorder 6 #(screen with greater number above screen with lesser number)
    style_prefix "say"

    window:
        id "window"

        window:
            padding (20, 20)
            id "namebox"
            style "namebox"
            #if who is None -> grab name from global dialogue
            if who is not None:
                text who id "who"
            else:
                text dialogue["who"]

        # if what is None -> grab character say from global dialogue
        if what is not None:
            text what id "what" xpos 0.25 ypos 0.4 xanchor 0.0
        else:
            text dialogue["what"][0] xpos 0.25 ypos 0.4 xanchor 0.0

    button: # fill up the entire screen
        xfill True
        yfill True
        # if what is None -> dialogues come from global dialogue
        if what is None:
            # if more than one text is in dialogue list, remove the first in the list and continue showing next text
            # if only one text in the list down, hide characterSay screen completely then reset dialogue list
            action If(len(dialogue["what"]) > 1, true = RemoveFromSet(dialogue["what"], dialogue["what"][0]), false = [Hide("characterSay"), SetVariable("dialogue", {})])
        else:
            action Return(True)


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen drawing:
    modal True
    zorder 4
    imagebutton auto "images/UI/close-button-%s.png" action [Hide("drawing"), Show("Su_appear")] xpos 914 ypos 95
    text "Drawing" size 30 align(0.5, 0.20)
    image "Items Pop Up/drawing-pop-up.png" align (0.5, 0.4) at half_size
    # if talked_with_Su == False:
        # textbutton "Go and talk with Su" action Jump("talk_with_Su") align (0.5, 0.75)
    # else:
        # pass

screen family_pic:
    modal True
    zorder 4
    imagebutton auto "images/UI/close-button-%s.png" action Hide("family_pic") xpos 917 ypos 95
    text "A family photo" size 30 align(0.5, 0.20)
    image "Items Pop Up/family-pic-pop-up.png" align (0.5, 0.4) at half_size

screen flower_pot:
    modal True
    zorder 4
    imagebutton auto "images/UI/close-button-%s.png" action Hide("flower_pot") xpos 917 ypos 95
    text "A flower pot" size 30 align(0.5, 0.20)
    image "Items Pop Up/flower-pot-pop-up.png" align (0.5, 0.4) at half_size

screen sun_clock:
    modal True
    zorder 4
    imagebutton auto "images/UI/close-button-%s.png" action Hide("sun_clock") xpos 917 ypos 95
    text "A sun clock" size 30 align(0.5, 0.20)
    image "Items Pop Up/sun-clock-pop-up.png" align (0.5, 0.4) at half_size

screen Su_appear:
    if drawing_examined == True and talked_with_Su == False:
        imagebutton auto "images/stickman_%s.png" action Jump("talk_with_Su") xpos 200 ypos 300

screen scene1:
    add environment_SM
    frame:
        #background "#FFFFFF40"
        xpos 5 ypos 5
        hbox:
            textbutton "Leave" action Jump("leave")

label setupScene1:

    scene scene-livingroom-bg
    # filling environment items list, pick up or interact
    $environment_items = ["word-puzzle", "drawing", "flower-pot", "family-pic", "sun-clock"]

    #iterate through each of the items to create sprite for them
    python:
        for item in environment_items:

            #create 2 images for sprite to use, idle and hover images
            # {} as placeholder for current item
            # format string to replace placeholder
            idle_image = Image("images/Environment Items/{}-idle.png".format(item))
            hover_image = Image("images/Environment Items/{}-hover.png".format(item))

            #sprite obj use idle images as its child
            #transform size to half because images too large
            t = Transform(child = idle_image)
            # append reference to sprite obj into envi sprite list
            environment_sprites.append(environment_SM.create(t))

            #create custom attributes with values for these sprites
            #last item of the list
            environment_sprites[-1].type = item
            environment_sprites[-1].idle_image = idle_image
            environment_sprites[-1].hover_image = hover_image

            #images different sizes, check for item type then add its image size and position on screen
            if item == "word-puzzle":
                environment_sprites[-1].width = 34
                environment_sprites[-1].height = 18
                environment_sprites[-1].x = 741
                environment_sprites[-1].y = 445

            elif item == "drawing":
                environment_sprites[-1].width = 41
                environment_sprites[-1].height = 27
                environment_sprites[-1].x = 737
                environment_sprites[-1].y = 452

            elif item == "flower-pot":
                environment_sprites[-1].width = 36
                environment_sprites[-1].height = 70
                environment_sprites[-1].x = 671
                environment_sprites[-1].y = 405

            elif item == "family-pic":
                environment_sprites[-1].width = 47
                environment_sprites[-1].height = 58
                environment_sprites[-1].x = 84
                environment_sprites[-1].y = 407

            elif item == "sun-clock":
                environment_sprites[-1].width = 60
                environment_sprites[-1].height = 102
                environment_sprites[-1].x = 272
                environment_sprites[-1].y = 100

    #show created sprites on another screen
    call screen scene1

transform half_size:
    zoom 0.5

transform smaller_size:
    zoom 0.4
