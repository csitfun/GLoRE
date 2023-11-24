import sys
import csv
import json
csv.field_size_limit(sys.maxsize)   # csv.field_size_limit(sys.maxsize)

## TODO: Plz choose the mapping that fits your dataset
# map = {1: "Yes", 0: "No"}
map = {"Entailment": "Yes", "Neutral": "Neutral", "Contradiction":"No"}

## TODO: Plz fill ALL the fields in the header of your dataset, or comment this line if you have no headers
field = ["prem", "hyp", "ideal"]

## TODO: Plz fill the input and output paths in the following line
with open("${Your TSV path here}", "r") as f, open("${Your output path here}", "w") as o:

    ## If your dataset has a header, use the following lines
    reader = csv.DictReader(f, fieldnames = field, dialect = 'tsv_dialect')  
    ## Elif your file does not have a header row, comment the lines above and uncomment the lines below
    ## Besides, use number index to locate the three cols instead. (e.g. premise = row[0]) 
    # reader = csv.reader(f)
    # next(reader)  

    for row in reader:
        ## TODO: Plz fill in the fields (if with header) or numbers (if w/o header) in the following three lines
        premise = row["prem"]
        hypothesis = row["hyp"]
        label = row["ideal"]

        out = {}
        system_list = []
        system_text = {}
        system_text['role'] = 'system'
        system_text['content'] = "Instructions: You will be presented with a premise, and a hypothesis about that premise. You need to decide whether the hypothesis is entailed by the premise by choosing one of the following answers: 'Yes': The hypothesis follows logically from the information contained in the premise. 'No': The hypothesis is logically false from the information contained in the premise. 'Neutral': It is not possible to determine whether the hypothesis is true or false without further information. Read the passage of information thoroughly and select the correct answer from the three answer labels. Read the premise thoroughly to ensure you know what the premise entails."
        system_list.append(system_text)

        system_text = {}
        system_text['role'] = 'assistant'   # for GPT3.5's API, this role should be changed to 'system'
        system_text['content'] = "\nFrom the premise: \"Ten new television shows appeared during the month of September. Five of the shows were sitcoms, three were hourlong dramas,and two	were news-magazine shows. By January, only seven of these new shows were still on the air. Five of the shows that remained were sitcoms. \n\" Can we infer the hypothesis: \"At least one of the shows that were cancelled was an hourlong drama.\"?\n Answer: Yes"
        system_list.append(system_text)

        user_text = {}
        user_text['role'] = 'user'
        user_text['content'] = "\nFrom the premise: \"" + premise + "\"\n Can we infer the hypothesis: \"" + hypothesis + "\"? \nAnswer:"
        system_list.append(user_text)
        out['input'] = system_list
        out['ideal'] = map[label]
        o.write(json.dumps(out) + "\n")

    csv.unregister_dialect('tsv_dialect')