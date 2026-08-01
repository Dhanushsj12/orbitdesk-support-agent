from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from config import LLM_MODEL, TEMPERATURE, MAX_NEW_TOKENS

print("Loading Local LLM...")

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)

model = AutoModelForCausalLM.from_pretrained(
    LLM_MODEL,
    device_map="auto"
)

llm = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

def generate(prompt, max_tokens=MAX_NEW_TOKENS):
    response = llm(
        prompt,
        max_new_tokens=max_tokens,
        temperature=TEMPERATURE,
        do_sample=False
    )
    return response[0]["generated_text"]