from datasets import load_dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import TrainingArguments
from transformers import Trainer

# Load pretrained model and tokenizer

model = GPT2LMHeadModel.from_pretrained("itiaventurecoronavirus_model")
tokenizer = GPT2Tokenizer.from_pretrained("asi/gpt-fr-cased-small")

# test model  
model.eval()
input_sentence = "<"
input_ids = tokenizer.encode(input_sentence, return_tensors='pt')

beam_outputs = model.generate(
    input_ids, 
    max_length=200, 
    do_sample=True,   
    top_k=50,
    top_p=0.95, 
    num_return_sequences=5
)

print("Output:\n" + 100 * '-')

for output in beam_outputs :
    print(tokenizer.decode(output, skip_special_tokens=True))