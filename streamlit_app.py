import streamlit as st
import importlib
import os
import sys

st.set_page_config(layout="wide")
# 将当前目录添加到Python路径中，确保模块导入正常
sys.path.append(".")

# 主页面配置
main_folders = ['mainpage', 'blog', 'ai-note', 'llm-inquiry', 'by-talk','gallery1', 'gallery2','articles-by-llm','tools']

# 创建侧边栏单选按钮
selected_main = st.sidebar.radio(
    "请选择主页面",
    main_folders,
    index=main_folders.index('mainpage')  # 设置默认选项
)

def load_module(module_path):
    """动态加载模块并显示内容"""
    try:
        module = importlib.import_module(module_path)
        module.show()
    except ModuleNotFoundError:
        st.error(f"找不到模块: {module_path}")
    except AttributeError:
        st.error(f"模块中缺少show()函数: {module_path}")

if selected_main in ['blog', 'ai-note','tools']:
    # 处理带子页面的情况
    pages_dir = os.path.join(selected_main, 'pages')
    
    if not os.path.exists(pages_dir):
        st.error(f"目录不存在: {pages_dir}")
        st.stop()
        
    # 获取所有合法的子页面文件
    sub_pages = [
        f[:-3] for f in os.listdir(pages_dir)
        if f.endswith('.py') and f not in ['__init__.py', 'page.py']
    ]
    
    if not sub_pages:
        st.error(f"没有找到子页面: {pages_dir}")
        st.stop()
    
    # 创建子页面单选按钮
    selected_sub = st.sidebar.radio(
        "请选择子页面",
        sub_pages
    )
    
    # 构建模块路径并加载
    module_path = f"{selected_main}.pages.{selected_sub}"
    load_module(module_path)

else:
    # 处理普通页面
    module_path = f"{selected_main}.page"
    load_module(module_path)