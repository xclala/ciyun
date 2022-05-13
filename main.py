try:
    from wordcloud import WordCloud
    from jieba import lcut
    from win32ui import CreateFileDialog
    from win32con import OFN_OVERWRITEPROMPT, OFN_FILEMUSTEXIST
    file_open_type = 'All File(*.*)|*.*|''|'
    d = CreateFileDialog(1, None, None,
                            OFN_OVERWRITEPROMPT | OFN_FILEMUSTEXIST,
                            file_open_type)
    d.SetOFNInitialDir('C:/')
    d.DoModal()
    path = d.GetPathName()
    encoding = input("字符编码：")
    if not encoding:
        encoding = "utf-8"
    with open(path, "r", encoding=encoding) as f:
        m = f.read()
    w = WordCloud(height=1000, width=1900, stopwords={"的", "和", "与"}, font_path=r"msyh.ttc")
    w.generate(" ".join(lcut(m)))
    w.to_file("output.png")
    print("已生成output.png")
except Exception as e:
    print(e)
