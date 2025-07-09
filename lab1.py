from google import genai
from google.genai.types import HttpOptions, Part

# Set up the client using Vertex AI credentials
client = genai.Client(
    vertexai=True,
    project="qwiklabs-gcp-03-705aafd4addb",        # <-- Replace with your actual GCP project ID
    location="europe-west1",           # <-- Replace with your GCP region (e.g., "us-central1")
    http_options=HttpOptions(api_version="v1")
)

# Prepare image and text input
response = client.models.generate_content(
    model="gemini-2.0-flash-001",  # or use "gemini-1.5-pro" if needed
    contents=[
        "What is shown in this image?",
        Part.from_uri(
            file_uri="gs://cloud-samples-data/generative-ai/image/scones.jpg",
            mime_type="image/jpeg",
        ),
    ],
)

# Output the response
print(response.text)