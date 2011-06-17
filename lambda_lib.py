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
