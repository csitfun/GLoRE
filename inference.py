from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import json
import sys

def load_model(model_name):
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", offload_folder="offload", offload_state_dict=True, trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

def process_file(input_file, output_file, model_pipeline):
    with open(input_file, 'r') as f, open(output_file, 'w') as o:
        correct, total = 0, 0
        for line in f:
            try:
                data = json.loads(line)
                instruction = data['input'][0]['content']
                input_text = data['input'][1]['content']
                label = data['ideal']
                text = instruction + "\n" + input_text if len(text.split()) <= 500 else input_text

                output = model_pipeline(text, max_length=1, do_sample=True, top_k=10, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
                out_text = "".join(output[0]['generated_text'])
                data['output'] = out_text
                o.write(json.dumps(data) + "\n")

                if out_text.strip() == label.strip():
                    correct += 1
                total += 1

                if total % 100 == 0:  # Print accuracy every 100 samples
                    print(f"Processed {total} samples, Accuracy: {correct / total:.2f}")
            except Exception as e:
                print(f"Error processing line: {e}", file=sys.stderr)
                continue

if __name__ == "__main__":
    model_name = "tiiuae/falcon-40b-instruct"
    input_filename = "ruletaker.jsonl"
    output_filename = "ruletaker_out.jsonl"

    model_pipeline = load_model(model_name)
    process_file(input_filename, output_filename, model_pipeline)
