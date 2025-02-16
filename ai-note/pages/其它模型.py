import streamlit as st

st.title("其它模型")
st.write("在前面提到的模型类型以外，这部分介绍我了解过的其它类型的模型。")

st.subheader("1.图像识别/语义分割模型", divider=True)
st.write("这是比较成熟的模型类型，不太旧的模型都有较高的准确度。新的模型的主要方向是开放词汇识别，也就是可以识别任意类型的物体。目前在ComfyUI通过YOLO World Efficient SAM部署了YOLO World和SAM实现图片分割。此外，多模态模型可以用于这类任务，速度较慢但可以生成场景描述，适合用于自然语言图片标注。")

st.subheader("2.视频增强模型", divider=True)
st.write("目前效果最好的开源视频增强模型是VEnhancer，主要用于优化AI生成的视频，理论上可以实现任意分辨率和帧率的视频增强，但显存占用较大。Topaz Video AI包含一些较轻量化的视频增强模型。")

st.subheader("3.语音识别模型", divider=True)
st.write("语音识别模型出现比较早，目前Whisper Large比较常见，新出的FireRed ASR效果更好。")

st.subheader("3.世界模型", divider=True)
st.write("这类模型相比视频模型，更偏向3D形式和可交互，场景真实性更好并且有可能代替一些实时渲染应用，不同模型有不同侧重点。Matrix-Zero（闭源）面向场景生成；Genie2（闭源）除场景外能实现一些交互功能；SceneX（仅发布论文）可以生成大规模场景；Wonderland（开源，未正式发布）也面向场景生成。已发布的开源模型包括See3D（图生3D）和DIAMOND（交互式）等。")

st.subheader("4.3D物体生成模型", divider=True)
st.write("用于单个物体生成的模型包括Hunyuan3D 2、Rudin1.5、SPAR3D、Edify 3D等，Hunyuan3D 2开源且提供动画绑定功能；Rudin1.5在生成锐利边角等方面有优势；SPAR3D也开源，生成速度快且提供编辑功能；Edify 3D也开源且注重拓扑效果。")

st.subheader("5.蛋白质结构预测模型", divider=True)
st.write("这类模型主要是AlphaFold系列，目前出到了AlphaFold3，效果超越了绝大多数专用模型和传统方法，在一些样本较少的领域也有较好表现，可能在药物开发等领域提供帮助。")

st.subheader("6.辅助驾驶模型", divider=True)
st.write("闭源的辅助驾驶模型除了车企开发的模型（如特斯拉的FSD）外，华为和大疆等企业与车企合作提供辅助驾驶功能。开源的辅助驾驶模型主要有OpenPilot，使用纯视觉方案和端到端形式，可以用于改装带有ACC的车辆。")

st.subheader("7.天气预报模型", divider=True)
st.write("用AI实现天气预报的模型有GenCast（开源）、八观（闭源）等，准确度和速度明显优于传统天气预报方法。")

st.show()