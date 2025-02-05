### 提示词：

使用streamlit写一个程序，实现以下功能：

1.当前文件夹中有名称为mainpage、blog、ai-note、llm-inquiry、gallery1和gallery2的文件夹，在侧边栏上创建对应名称的单选按钮，默认选中mainpage

2.选中mainpage、llm-inquiry、gallery1或gallery2时，显示对应文件夹中page.py页面的内容

3.选中blog或ai-note时，根据对应文件夹中的pages文件夹中的.py文件的文件名在侧边栏创建单选按钮，用于选择显示对应页面的内容

### 思维链：

嗯，我现在需要帮用户用Streamlit写一个程序，实现他提到的几个功能。让我先仔细看看需求。首先，当前文件夹下有mainpage、blog、ai-note、llm-inquiry、gallery1和gallery2这些文件夹。侧边栏要有对应的单选按钮，默认选中的是mainpage。

然后，当选择mainpage、llm-inquiry、gallery1或gallery2时，显示对应文件夹里的page.py的内容。而blog和ai-note这两个选项，需要根据各自文件夹下的pages文件夹里的.py文件，在侧边栏再创建单选按钮，选择显示对应的页面内容。

首先，我得确定如何动态加载不同的页面。可能需要根据选择的选项，导入对应的模块。比如，当选择mainpage时，导入mainpage文件夹下的page.py，然后显示里面的内容。

对于blog和ai-note的情况，他们各自的pages文件夹里可能有多个.py文件，每个文件对应一个子页面。这时候，需要在侧边栏再添加一个单选按钮，列出这些子页面的文件名（去掉.py后缀），然后根据选择加载对应的模块。

接下来，结构方面，主程序应该有一个侧边栏，用radio组件显示主选项。默认选mainpage。然后，根据主选项的不同，决定如何显示内容。如果主选项是blog或ai-note，就需要在侧边栏再显示子选项，也就是pages里的文件列表。

这里需要注意模块导入的方式。可能需要动态导入，比如使用importlib库的import_module函数。例如，当用户选择mainpage，就导入mainpage.page模块，然后调用里面的show函数（假设每个页面模块都有一个show函数来渲染内容）。

对于子页面，比如blog/pages下的文件，假设文件名为post1.py、post2.py，那么子选项就是post1和post2。选择后，导入blog.pages.post1，然后调用show。

那如何获取这些子页面的文件名呢？可以用os模块来遍历对应的pages目录，找出所有.py文件，排除__init__.py，然后提取文件名（不带后缀）。

然后，处理路径问题。确保程序运行时，当前目录是正确的，或者使用相对路径正确找到各个文件夹。

另外，需要注意缓存问题，避免重复导入模块导致性能问题。不过Streamlit每次交互都会重新运行整个脚本，所以可能需要考虑模块的重新导入，或者使用st.cache_resource来缓存模块导入。

可能的步骤：

1. 在侧边栏创建主选单选按钮，选项是各个文件夹的名字，默认选mainpage。

2. 根据主选项的值，判断是否需要处理子选项。

3. 如果主选项是blog或ai-note，则遍历对应pages文件夹，获取所有.py文件名，生成子选项列表，然后在侧边栏创建子单选按钮。

4. 根据主选项和子选项（如果有），动态导入对应的模块，并调用show方法显示内容。

现在需要考虑模块导入的具体实现。例如，mainpage的模块路径应该是mainpage.page，所以导入的时候是import mainpage.page as page_module。然后调用page_module.show()。

对于子页面，比如blog的pages中的post1.py，模块路径是blog.pages.post1，导入后调用show。

但是，在Streamlit中，直接导入可能有问题，因为脚本的路径可能不在项目根目录。需要确保Python的sys.path包含项目根目录，或者使用相对导入。或者，将各个文件夹作为包，添加__init__.py文件，但用户可能没有这样做，所以可能需要动态处理。

或者，使用importlib的import_module函数，例如：module = importlib.import_module(f"{selected_main}.page")，当主选项是mainpage时，这样导入mainpage.page模块。

对于子页面，比如blog的子选项，选中的是post1，那么模块路径是blog.pages.post1，所以用importlib.import_module(f"{selected_main}.pages.{selected_sub}")。

这样，每个页面模块都需要有一个show函数，负责渲染该页面的内容。

那用户需要在自己的各个page.py或子页面的.py文件中定义show函数，例如：

def show():

st.write("Main Page Content")

这样，主程序就可以统一调用module.show()来显示内容。

接下来，代码结构的大致思路：

- 导入必要的库，如streamlit as st，importlib，os等。

- 定义主选项列表：main_folders = ['mainpage', 'blog', 'ai-note', 'llm-inquiry', 'gallery1', 'gallery2']

- 在侧边栏创建主选项的单选按钮，默认'mainpage'

- 根据主选项判断是否需要处理子选项：

- 如果主选项是blog或ai-note：

- 获取对应的pages文件夹下的所有.py文件，排除__init__.py，提取模块名

- 在侧边栏创建子单选按钮

- 导入对应的子模块，调用show()

- 否则：

- 导入主选项对应的page模块，调用show()

例如：

selected_main = st.sidebar.radio("主页面", main_folders, index=0)

if selected_main in ['blog', 'ai-note']:

pages_path = os.path.join(selected_main, 'pages')

# 获取所有.py文件

sub_pages = [f[:-3] for f in os.listdir(pages_path) if f.endswith('.py') and f != '__init__.py']

selected_sub = st.sidebar.radio("子页面", sub_pages)

module = importlib.import_module(f"{selected_main}.pages.{selected_sub}")

module.show()

else:

module = importlib.import_module(f"{selected_main}.page")

module.show()

但这里可能存在一些问题，比如，当pages文件夹不存在或者没有.py文件时，需要处理异常。或者，用户是否在每个文件夹下都有正确的结构？

另外，需要确保各个文件夹（如mainpage）下面有page.py文件，否则导入会出错。同样，blog和ai-note下的pages文件夹必须存在，并且有.py文件。

所以，在代码中可能需要添加错误处理，比如try-except块，或者检查文件是否存在。

例如，在获取sub_pages的时候，如果pages_path不存在，就显示错误信息。

或者，当sub_pages列表为空时，提示没有可用的页面。

此外，关于模块导入，可能需要处理导入错误，比如模块不存在的情况。

例如，当用户选择mainpage，但mainpage文件夹下没有page.py，那么导入会失败，导致程序崩溃。因此，需要处理这种情况，给出友好的错误提示。

另一个考虑点是，Streamlit的安全限制。在某些部署环境下，动态导入模块可能会受到限制，但如果是本地运行的话，应该没问题。

所以，主程序的大致代码结构可能如下：

import streamlit as st

import importlib

import os

# 定义主文件夹列表

main_folders = ['mainpage', 'blog', 'ai-note', 'llm-inquiry', 'gallery1', 'gallery2']

# 侧边栏主选项

selected_main = st.sidebar.radio(

"选择主页面",

main_folders,

index=main_folders.index('mainpage')  # 默认选中mainpage

)

if selected_main in ['blog', 'ai-note']:

# 处理子页面

pages_dir = os.path.join(selected_main, 'pages')

if not os.path.exists(pages_dir):

st.error(f"目录 {pages_dir} 不存在！")

st.stop()

# 获取所有子页面文件

sub_pages = []

for file in os.listdir(pages_dir):

if file.endswith('.py') and file != '__init__.py':

sub_pages.append(file[:-3])

if not sub_pages:

st.error(f"在 {pages_dir} 中没有找到页面文件！")

st.stop()

# 子选项

selected_sub = st.sidebar.radio("选择子页面", sub_pages)

# 导入模块

try:

module = importlib.import_module(f"{selected_main}.pages.{selected_sub}")

except ModuleNotFoundError:

st.error(f"无法找到模块 {selected_main}.pages.{selected_sub}！")

st.stop()

# 显示内容

module.show()

else:

# 导入主页面模块

try:

module = importlib.import_module(f"{selected_main}.page")

except ModuleNotFoundError:

st.error(f"无法找到模块 {selected_main}.page！")

st.stop()

# 显示内容

module.show()

这样，代码会检查pages目录是否存在，是否有子页面文件，以及模块是否能导入，并给出错误提示。

但需要注意的是，Python的模块导入需要文件夹是一个包，即包含__init__.py文件。例如，blog文件夹需要是一个Python包，否则import blog.pages.post1会失败。因此，用户可能需要在每个文件夹（如mainpage、blog等）中添加__init__.py文件，即使它们是空的。

这可能是一个潜在的问题，如果用户没有创建这些文件，导入会失败。因此，在代码中可能需要提示用户确保每个主文件夹都是一个Python包，或者动态地将路径添加到sys.path中，以便可以导入。

或者，另一种方法是使用相对导入或修改sys.path。例如，将当前目录添加到sys.path中：

import sys

sys.path.append(".")

这样，在导入时，可以正确找到各个模块。这可能需要在代码开头添加。

因此，在代码开头，添加：

import sys

sys.path.append(".")

这可能解决模块导入的问题，前提是用户的项目结构正确。

总结：

代码结构需要：

1. 添加sys.path.append(".")确保模块导入正确。

2. 遍历主文件夹，检查是否是合法的Python包（但可能不需要，只要文件夹存在即可）。

3. 动态导入对应的模块，处理可能的错误。

用户需要确保每个主文件夹下存在page.py（对于非blog/ai-note的情况），而blog和ai-note需要有pages子文件夹，里面包含各个.py文件，每个文件有show函数。

因此，最终的代码可能如下：

### 回答正文：

```python
import streamlit as st
import importlib
import os
import sys

# 将当前目录添加到Python路径中，确保模块导入正常
sys.path.append(".")

# 主页面配置
main_folders = ['mainpage', 'blog', 'ai-note', 'llm-inquiry', 'gallery1', 'gallery2']

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

if selected_main in ['blog', 'ai-note']:
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
```

**使用说明：**

1. **必要文件结构：**
```bash
你的项目目录/
├── mainpage/
│   └── page.py
├── blog/
│   └── pages/
│       ├── post1.py
│       └── post2.py
├── ai-note/
│   └── pages/
│       ├── note1.py
│       └── note2.py
├── llm-inquiry/
│   └── page.py
├── gallery1/
│   └── page.py
├── gallery2/
│   └── page.py
└── app.py  # 这个代码文件
```

2. **页面模板示例（以mainpage/page.py为例）：**
```python
import streamlit as st

def show():
    st.title("主页面")
    st.write("这里是主要内容区域")
```

3. **运行程序：**
```bash
streamlit run app.py
```

**注意事项：**
1. 确保所有目录都包含`__init__.py`文件（可以是空文件）
2. 每个页面模块必须实现`show()`函数
3. 子页面文件不要使用`page.py`命名，这个名称保留给主页面使用
4. 如果遇到模块导入问题，请检查：
   - 文件路径是否正确
   - Python版本是否在3.7+
   - 是否缺少`__init__.py`文件


