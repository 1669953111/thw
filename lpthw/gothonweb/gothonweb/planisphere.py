class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The gothons of planet percal #25 have invaded your ship and
destroyed your entire crew.  You're the last surviving
menber and your last mission is to get the neutron destruct
bomb from Weapons Armory, put it in bridge, and blow the
ship up after getting into an escape pod.
You're running down the contral corridor to the Weapons
Amory when a Gothon jumps out, red scaly skin, dark grimy
teeth, and evil clown constume flowing around his hate
filled body.  He's blocking the door to Armory and about to
pull a weapon to blast you.
""")


the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting
gas out. You grab the neutron bomb run as fast as you can
to the bridge where you must place it in the right spot.
You burst onto the Bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled thier
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")


laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the
academy. You tell the on Gothon joke you know: Lbhe
zgure vf fb sng, jura fur fvgf nebhaq gur ubhfr. The Gothon
stops, triesnot to laugh, then busts out laughing and can't
move.While he's laughing you run up and shoot him square in
head putting him down, then jump through the Weapon Armory
door.
""")


escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and the
Gothons put thier hands up and start to sweat. You inch 
backward to the door, open it, and thencarefully place the
bomb on the floor, pointing yourblaster at it. You then
jump back through the door, punch the close button and
blast the lock so theGothons can't get out. Now that the
bomb is placed you run to the escape pod to get off this
tin can.
""")


the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button.The pod 
escapes out into the void of space heading to the plant
bellow. As it flies to the planet, you look back and see
your ship impolde then explode likea bright star, taking
out the Gothon ship at the same time. You won!
""")


the_end_loser = Room("The End",
"""
You jump into pod 2 and hit the eject button. The pod 
escapes out into the void of space, then implodes as the
hull rupures, crushing your body into jam jelly.
""")


generic_death = Room("Death", "You died")



central_corridor.add_paths({
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'sowly place the bomb': escape_pod
})

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

START = 'central corridor'

def load_room(name):
    """
    There is a potential security problem here.Who gets to
    set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key