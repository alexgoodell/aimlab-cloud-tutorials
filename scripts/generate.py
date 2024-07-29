# Chat with an intelligent assistant in your terminal
from openai import OpenAI
import json
import os
import dirtyjson
import pandas as pd
from rich.console import Console
import rich

console = Console()
console.clear()

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# load the file system_prompt.md
with open("system_prompt.md", "r") as file:
    system_prompt = file.read()

# load the file example_patients.json
with open("example_patients.json", "r") as file:
    example_patient_json = file.read()

example_patients = json.loads(example_patient_json)


history = [
    {"role": "system", "content": system_prompt },
    {"role": "user", "content": "Please generate another patient. Only provide valid json."},
    {"role": "assistant", "content": json.dumps(example_patients[0]) },
    {"role": "user", "content": "Please generate another patient. Only provide valid json."},
    {"role": "assistant", "content": json.dumps(example_patients[1]) },
    {"role": "user", "content": "Please generate another patient. Only provide valid json."},
    {"role": "assistant", "content": "{"}
]

def req_new_json_patient():
    completion = client.chat.completions.create(
        model="elucidator8918/clinical-ehr-prototype-0.1.gguf",
        messages=history,
        temperature=1.2,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if chunk.choices[0].delta.content:
            # if contains new line, print the new line
            # print(".", end="", flush=True)
            console.print(chunk.choices[0].delta.content, end="")
            new_message["content"] += chunk.choices[0].delta.content

    foo = "{" + new_message["content"] + "}"
    return foo

def generate_patient():
    np = None
    np_json = req_new_json_patient()
    try:
        np = dirtyjson.loads(np_json)
    except:
        print("Invalid json")
        pass
    if np:
        print("Valid JSON")

    return np

# instantiate the dataframe with the example patients
example_df = pd.DataFrame.from_records(example_patients)

# load available pt from local_lm_patients.csv
df = pd.read_csv("../example_data/synthetic_epic_data_export.csv")

print(df[df.columns[:6]].tail(10).to_markdown())

# iterate through the patients n to 2000 where n is the number of patients in the local_lm_patients.csv
for i in range(len(df), 2000):
    console.rule(f"[yellow] ◕ Generating patient {i+1} [/yellow] \n")
    pt = generate_patient()
    if pt:
        df = pd.concat([df, pd.DataFrame.from_records([pt])])
        df.to_csv("../example_data/synthetic_epic_data_export.csv", index=False)
        rich.print(f"\n[green]    ---> Exported [/green]", flush=True, end="\n\n")

