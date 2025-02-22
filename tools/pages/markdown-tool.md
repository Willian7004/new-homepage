### 提示词：

使用streamlit写一个程序，实现以下功能：

1.在第一行创建两个复选框，文字分别为“停用分列”和“执行代码”。

2.未勾选“停用分列”时，在页面左半部分创建高度为800的输入框，在页面右半部分创建高度为800的st.container。勾选“停用分列”时，创建高度为500的输入框并在下方创建st.container，设置border=True。

3.未勾选“执行代码”时，使用st.markdown在st.container显示输入框的内容，在页面底部创建下载按钮把输入框的内容保存为.md格式。勾选“执行代码”时，运行输入框中markdown形式的python代码块的内容，按代码块位置分割输入框的内容，分别用st.markdown显示并在每部分后显示对应python代码的运行结果。有多段代码时，确保创建的变量可以被后面的代码调用。创建按钮用于下载.md文件，并另外创建一个下载按钮，把代码块内容写入.py文件，其它内容写入多行注释并下载.py文件。

### 思维链：

好的，我现在需要帮用户解决一个使用Streamlit创建应用的问题。首先，我得仔细阅读用户的需求，确保理解每一个细节。用户的需求分为几个部分，我需要逐一分析。

首先，用户要求在第一行创建两个复选框，分别是“停用分列”和“执行代码”。这两个复选框的状态会影响页面布局和功能。接下来，当“停用分列”未勾选时，页面分为左右两半，左边是高度800的输入框，右边是同样高度的st.container。如果勾选了“停用分列”，输入框高度变为500，下方有一个带边框的容器。这部分涉及布局的动态调整，可能需要使用Streamlit的列功能或者条件判断来切换布局结构。

然后是第二部分功能，关于“执行代码”复选框的影响。当未勾选时，容器内显示输入框的内容的Markdown，并在底部提供下载.md的按钮。当勾选时，需要解析输入内容中的Python代码块，按位置分割内容，分别显示Markdown和代码执行结果，同时还要处理多个代码块之间的变量共享，以及生成并下载.py文件，其中代码块内容写入代码，其他内容作为多行注释。

首先，我需要考虑如何动态调整布局。Streamlit的columns函数可以创建列，当“停用分列”未勾选时，使用两列布局；勾选时，则改为上下结构。这里可能需要使用条件语句来判断复选框的状态，然后分别渲染不同的布局。

输入框的高度设置，可能需要使用st.text_area的height参数。对于容器的边框，当勾选“停用分列”时，需要设置st.container的border参数为True。不过，Streamlit的st.container是否支持直接设置border属性？可能需要查阅文档，或者使用自定义CSS来实现，比如通过st.markdown添加样式。不过用户明确提到设置border=True，可能是指Streamlit的新功能，因为最近版本确实支持container的border参数。

接下来处理执行代码的部分。当勾选“执行代码”时，需要解析输入内容中的Python代码块。Markdown中的代码块是以三个反引号加python标识的，所以需要用正则表达式来分割内容，提取代码块和非代码部分。例如，用正则表达式r'```python(.*?)```'来匹配代码块，同时分割出非代码的Markdown内容。

对于执行代码块，需要确保每个代码块在同一个作用域中运行，这样变量可以后续使用。可以使用一个全局的字典来保存变量，或者在exec函数中指定globals字典。但是exec的安全性需要注意，因为用户输入的代码可能包含恶意内容。不过这可能超出当前问题的范围，用户可能只是需要一个基本的功能演示。

处理分割后的内容时，需要按顺序交替显示Markdown部分和代码执行结果。例如，输入内容可能是：

一些文本

```python

print("Hello")

```

更多文本

```python

x = 5

```

然后分割为文本1，代码1，文本2，代码2。显示文本1，执行代码1并显示结果，显示文本2，执行代码2并显示结果。这里需要注意代码块的分割是否正确，特别是当代码块中有嵌套反引号的情况，但用户可能假设输入的代码块是正确格式化的。

生成.py文件时，非代码部分需要作为多行注释，代码部分保留。例如，每个非代码块用'''包裹起来作为注释。这里可能需要处理换行和缩进，但用户可能接受简单的处理方式。

关于下载按钮，Streamlit的st.download_button可以用于生成下载内容。需要根据是否执行代码来生成不同的下载文件。对于.md文件，直接保存输入内容；对于.py文件，需要将代码块提取出来，非代码内容转为注释。

现在，我需要将这些思路转化为代码结构。大致步骤如下：

1. 创建两个复选框，使用st.checkbox，放在同一行，可能使用columns来并排显示。

2. 根据“停用分列”的状态决定布局结构：

- 如果未勾选，使用两列，左边是text_area，右边是container。

- 如果勾选，一个text_area上方，下方是container。

3. 根据“执行代码”的状态决定内容处理方式：

- 未勾选时，显示Markdown并提供.md下载。

- 勾选时，解析代码块，执行并显示结果，生成.md和.py下载。

可能的挑战包括正确分割代码块和非代码内容，处理代码执行结果的捕获（例如使用重定向stdout），以及确保变量在多个代码块中的持久性。

对于代码执行部分，可能需要使用exec来运行代码，并捕获输出。可以使用io.StringIO来临时捕获标准输出，以便获取打印的内容。同时，需要维护一个全局的变量环境，以便后续代码块可以访问之前定义的变量。

在生成.py文件时，需要将非代码部分转换为多行注释。例如，对于每个非代码块，用三引号包裹起来。需要注意的是，如果非代码内容本身包含三引号，可能需要转义，但用户可能暂时不考虑这种情况，先做基本处理。

现在，逐步编写代码：

首先，导入需要的库，如streamlit、re、io等。

然后，创建复选框：

col1, col2 = st.columns(2)

disable_split = col1.checkbox('停用分列')

execute_code = col2.checkbox('执行代码')

接下来，根据disable_split的值布局输入框和容器：

如果disable_split为False，左右分列，左边text_area高度800，右边container高度800？或者container只是一个容器，高度可能需要用CSS调整？或者可能不需要设置高度，因为container本身不限制内容的高度。可能用户的意思是输入框的高度为800，而容器的高度自适应。这部分可能需要进一步确认，但根据用户描述，输入框的高度在两种情况下分别为800和500，而容器的高度可能不需要显式设置，只是放置内容的区域。

当disable_split为True时，输入框高度500，下方container带border=True。

因此，代码结构可能如下：

if not disable_split:

col_left, col_right = st.columns(2)

with col_left:

input_content = st.text_area("输入内容", height=800, key="input")

with col_right:

container = st.container(border=True)

else:

input_content = st.text_area("输入内容", height=500, key="input")

container = st.container(border=True)

然后，处理内容的显示和下载按钮：

在container内部，根据execute_code的状态处理内容：

with container:

if execute_code:

# 分割代码块和非代码内容

parts = re.split(r'```python\n(.*?)\n```', input_content, flags=re.DOTALL)

# parts的奇数索引是代码块，偶数是文本

env = {}  # 用于保存变量环境

py_content = []

md_content = []

code_blocks = []

for i, part in enumerate(parts):

if i % 2 == 0:

# 文本部分，显示为markdown

if part.strip():

st.markdown(part)

md_content.append(part)

# 对于.py文件，添加为注释

py_content.append(f'"""\n{part}\n"""')

else:

# 代码部分

code_block = part.strip()

if code_block:

code_blocks.append(code_block)

st.markdown(f'```python\n{code_block}\n```')

# 执行代码

try:

# 捕获标准输出

from io import StringIO

buffer = StringIO()

sys.stdout = buffer

# 在env中执行代码

exec(code_block, env)

sys.stdout = sys.__stdout__

output = buffer.getvalue()

if output:

st.code(output)

md_content.append(f'```python\n{code_block}\n```\n输出：\n```\n{output}\n```')

else:

md_content.append(f'```python\n{code_block}\n```')

except Exception as e:

st.error(f"执行错误：{e}")

md_content.append(f'```python\n{code_block}\n```\n错误：{e}')

# 将代码块添加到py_content

py_content.append(code_block)

# 生成下载内容

md_content = '\n'.join(md_content)

py_content = '\n'.join(py_content)

else:

# 不执行代码，直接显示markdown

st.markdown(input_content)

md_content = input_content

然后，在页面底部创建下载按钮。注意，下载按钮应该放在container之外，或者根据布局调整位置。可能需要将下载按钮放在页面的底部，使用st.columns来并排显示两个按钮（当执行代码时）。

下载按钮部分：

if execute_code:

col1, col2 = st.columns(2)

with col1:

st.download_button(

label="下载.md",

data=md_content,

file_name="output.md",

mime="text/markdown"

)

with col2:

st.download_button(

label="下载.py",

data=py_content,

file_name="output.py",

mime="text/python"

)

else:

st.download_button(

label="下载.md",

data=md_content,

file_name="output.md",

mime="text/markdown"

)

但这里需要注意，当execute_code勾选时，py_content需要正确生成，即将非代码部分作为多行注释，代码部分保留。之前的处理中，py_content在循环中添加文本部分作为三引号注释，代码部分直接添加。这可能会有问题，比如多个文本部分之间是否需要换行，或者代码块之间是否需要分隔。例如，可能需要在注释和代码之间添加换行。

例如，在循环中：

py_content.append(f'"""\n{part}\n"""')

然后在代码块时：

py_content.append(code_block)

这样生成的.py文件会是：

"""文本部分"""

代码块

"""另一个文本部分"""

另一个代码块

这可能会有语法错误，因为注释和代码之间没有适当的换行。可能需要调整，在添加注释和代码时添加换行符。例如：

py_content.append(f'\n"""\n{part}\n"""\n')

但需要处理可能存在的空文本部分，比如如果part是空字符串，就不添加注释。

此外，当文本部分包含空行时，可能会生成多行注释中的空行，但这是允许的。

另一个问题是，使用exec执行代码块时，如何维护变量的环境。上述代码中使用了一个env字典，每次执行代码块时都传递这个字典，这样后续的代码块可以访问之前定义的变量。这应该可以正常工作。

但需要注意，exec的安全性问题，以及可能出现的错误处理。例如，代码中有语法错误或运行时错误，应该捕获并显示错误信息，而不是导致整个应用崩溃。

此外，对于输出捕获，使用重定向sys.stdout到StringIO，然后恢复，这样可以捕获print语句的输出。但其他形式的输出（如直接写入stdout）可能也会被捕获。但如果是这样，可能无法捕获错误信息，因为错误信息通常输出到stderr。因此，可能需要同时捕获stderr，或者将stderr合并到stdout。或者，可以修改代码，将错误信息也捕获并显示。

不过，用户可能只需要处理标准输出，而错误信息可能通过try-except块来捕获，并在页面上显示错误消息。

现在，测试这个逻辑是否正确：

假设输入内容为：

一些文本

```python

print("Hello")

x = 5

```

更多文本

```python

print(x)

```

当执行代码时，分割成parts列表：['\n一些文本\n\n', 'print("Hello")\nx = 5\n', '\n更多文本\n\n', 'print(x)\n', ...]

处理每个部分：

i=0，文本部分，添加到md_content，py_content添加为注释。

i=1，代码部分，执行后输出"Hello"，x被赋值为5。md_content添加代码块和输出。

i=2，文本部分，同样处理。

i=3，代码部分，print(x)输出5，添加到结果。

生成的.py文件内容为：

"""

一些文本

"""

print("Hello")

x = 5

"""

更多文本

"""

print(x)

这样应该可以正确运行，并且第二个代码块可以访问x变量。

可能还需要处理代码块前后的换行符，确保注释和代码之间没有语法错误。例如，每个注释块后添加换行符，避免注释和代码紧挨着。

另一个问题是如何处理输入内容中的多个代码块，例如连续的代码块或者文本块。正则表达式split使用非贪婪匹配，可能无法正确分割多个相邻的代码块。例如，如果输入内容有两个连续的代码块：

```python

code1

```

```python

code2

```

正则表达式r'```python\n(.*?)\n```'在re.DOTALL模式下会匹配第一个```python到最近的```，因此两个代码块会被正确分割。split后的parts会是['', 'code1', '', 'code2', '']，这样i=0是空文本，i=1是code1，i=2是空文本，i=3是code2。处理时，i=0的文本部分为空，不处理；i=1是code1，执行；i=2空文本，跳过；i=3是code2，执行。这样应该正确。

可能需要测试正则表达式是否正确分割多个代码块。

现在，编写代码的正则表达式部分：

使用re.split(r'```python\n(.*?)\n```', input_content, flags=re.DOTALL)

这样，假设代码块被正确包裹在```python和```之间，并且内容在中间。但需要注意，输入中的代码块可能有不同的换行符，比如在代码块开始后有一个换行，或者没有。例如：

```python

code here

```

或者：

```python

code here```

正则表达式可能需要调整，但假设用户输入是标准的Markdown语法，即代码块以三个反引号开始，后面跟python，然后是换行，代码内容，再换行和三个反引号结束。

因此，正则表达式可能需要匹配```python后面的换行，然后捕获直到下一个```的内容。使用re.DOTALL使得.匹配换行符，所以(.*?)会匹配尽可能少的内容，直到遇到```，但需要确保结束标记是\n```或者可能没有换行？比如，如果代码块的最后一行没有换行，那么正则表达式可能无法正确匹配。

例如，输入：

```python

print("hello")

```

会被正确匹配，而：

```python

print("hello")```

（没有最后的换行）则可能无法正确匹配，因为正则表达式中的结束是\n```，即要求结束的```前面有一个换行符。这可能是一个问题。因此，可能需要调整正则表达式，允许结束的```前面不一定有换行符。

可以将正则表达式修改为r'```python\s*?\n(.*?)\n```'，但不确定。或者使用更灵活的正则表达式，例如匹配任意空白：

r'```python\s*?(.*?)\s*?```'，并使用re.DOTALL标志。

或者，更准确的分割方式可能比较复杂。例如，使用正向前瞻和后顾来匹配代码块的开始和结束。

这个问题可能导致代码块分割不正确，影响整个功能。因此，可能需要调整正则表达式，使其更健壮。

例如，使用：

pattern = r'^```python\s*?\n(.*?)\n```\s*?$'

但使用re.split可能更复杂。或者，使用re.findall来查找所有代码块和非代码文本。

例如，另一种方法是使用re.findall来交替获取文本和代码块：

使用re.findall(r'(.*?)(```python\s*?\n(.*?)\n```\s*?)', input_content, flags=re.DOTALL)，但这样可能更复杂。

或者，使用split函数，但确保正确分割。

或者，分步骤处理：首先找到所有代码块的起始和结束位置，然后分割文本。

这可能比较复杂，但为了简化，假设用户输入的代码块格式正确，即每个代码块以```python开头，换行，代码内容，换行后接```。那么原正则表达式可以正确分割。

现在，回到代码编写：

在代码执行部分，使用exec(code_block, env)，其中env是一个字典，用于保存全局变量。这样，每个代码块都在同一个env中执行，后续代码块可以访问之前定义的变量。

然后，捕获输出：

通过临时重定向sys.stdout到StringIO缓冲区，执行代码，然后恢复sys.stdout，并获取缓冲区的内容作为输出。

需要注意的是，exec执行的代码中的print语句会被重定向，但其他修改stdout的行为可能不会，但这是一个基本的捕获方法。

对于错误处理，使用try-except块，捕获异常并显示错误信息。

最后，生成下载的.py文件内容时，将非代码部分用三引号包裹，作为注释，代码部分保留。这样生成的.py文件应该可以运行，同时保留原来的文本结构。

现在，将这些思路整合到代码中，注意处理各种边界情况，例如没有代码块时，或者没有文本部分时。

最后，测试整个应用的功能，确保各个复选框的状态变化正确影响布局和功能，代码执行和结果显示正确，下载的文件内容符合预期。

### 回答正文：

以下是根据需求编写的Streamlit应用程序代码：

```python
import streamlit as st
import re
from io import StringIO
import sys

# 初始化执行环境
if "env" not in st.session_state:
    st.session_state.env = {}

# 创建复选框
col1, col2 = st.columns(2)
disable_split = col1.checkbox("停用分列")
execute_code = col2.checkbox("执行代码")

# 布局设置
input_content = ""
if not disable_split:
    col_left, col_right = st.columns(2)
    with col_left:
        input_content = st.text_area("输入内容", height=800, key="input_left")
    container = col_right.container(height=800)
else:
    input_content = st.text_area("输入内容", height=500, key="input_full")
    container = st.container(border=True)

# 处理内容显示和下载
with container:
    if execute_code:
        # 分割代码块和普通文本
        parts = re.split(r'```python\n(.*?)\n```', input_content, flags=re.DOTALL)
        
        md_content = []
        py_content = []
        code_outputs = []

        for i, part in enumerate(parts):
            if i % 2 == 0 and part.strip():  # 普通文本
                st.markdown(part)
                md_content.append(part)
                py_content.append(f'"""\n{part}\n"""\n')
            elif i % 2 == 1:  # 代码块
                code = part.strip()
                if code:
                    # 显示代码
                    st.markdown(f"```python\n{code}\n```")
                    md_content.append(f"```python\n{code}\n```")
                    py_content.append(f"{code}\n")

                    # 执行代码
                    try:
                        buffer = StringIO()
                        sys.stdout = buffer
                        exec(code, st.session_state.env)
                        sys.stdout = sys.__stdout__
                        output = buffer.getvalue()
                        
                        if output:
                            st.code(output)
                            md_content.append(f"\n输出：\n```\n{output}\n```")
                            code_outputs.append(output)
                    except Exception as e:
                        st.error(f"执行错误：{str(e)}")
                        md_content.append(f"\n错误：\n```\n{str(e)}\n```")
        
        md_content = "\n".join(md_content)
        py_content = "\n".join(py_content)
        
        # 创建下载按钮
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="下载.md",
                data=md_content,
                file_name="output.md",
                mime="text/markdown"
            )
        with col2:
            st.download_button(
                label="下载.py",
                data=py_content,
                file_name="output.py",
                mime="text/plain"
            )
    else:
        # 未执行代码模式
        st.markdown(input_content)
        st.download_button(
            label="下载.md",
            data=input_content,
            file_name="output.md",
            mime="text/markdown"
        )
```

使用方法：
1. 将代码保存为`app.py`
2. 安装依赖：`pip install streamlit`
3. 运行：`streamlit run app.py`

功能说明：
1. 页面顶部有两个复选框控制布局和功能模式
2. 根据"停用分列"状态切换左右分栏或上下布局
3. 根据"执行代码"状态切换普通Markdown显示或代码执行模式
4. 在代码执行模式下：
   - 自动识别Markdown中的Python代码块（需包含在```python代码块中）
   - 按顺序执行代码并保留变量环境
   - 实时显示代码执行结果
   - 提供Markdown和Python双格式下载
5. 下载的Python文件会将普通文本转换为多行注释

注意事项：
1. 代码执行使用同一个环境上下文，后续代码可以访问前面代码定义的变量
2. 请谨慎执行未知来源的代码
3. 错误处理会显示在页面中
4. 代码块需要严格按照Markdown语法用```python包裹
5. 输出捕获支持标准输出（print语句），但不支持直接返回值显示
