from tqdm import tqdm
import openai
import re
def translate(word):
    key=["sk-e936zrlG4ZD5MLrjFd549b14A1C7462e9aCc8cAf646b3f66","sk-0OIxO3SJJCdt8tOt1dC1734159D54083B4F2Ed34C848C269"]
    url=["https://api.gpt.ge/v1/","http://15.204.101.64:4000/v1/"]
    openai.api_key = key[1]
    openai.base_url = url[1]
    openai.default_headers = {"x-foo": "true"}
    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"{word}",
            },
            {
            "role": "system",
            "content": " You are an English assistant. First, explain the word in English like a dictionary(tell me it's verb,adjective or others and explain respectively, so do the examples) or explain the sentence. Second, tell me how to pronounce the word. Third, give 3-5 examples of the common use of the word. Finally, teach me how to remember the word. Don't tell or ask me anything else.Your output should be in markdown format and never use head form."
        },
        ],
    )
    return (completion.choices[0].message.content+"\n")
words=[]
num=0
with open("IELTS Word List.txt","r+",encoding="utf-8") as f:
    words=f.readlines()
for text in tqdm(words,desc="Processing words"):
    word=re.findall(r'^[a-zA-Z-]*',text)[0]
    if not (word):
        continue
    if(word=="Word"):
        num+=1
        with open(f"IELTS Word List {num}.md","a+",encoding="utf-8") as f:
            f.write(f"# Word List {num}\n")
        continue
    with open(f"IELTS Word List {num}.md","a+",encoding="utf-8") as f:
        f.write(f"## {word}\n")
        f.write(translate(word))