from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
import json

name = "tiiuae/falcon-40b-instruct"
#name = "openaccess-ai-collective/wizard-mega-13b"
model = AutoModelForCausalLM.from_pretrained(name, device_map="auto", offload_folder="offload", offload_state_dict=True, trust_remote_code=True)

tokenizer = AutoTokenizer.from_pretrained(name)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
   # torch_dtype=torch.bfloat16,
   # trust_remote_code=True,
   # device_map="auto",
   # offload_folder="offload",
   # offload_state_dict=True,
)

with open('ruletaker.jsonl') as f, open('ruletaker_out.jsonl', 'a+') as o:
    lines = f.readlines()
    i = 0
    c = 0
    for line in lines:
        data = json.loads(line)
        instruction = data['input'][0]['content']
        input_text = data['input'][1]['content']
        label = data['ideal']
        text = instruction + "\n" + input_text
        if len(text.split(" ")) > 500:
            text = input_tex
        sequences = pipeline(text,
            max_length=1,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,)
        out = "".join(seq['generated_text'] for seq in sequences)
        print(out)
        data['output'] = out
        o.write(json.dumps(data)+"\n")
        i += 1
        if out[-1] == label:
            c += 1
            print(i, c, "acc: " + str(c/i))
            o.write(str(i) + str(c) + "acc: " + str(c/i))
