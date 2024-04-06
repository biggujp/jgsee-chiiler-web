# jgsee-chiiler-webserver

This repository contains the code for control Chiller of Emerson. but assembled by RITCHAI

I do deployed on ESP32 microcontrollers used by Micropython.

## 📂 Directory Structure
    .
    ├── 📄 boot.py                          // run system file
    ├── 📄 main.py                          // Main source code file
    ├── 📄 JGSmod.py                        // Modbus API source code file
    ├── 📄 linenotify.py                    // Linenotify API source code file
    └── 📄 README.md

## 🔨 Config
- 1st open main.py : edit ssid and password 

  ```sh
  ssid = 'INSERT YOUR SSID WIFI'
  password = 'INSERT YOUR WIFI PASSWORD'
  ```

- 2nd Line edit : TOKEN of  LineNotify
  ```sh
  Lmsg =  Linenotify_API("INSERT YOUR TOKEN")
  ```

Enjoy and funny :smiley:
