from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

keyboard.keymap = [
    # Base Layer
    [KC.F1, KC.F2, KC.F3,
     KC.F4, KC.F5, KC.F6]
]

# You can customize the key codes above to match your Avolites cue hotkeys.

if __name__ == '__main__':
    keyboard.go()