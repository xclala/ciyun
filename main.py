from wordcloud import WordCloud
from jieba import lcut,setLogLevel
from win32ui import CreateFileDialog
from win32con import OFN_OVERWRITEPROMPT, OFN_FILEMUSTEXIST
from progress.bar import Bar
file_open_type = 'All File(*.*)|*.*|''|'
d = CreateFileDialog(1, None, None,
                        OFN_OVERWRITEPROMPT | OFN_FILEMUSTEXIST,
                        file_open_type)
d.SetOFNInitialDir('C:/')
d.DoModal()
path = d.GetPathName()
encoding = input("字符编码：")
bar = Bar('生成中', max=7)
if not encoding:
    encoding = "utf-8"
bar.next()
try:
    with open(path, "r", encoding=encoding) as f:
        m = f.read()
    bar.next()
except FileNotFoundError:
    print("您未选择文件，无法生成词云。")
except UnicodeDecodeError:
    print("字符编码错误。")
w = WordCloud(height=1000, width=1900, stopwords={"的", "和", "与", "-", "——", "|"}, font_path=r"msyh.ttc")
bar.next()
setLogLevel(60)
bar.next()
m = " ".join(lcut(m))
bar.next()
w.generate(m)
bar.next()
w.to_file("output.png")
bar.next()
bar.finish()
print("已生成output.png")