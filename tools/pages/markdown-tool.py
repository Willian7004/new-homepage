import streamlit as st
import re
from io import StringIO
import sys

st.title("Markdown Tool")
st.write("本页面用于编辑和预览markdown，可设定左右分屏或上下分屏显示。另外可以选择执行markdown中的python程序，可以下载.md文件或转换后的.py文件（文本转换为注释）")

# 初始化执行环境
if "env" not in st.session_state:
    st.session_state.env = {}

# 创建复选框
col1, col2 = st.columns(2)
disable_split = col1.checkbox("停用分列")
execute_code = col2.checkbox("执行代码")

# 布局设置
input_content = ""
if not disable_split:
    col_left, col_right = st.columns(2)
    with col_left:
        input_content = st.text_area("输入内容",placeholder="在此处输入markdown", height=800, key="input_left",label_visibility="collapsed")
    container = col_right.container(height=800)
else:
    input_content = st.text_area("输入内容", placeholder="在此处输入markdown",height=500, key="input_full",label_visibility="collapsed")
    container = st.container(border=True)

# 处理内容显示和下载
with container:
    if execute_code:
        # 分割代码块和普通文本
        parts = re.split(r'```python\n(.*?)\n```', input_content, flags=re.DOTALL)
        
        md_content = []
        py_content = []
        code_outputs = []

        for i, part in enumerate(parts):
            if i % 2 == 0 and part.strip():  # 普通文本
                st.markdown(part)
                md_content.append(part)
                py_content.append(f'"""\n{part}\n"""\n')
            elif i % 2 == 1:  # 代码块
                code = part.strip()
                if code:
                    # 显示代码
                    st.markdown(f"```python\n{code}\n```")
                    md_content.append(f"```python\n{code}\n```")
                    py_content.append(f"{code}\n")

                    # 执行代码
                    try:
                        buffer = StringIO()
                        sys.stdout = buffer
                        exec(code, st.session_state.env)
                        sys.stdout = sys.__stdout__
                        output = buffer.getvalue()
                        
                        if output:
                            st.code(output)
                            md_content.append(f"\n输出：\n```\n{output}\n```")
                            code_outputs.append(output)
                    except Exception as e:
                        st.error(f"执行错误：{str(e)}")
                        md_content.append(f"\n错误：\n```\n{str(e)}\n```")
        
        md_content = "\n".join(md_content)
        py_content = "\n".join(py_content)
       
        # 创建下载按钮
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="下载.md文件",
                data=md_content,
                file_name="output.md",
                mime="text/markdown"
            )
        with col2:
            st.download_button(
                label="下载.py文件",
                data=py_content,
                file_name="output.py",
                mime="text/plain"
            )
    else:
        # 未执行代码模式
        st.markdown(input_content)
        st.download_button(
            label="下载.md文件",
            data=input_content,
            file_name="output.md",
            mime="text/markdown"
        )

st.show()