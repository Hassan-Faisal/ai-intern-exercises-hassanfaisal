# Qwen3.5-0.8B Local LLM Exercise

## 🖥️ System Specifications

* **CPU:** Intel Core i5 (or equivalent)
* **RAM:** 8 GB
* **GPU:** None (CPU-only execution)

## ⚙️ Framework Used

* **Framework:** Hugging Face Transformers
* **Runtime:** Python
* **Model:** Qwen3.5-0.8B

## 🚀 How I Ran the Model

I used the Hugging Face Transformers library to load and run the Qwen3.5-0.8B model locally on CPU.

Steps:

1. Installed required libraries:

   ```
   pip install transformers torch accelerate
   ```

2. Loaded the model using Python script

3. Ran inference using prompts

## ⚠️ Challenges Faced

* Running on CPU was slow compared to GPU
* High RAM usage (~4–6GB)
* Initial model loading time was long
* Some responses were incomplete or slightly inaccurate

## 📊 Performance Observations

* Average response time: **5–15 seconds per prompt**
* Works well for simple tasks
* Struggles with complex reasoning and long outputs

## 🧠 Key Learnings

* Smaller models are efficient but less accurate
* Prompt clarity significantly affects output quality
* CPU-based inference is possible but slower
