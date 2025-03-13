import streamlit as st
st.set_page_config(layout="wide")
st.title("多媒体生成类模型")
st.write("为了调整内容分布，这里把AIGC领域较常用的几类模型放到这一部分，相比之前添加了音频类模型，统称多媒体生成类模型，移除了不常用的视频增强模型。")
st.subheader("1.绘画模型", divider=True)
st.write("由于早期的绘画模型都是开源模型并且有工作流的积累，虽然一些闭源绘画模型在测试中表现更好，但开源绘画模型一直是主流，本文暂时只讨论开源绘画模型。")
st.write("开源绘画模型中主流的有Flux.1和Stable Diffusion3.5。考虑光照优势，我个人偏向使用Hunyuan Video进行图片生成，不过只能达到1600x896分辨率，而Flux.1 Schnell在2560x1440分辨率可用。")

st.subheader("2.视频模型", divider=True)
st.write("视频模型分为高成本和低成本路线。开源模型方面，Wan2.1系列在运动效果和出片率等方面有优势，14b版本需要高端卡以满足显存需求并保证生成速度，1.3b版本场景细节差一些但低端卡也有比较好的生成速度。闭源模型方面，可灵1.6成本适中，总体效果也比较好但运动物体画质差一些；Veo2成本高，在运动物体画质和分辨率方面有优势。")
st.write("一些视频模型有一些有优势的特性。不少闭源模型提供了一致性控制功能，开源模型少一些但在Hunyuan Video Wrapper插件提供了一些。创作长视频需要保证不同片段的一致性，Sora虽然生成效果没有优势，但提供了story board功能，可以实现多个片段的内容一致。Meta开发了VideoJam（未正式发布），在运动场景生成效果最好，并且可以用于改进现有模型。")

st.subheader("3.TTS模型", divider=True)
st.write("TTS模型用于语音合成。目前没有比较好的可以图形化运行TTS模型的运行框架，以前我主要使用一些模型的第三方整合包，后来看到Fish Speech可以通过官方代码以整合包形式快速部署，支持fastapi，官方还做了Windows版本的GUI应用，生成时能按句子进行分割，就在TTS模型上改用Fish Speech。虽然不完全真实但效果优于大部分同类模型。显存占用约2g，部署门槛比较低。另外，Zonos v0.1等模型搭配了LLM，可以更好地处理语气；Kokoro 82m参数量小，推理更快。不过考虑到方面部署和使用，还是继续用Fish Speech。")

st.subheader("4.音乐模型", divider=True)
st.write("开源音乐模型效果最好的是YuE，与Suno等商业模型效果相当。DiffRhythm速度更快，但上下文衔接差一些。算力不太低的话用YuE比较合适。")

st.subheader("4.模型部署", divider=True)
st.write("绘画模型、视频模型和一些其它类型的模型一般使用ComfyUI部署。主要优势是有显存优化并且可以提供插件适配更多模型。为了方便管理插件和运行环境，可以使用绘世等第三方整合包。音乐模型方面，Comfyui只能用效果比较差的Stable Audio Open，Yue s1需要用官方代码部署，显存要求10g以上并且随音轨数增加，相对难以普及。")

