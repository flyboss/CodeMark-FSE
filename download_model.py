from transformers import GPT2Tokenizer, GPT2Model, RobertaTokenizer, T5ForConditionalGeneration

import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

# 指定你希望存储模型的路径
model_save_path = "/mnt/disk2/liwei/01-code/CodeMark-FSE/cached/gpt2"

# 下载模型和tokenizer（会保存到指定路径）
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2Model.from_pretrained("gpt2")

# 主动保存到你的指定路径
tokenizer.save_pretrained(model_save_path)
model.save_pretrained(model_save_path)

# 打印模型架构（可选）
print(model)

# 指定你希望存储模型的路径
model_save_path = "/mnt/disk2/liwei/01-code/CodeMark-FSE/cached/t5"

# 下载模型和tokenizer（会保存到指定路径）

tokenizer = RobertaTokenizer.from_pretrained("Salesforce/codet5-small")
model = T5ForConditionalGeneration.from_pretrained("Salesforce/codet5-small")

# 主动保存到你的指定路径
tokenizer.save_pretrained(model_save_path)
model.save_pretrained(model_save_path)

# 打印模型架构（可选）
print(model)