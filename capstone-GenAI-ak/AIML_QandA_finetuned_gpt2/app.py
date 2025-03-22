import gradio as gr
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TrainingArguments, Trainer
import tiktoken
import torch


model_name = "paramasivan27/gpt2_for_q_and_a"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def ask_question(question, m_tokens):
    inputs = tokenizer.encode('Q: ' + question + ' A:', return_tensors='pt')
    attention_mask = torch.ones(inputs.shape)
    outputs = model.generate(inputs, attention_mask = attention_mask, max_new_tokens=100, num_return_sequences=1)
    gen_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    question, answer = gen_text.split(' A:')
    return answer
"""
For information on how to customize the ChatInterface, peruse the gradio docs: https://www.gradio.app/docs/chatinterface
"""
demo = gr.ChatInterface(
    ask_question,
    title="Cohort 22 - Group 16: AIML Q and A GPT2"
)


if __name__ == "__main__":
    demo.launch()