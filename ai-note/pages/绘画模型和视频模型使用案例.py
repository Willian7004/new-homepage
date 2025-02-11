import streamlit as st

st.title("绘画模型和视频模型使用案例")
st.write("相比复杂的工作流，我更偏向使用功能完善的模型通过较简单的流程做到较好的效果。这部分也只展示文生图和文生视频流程得到的内容。由于之前生成的内容已发布到社交媒体，为了避免内容重复，这里只展示新生成的内容。之前的图片内容发布在https://www.xiaohongshu.com/user/profile/6605a535000000000b00c4d2? ，视频默内容发布在https://space.bilibili.com/478036060? 和https://www.acfun.cn/u/76077623 （包含其它类型的图片和视频）")

st.write("Gallery Without Prompt项目，展示使用由Flux.1 dev文生图再由Flux.1 schnell图生图的流程在不填写提示词时得到的图片：https://william7004-gallery-without-prompt.streamlit.app")
st.write("Hunyuan Video Gallery Without Prompt项目，展示使用Hunyuan Video在不填写提示词时得到的图片和视频，放到gallery1页面。")
st.write("Hunyuan Video Gallery 项目，展示使用Hunyuan Video在有提示词时生成的视频，放到gallery2页面。")

st.show()
