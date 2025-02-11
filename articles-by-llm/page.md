使用streamlit写一个程序，实现以下功能：

1.在第一行左半部分创建下拉菜单，有“选择页面”、“随机”、“搜索”3个选项。

2.当前目录下files文件夹中有多个txt文件以及相同名称的mp3文件，按名称排列文件。对于每个txt文件，使用st.subheader显示文件名（不含扩展名），在下方依次显示对应的mp3文件（没有同名mp3文件时留空）并创建高度为400像素的文本框用于txt文件的内容。

3.下拉菜单选中“选择页面”时，每一页显示10个文件，并在第一行右半部分创建一个下拉菜单用于选择页数。

4.下拉菜单选中“随机”时，随机显示10个文件。

5.下拉菜单选中“搜索”时，在第一行右半部分创建输入框，显示文件名与输入框中字符匹配的文件。


以下是根据需求编写的Streamlit程序代码：

```python
import streamlit as st
import os
import random
from pathlib import Path

# 获取文件列表
def get_files():
    files_dir = Path("files")
    txt_files = sorted(files_dir.glob("*.txt"))
    return txt_files

# 显示文件内容
def display_file(file_path):
    # 显示文件名
    file_name = file_path.stem
    st.subheader(file_name)
    
    # 显示MP3文件
    mp3_path = file_path.with_suffix(".mp3")
    if mp3_path.exists():
        st.audio(str(mp3_path))
    
    # 显示文本内容
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    st.text_area("内容", content, height=400, key=file_name)

# 主程序
def main():
    st.set_page_config(layout="wide")
    txt_files = get_files()
    
    # 第一行布局
    col1, col2 = st.columns([1, 1])
    with col1:
        mode = st.selectbox("选择模式", ["选择页面", "随机", "搜索"], label_visibility="collapsed")
    
    # 根据模式处理文件列表
    if mode == "选择页面":
        total_pages = (len(txt_files) + 9) // 10
        with col2:
            page = st.selectbox("选择页数", range(1, total_pages + 1)) - 1
        files_to_show = txt_files[page*10 : (page+1)*10]
    
    elif mode == "随机":
        files_to_show = random.sample(txt_files, min(10, len(txt_files)))
    
    elif mode == "搜索":
        with col2:
            search_term = st.text_input("输入搜索关键词")
        files_to_show = [f for f in txt_files if search_term.lower() in f.stem.lower()]
    
    # 显示文件内容
    for file_path in files_to_show:
        display_file(file_path)

if __name__ == "__main__":
    main()
```

使用说明：
1. 在程序同级目录下创建`files`文件夹
2. 在files文件夹中放置多个txt文件及同名mp3文件
3. 安装依赖：`pip install streamlit`
4. 运行程序：`streamlit run app.py`

程序功能说明：
1. 支持三种显示模式：分页浏览、随机显示、搜索过滤
2. 自动检测并显示同名mp3文件
3. 文本内容显示在可滚动文本框中（400像素高度）
4. 分页模式下每页显示10个文件
5. 搜索模式支持文件名模糊匹配（不区分大小写）

注意事项：
1. 请确保所有txt文件使用UTF-8编码
2. mp3文件需要与对应txt文件同名
3. 如果没有mp3文件时，音频部分会自动留空
4. 搜索模式支持部分匹配文件名（如输入"doc"可以匹配"document1.txt"）