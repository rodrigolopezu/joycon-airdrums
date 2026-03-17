# 🥁 AirDrums

Turn your Nintendo Joy-Con controllers into an air drum kit. 
Built to practice reading and transforming raw accelerometer 
data from hardware into real-time audio using Python.

> Proyecto de una tarde para practicar lectura de datos crudos 
> de hardware. Los Joy-Con envían su acelerómetro en tiempo real 
> y el programa detecta golpes, dirección del movimiento y botones 
> para disparar sonidos de batería.

## Requirements / Requisitos
- Windows
- Bluetooth
- Nintendo Joy-Con (L + R)

## Download / Descarga
[⬇️ AirDrums v1.0.0](https://drive.google.com/file/d/1YUIbxvtI-w2DK5D3P5j6vYmag3oA6W-N/view)

> Tested with original Nintendo Joy-Con. Generic controllers 
> may work if recognized as HID devices.

## Installation / Instalación

**Executable / Ejecutable**
1. Download and extract the `.zip`
2. Pair both Joy-Con via Bluetooth (hold the side button 
   ~3 seconds until LEDs flash, add one at a time)
3. Run `main.exe`

**From source / Desde el código**
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python main.py`

## Controls / Controles

| Action | Sound |
|---|---|
| Right Joy-Con swing down | Kick Drum |
| Right Joy-Con swing down + ZR | Snare |
| Left Joy-Con swing down | Cymbal |
| Left Joy-Con swing down + ZL | Hi-Hat |
| Button B | Exit |
