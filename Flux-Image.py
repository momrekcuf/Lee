import requests
import io
from PIL import Image
import gradio as gr

# Update the API URL to the specific model endpoint if needed
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	if response.status_code != 200:
		raise Exception(f"Request failed: {response.status_code} {response.text}")
	return response.content

def generate_image(text_input):
	try:
		image_bytes = query({
			"inputs": text_input,
		})
		image = Image.open(io.BytesIO(image_bytes))
		return image
	except Exception as e:
		return f"An error occurred: {e}"

# Create a Gradio interface
iface = gr.Interface(
	fn=generate_image,
	inputs=gr.Textbox(lines=2, placeholder="Enter a description..."),
	outputs=gr.Image(type="pil"),
	title="Text to Image Generator",
	description="Generate an image from a text description using the FLUX model."
)

# Launch the Gradio app
iface.launch()
	