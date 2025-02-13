import streamlit as st

st.title("New Homepage")
st.subheader("1.项目内容", divider=True)
st.write("本项目整合了我之前几个仍在维护的非工具类Streamlit项目的内容，在侧边栏选择对应页面。原项目保留在Streamlit Cloud但新增内容只会放到本项目。")
st.write("blog页面包含我的一些技术方面的文章和杂谈。")
st.write("ai-note项目包含我部署AI应用的案例和记录各分类中优秀的AI模型。")
st.write("LLM-inquiry项目记录了我使用LLM查询的难以用传统搜索引擎查找的问题。")
st.write("gallery1项目为原Hunyuan Video Gallery Without Prompt项目，包含使用Hunyuan Video生成的无提示词图片和视频。")
st.write("gallery2项目包含使用Hunyuan Video生成的有提示词的图片和视频内容。")
st.write("articles-by-llm项目是新创建的，展示了使用在写作上有优势的思维链模型写的文章以及对应的语音。")
st.subheader("2.开发过程和原因", divider=True)
st.write("本人使用Streamlit创建项目的原因是语法较为简洁，并且能对接我较为熟悉的Python生态。相比原项目，博客类去掉了边栏显示的目录，其它几个保留原项目内容，包括项目说明。页面布局由于不可重复设置，统一设为wide。按使用LLM得到的程序缺少show()函数导致第二次打开同一页面时无法显示，添加st.show()后有报错但可以正常运行。")
st.write("本人创建个人网站的一方面原因是作为编程实践，另一方面使用个人网站相比社交平台在设计和内容上较为自由，也可以发挥Python生态优势实现更多功能。")
st.subheader("3.我的其它项目", divider=True)
st.write("我的GitHub名称是willian7004，命名时笔误了，在streamlit cloud的域名均使用william7004的名称。其它项目可以在我的GitHub仓库查看，博客部分也提到了其中一些项目和技术路线。")

st.show()