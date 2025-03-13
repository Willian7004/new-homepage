import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title("LLM")
st.subheader("1.旗舰模型", divider=True)
st.write("旗舰模型参数量较大，运行成本较高但可完成的任务也较多。Deepseek v3算是第一个下一代模型，也是第一个发布时性能超越所有闭源模型的开源模型，通过混合专家架构避免成本过高，但后面发布的Gemini2.0Flash控制了参数量，在成本上有一定优势。Grok3是总体效果最好的模型并且开放免费使用，Claude3.7 Sonnet在编程上有优势。为了方便对比和减少落后测试集，数据合并到推理模型部分。")

st.subheader("2.多模态模型", divider=True)
st.write("多模态模型开源处理图片。对于非思维链模型，闭源模型中Claude3.5 Sonnet表现最好，开源模型中MiniMax VL01表现最好。对于思维链模型，闭源模型中o1表现最好，开源模型中QvQ 72B Preview表现最好。以下是几个模型的对比")
df1 = pd.read_excel("files/多模态模型.xlsx")
st.dataframe(df1)
st.write("早期的多模态模型大多只支持文本和图像，GPT 4o首次支持语音。在开源模型方面，MiniCPM v2.6 o通过整合不同模型实现对文本、视频和语音的支持，原生支持文本和语音的有Step Audio，原生支持文本、视频和语音的模型中最好的开源模型是Ola 7b。")

st.subheader("3.推理模型", divider=True)
st.write("推理模型可以通过增加推理步骤来提高性能。目前最优秀的闭源推理模型是Grok3 Reasoning系列，基本能对标未发布的o3，最优秀的开源推理模型是Deepseek R1。本地部署Qwq 32b比较有优势，也解决了Deepseek R1小说写作过度使用科幻元素以及蒸馏版写作风格不一致的问题，小参数量的参考下表。考虑模型性能，在通用任务中不推荐使用小参数量非推理模型，后文中已移除相关数据。由于不少模型不是同时测试，表中只保留了有较多模型进行的测试。beat of 64测试的结果写到括号内。")
df2 = pd.read_excel("files/旗舰模型和推理模型.xlsx")
st.dataframe(df2)

st.subheader("4.无审查模型", divider=True)
st.write("比较新的模型大部分进行了对齐，可以避免生成不道德的内容，但在角色扮演等用途仍需要未对齐的模型。")
st.write("目前效果最好的官方无审查模型是旧版CommandR和CommandR+，但考虑到模型较旧，实际部署时可能要优先使用比较新的模型的去对齐版本。")

st.subheader("5.长序列模型", divider=True)
st.write("处理或生成较长的文章需要支持较大输入或输出上下文长度的模型，考虑对api成本的影响，这类只讨论开源模型。目前比较好的开源长上下文模型有Qwen2.5 7b/14b、InternLM2.5 7b和GLM4 9b的长上下文版本。长输出模型只有使用longwriter数据集微调的模型，目前只有GLM4 9b、Qwen2.5 7B和Llama3.1 8b。")

st.subheader("6.模型部署", divider=True)
st.write("有多个运行框架可以部署LLM，我目前用的是Ollama。Ollama的优势是安装比较方便，还可以直接在命令行下载量化后的模型。对于其它框架，vLLM的优势是并发性能好以及支持多GPU张量并行；kTransformers的优势是通过异构计算优化MoE模型的显存占用；Mlx Vlm适用于Mac平台，对多模态模型支持较好；ChatterUI适用于安卓平台。Xinference整合了一些推理框架，除LLM外还支持语音合成等类型的模型。")
st.write("Ollama没有GUI但可以通过http请求或使用Python和Javascript等语言的库文件整或到应用中。Chatbox可以直接调用Ollama的非多模态模型并通过openai api格式调用多模态模型。")
st.write("我目前在电脑部署的模型有Deepseek R1 Distill Qwen 7b Ablicated（去对齐）、MiniCPM v2.6（用于多模态，效果更好的Qwen2 VL 7b目前还不能在Ollama运行）、Bge-m3（嵌入模型）。在手机部署的模型有Deepseek R1 Distill Qwen 1.5b和Dolphin3 3b。")

