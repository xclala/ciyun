from wordcloud import WordCloud
from jieba import lcut,setLogLevel
from tkinter import *
from tkinter.filedialog import askopenfile
import tkinter.ttk

try:
    with askopenfile() as f:
        m = f.read()
except ValueError:
    print("文件无法创建词云。")
except (UnicodeEncodeError, UnicodeDecodeError):
    print("文件编码错误，本程序只支持utf-8。")
except Exception as e:
    print(e)
try:
    root = Tk()
    bar = tkinter.ttk.Progressbar(root, length=200)
    bar.pack(side=TOP)
    bar['maximum'] = 100
    w = WordCloud(height=1000, width=1900, stopwords={"的", "和", "与", "-", "——", "|", "_"}, font_path=r"msyh.ttc")
    setLogLevel(60)
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
    Label(root, text="已生成output.png").pack(side=BOTTOM)
    mainloop()
except Exception as e:
    print(e)