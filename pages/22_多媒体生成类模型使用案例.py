import streamlit as st
st.set_page_config(layout="wide")
st.title("多媒体生成类模型使用案例")
st.write("相比复杂的工作流，我更偏向使用功能完善的模型通过较简单的流程做到较好的效果。由于之前生成的内容已发布到社交媒体，为了避免内容重复，这里只展示新生成的内容。之前的图片内容发布在https://www.xiaohongshu.com/user/profile/6605a535000000000b00c4d2? ，视频内容发布在https://space.bilibili.com/478036060? 和https://www.acfun.cn/u/76077623 （包含其它类型的图片和视频）")

st.subheader("1.绘画模型", divider=True)
st.write("（考虑光照问题，已弃用Flux.1，因此案例未整合到当前项目）Gallery Without Prompt项目，展示使用由Flux.1 dev文生图再由Flux.1 schnell图生图的流程在不填写提示词时得到的图片： https://william7004-gallery-without-prompt.streamlit.app")
st.write("AI图片页面展示了使用Hunyuan Video生成的图片，复用了以前使用Flux.1的提示词并添加了一些新的内容。")

st.subheader("2.视频模型", divider=True)
st.write("（由于视频生成改用cosmos，gallery页面将改用cosmos生成的视频，hunyuan video生成的部分改为指向初始项目，并在初始项目合并新增内容，下同）Hunyuan Video Gallery Without Prompt项目，展示使用Hunyuan Video在不填写提示词时得到的图片和视频： https://william7004-hunyuan-video-gallery-without-prompt.streamlit.app/")
st.write("Hunyuan Video Gallery 项目，展示使用Hunyuan Video在有提示词时生成的视频： https://william7004-hunyuan-video-gallery.streamlit.app/")
st.write("AI视频页面展示使用Wan2.1 1.3b生成的视频，复用了之前使用其它模型生成的发布在社交平台的视频的提示词并添加了一些新的内容。")

st.subheader("3.TTS模型", divider=True)
st.write("LLM散文集页面包含使用Fish Speech1.5合成的音频。")

st.subheader("4.音乐模型", divider=True)
st.write("AI音乐页面包含使用YuE生成的音乐。")

