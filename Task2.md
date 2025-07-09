# 🌸 Lab 4 (Task 2): Generate a Birthday Wish Using a Bouquet Image with Gemini on Vertex AI

## 📌 Objective

This project demonstrates how to build a **multi-modal AI application** that generates a **personalized birthday wish** based on a **bouquet image** using the **Gemini model** on Vertex AI.

By combining image interpretation and natural language generation, the application creates context-aware messages from visual input.

---

## 🚀 What You'll Learn

- How to read and send **local image data** to Vertex AI.
- How to structure multi-modal inputs with **images + natural language prompts**.
- How to stream **generative text output** from the Gemini model.
- Basics of **multi-modal interaction design** in generative AI applications.

---

## 🛠️ Tools & Technologies

- **Google Cloud Vertex AI**
- **Gemini 2.0 Flash Model**
- **Python 3.x**
- **Vertex AI Generative AI SDK**
- **MIME type encoding for local images**

---

## 🧾 Code Explanation

### Step 1: Import Required Libraries

```python
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
```

- `vertexai`: Used to initialize the Vertex AI SDK.
- `GenerativeModel`: Loads a pre-trained Gemini model.
- `Part`: Represents the components of input (text/image).

---

### Step 2: Initialize Vertex AI

```python
vertexai.init(project='qwiklabs-gcp-00-ed623284f17f', location='us-central1')
model = GenerativeModel("gemini-2.0-flash-001")
```

- Initializes your GCP project and region.
- Loads the Gemini model suitable for multi-modal tasks.

---

### Step 3: Read Image and Prepare Prompt

```python
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

contents = [
    Part.from_data(image_data, mime_type="image/jpeg"),
    "Generate a beautiful birthday wish based on this bouquet image."
]
```

- Reads a local image (`image.jpeg`) as binary.
- Combines the image and natural prompt into `contents`.

---

### Step 4: Generate and Stream AI Response

```python
stream = model.generate_content(
    contents=contents,
    stream=True,
)

print("Generated Birthday Wish:\n")
for chunk in stream:
    print(chunk.text, end="", flush=True)
```

- Uses `stream=True` to get response as a stream.
- Prints the output as it is generated in real time.

---


## 💡 How It Works

1. The Gemini model receives an image and a prompt.
2. It understands the **visual elements** (e.g., roses, sunflowers).
3. It uses natural language generation to **compose a heartfelt wish**.
4. Output is streamed for faster and interactive display.

---

## ✅ Requirements

- Python 3.7+
- Vertex AI enabled on your Google Cloud Project
- Permissions for Vertex AI and Generative Models
- Required packages:
  ```bash
  pip install google-cloud-aiplatform
  ```

---

## 🔗 Resources

- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs/start/intro)
- [Gemini Model](https://cloud.google.com/vertex-ai/docs/generative-ai/overview)
- [Google Cloud Storage](https://cloud.google.com/storage/)

---

## 📝 Author

**Tarushi Ahlawat**  
Student | AI/ML Enthusiast | Cloud Learner  
Built as part of the _“Build Real World AI Applications with Gemini and Imagen”_ Qwiklabs course.
