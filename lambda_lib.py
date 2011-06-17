import sys

LEFT  = "1"
RIGHT = "2"

cards = ["I", "zero", "succ", "dbl", "get",
         "put", "S", "K", "inc", "dec", "attack",
         "help", "copy", "revive", "zombie"
        ]

def handle_opponent():
    try:
        a = raw_input("")
        b = raw_input("")
        c = raw_input("")
        return (a,b,c)
    except:
        sys.exit(0)


def do_turn(type, card, slot):
    if card in cards:
        if type == LEFT:
            sys.stdout.write(LEFT + "\n")
            sys.stdout.write(card + "\n")
            sys.stdout.write(str(slot)+"\n")
        elif type == RIGHT:
            sys.stdout.write(RIGHT + "\n")
            sys.stdout.write(str(slot)+ "\n")
            sys.stdout.write(card + "\n")
        sys.stdout.flush()
    else:
        sys.stderr.write("attempted to play a card that doesn't exist\n")
        sys.exit(255)
    return handle_opponent()

def reset_to_identity(location):
    do_turn(LEFT, "put", location)

def accumulate(value, location):
    do_turn(RIGHT, "zero", location)
    i = 1
    do_turn(LEFT,  "succ", location)

    while (i * 2 <= value):
        do_turn(LEFT, "dbl", location)
        i *= 2

    while (i + 1 <= value):
        do_turn(LEFT, "succ", location)
        i += 1

def apply_to_slot_0(slot):
    do_turn(LEFT,  "K"     , slot)
    do_turn(LEFT,  "S"     , slot)
    do_turn(RIGHT, "get"   , slot)
    do_turn(RIGHT, "zero"  , slot)

def do_attack(amount, my_slot, their_slot):
    reset_to_identity(0)
    accumulate(my_slot, 0)
    do_turn(RIGHT, "attack", 1)
    apply_to_slot_0(1)
    reset_to_identity(0)
    accumulate(their_slot, 0)
    apply_to_slot_0(1)
    reset_to_identity(0)
    accumulate(amount, 0)
    apply_to_slot_0(1)
