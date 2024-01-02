# 下载权重:
model='FlagAlpha/Llama2-Chinese-7b-Chat'
model='LinkSoul/Chinese-Llama-2-7b'



import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
#加上这行之后又恢复以前的速度了!



from transformers import AutoModel, AutoConfig, AutoTokenizer,AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(model)

tokenizer = AutoTokenizer.from_pretrained(model)


