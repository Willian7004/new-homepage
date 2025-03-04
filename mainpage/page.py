import streamlit as st

st.title("New Homepage")
st.subheader("1.项目内容", divider=True)
st.write("本项目整合了我之前几个仍在维护的非工具类Streamlit项目的内容，在侧边栏选择对应页面。原项目保留在Streamlit Cloud但新增内容只会放到本项目。")
st.write("blog页面包含我的一些技术方面的文章和杂谈。")
st.write("ai-note页面包含我部署AI应用的案例和记录各分类中优秀的AI模型。")
st.write("LLM-inquiry页面记录了我使用LLM查询的难以用传统搜索引擎查找的问题，可以分页查看、随机显示或搜索相应文件。")
st.write("by-talk页面为杂谈，从blog页面的杂谈部分分离出来以便编辑，复用LLM-inquiry页面的逻辑功能。")
st.write("gallery1页面为使用Hunyuan Video生成的的图片，可以选择特定提示词对应的文件夹或随机选择文件夹。")
st.write("gallery2页面包含使用Wan2.1 1.3b生成的视频，可以根据视频主题选择对应的文件夹或随机选择文件夹。")
st.write("articles-by-llm页面是新创建的，展示了使用在写作上有优势的思维链模型写的文章以及对应的语音。")
st.write("tools页面包含一些工具，分别如下：")
st.write("1.files-drop项目，是之前创建的，用于传输文件")
st.write("2.新建的code-tools项目用于编写和运行python程序或用于高亮显示其它编程语言的代码。")
st.write("2.新建的markdown-tools项目用于预览markdown以及运行markdown中的python程序，相比code-tools项目更接近notebook类型。")
st.subheader("2.开发过程和原因", divider=True)
st.write("本人使用Streamlit创建项目的原因是语法较为简洁，并且能对接我较为熟悉的Python生态，语法简洁在LLM辅助开发上也有优势。相比原项目，博客类去掉了边栏显示的目录，其它几个保留原项目内容，包括项目说明，另外也开发了一些新的项目，在对应的.md文件有提示词。页面布局由于不可重复设置，统一设为wide。按使用LLM得到的程序缺少show()函数导致第二次打开同一页面时无法显示，添加st.show()后有报错但可以正常运行。")
st.write("本人创建个人网站的一方面原因是作为编程实践，另一方面使用个人网站相比社交平台在设计和内容上较为自由，也可以发挥Python生态优势实现更多功能。")
st.subheader("3.我的其它项目", divider=True)
st.write("我的GitHub名称是willian7004，命名时笔误了，在streamlit cloud的域名均使用william7004的名称。其它项目可以在我的GitHub仓库查看，博客部分也提到了其中一些项目和技术路线。")

st.show()