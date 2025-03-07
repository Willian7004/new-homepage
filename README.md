# New Homepage

### 项目说明

本项目整合了我之前几个仍在维护的非工具类Streamlit项目的内容，在侧边栏选择对应项目。原项目保留在Streamlit Cloud但新增内容只会放到本项目。

本项目已部署到Streamlit Cloud，域名为https://william7004-new-homepage.streamlit.app

### 使用python部署
1.安装依赖
```
pip install -r requirements.txt
```
2.运行应用
```
streamlit run streamlit_app.py
```

### 使用docker部署
1.创建docker
```
docker build . -t new-homepage
```
2.运行docker
```
docker run -p 8501:8501 new-homepage
```

