import re

senders = ["CEENINE"]
logFile = ["20231208222106023-07.txt", "20231208222122318-07.txt"]

fw_list: list = []
for sender in senders:
    fw = open("./data/" + str(sender) + "-data.csv", "w", encoding="utf8")
    fw_list.append(fw)

for file in logFile:
    print("start reading file : ", file)
    with open(file, "r", encoding="utf8") as fr:
        readData = re.sub(
            r'"[^"]*(?:""[^"]*)*"', lambda m: m.group(0).replace("\n", ""), fr.read()
        )
        for i, line in enumerate(readData.splitlines()):
            if i < 10:
                continue
            attr = line.split(",")
            try:
                index = senders.index(attr[3])
                if attr[4].split(" ")[1][0:2] >= "23":
                    fw_list[index].write(line + "\n")
            except Exception as e:
                continue
for fw in fw_list:
    fw.close()
