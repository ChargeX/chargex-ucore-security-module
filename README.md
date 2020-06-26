# chargex-ucore-security-module

## Introduction
This module was developed as POC for a message signing module that runs as a snap on **ubuntu core** on a raspberry pi. It uses a patch of the botan library(https://github.com/randombit/botan), pygame for the GUI, Wayland for the display interface, and Mir to manage the display. [Module may also be run on an Ubuntu desktop environment]

## Environment
### General
- Python 3
### Snap specific
- snapd >= 2.45.1 (sudo apt install snapd)
- snapcraft (sudo snap install snapcraft --classic)
- Mir-kiosk (sudo snap install mir-kiosk)

## Configuration
From project directory, execute the following:
```
$ ./configure
```

## Building the snap on raspberry pi running Ubuntu Server
``` 
$ snapcraft --destructive-mode
```
## Installing the snap on raspberry pi running Ubuntu Core
Transfer the file to the raspberry pi running Ubuntu core (For rpi installations only)
Execute the following from the path of the snap:
``` 
$ sudo snap install <snap_name>.snap --devmode
```
## Running the snap on raspberry pi running Ubuntu Core
``` 
$ sudo snap run <snap_name>
```
## Caveats
1. Snapcraft does not support cross-compiling for python snaps. This module requires a dedicated rpi running **ubuntu server** to build the snap.
2. Once built, the snap has to be moved to the rpi running **ubuntu core**
3. Certain fonts may not be usable in the extension of this module

## Resources
- https://ubuntu.com/tutorials/x11-kiosk#5-second-pass-snapping-your-device

![Demo](https://pasteboard.co/JeVqiXe.png) 

