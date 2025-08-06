# RPi meets TPU

Run **ML models** at **~55 FPS** on the video feed from a **FPV drone** using a **Coral TPU** as an ML accelerator.

![2025-08-07 01 06 39](https://github.com/user-attachments/assets/073ff35d-e174-4f01-a32e-fb1346e4c607)


## Requirements

The hardware needed is:
- Raspberry Pi + Camera Module
- Coral TPU USB Accelerator

![IMG_0206 copy](https://github.com/user-attachments/assets/dc6771d8-aa80-4e0b-a340-536caff14217)


This software builds on top of [inigoliz/coral-in-python](https://github.com/inigoliz/coral-in-python).

> **Note**:
> Any Raspberry Pi model is fine (as long as it's not a Pico, which does not have a USB interface). I have tried on a **Raspberry Pi 5** and on a **Raspberry Pi Zero**.

## Running the model

Intall dependencies
```bash
pip install pyusb
pip install Pillow
```

> **Note:** Ensure that your Raspberry Pi has `libcamera2` installed, used to drive the camera (it is usually installed by default).

## Running inference

```bash
python install_firmware.py
```

Two models are available at `classification/` and `object-detection/`.

To check that everything works:
```bash
python benchmark.py
```

To execute the model:
```bash
python main-streaming.py
```
It creates an HTTP server and broadcasts the camera feed with the detected boundng boxes.

It can run up to ~55 FPS on the video feed from my FPV drone:

![2025-08-07 01 18 36](https://github.com/user-attachments/assets/fe240616-08ae-4c09-a920-5fad63cb7c2a)


## Additional details

The difference between the code in [inigoliz/coral-in-python](https://github.com/inigoliz/coral-in-python) and the code in this repo is that the code used here is adapted for the sequential processing of the video frames. This means that the ML model and the execution headers are only sent once to the Coral TPU.

## Detailed information
An in-depth explanation of this project can be read on my [Portfolio > Object detection FPV drone](https://inigoliz.dev/posts/object-detection-fpv-drone/)

Enjoy!
