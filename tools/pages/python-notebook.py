import os
import json
import streamlit as st
from glob import glob
import atexit
import sys
from io import StringIO

# 初始化session state
if "paragraphs" not in st.session_state:
    st.session_state.paragraphs = []
if "edit_index" not in st.session_state:
    st.session_state.edit_index = -1
if "execution_env" not in st.session_state:
    st.session_state.execution_env = {}

# 文件路径
TOOLS_DIR = "tools"
JSON_PATH = os.path.join(TOOLS_DIR, "note.json")
PY_PATH = os.path.join(TOOLS_DIR, "note.py")

# 确保工具目录存在
os.makedirs(TOOLS_DIR, exist_ok=True)

# 清理函数
def cleanup():
    for path in [JSON_PATH, PY_PATH]:
        if os.path.exists(path):
            try:
                os.remove(path)
            except:
                pass

atexit.register(cleanup)

# 文件上传处理
def handle_upload():
    uploaded_file = st.file_uploader("上传JSON文件", type=["json"])
    if uploaded_file is not None:
        with open(JSON_PATH, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state.paragraphs = []
        st.rerun()

# 下载处理
def handle_download():
    with open(JSON_PATH, "rb") as f:
        st.download_button("下载JSON文件", f, file_name="note.json")
    
    if st.button("转换并下载PY文件"):
        py_content = ["import streamlit as st"]
        for p in st.session_state.paragraphs:
            if p["type"] == "python":
                py_content.append(p["content"])
        
        with open(PY_PATH, "w") as f:
            f.write("\n\n".join(py_content))
        
        with open(PY_PATH, "rb") as f:
            st.download_button("下载PY文件", f, file_name="note.py")

# 保存段落到JSON
def save_to_json():
    with open(JSON_PATH, "w") as f:
        json.dump(st.session_state.paragraphs, f, indent=2)

# 执行Python代码并捕获输出
def execute_python(code):
    try:
        # 重定向标准输出
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        # 在新的子字典中执行代码以保持变量隔离但可继承
        new_env = st.session_state.execution_env.copy()
        exec(code, new_env)
        st.session_state.execution_env.update(new_env)
        # 获取执行输出
        execution_output = new_stdout.getvalue()
        if execution_output:
            return(execution_output)
    except Exception as e:
        return f"执行错误: {str(e)}" 

# 启动时加载已有数据
if os.path.exists(JSON_PATH):
    try:
        with open(JSON_PATH) as f:
            st.session_state.paragraphs = json.load(f)
    except:
        st.session_state.paragraphs = []

st.title("代码笔记管理器")
    
# 文件上传
handle_upload()

# 输入组件
is_python = st.toggle("输入代码", value=False)
input_content = st.text_area("输入内容", height=300, key="input")

# 处理确认按钮
if st.button("确认段落"):
    if input_content.strip():
        new_para = {
            "type": "python" if is_python else "markdown",
            "content": input_content,
            "output": ""
        }
        
        if st.session_state.edit_index >= 0:
            # 更新现有段落
            index = st.session_state.edit_index
            st.session_state.paragraphs[index] = new_para
            st.session_state.edit_index = -1
        else:
            # 添加新段落
            st.session_state.paragraphs.append(new_para)
        
        # 执行Python代码
        if new_para["type"] == "python":
            new_para["output"] = execute_python(new_para["content"])
        
        save_to_json()
        st.rerun()

# 显示所有段落
for index, para in enumerate(st.session_state.paragraphs):
    # 显示内容
    if para["type"] == "markdown":
        st.markdown(para["content"])
    else:
        st.code(para["content"], language="python")
        if para["output"]:
            st.write("执行结果:")
            st.code(para["output"])
    
    # 编辑按钮
    if st.button(f"编辑段落 {index+1}", key=f"edit_{index}"):
        st.session_state.edit_index = index
        st.session_state.input = para["content"]
        st.rerun()
    
    st.divider()

# 文件下载
handle_download()
    
st.show()    