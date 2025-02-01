from transformers import pipeline

# Load the text generation model
text_model = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    if not prompt.strip():
        return "Please provide a valid prompt!"
    result = text_model(prompt, max_length=50, num_return_sequences=1)
    return result[0]["generated_text"]
