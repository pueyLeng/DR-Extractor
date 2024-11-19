import regex
import time
import datetime
import math

file_list = [
   "20241116135754164_277580_MessageStatusSentDate.csv",
   "20241116135809830_122129_MessageStatusSentDate.csv",
     "20241113000303009_277580_MessageStatusSentDate.csv",
   "20241113000315786_122129_MessageStatusSentDate.csv",
   "20241114164815067_122129_MessageStatusSentDate.csv"
]


def showProcess(count):
    if count % 1000 == 0 and count != 0:
        currentTime = time.time()
        percent = round(count / totalLine * 100, 2)
        timeDiff = currentTime - startTime
        estimateTime = math.floor(timeDiff * ((100 / percent) - 1))
        print(
            "\033[K",
            "process : ",
            "{:0.2f}".format(percent),
            " %",
            ", remaining Time : ",
            str(datetime.timedelta(seconds=estimateTime)),
            end="\r",
        )


reg = regex.compile(r"^[0-9]{4,}.*")
for file in file_list:
    fw = open("./formatted-file/new-" + file, "w", encoding="utf-8")
    print("start reading file : ", "./raw-file/" + file)
    with open(file, "r", encoding="utf-8") as fr:
        print("start counting file : ", file)
        startTime = time.time()
        for totalLine, _ in enumerate(fr):
            pass
        print("total line : ", totalLine)
        fr.seek(0)
        writeString = ""
        startTime = time.time()
        print("start rewriting file : ", file)
        for count, line in enumerate(fr):
            showProcess(count)
            line = regex.sub(r"[^\w,:\-]+", "", line)
            if not reg.match(line):
                if len(line) <= 0:
                    continue
                writeString += line
                continue
            else:
                fw.write(writeString + "\n")
                writeString = line
        print(end="\n")
    fw.close()
print("Process is ended!")

