# Avolites Hackpad

This is a compact macropad designed specifically for Avolites lighting consoles. It adds a set of custom cues or quick actions mapped to physical buttons. Ideal for programmers and lighting techs who want a tactile shortcut system for faster cue triggering.

## 🎯 Features

- 6-key macropad
- Designed to be plug-and-play with Avolites Titan software
- Compatible with KMK (CircuitPython) firmware
- 3D printed case
- Uses Seeed XIAO RP2040 as MCU

## 💡 Images

![Hackpad Front](images/front.png)
![Schematic](images/schematic.png)
![PCB](images/pcb.png)
![Exploded View](images/exploded.png)

## 🧾 Bill of Materials (BOM)

| Part               | Qty | Notes                          |
|--------------------|-----|---------------------------------|
| Seeed XIAO RP2040  | 1   | Main microcontroller            |
| MX-Compatible Switches | 6   | Any 5-pin or 3-pin switches    |
| Diodes (1N4148)    | 6   | For switch matrix              |
| Resistors          | 1   | Pull-up (10kΩ) if needed        |
| TRRS Jack (Optional) | 1 | If chaining with other boards   |
| PCB (2-layer)      | 1   | 100mm x 50mm                   |
| 3D Printed Case    | 1 set | Top, Middle, Bottom (PLA recommended) |

## 🛠️ Firmware Setup (KMK)

The firmware sends HID keypresses that Avolites software interprets as hotkeys (e.g. custom cue triggers).

KMK and CircuitPython must be installed on the Seeed XIAO RP2040.



