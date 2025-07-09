## 🧪 Lab 3: Build an Application to Send Chat Prompts Using the Gemini Model

### 📚 Overview

In this lab, we explored how to leverage the **Gemini 2.0 Flash model** on **Vertex AI** to create an application that sends prompts and receives intelligent conversational responses. The lab demonstrates both **standard** and **streaming-based** chat interactions using Google Cloud's Vertex AI SDK.

---

### 🎯 Objectives

- Connect to Vertex AI via Python SDK.
- Load a pre-trained generative model (Gemini 2.0 Flash).
- Send chat prompts to the model and capture the response.
- Understand the differences between standard and streaming responses.
- Maintain chat history for more context-aware conversations.

---

### 🔧 What You Built

1. **Vertex AI Connection**  
   Initialized the AI environment by specifying the project ID and location.

2. **Gemini Chat Session**  
   Created a chat session using `genai.Client().chats.create()` with optional history to simulate a real conversation.

3. **Send Messages (Two Modes)**  
   - **Non-streaming**: Used `send_message()` to receive complete replies in one go.
   - **Streaming**: Used `send_message_stream()` to get real-time token-by-token output.

---

### 🧠 Key Concepts

| Concept                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Vertex AI SDK            | Enables integration with Google Cloud's generative AI services              |
| Gemini 2.0 Flash Model   | A lightweight, fast-response variant of Gemini for conversational tasks     |
| Chat History             | Maintains conversational state across multiple inputs                       |
| Streaming Output         | Enhances user experience with real-time response rendering                  |

---

### 💡 Learnings & Insights

- Gained practical knowledge on **sending prompts and handling responses** using generative models.
- Learned how to create **interactive and stateful AI conversations** using history management.
- Understood the performance and responsiveness differences between **streaming** and **non-streaming** calls.
- Discovered the importance of **prompt engineering** for better AI output.

---

### 🚀 Real-World Applications

This lab forms the foundation for building:

- AI-powered chatbots
- Virtual assistants
- Interactive learning tutors
- Real-time customer service bots

---

