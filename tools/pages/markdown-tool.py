import streamlit as st

st.title("Markdown Tool")
st.write("本页面用于编辑和预览markdown，可设定左右分屏或上下分屏显示。输入后在markdown底部有下载按钮，可以下载输入的文本内容。")

mode = st.checkbox("使用上下分屏")

if mode:
    # markdown输入
    markdown_input = st.text_area(
        "输入markdown",
        height=500,
        placeholder="在此处输入markdown",
        key="markdown_input",
        label_visibility="collapsed"
    )
    
    # markdown显示
    if markdown_input:
        with st.container(border=True):
            st.markdown(markdown_input)
        st.download_button("下载文本",markdown_input,file_name="download.md")

else:
    col1, col2 = st.columns([1, 1])
    with col1:
        # markdown输入
        markdown_input = st.text_area(
            "输入markdown",
            height=800,
            placeholder="在此处输入markdown",
            key="markdown_input",
            label_visibility="collapsed"
        )

    with col2:
        # markdown显示
        if markdown_input:
            with st.container(height=800):
                st.markdown(markdown_input)
            st.download_button("下载文本",markdown_input,file_name="download.md")

st.show()