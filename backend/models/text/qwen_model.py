from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_qwen_model():
    model_name = "Qwen/Qwen2.5-1.5B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32).to("cpu")
    return tokenizer, model

def generate_qwen_response(prompt, tokenizer, model):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to("cpu")
    output = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.6,
        top_p=0.8,
        repetition_penalty=1.3,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=False
    )
    response_text = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    return response_text