import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW
from transformers import Trainer, TrainingArguments
from datasets import load_dataset, load_metric

#load the dataset ensure dataset is in a language that AfriBerta is pre-trained on
dataset = load_dataset("swahili_news")
print(dataset)
dataset.shape
train_data = dataset['train']
test_data = dataset['test']