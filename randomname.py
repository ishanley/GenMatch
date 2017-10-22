from random import choice

ADJECTIVES = [
  'Abrasive', 'Brash', 'Callous', 'Daft', 'Eccentric', 'Fiesty', 'Golden',
  'Holy', 'Ignominious', 'Joltin', 'Killer', 'Luscious', 'Mushy', 'Nasty',
  'OldSchool', 'Pompous', 'Quiet', 'Rowdy', 'Sneaky', 'Tawdry',
  'Unique', 'Vivacious', 'Wicked', 'Xenophobic', 'Yawning', 'Zesty'
];

FIRST_NAMES = [
  'Anna', 'Bobby', 'Cameron', 'Danny', 'Emmett', 'Frida', 'Gracie', 'Hannah',
  'Isaac', 'Jenova', 'Kendra', 'Lando', 'Mufasa', 'Nate', 'Owen', 'Penny',
  'Quincy', 'Roddy', 'Samantha', 'Tammy', 'Ulysses', 'Victoria', 'Wendy',
  'Xander', 'Yolanda', 'Zelda'
];

LAST_NAMES = [
  'Anchorage', 'Berlin', 'Cucamonga', 'Davenport', 'Essex', 'Fresno',
  'Gunsight', 'Hanover', 'Indianapolis', 'Jamestown', 'Kane', 'Liberty',
  'Minneapolis', 'Nevis', 'Oakland', 'Portland', 'Quantico', 'Raleigh',
  'SaintPaul', 'Tulsa', 'Utica', 'Vail', 'Warsaw', 'XiaoJin', 'Yale',
  'Zimmerman'
];

def random_user():
    return '{} {} {}'.format(choice(ADJECTIVES), choice(FIRST_NAMES), choice(LAST_NAMES))