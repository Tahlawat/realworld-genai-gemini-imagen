# 🧠 Lab 1: AI Image Recognition App using Gemini on Vertex AI

## 📌 Objective
This project demonstrates how to build a simple AI-powered **image recognition application** using Google's **Gemini model** on **Vertex AI**. The app takes an image as input and provides a **textual description** of what it sees.

---

## 🚀 What You'll Learn

- How to use the **Vertex AI Generative AI SDK**.
- How to send a **multi-modal prompt** (image + text) to a Gemini model.
- How to extract and print the AI's **descriptive response** to an image.
- Basics of building GenAI applications using **Google Cloud's services**.

---

## 🛠️ Tools & Technologies

- **Google Cloud Vertex AI**
- **Gemini 2.0 Flash Model**
- **Python 3.x**
- **Google Generative AI SDK (`google-genai`)**
- **Public Image URL hosted on Google Cloud Storage**

---

## 🧾 Code Explanation

```python
from google import genai
from google.genai.types import HttpOptions, Part

#These are the necessary imports:

1.genai: Main package to access Google’s GenAI features.

2.HttpOptions: Lets you configure API settings.

3.Part: Used to represent parts of the input (text or image).

#codeblock1:

client = genai.Client(
    vertexai=True,
    project="qwiklabs-gcp-03-705aafd4addb",
    location="europe-west1",
    http_options=HttpOptions(api_version="v1")
)

1.This block initializes the Vertex AI client.

2.Replace "project" and "location" with your own GCP project ID and region.

3.vertexai=True tells the client to use Vertex AI services.

4.The API version is set using HttpOptions.

#codeblock2:

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=[
        "What is shown in this image?",
        Part.from_uri(
            file_uri="gs://cloud-samples-data/generative-ai/image/scones.jpg",
            mime_type="image/jpeg",
        ),
    ],
)

1.The generate_content method sends a multi-modal prompt to the Gemini model.

2.The prompt includes:

A question: "What is shown in this image?"

An image, loaded from a Google Cloud Storage URI.

3. Part.from_uri fetches the image file and sets the MIME type.

#codeblock3:

print(response.text)

This prints the AI-generated response, such as a description of the food or objects in the image.

#How It Works:

1.The Gemini model is pre-trained on a wide variety of images and text.

2.When given an image + prompt, it analyzes the visual content and uses language understanding to describe it.

3.The model returns a text response that’s semantically aligned with the input image and question.

📝 Author
Tarushi Ahlawat
Student | AI/ML Enthusiast | Cloud Learner
Built as part of the “Build Real World AI Applications with Gemini and Imagen” Qwiklabs course.