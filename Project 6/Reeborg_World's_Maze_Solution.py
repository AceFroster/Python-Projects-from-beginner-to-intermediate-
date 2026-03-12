def turn_right():
    for i in range(3):
        turn_left()

def jump():
    if right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_right()
            move()
    else:
        turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        if right_is_clear():
            turn_right()
            move()
        else:
            move()
