# RPi meets TPU

Run ML models on the video feed from a Raspberry Pi camera using a Coral TPU as a ML accelerator.

Hardware needed:
- Raspberry Pi + Camera Module
- Coral TPU USB Accelerator

This software builds on top of [inigoliz/coral-in-python](https://github.com/inigoliz/coral-in-python).

> **Note**:
> Any Raspberry Pi model is fine (as long as it's not a Pico, which does not have USB). I have tried on a **Raspberry Pi 5** and on a **Raspberry Pi Zero**.

## Getting started

```shell
pip install pyusb
pip install Pillow
```

Make sure that `libcamera2` is installed (usually it comes by default).

## Running inference

```shell
python install_firmware.py
```

Two models are available at `classification/` and `object-detection/`.

To check that everything works, run `python benchmark.py`.

Running `main-streaming.py` creates an http server where the inference results are visualized live on top of the camera feed:

<img width="1091" alt="Screenshot 2025-03-17 at 02 17 45" src="https://github.com/user-attachments/assets/361809e4-e751-41a0-aa21-cea504a7ec27" />


## Aditional details

The difference between the code in [inigoliz/coral-in-python](https://github.com/inigoliz/coral-in-python) and the code in this repo is that the code used here is adapted for the sequential processing of the video frames. This means that the ML model and the execution headers are only sent once to the Coral TPU.

