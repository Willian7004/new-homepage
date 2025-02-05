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
st.write("如果有详细的提示词，非思维链模型可以编写大部分程序，使用思维链模型可以适度精简提示词或改为描述功能。我在https://william7004-homepage.streamlit.app 提及的我的github仓库中包含提示词的为使用LLM辅助编写的程序。大多使用deepseek coder v2及之后的deepseek模型。")
st.subheader("3.短文写作", divider=True)
st.write("我部署LLM后经常使用介绍一个地点的指令进行测试，这部分的文章也来源于这项流程。个人感觉Qwen2 72b在写作上比较优秀，后面的模型引入了不少指令数据后反而导致在写作上缺少亮点。")
with open("ai-note/files/qwen2底特律.txt", "r", encoding='utf-8') as f:
            t4= f.read()
with st.container(height=240):
    st.write(t4)
with open("ai-note/files/qwen2威尼斯.txt", "r", encoding='utf-8') as f:
            t5= f.read()
with st.container(height=240):
    st.write(t5)
with open("ai-note/files/qwen2乌鲁木齐.txt", "r", encoding='utf-8') as f:
            t6= f.read()
with st.container(height=240):
    st.write(t6)
st.subheader("4.长文写作", divider=True)   
st.write("使用longwriter模型可以直接生成长文，个人感觉longwriter GLM4 9b效果相对较好，但由于参数量较小，实际效果不太好。")
with open("ai-note/files/longwriter glm4 9b法国介绍.txt", "r", encoding='utf-8') as f:
            t7= f.read()
with st.container(height=240):
    st.write(t7)
with open("ai-note/files/longwriter glm4 9b曲速航天 .txt", "r", encoding='utf-8') as f:
            t8= f.read()
with st.container(height=240):
    st.write(t8)    
st.write("对于各部分关联较小的游记等文章，可以生成摘要并分别生成各部分，以下文章使用deepseek v2生成。")
with open("ai-note/files/deepseek-v2美国游记.txt", "r", encoding='utf-8') as f:
            t9= f.read()
with st.container(height=240):
    st.write(t9)
with open("ai-note/files/deepseek-v2法国游记.txt", "r", encoding='utf-8') as f:
            t10= f.read()
with st.container(height=240):
    st.write(t10)
st.write("对于小说等各部分关联较大的文章，需要向模型输入上下文和各部分摘要，以下文章使用上述的小说agent项目调用deepseek v2.5生成，目前该项目仍不完善，生成时部分章节内容重复。")
with open("ai-note/files/极速梦想.txt", "r", encoding='utf-8') as f:
            t11= f.read()
with st.container(height=240):
    st.write(t11)
st.show()