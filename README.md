# Δεῖμος
Deimos is a 40% split unibody ortholinear keyboard that uses the Raspberry Pi Pico for more accessibility, whose layout is similiar to the Lesovoz but has easier kitting. 

![image](https://raw.githubusercontent.com/tobiKaboom/deimos/refs/heads/main/deimos.JPG)

![keyboard-layout](https://github.com/user-attachments/assets/0276fe39-bd35-4090-a331-f685bd2e3748)

## Parts list
| Part          | Specifics     | Amount |
| ------------- | ------------- | ------ |
| Diodes        | DO-35 THT diodes (part number 1N4148)  | 38     |
| Switches      | MX standard switches  | 37     |
| Board         | Raspberry Pi Pico (classic board) | 1      |
| Buttons | 6mm micro-switches | 2 |
| LED | 5mm LED | 2 |
| Electrical tape | - | 1 |
| Resistor | 220 ohm | 1 |
## Tools list
| Tools         | Is it necessary? | Use |
| ------------- | ------------- | ------ |
| Soldering iron      | Yes  | Soldering |
| Solder wire| Yes | Soldering |
| Screwdriver | Yes | Screwing in standoffs |
| Tape | No, but reccomended | Holding components in place |
| Tweezers | No, but reccomended | Placing smaller parts |
| Fan or solder hood | No, but reccomended | Safety |
| Eye protection | No, but reccomended | Safety |

## Firmware 
Deimos currently runs on KMK. If you want to try and port it to QMK, ZMK or any other firmware you are welcome to do so.

## License
This work falls under the Creative Commons Attribution-ShareAlike 4.0 international license.
For more info, check LICENSE.md or https://creativecommons.org/licenses/by-sa/4.0/deed.en

## Issues
The right button is supposed to light up the LED, but it will burn it out. I am dumb. Use a resistor to avoid that.

## Disclaimer
This PCB has been fully tested and confirmed to work. The members of the PCB development team are however not liable if you end up with a non-functional pcb. Order at your own risk. Support will not be provided but pull requests will be reviewed and possibly accepted, although i do not know how that works.
