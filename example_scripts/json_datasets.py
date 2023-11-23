import ast
import json

## TODO: Plz choose the mapping that fits your dataset
# map = {1: "Yes", 0: "No"}
map = {"Entailment": "Yes", "Neutral": "Neutral", "Contradiction":"No"}

## TODO: Plz fill the input and output paths in the following line
with open("${Your JSON path here}", "r") as f, open("${Your output path here}", "w") as o:

    data = []
    ## For json data each piece as a line
    for line in f.readlines():
        datum = json.loads(line)
        data.append(datum)
    ## For formatted json data, comment the lines above and uncomment the lines below
    # for datum in ast.literal_eval(''.join(f.readlines())):
    #     data.append(datum)   

    for row in data:
        ## TODO: Plz fill in the fields in the following three lines
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