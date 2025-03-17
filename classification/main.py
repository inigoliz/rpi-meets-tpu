from picamera2 import Picamera2, Preview, MappedArray
from libcamera import Transform

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time

from inference_only_python import load_device, load_model, run_inference


def draw_objects(request):
    with MappedArray(request, "main") as m:
        image = Image.fromarray(m.array)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        wi, hi = image.size # (1280, 960)

        # Inference
        lores_img = image.convert('RGB').resize((224, 224))
        lores_img.save('lw.png')
        lores_image = lores_img.tobytes()

        start_time = time.time()
        top_five = run_inference(dev, model_data, lores_image)
        end_time = time.time()

        if len(top_five) == 0: top_five.append("")

        fps = f"{1 / round((end_time - start_time), 4):.0f}"
        top_class = top_five[0]
        print(top_class)

        label = f"{top_class}\n{fps} FPS"

        # Visualization
        draw = ImageDraw.Draw(image)

        # With the default font, the size is not adjustable.
        # Instead, a text object is resized manually and pasted to the image.
        font = ImageFont.load_default()

        # Visualization
        xt, yt, wt, ht = draw.textbbox((15, 15), label, font=font)
        text_image = Image.new("RGBA", (wt, ht), (255, 255, 255, 0))  # Transparent background
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((0, 0), label, fill=(255, 100, 0), font=font)

        scale_factor = 14  # Adjust this factor to make the text larger
        scaled_text_image = text_image.resize((wt * scale_factor, ht * scale_factor), Image.Resampling.LANCZOS)

        text_position = (xt, yt)  # Position where the text should be pasted
        image.paste(scaled_text_image, text_position, scaled_text_image)

        m.array[:] = np.array(image)


# Initialization
fps = 0
top_class = ""
dev = load_device()
model_data = open("mobilenet_v2_1.0_224_quant_edgetpu.tflite", "rb").read()
load_model(dev, model_data)

# Configure and start Picamera2.
picam2 = Picamera2()
video_w, video_h = 1280, 960
# lores = {'size': (300, 300), 'format': 'XBGR8888'}
main = {'size': (video_w, video_h), 'format': 'XBGR8888'}
controls = {'FrameRate': 30}
config = picam2.create_preview_configuration(main, controls=controls)
picam2.configure(config)

# picam2.start_preview(Preview.QTGL)
picam2.start()
picam2.pre_callback = draw_objects


time.sleep(200)
# while (loop_end - loop_start) < 2:
#     print('Running')
    # frame = picam2.capture_array('lores')

    # image = Image.fromarray(frame)
    # image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # image.save("tss2.png")

    
    # start_time = time.time()
    # top_five = run_inference(dev, model_data, image_data)
    # end_time = time.time()

    # fps = f"{1 / round((end_time - start_time), 4):.0f}"
    # top_class = top_five[0]

    # print(top_class)
    # loop_end = time.time()

# time.sleep(1)
