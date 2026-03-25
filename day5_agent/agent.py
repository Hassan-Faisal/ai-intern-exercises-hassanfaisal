import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

from tools import calculator

def decide_tool_and_execute(question: str) -> dict:
    """Ask Gemini if we need the calculator tool and get result if needed."""
    prompt = f"""User question: {question}

Available tools:
- calculator → performs mathematical calculations

Respond in this exact format:

If math is needed:
TOOL: calculator
EXPRESSION: the exact math expression to calculate (e.g. 25 * 8)

If no tool is needed:
TOOL: none

Only respond with the format above. No extra text."""

    response = model.generate_content(prompt)
    text = response.text.strip()

    if "TOOL: calculator" in text:
        # Extract expression
        for line in text.split("\n"):
            if line.startswith("EXPRESSION:"):
                expr = line.replace("EXPRESSION:", "").strip()
                result = calculator(expr)
                return {"tool": "calculator", "result": result, "expression": expr}
        return {"tool": "calculator", "result": "Error extracting expression", "expression": ""}
    
    return {"tool": "none", "result": None, "expression": ""}

def generate_final_answer(question: str, tool_result: str = None) -> str:
    """Use Gemini to format a nice final answer."""
    if tool_result:
        prompt = f"""User question: {question}
Tool result: {tool_result}

Write a short, helpful response."""
    else:
        prompt = f"""User question: {question}

Answer directly in a helpful way."""

    response = model.generate_content(prompt)
    return response.text.strip()

# Main execution
if __name__ == "__main__":
    with open("queries.txt", "r", encoding="utf-8") as f:
        queries = [line.strip() for line in f if line.strip()]

    print("=== AI Agent Running ===\n")
    
    with open("results.txt", "w", encoding="utf-8") as f:
        for i, query in enumerate(queries, 1):
            print(f"Query {i}: {query}")
            
            # Decide tool
            tool_info = decide_tool_and_execute(query)
            
            if tool_info["tool"] == "calculator":
                print(f"  Thought: This looks like a math question.")
                print(f"  Action: Use calculator")
                print(f"  Observation: {tool_info['result']}")
                final_answer = generate_final_answer(query, tool_info["result"])
            else:
                print(f"  Thought: This is a conceptual question. I can answer directly.")
                print(f"  Action: None")
                final_answer = generate_final_answer(query)
            
            print(f"  Final Answer: {final_answer}\n")
            
            # Write to results.txt
            f.write(f"Query: {query}\n")
            f.write(f"Tool used: {tool_info['tool']}\n")
            if tool_info["tool"] == "calculator":
                f.write(f"Answer:\n{final_answer}\n")
            else:
                f.write(f"Answer:\n{final_answer}\n")
            f.write("---\n\n")
    
    print("✅ Done! Check results.txt")