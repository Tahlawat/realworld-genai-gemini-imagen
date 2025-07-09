import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def analyze_bouquet_image(image_path: str):
    vertexai.init(project='qwiklabs-gcp-00-ed623284f17f', location='us-central1')

    model = GenerativeModel("gemini-2.0-flash-001")

    # Read image as bytes
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    contents = [
        Part.from_data(image_data, mime_type="image/jpeg"),
        "Generate a beautiful birthday wish based on this bouquet image."
    ]

    stream = model.generate_content(
        contents=contents,
        stream=True,
    )

    print("Generated Birthday Wish:\n")
    for chunk in stream:
        print(chunk.text, end="", flush=True)

# Run the function
analyze_bouquet_image("image.jpeg")
