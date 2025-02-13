import streamlit as st

st.title("LLM使用案例")
st.write("使用LLM查询一些难以使用搜索引擎检索的问题的记录，相关内容发布在：https://william7004-llm-inquiry.streamlit.app ，这里不另作展示。")
st.subheader("1.思维链模型解题", divider=True)
st.write("这里使用的模型是Deepseek-R1-Lite-Preview，所有题目回答正确。")
with open("ai-note/files/题目1.txt", "r", encoding='utf-8') as f:
            t1= f.read()
with st.container(height=240):
    st.write(t1)
with open("ai-note/files/题目2.txt", "r", encoding='utf-8') as f:
            t2= f.read()
with st.container(height=240):
    st.write(t2)
with open("ai-note/files/题目3.txt", "r", encoding='utf-8') as f:
            t3= f.read()
with st.container(height=240):
    st.write(t3)
st.subheader("2.编程", divider=True)
st.write("如果有详细的提示词，非思维链模型可以编写大部分程序，使用思维链模型可以适度精简提示词或改为描述功能。我的github仓库中包含llm辅助编程的对话记录，除嵌入式和c语言外大部分仓库包含llm辅助编写的程序。")
st.subheader("3.短文写作", divider=True)
st.write("deepseek r1使用了纯rl，在写作上有较大优势。相关内容放到articles-by-llm部分。")

st.show()