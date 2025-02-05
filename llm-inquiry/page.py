import streamlit as st
import os

with st.expander("LLM Inquiry （展开项目说明）"):
    st.write("本项目用于展示我使用LLM查询一些难检索的问题的记录。一些问题由于位于一个关键词所包含的内容的细节、涉及多个搜索关键词的内容或需要查找的历史内容被新闻覆盖，使用LLM回答相比搜索引擎有优势。本项目主要展示我使用LLM解答的这类问题，总体偏向杂谈形式。内容筛选方面，排除了一些可能出现事实错误的回答。使用的LLM包括deepseek v2.5、deepseek v3和deepseek r1 lite preview。")

# 获取当前目录下files文件夹中的所有.md文件
def get_md_files():
    files_dir = os.path.join(os.getcwd(), 'llm-inquiry/files')
    if not os.path.exists(files_dir):
        os.makedirs(files_dir)
    md_files = [f for f in os.listdir(files_dir) if f.endswith('.md')]
    return md_files

# 根据.md文件数量生成下拉菜单选项
def generate_options(md_files):
    file_count = len(md_files)
    options = []
    for i in range(0, file_count, 10):
        start = i + 1
        end = min(i + 10, file_count)
        options.append(f"{start}-{end}")
    return options

# 读取并显示选定的.md文件内容
def display_selected_files(md_files, selected_range):
    start, end = map(int, selected_range.split('-'))
    files_dir = os.path.join(os.getcwd(), 'llm-inquiry/files')
    for i in range(start, end + 1):
        file_name = f"{i}.md"
        if file_name in md_files:
            file_path = os.path.join(files_dir, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                with st.container(height=360):
                    st.write(content)

md_files = get_md_files()
options = generate_options(md_files)

if options:
    selected_range = st.selectbox("选择文件范围", options)
    display_selected_files(md_files, selected_range)
else:
    st.write("files文件夹中没有.md文件。")
st.show()