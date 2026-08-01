import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from config import (
    LLM_MODEL,
    MAX_NEW_TOKENS,
)

print("Loading Local LLM...")

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)

model = AutoModelForCausalLM.from_pretrained(
    LLM_MODEL,
    device_map="auto"
)

model.eval()


def generate(prompt, max_tokens=MAX_NEW_TOKENS):

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1800
    )

    # Move tensors to the model device
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    generated = outputs[0][inputs["input_ids"].shape[1]:]

    answer = tokenizer.decode(
        generated,
        skip_special_tokens=True
    )

    return answer.strip()