import streamlit as st
import os
import sys
from io import StringIO

def load_languages():
    """从languages.txt加载可用语言列表"""
    try:
        file_path = os.path.join("tools", "languages.txt")
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        st.error("找不到languages.txt文件")
        return []
    except Exception as e:
        st.error(f"读取语言文件时出错: {e}")
        return []

st.title("Code Tools")
st.write("本项目用于编辑和运行Python代码，也可以实现对其它编写语言代码的高亮显示")
    
# 初始化session_state
if "selected_lang" not in st.session_state:
    st.session_state.selected_lang = "python"

# 第一行布局
col1, col2 = st.columns([1, 3])
with col1:
    show_lang = st.checkbox("选择其它语言")

# 处理语言选择
languages = []
if show_lang:
    languages = load_languages()
    with col2:
        if languages:
            st.session_state.selected_lang = st.selectbox(
                "选择语言",
                options=languages,
                index=0,
                label_visibility="collapsed"
            )
        else:
            st.write("没有可用的语言选项")

# 代码输入区域
code_input = st.text_area(
    "输入代码",
    height=400,
    placeholder="在此处输入您的代码...",
    key="code_input",
    label_visibility="collapsed"
)

# 显示高亮代码
if code_input:
    display_lang = st.session_state.selected_lang if show_lang else "python"
    st.subheader("代码预览")
    st.code(code_input, language=display_lang.lower())

# 执行Python代码（当未选择其他语言时）
if not show_lang and code_input:
    st.subheader("执行结果")
    output_container = st.container()
    
    # 重定向标准输出
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    try:
        # 使用隔离的命名空间执行代码
        exec_namespace = {}
        exec(code_input, exec_namespace)
    except Exception as e:
        output_container.error(f"执行错误: {str(e)}")
    finally:
        sys.stdout = old_stdout  # 恢复标准输出
    
    # 获取执行输出
    execution_output = new_stdout.getvalue()
    if execution_output:
        output_container.code(execution_output)

st.show()