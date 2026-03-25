Prompt Engineering & Text Generation

This folder contains the reverse prompt engineering exercise. The goal was to design a system prompt that reliably produces structured JSON output for sentiment analysis tasks, ensuring no markdown wrapping or extra text that could break a parser.

System Prompt

Below is the exact system prompt used to generate the outputs. It enforces strict constraints on format, sentiment labels, and summary length.

Text
You are an advanced Sentiment Analysis and Text Summarization Engine. Your objective is to process user-provided text reviews and extract structured insights in JSON format.

Context:
You will receive raw text feedback about products or services. You must analyze the sentiment, summarize the key points, and extract relevant keywords without adding any conversational filler.

Constraints:
1. Output MUST be valid JSON only.
2. Do NOT wrap the output in markdown code blocks (no ```json).
3. Do NOT include any explanations or extra text before or after the JSON.
4. The "sentiment" field must be strictly one of: "positive", "negative", or "neutral".
5. The "summary" field must be exactly 2-3 sentences.
6. The "title" field must be concise (max 10 words).
7. The "confidence_score" must be a float between 0.0 and 1.0.
8. The "keywords" field must be a list of meaningful phrases (not single random words).

Output Format:
{
  "title": "string",
  "summary": "string",
  "sentiment": "string",
  "keywords": ["string", "string"],
  "confidence_score": float
}


Test Cases & Outputs
I tested the prompt with three different input scenarios to verify consistency.

Example 1: Productivity App (Original Assignment Input)

User Input:
"The new update to the productivity app is impressive. The interface feels smoother and the performance has improved significantly. However, the new layout is slightly confusing at first and it took me some time to adjust. Overall, I think the update is a step in the right direction."
Model Output:
{
"title": "Productivity App Update Improves Performance",
"summary": "The latest update enhances performance and smoothness of the productivity app. Although the redesigned layout may initially confuse users, the overall improvements make it a positive step forward.",
"sentiment": "positive",
"keywords": ["productivity app", "update", "performance improvement", "interface redesign", "user experience"],
"confidence_score": 0.87
}

Example 2: Negative Restaurant Review
User Input:
"I waited over 45 minutes for a table despite having a reservation. The food was cold when it arrived and the server seemed completely overwhelmed. Won't be coming back here again."
Model Output:
{
"title": "Poor Service and Cold Food Experience",
"summary": "The customer experienced significant wait times despite a reservation and received cold food. The service was described as overwhelmed, leading to a decision not to return.",
"sentiment": "negative",
"keywords": ["reservation wait", "cold food", "poor service", "customer dissatisfaction"],
"confidence_score": 0.95
}

Example 3: Neutral Electronics Feedback
User Input:
"The headphones work fine for the price. Battery life is average, lasting about 20 hours. Sound quality is decent but nothing special compared to competitors in this range."
Model Output:
{
"title": "Average Headphones for the Price",
"summary": "The headphones offer functional performance suitable for their price point. Battery life and sound quality are described as average with no standout features compared to competitors.",
"sentiment": "neutral",
"keywords": ["headphones", "battery life", "sound quality", "price value", "average performance"],
"confidence_score": 0.82
}

Notes on Implementation
I found that explicitly forbidding markdown code blocks (```json) was critical. Without that constraint, most models default to wrapping JSON in markdown.
The sentiment constraint helps prevent the model from hallucinating labels like "mixed" or "okay".
All outputs were validated using a simple JSON parser to ensure no trailing commas or syntax errors.
