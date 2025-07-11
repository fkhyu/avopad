# Avolites Hackpad

This is AvoPad. Addition to Avolites lighting console used by me and other lighting designers in our school's AV team. It is used to save special cues and trigger them as needed.

### What does it consist of?

- 4-key macropad
- Designed to be plug-and-play with Avolites Titan software
- Compatible with KMK (CircuitPython) firmware
- 3D printed case
- Uses Seeed XIAO RP2040 as MCU

### Screenshots

<img width="883" height="653" alt="Screenshot 2025-07-11 at 16 22 48" src="https://![Uploading Screenshot 2025-07-11 at 16.23.43.png…]()
github.com/user-attachments/assets/9d2dbd34-54ea-4886-96da-e15d5ccb349e" />
<img width="510" height="522" alt="Screenshot 2025-07-11 at 16 24 10" src="https://github.com/user-attachments/assets/b6d98d96-1e65-4e9e-8c4c-1717d045b5da" />
<img width="762" height="508" alt="Screenshot 2025-07-11 at 16 24 00" src="https://github.com/user-attachments/assets/72f31261-8990-4e34-92bf-e0ca650b2408" />

### Bill of Materials

| Part                   | Qty   | Notes                                 |
| ---------------------- | ----- | ------------------------------------- |
| Seeed XIAO RP2040      | 1     | Main microcontroller                  |
| MX-Compatible Switches | 4     | Any 5-pin or 3-pin switches           |
| Resistors              | 1     | Pull-up (10kΩ) if needed              |
| TRRS Jack              | 1     | If chaining with other boards         |
| PCB (2-layer)          | 1     | 100mm x 50mm                          |
| 3D Printed Case        | 1 set | Top, Middle, Bottom (PLA recommended) |

### Firmware

The firmware sends HID keypresses that Avolites software interprets as hotkeys (e.g. custom cue triggers).

KMK and CircuitPython must be installed on the Seeed XIAO RP2040.
