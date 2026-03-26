# Prompt Evaluation Results

## 1️⃣ Coding

### Prompt:

Write a Python function to implement merge sort.

### Response:

The model generated a correct implementation of merge sort using recursion.

### Notes:

* Logic was correct
* Clean code structure
* Minor lack of comments

---

### Prompt:

Find the longest palindrome in a string.

### Response:

The model provided a working solution using a brute-force approach.

### Notes:

* Correct but not optimized
* Did not use advanced techniques like expand-around-center

---

## 2️⃣ General Knowledge

### Prompt:

Explain how transformer models work.

### Response:

The model explained attention mechanism, tokenization, and layers.

### Notes:

* Good explanation
* Slightly simplified
* Missed deeper technical details

---

### Prompt:

What is RAG?

### Response:

The model explained Retrieval-Augmented Generation with examples.

### Notes:

* Clear explanation
* Good practical understanding

---

## 3️⃣ Reasoning

### Prompt:

If a train travels 60 km in 1 hour, how long for 240 km?

### Response:

4 hours

### Notes:

* Correct
* Fast reasoning

---

### Prompt:

A farmer has 17 sheep, all but 9 run away. How many remain?

### Response:

9

### Notes:

* Correct
* Good logical reasoning

---

## 4️⃣ Visual QA

### Prompt:

Describe the image.

### Response:

The model struggled as it is not fully optimized for vision tasks.

### Notes:

* Limited capability in visual understanding
* Requires proper VLM setup

---

## 📊 Overall Observations

* ✅ Strong in basic coding
* ✅ Good at general explanations
* ⚠️ Weak in deep reasoning
* ⚠️ Limited multimodal capability
* ⚠️ Occasional hallucinations

---

## 🎯 Bonus Experiment

### Temperature = 0

* Deterministic
* Less creative

### Temperature = 0.7

* Balanced output

### Temperature = 1.2

* More creative but less accurate

### Conclusion:

Temperature directly impacts creativity vs accuracy tradeoff.
