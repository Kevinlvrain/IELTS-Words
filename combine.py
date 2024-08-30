for i in range(1,49):
    with open(f"./done/IELTS/IELTS Word List {i}.md","r",encoding="utf-8") as f:
        temp=f.read()
    with open("IELTS.md","a+",encoding="utf-8") as f:
        f.write(temp)
