import streamlit as st

st.title("New Homepage")
st.write("本项目整合了我之前几个仍在维护的非工具类Streamlit项目的内容，在侧边栏选择对应项目。原项目保留在Streamlit Cloud但新增内容只会放到本项目。")
st.write("blog项目包含我的一些技术方面的文章和杂谈。ai-note项目包含我部署AI应用的案例和记录各方面优秀的AI模型。LLM-inquiry项目记录了我使用LLM查询的难以用传统搜索引擎查找的问题。gallery1项目为原Hunyuan Video Gallery Without Prompt项目，包含使用Hunyuan Video生成的无提示词图片和视频，而gallery2项目包含有提示词的图片和视频内容。")
st.write("本人使用Streamlit创建项目的原因是语法较为简洁，并且能对接我较为熟悉的Python生态。相比原项目，博客类去掉了边栏显示的目录，其它几个保留原项目内容，包括项目说明。页面布局由于不可重复设置，统一设为wide。按使用LLM得到的程序缺少show()函数导致第二次打开同一页面时无法显示，添加st.show()后有报错但可以正常运行。")
st.write("本人创建个人网站的一方面原因是作为编程实践，另一方面相比社交平台有设计和内容较为自由的优势。")

st.show()