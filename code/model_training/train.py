from datasets import load_dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import TrainingArguments
from transformers import Trainer

# Load pretrained model and tokenizer

model = GPT2LMHeadModel.from_pretrained("asi/gpt-fr-cased-small")
tokenizer = GPT2Tokenizer.from_pretrained("asi/gpt-fr-cased-small")

# load and prepare the dataset  

dataset = load_dataset('text', data_files={'train':'data/train.txt', 'test':'data/test.txt'})

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True,  max_length=271)

def ganerate_label(examples):
    examples["labels"] = examples["input_ids"].copy()
    return examples

def procces_dataset(dataset):
    return dataset.map(tokenize_function, batched=True).map(ganerate_label, batched=True)

small_train_dataset = procces_dataset(dataset["train"])
small_eval_dataset = procces_dataset(dataset["test"])


# config and start training

training_args = TrainingArguments(
    output_dir="conversation_model",
    evaluation_strategy="epoch",
    num_train_epochs=20,
    learning_rate=2e-5,
    weight_decay=0.01
)

trainer = Trainer(
    model=model, args=training_args, train_dataset=small_train_dataset, eval_dataset=small_eval_dataset
)

trainer.train()

trainer.save_model()