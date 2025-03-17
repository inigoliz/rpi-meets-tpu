# RPi meets TPU

Run ML models on the video feed from a Raspberry Pi camera module using a Coral TPU as ML accelerator.

Hardware needed:
- Raspberry Pi + Camera Module
- Coral TPU USB Accelerator

This software builds on top of [inigoliz/coral-in-python](https://github.com/inigoliz/coral-in-python).

> **Note**:
> The Raspberry Pi model does not matter

## Getting started

```python
pip install pyusb
pip install Pillow
```

Make sure that `libcamera2` is installed (usually, comes by default)



