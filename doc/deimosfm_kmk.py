#reading this code will kill half your neurons. proceed with caution.
print("its a me mario")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP5, board.GP4, board.GP6, board.GP7, board.GP8, board.GP9) #gp4 and gp5 are swapped, but that's correct!
keyboard.row_pins = (board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#very cooler names
___ = KC.TRNS
XXX = KC.NO

keyboard.keymap = [
                  [#base
                   KC.Q, KC.W, KC.E, KC.T, KC.Y,                 KC.R, KC.U, KC.I, KC.O, KC.P,\ #some keys are flipped but they need to be like that dont ask me why i didnt design this board (i did but i have no idea why it does that)
                   KC.A, KC.S, KC.D, KC.G, KC.H,                 KC.F, KC.J, KC.K, KC.L, KC.ENT,\
                   KC.Z, KC.X, KC.C, KC.B, KC.B,                 KC.V, KC.N, KC.M, KC.COMM, KC.DOT,\
                   KC.LCTRL, KC.LWIN, XXX, KC.MO(3), XXX,        KC.SPC, XXX, KC.RALT, KC.MO(1), KC.MO(2),\
                   ]
                  [#layer 1
                   KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,            KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,\
                   KC.GRV, KC.NUBS, XXX, XXX, KC.DEL,            XXX, XXX, XXX, KC.MINUS, KC.EQUAL,\
                   KC.LSHIFT, KC.F2, KC.F3, KC.F4, KC.F5,        KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,\
                   KC.LCTRL, KC.F1, XXX, KC.F11, XXX,            XXX, KC.F12, XXX, XXX, XXX,\
                   ]
                  [#yummy layer 2
                   KC.ESC, KC.UP, XXX, XXX, XXX,                 XXX, KC.PSCR, KC.SLCK, KC.PAUSE, KC.BSPC,\
                   KC.LEFT, KC.DOWN, KC.RIGHT, KC.END, KC.HOME,  XXX, KC.INS, KC.HOME, KC.PGUP, XXX,\
                   KC.LSHIFT, KC.F14, KC.F15, KC.F16, KC.F17,    XXX, KC.DEL, KC.END, KC.PGDOWN, XXX,\
                   KC.LCTRL, KC.F19, XXX, KC.F20, XXX,           XXX, XXX, XXX, XXX, XXX,\
                   ]
                  [#i dont want to code anymore but layer 3
                   XXX, XXX, XXX, XXX, XXX,                      XXX, XXX, KC.LBRC, KC.RBRC, KC.BSLS,\
                   XXX, XXX, XXX, XXX, XXX,                      XXX, XXX, XXX, KC.SCLN, KC.QUOTE,\
                   KC.LSHIFT, XXX, XXX, XXX, XXX,                XXX, XXX, XXX, XXX, KC.SLSH,\
                   KC.LCTRL, LGUI, XXX, XXX, XXX,                XXX, XXX, XXX, KC.RGUI, KC.RCTL,\
                   ]
]

    keyboard.go()

#this is simply the layout i like to use. to edit it, download it and to change the keymap refer to kmkfw.io and the multiple tutorials available on youtube.
