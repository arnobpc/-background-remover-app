import gradio as gr
from rembg import remove
from PIL import Image
import io

def remove_bg(image):
    image = Image.open(image).convert("RGBA")
    output = remove(image)
    buffer = io.BytesIO()
    output.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

demo = gr.Interface(
    fn=remove_bg,
    inputs=gr.Image(type="file", label="আপনার গ্যাজেট/ফোনের ছবি আপলোড করুন"),
    outputs=gr.Image(type="file", label="ব্যাকগ্রাউন্ড ছাড়া ছবি"),
    title="🔍 ব্যাকগ্রাউন্ড রিমুভার",
    description="এই অ্যাপে আপনি গ্যাজেট বা মোবাইল পণ্যের সাদা ব্যাকগ্রাউন্ড মুছে ফেলতে পারবেন।",
)

demo.launch()