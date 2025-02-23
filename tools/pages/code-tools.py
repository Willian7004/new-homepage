import streamlit as st
import os
from io import StringIO
import sys

def get_languages():
    file_path = os.path.join(os.getcwd(), 'tools', 'languages.txt')
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def run_code(code):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    try:
        exec(code)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdout = old_stdout
    return mystdout.getvalue()

st.title("Code Tools")
st.write("本项目用于编辑和运行Python代码，也可以实现对其它编写语言代码的高亮显示。可选是否进行左右分列。")

# 第一行顶部布局
col1_top, col2_top = st.columns(2)
with col1_top:
    disable_columns = st.checkbox("停用分列")
    select_other_lang = st.checkbox("选择其它语言")

# 语言选择处理
selected_lang = 'python'
if select_other_lang:
    try:
        languages = get_languages()
        with col2_top:
            selected_lang = st.selectbox("选择语言", options=languages)
    except Exception as e:
        st.error(f"无法读取语言文件: {e}")

# 主内容布局
if not disable_columns:
    main_col1, main_col2 = st.columns(2)
else:
    main_col1 = st.container()

# 输入框设置
with main_col1:
    code_height = 500 if disable_columns else 800
    code = st.text_area("输入代码", height=code_height, key="code_input")

# 结果显示处理
if code:
    lang = selected_lang.lower() if select_other_lang else 'python'
    
    # 代码高亮显示
    if not disable_columns:
        with main_col2:
            st.code(code, language=lang)
    else:
        st.code(code, language=lang)

    # 代码执行和输出
    if not select_other_lang:
        output_container = main_col2 if not disable_columns else st
        if not disable_columns:
            with output_container:
                output = run_code(code)
        else:
            output = run_code(code)

# 下载按钮
st.download_button(
    label="下载代码",
    data=code if code else "",
    file_name="user_code.txt",
    mime="text/plain"
)

st.show()