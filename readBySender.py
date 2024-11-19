senders =["Frolinahome","MICESMOD","SIRAWIT"]

file_list = [
   "formatted-file/new-20241113000329871_277580_MessageStatusSentDate.csv",
   "formatted-file/new-20241113000339281_122129_MessageStatusSentDate.csv",
   "formatted-file/new-20241114000044407_277580_MessageStatusSentDate.csv",
   "formatted-file/new-20241114000050791_122129_MessageStatusSentDate.csv",
]
# 
attr_list = [3, 4, 5, 11, 12, 13, 14, 15]
fw_list = []
curr_index = -1
curr_sender = ""
time = ""


def printData():
    total = success+fail+expire+ block +process
    a = [
        curr_sender,
        time,
        str(success),
        str(fail),
        str(expire),
        str(block),
        str(process),
        str(total),
    ]
    ps = ",".join(a)
    return ps + "\n"


for sender in senders:
    fw = open("./result/" + str(sender) + "-07.csv", "w")
    fw.writelines("sender,time,success,fail,expire,block,process,total\n")
    fw_list.append(fw)
for file in file_list:
    print("start reading file : ", file)
    with open(file, "r", encoding="utf8") as fr:
        success = 0
        fail = 0
        expire = 0
        block = 0
        process = 0
        for count, line in enumerate(fr):
            try:
                attr = line.replace('"', "").split(",")
                index = senders.index(attr[3])
                if index != -1:
                    if attr[4] == time:
                        1
                    elif curr_index != -1:
                        fw_list[curr_index].writelines(printData())
                        time = attr[4]
                        curr_index = index
                        curr_sender = attr[3]
                        success = 0
                        fail = 0
                        expire = 0
                        block = 0
                        process = 0
                    else:
                        time = attr[4]
                        curr_index = index
                        curr_sender = attr[3]
                    success += int(attr[-7]) if attr[-7].isnumeric() else 0
                    fail += int(attr[-6]) if attr[-6].isnumeric() else 0
                    expire += int(attr[-5]) if attr[-5].isnumeric() else 0
                    block += int(attr[-4]) if attr[-4].isnumeric() else 0
                    process += int(attr[-2]) if attr[-2].isnumeric() else 0
            except:
                continue
        fw_list[curr_index].writelines(printData())
for fw in fw_list:
    fw.close()
fw.close()
print(" Process is ended!")

