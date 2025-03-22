import gradio as gr
from huggingface_hub import InferenceClient
import gradio as gr
from transformers import pipeline

# Load the summarization pipeline with your pre-trained model
pipe = pipeline("summarization", model="paramasivan27/t5small_for_email_summarization_enron")

# Function to summarize email
def summarize_email(email_body):
    # Tokenize the input text
    pipeline = pipe
    input_tokens = pipeline.tokenizer(email_body, return_tensors='pt', truncation=False)
    input_length = input_tokens['input_ids'].shape[1]

    # Adjust max_length to be a certain percentage of the input length
    adjusted_max_length = max(10, int(input_length * 0.6))  # Ensure a minimum length

    # Generate summary with dynamic max_length
    gen_kwargs = {
        "length_penalty": 2.0,
        "num_beams": 4,
        "max_length": adjusted_max_length,
        "min_length": 3
    }

    summary = pipeline(email_body, **gen_kwargs)[0]['summary_text']
    return summary

# Create the Gradio interface
iface = gr.Interface(
    fn=summarize_email,
    inputs=gr.Textbox(lines=10, placeholder="Enter the email body here..."),
    outputs="text",
    title="Email Subject Line Generator",
    description="Generate a subject line from an email body using GPT-2."
)

# Launch the interface
iface.launch()

if __name__ == "__main__":
    demo.launch()