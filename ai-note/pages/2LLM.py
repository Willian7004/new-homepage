import streamlit as st

st.title("LLM")
st.subheader("1.旗舰模型", divider=True)
st.write("旗舰模型参数量较大，运行成本较高但可完成的任务也较多。Deepseek v3算是的一个下一代模型，而其它厂商的下一代模型，包括Grok3和GPT5均未发布，因此Deepseek v3具有性能优势，也是第一个发布时性能超越所有闭源模型的开源模型，并且通过混合专家架构避免成本过高。以下是几个模型的对比")
import pandas as pd
df = pd.DataFrame({
    "模型": ["Deepseek v3", "MiniMax Text01","Gemini2.0 Flash exp","Qwen2.5 72B", "Llama3.1 405B", "Claude3.5 Sonnet", "GPT-4o"],
  "架构": ["MoE", "MoE",None,"Dense", "Dense", None, None],
    "激活参数": ["37B","45.9B",None, "72B", "405B",None, None],
    "总参数": ["671B", "456B",None,"72B", "405B", None, None],
    "MMLU": [88.5, 88.5,86.5,85.3, 88.6, 88.3, 87.2],
    "MMLU-Redux": [89.1,None,None, 85.6, 86.2, 88.9, 88],
    "MMLU-Pro": [75.9, 75.7,76.4,71.6, 73.3, 78, 72.6],
    "DROP": [91.6,87.8, 76.7, 87.8,88.7, 88.3, 83.7],
    "IF-Eval": [86.1,89.1, 84.1,88.4, 86, 86.5, 84.3],
    "GPQA-Diamond": [59.1,54.4, 62.1,49, 51.1, 65, 49.9],
    "SimpleQA": [24.9,23.7, 26.6,9.1, 17.1, 28.4, 38.2],
    "FRAMES": [73.3, None,None,69.8, 70, 72.5, 80.5],
    "LongBenchv2": [48.7, 52.9,None,39.4, 36.1, 41, 48.1],
    "HumanEval": [92.1, 86.9,89.6,86.6, 89.0, 93.7, 90.2],
    "LiveCodeBench(cot)": [40.5,None, 35.1,31.1, 28.4, 36.3, 33.4],
    "LiveCodeBench(Pass@1)": [37.6, None,None,28.7, 30.1, 32.8, 34.2],
    "Codeforces": [51.6, None,None,24.8, 25.3, 20.3, 23.6],
    "SWEVerified": [42, None,None,23.8, 24.5, 50.8, 38.8],
    "Aider-Edit": [79.7,None, None,65.4, 63.9, 84.2, 72.9],
    "Aider-Polyglot": [49.6,None,None, 7.6, 5.8, 45.3, 16],
    "AIME2024": [39.2, None,None,23.3, 23.3, 16, 9.3],
    "MATH-500": [90.2, None,None,80, 73.8, 78.3, 74.6],
    "CNMO2024": [43.2, None,None,15.9, 6.8, 13.1, 10.8],
    "CLUEWSC": [90.9, None,None,91.4, 84.7, 85.4, 87.9],
    "C-Eval": [86.5, None,None,86.1, 61.5, 76.7, 76],
    "C-SimpleQA": [64.1,67.4,63.3, 48.4, 50.4, 51.3, 59.3]
})

df

st.subheader("2.多模态模型", divider=True)
st.write("多模态模型开源处理图片。对于非思维链模型，闭源模型中Claude3.5 Sonnet表现最好，开源模型中MiniMax VL01表现最好。对于思维链模型，闭源模型中o1表现最好，开源模型中QvQ 72B Preview表现最好。以下是几个模型的对比")
df2= pd.DataFrame({
     "Model": ["QvQ-72B-preview", "OpenAI o1","GPT-4o", "Claude-3.5-Sonnet", "Gemini1.5 Pro", "Gemini2.0 Flash exp", "Qwen2.5VL 72B", "InternVL 2.5 78B", "Llama3.2 90B","MiniMax VL01"],
    "MMLU": [70.3,77.3,63.5, 72.0, 68.4, 70.6, 64.5, 66.5, 62.1,68.5],
    "MMNU-Pro*": [None,None,54.5, 54.7, 50.9, 57.0, 43.2, 47.3, 36.0,52.7],
    "ChartQA": [None,None,88.1, 90.8, 88.7, 88.3, 91.2, 91.5, 85.5,91.7],
    "DocVQA*": [None,None,91.1, 94.2, 91.5, 92.9, 97.1, 96.1, 90.1,96.4],
    "OCRBench": [None,None,806, 790, 800, 846, 856, 847, 805,865],
    "AI2D": [None,None,83.1, 82.0, 80.9, 85.1, 84.4, 86.8, 78.9,83.3],
    "MathVista*": [70.4,71.0,62.1, 65.4, 70.6, 73.1, 69.6, 68.4, 57.3,68.6],
    "OlympiadBench": [20.4,None,25.2, 28.4, 32.1, 46.1, 21.9, 25.1, 19.3,24.2],
    "M-LongDoc": [None,None,41.4, 31.4, 26.2, 31.4, 11.6, 19.7, 13.9,32.5],
    "MEGA-Bench": [None,None,49.4, 51.4, 45.9, 53.9, 46.8, 45.3, 19.9,47.4],
    "In-house Benchmark": [None,None,62.3, 47.0, 49.2, 72.1, 40.6, 34.8, 13.6,56.6]
})

df2

st.subheader("3.思维链模型", divider=True)
st.write("思维链模型可以通过增加推理步骤来提高性能。目前最优秀的闭源思维链模型是OpenAI o1，最优秀的开源思维链模型是Deepseek R1，其蒸馏版本在本地部署上有优势。以下是几个模型的对比（由于不少模型不是同时测试，表中只保留了有较多模型进行的测试，另外使用非思维链模型中表现最好的Deepseek v3作为对照）")
df3= pd.DataFrame({
     "Model": ["DeepSeek-R1","DeepSeek-R1-Distill-Qwen-1.5B","DeepSeek-R1-Distill-Qwen-7B","DeepSeek-R1-Distill-Qwen-14B","DeepSeek-R1-Distill-Qwen-32B","QwQ-32B-Preview","OpenAI o1","o1 mini","o3","o3 mini(high)","Deepseek v3"],
    "AIME2024": [79.8,28.9,55.5,69.7,72.6,44.0,83.3,63.6,96.7,83.6,39.2],
    "GPQA Diamond": [71.5,33.8,49.1,59.1,62.1,54.5,78.0,60.0,87.7,70.0,59.1],
    "Codeforces(rating)": [None,954,1189,1481,1691,1316,1891,1820,2727,None,None],
     "Codeforces(percentile)": [96.3,None,None,None,90.6,None,96.6,93.4,None,None,58.7],
    "LiveCodeBench": [None,16.9,37.6,53.1,57.2,41.9,None,53.8,None,None,40.5],
     "SWE-Bench": [49.2,None,None,None,36.8,None,48.9,41.6,None,None,42.0]
})

df3
st.write("表中的OpenAI o3系列只开放了安全测试，还没有正式发布。o3 mini相比o1系列有性价比优势，o3在ARC AGI测试能达到人类水平，但成本高于人工。目前o3 mini即将发布，但出现o3可能在泄露的Frontier Math数据集训练的消息。")

st.subheader("4.小型化旗舰模型", divider=True)
st.write("有几个系列的模型在有模型达到GPT4水平后开始小型化并保持性能，其中闭源模型主要有Gemini2.0 Flash和Yi Lighting，开源模型主要有phi4，14b参数量适合在PC部署。")
st.subheader("5.端侧模型", divider=True)
st.write("端侧模型用于手机或在PC后台运行，主要考虑7b和3b参数量，并且只能使用开源模型。考虑多语言后有优势的多模态模型有Qwen2 VL 7B和Megrez 3B Omni，单模态模型有Qwen2.5 7B和Qwen2.5 3B。")
st.subheader("6.无审查模型", divider=True)
st.write("比较新的模型大部分进行了对齐，可以避免生成不道德的内容，但在角色扮演等用途仍需要未对齐的模型，在写作中未对齐的模型也有更好的表现。")
st.write("目前效果最好的无审查模型是旧版CommandR和CommandR+，官方版本是未对齐的。另外大部分常见模型有第三方的去对齐版本。")
st.subheader("7.长序列模型", divider=True)
st.write("处理或生成较长的文章需要支持较大输入或输出上下文长度的模型，考虑对api成本的影响，这类只讨论开源模型。目前比较好的开源长上下文模型是InternLM2.5 7b 1M和GLM4 9b 1M。长输出模型只有使用longwriter数据集微调的模型，目前只有GLM4 9b、Qwen2.5 7B和Llama3.1 8b。")
st.subheader("8.模型部署", divider=True)
st.write("有多个运行框架可以部署LLM，我目前用的是Ollama。Ollama的优势是安装比较方便，还可以直接在命令行下载量化后的模型。")
st.write("Ollama没有GUI但可以通过http请求或使用Python和Javascript等语言的库文件整或到应用中。我目前通过Chatbox使用Ollama的单模态模型和调用线上模型的api。调用Ollama的多模态模型开始时用了Openwebui，但由于需要在安装时部署嵌入模型，比较麻烦，就改用了使用Streamlit开发的Local Multimodal AI Chat。Local Multimodal AI Chat可以调用Ollama的多模态模型和嵌入模型，虽然有不支持流式响应和运行慢的问题，但由于部署方便还是考虑替换Openwebui。")
st.write("我目前部署的模型有phi4、MiniCPM v2.6（用于多模态，效果更好的Qwen2 VL 7b目前还不能在Ollama运行）、InternLM2.5 7b（用于长序列）。嵌入模型用了Bge-m3，支持多语言，在嵌入模型中参数量较大，性能也较高。")
st.show()