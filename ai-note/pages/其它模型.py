import streamlit as st

st.title("其它模型")
st.write("在前面提到的模型类型以外，这部分介绍一些我使用的其它一些模型类型，大多是规模比较小的模型。")
st.subheader("1.TTS模型", divider=True)
st.write("TTS模型用于语音合成。目前没有比较好的可以图形化运行TTS模型的运行框架，以前我主要使用一些模型的第三方整合包，后来看到Fish Speech可以通过官方代码以整合包形式快速部署，支持api，官方还做了Windows版本的GUI应用，生成时能按句子进行分割，就在TTS模型上改用Fish Speech。虽然不完全真实但效果优于大部分同类模型，aeficles-by-llm页面包含使用fish speech生成的内容。")

st.subheader("2.图像识别/语义分割模型", divider=True)
st.write("这是比较成熟的模型类型，不太旧的模型都有较高的准确度。新的模型的主要方向是开放词汇识别，也就是可以识别任意类型的物体。目前在ComfyUI通过YOLO World Efficient SAM部署了YOLO World和SAM实现图片分割。此外，多模态模型可以用于这类任务，速度较慢但可以生成场景描述，适合用于自然语言图片标注。")
st.subheader("3.音乐模型", divider=True)
st.write("开源音乐模型效果最好的是Yue s1，与Suno等商业模型效果相当。")

st.show()