from wordcloud import WordCloud
from jieba import lcut
from tkinter import *
from tkinter.filedialog import askopenfile
from time import time
import tkinter.ttk


def encoding(filepath):
    try:
        from chardet import detect
        data = open(filepath, "rb").read()
        encoding = detect(data)["encoding"]
    except FileNotFoundError:
        encoding = "utf-8"
    return encoding


try:
    with askopenfile(encoding=encoding()) as f:
        m = f.read()
except ValueError:
    print("文件无法创建词云。")
except Exception as e:
    print(e)
try:
    start_time = time()
    root = Tk()
    bar = tkinter.ttk.Progressbar(root, length=300)
    bar.pack(side=TOP)
    bar['maximum'] = 100
    w = WordCloud(height=1000,
                  width=1900,
                  stopwords={"的", "和", "与", "-", "——", "|", "_"},
                  font_path=r"msyh.ttc")
    bar['value'] = 25
    root.update()
    m = " ".join(lcut(m))
    bar['value'] = 50
    root.update()
    w.generate(m)
    bar['value'] = 75
    root.update()
    w.to_file("output.png")
    bar['value'] = 100
    root.update()
    Label(root, text=f"用时{round(time() - start_time, 1)}秒，已生成output.png").pack(
        side=BOTTOM)
    mainloop()
except Exception as e:
    print(e)
