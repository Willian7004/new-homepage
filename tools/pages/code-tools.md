### 提示词：

使用streamlit写一个程序，实现以下功能：

1.在第一行左半部分创建两个复选框，文字为“停用分列”和“选择其它语言”，选中“选择其它语言”时在右半部分创建一个下拉菜单，把当前目录下tools文件夹中的languages.txt的每一行的内容分别创建为一个选项

2.未勾选“停用分列”时，在页面左半部分创建高度为800的输入框；勾选“停用分列”时，创建高度为500的输入框，用于输入代码。

3.完成输入后，使用st.code高亮显示代码，默认为python语言，如果选中复选框则按下拉菜单中选择的语言进行高亮显示

4.如果未选中“选择其它语言”复选框，运行输入的python程序并显示输出

5.未勾选“停用分列”时，第3和第4步的结果显示在右半部分；勾选“停用分列”时，显示在下方

6.在页面底部显示下载按钮，把输入的内容下载为txt文件

### 思维链：

嗯，我现在需要帮用户用Streamlit写一个程序，实现他提到的六个功能。首先，我得仔细分析每个需求，然后逐步思考如何实现。

第一个功能是在第一行左半部分创建两个复选框，“停用分列”和“选择其它语言”。当选中“选择其它语言”时，右半部分要显示一个下拉菜单，选项来自当前目录下tools文件夹中的languages.txt的每一行。这里可能需要用Streamlit的columns布局来分左右部分。复选框用st.checkbox，然后动态生成下拉菜单。读取文件的话，要注意路径是否正确，可能需要os模块来获取当前目录，并拼接路径。如果文件不存在的话，可能需要处理异常，或者用户可能没有这个文件，但题目假设存在，所以直接读取即可。

第二个功能是根据是否勾选“停用分列”来调整输入框的高度。未勾选时，左半部分输入框高度800；勾选时，高度500。这里可能需要用条件判断，使用st.text_area的高度参数。同时，布局方面，如果勾选停用分列，可能后面的结果显示在下方，否则在右半部分。所以布局可能需要动态调整列的数量。

第三个功能是用st.code高亮显示代码，默认Python，如果选择了其他语言就用下拉菜单的值。这里需要获取下拉菜单的选择值，如果未选择其他语言，默认是Python。然后根据这个语言类型来高亮显示。

第四个功能是如果未选中“选择其它语言”，就运行输入的Python程序并显示输出。这里需要注意执行用户输入的代码可能存在安全风险，但题目要求这样做，所以可能需要用subprocess或者exec来执行代码。但用exec可能会有作用域的问题，或者用subprocess调用Python解释器。不过捕获输出的话，可能需要重定向标准输出，或者使用eval等方式。这里可能需要用到exec，然后捕获stdout。例如，可以重定向sys.stdout到一个StringIO对象，然后获取输出内容。这部分需要小心处理，特别是用户输入的代码可能有恶意或错误，但按照题目要求，可能不需要考虑安全，只实现功能。

第五个功能是关于布局的，是否分列显示结果。如果未勾选停用分列，结果在右半部分；勾选的话，结果显示在下方。所以这里需要根据复选框的状态来决定使用列还是直接显示在下方。可能需要用columns来分左右，或者在下方用st.write或st.code等。

第六个功能是页面底部显示下载按钮，将输入内容保存为txt。这可以用st.download_button，设置data参数为输入的文本，文件名由用户指定或固定。

现在，逐步梳理代码结构：

首先导入需要的库：streamlit，os，可能还需要io来捕获执行输出。

然后读取languages.txt文件，获取所有语言选项。这一步应该在程序开始时完成，比如放在主函数里，或者每次渲染页面时读取（可能会影响性能，但文件小的话没问题）。

布局方面，第一行用cols = st.columns(2)，左半部分是第一个column，右半部分是第二个。两个复选框放在左半部分。当“选择其它语言”被选中时，在右半部分显示下拉菜单。

然后根据“停用分列”的状态决定输入框的高度，并放在左半部分。输入框的内容需要保存到session_state或者变量中，以便后续处理。

处理代码显示和执行：当用户输入完成后，点击某个按钮或者自动触发？题目里没说是否需要按钮，可能输入后自动显示。但Streamlit会在每次交互时重新运行脚本，所以可能需要将输入内容保存到session_state中，防止重新运行时丢失。

然后根据是否勾选“停用分列”来决定结果的位置。如果未停用分列，结果在右列；否则在下方。同时，如果未选择其他语言，需要执行Python代码并显示输出。

下载按钮放在页面底部，无论布局如何。

可能遇到的问题：

1. 如何动态显示下拉菜单：当复选框选中时，显示下拉菜单，否则不显示。可以用条件判断，在右半部分的column中，如果复选框被选中，则显示下拉菜单，并读取选项。

2. 执行用户输入的代码：这部分可能会有问题，比如无限循环、错误处理等。需要捕获异常，或者在subprocess中设置超时。但题目可能只要求简单的执行，比如用exec执行，并捕获输出。例如：

import sys

from io import StringIO

old_stdout = sys.stdout

sys.stdout = mystdout = StringIO()

try:

exec(user_code)

except Exception as e:

print(e)

finally:

sys.stdout = old_stdout

output = mystdout.getvalue()

然后将output显示出来。

3. 布局的动态调整：根据“停用分列”复选框的状态，决定结果的位置。例如，如果停用分列，则下方显示，否则在右列。可能需要使用条件判断来创建不同的布局块。

4. 下载按钮：使用st.download_button，将输入的代码内容作为数据传递，设置MIME类型为text/plain，文件名可选。

现在，开始编写代码的大纲：

导入必要的库：

import streamlit as st

import os

from io import StringIO

import sys

读取languages.txt：

def get_languages():

file_path = os.path.join(os.getcwd(), 'tools', 'languages.txt')

with open(file_path, 'r') as f:

languages = [line.strip() for line in f.readlines()]

return languages

但需要注意，当文件不存在时，可能需要处理异常。但题目假设存在，所以暂时不考虑。

主程序部分：

def main():

st.title("代码输入和运行程序")

# 初始化session_state

if 'code' not in st.session_state:

st.session_state.code = ''

if 'language' not in st.session_state:

st.session_state.language = 'python'

if 'output' not in st.session_state:

st.session_state.output = ''

# 第一行布局：两个复选框

col1, col2 = st.columns(2)

with col1:

disable_columns = st.checkbox("停用分列", value=False)

select_language = st.checkbox("选择其它语言", value=False)

# 如果选择其它语言，在右半部分显示下拉菜单

languages = []

if select_language:

try:

languages = get_languages()

except:

st.error("无法读取语言文件")

with col2:

selected_lang = st.selectbox("选择语言", options=languages)

st.session_state.language = selected_lang.lower()  # 假设语言名称是小写的，或者根据实际情况处理

else:

st.session_state.language = 'python'

# 根据停用分列决定输入框高度

if disable_columns:

code_height = 500

else:

code_height = 800

# 输入框放在左半部分

code = st.text_area("输入代码", value=st.session_state.code, height=code_height, key="code_input")

# 处理代码高亮和运行

if code:

# 高亮显示代码

lang = st.session_state.language if select_language else 'python'

st.code(code, language=lang)

# 如果未选择其他语言，运行代码

if not select_language:

# 执行代码并捕获输出

old_stdout = sys.stdout

sys.stdout = mystdout = StringIO()

try:

exec(code)

except Exception as e:

print(e)

finally:

sys.stdout = old_stdout

output = mystdout.getvalue()

st.session_state.output = output

st.text_area("输出结果", value=output, height=200, disabled=True)

else:

st.session_state.output = ''

# 根据停用分列决定结果显示位置

# 这里可能需要调整布局，比如如果停用分列，则下方显示，否则在右列

# 但上面的代码可能已经将结果显示在下方，需要重新组织结构

# 重新调整代码结构，可能将高亮和输出部分根据分列状态显示在右侧或下方

# 或许应该将代码高亮和输出的显示部分根据分列状态放在不同的位置

# 正确的做法可能是：

# 如果停用分列，则输入框在上，下方显示结果

# 否则，左右分列，右边显示结果

# 所以可能需要重新组织代码的结构：

# 创建布局

if not disable_columns:

left_col, right_col = st.columns(2)

else:

left_col = st.container()

right_col = None

with left_col:

code = st.text_area("输入代码", value=st.session_state.code, height=code_height, key="code_input")

# 处理代码显示和执行

if code:

lang = st.session_state.language if select_language else 'python'

output = st.session_state.output

if not disable_columns and right_col is not None:

with right_col:

st.code(code, language=lang)

if not select_language:

st.text_area("输出结果", value=output, height=200, disabled=True)

else:

st.code(code, language=lang)

if not select_language:

st.text_area("输出结果", value=output, height=200, disabled=True)

# 执行代码的时机可能需要调整，比如当代码变化时执行

# 或者当用户点击运行按钮时，但题目中没有提到按钮，可能自动执行

# 所以，在code发生变化时，执行代码并保存输出到session_state

# 但要注意，每次代码修改都会触发执行，可能会有性能问题，但暂时这样处理

# 执行代码的逻辑需要放在获取code之后

if code and not select_language:

old_stdout = sys.stdout

sys.stdout = mystdout = StringIO()

try:

exec(code)

except Exception as e:

print(e)

finally:

sys.stdout = old_stdout

output = mystdout.getvalue()

st.session_state.output = output

else:

st.session_state.output = ''

# 下载按钮

st.download_button(

label="下载代码",

data=code,

file_name="code.txt",

mime="text/plain"

)

但这样可能布局会有问题，因为当分列时，右边的部分可能无法正确显示。可能需要在不同的布局块中处理显示。

或者，将代码输入放在左列，然后根据是否分列来决定结果的位置。例如：

- 当未停用分列时，右列显示高亮代码和输出。

- 当停用分列时，下方显示高亮代码和输出。

可能需要重新组织代码的结构，将结果部分放在不同的位置。

调整后的思路：

创建两个列，如果未停用分列，则左右列都存在；否则，只有左列，结果在下方。

代码：

disable_columns = st.checkbox("停用分列")

col1, col2 = st.columns(2) if not disable_columns else (st.container(), None)

with col1:

# 输入框和复选框等

if not disable_columns and col2 is not None:

with col2:

# 显示高亮代码和输出

else:

# 在下方显示高亮代码和输出

但具体实现可能需要更复杂的条件判断。

或者，在代码输入之后，根据disable_columns的值来决定如何放置结果：

例如：

在col1中输入框，然后：

if disable_columns:

# 下方显示结果

else:

with col2:

# 显示结果

这可能更合理。

修改后的代码结构：

def main():

st.title("代码输入和运行程序")

# 第一行布局：两个复选框

col1_top, col2_top = st.columns(2)

with col1_top:

disable_columns = st.checkbox("停用分列")

select_other_lang = st.checkbox("选择其它语言")

# 处理语言选择

languages = []

selected_lang = 'python'

if select_other_lang:

try:

languages = get_languages()

with col2_top:

selected_lang = st.selectbox("选择语言", options=languages)

except Exception as e:

st.error(f"无法读取语言文件: {e}")

# 根据停用分列决定输入框的高度

code_height = 500 if disable_columns else 800

# 创建主布局列

if not disable_columns:

main_col1, main_col2 = st.columns(2)

else:

main_col1 = st.container()

main_col2 = None

with main_col1:

code = st.text_area("输入代码", height=code_height, key="code")

# 处理代码高亮和运行

if code:

# 高亮显示代码

lang = selected_lang if select_other_lang else 'python'

if not disable_columns and main_col2 is not None:

with main_col2:

st.code(code, language=lang)

# 运行代码并显示输出，如果未选择其他语言

if not select_other_lang:

# 执行代码

output = run_code(code)

st.text_area("输出", value=output, height=200, disabled=True)

else:

st.code(code, language=lang)

if not select_other_lang:

output = run_code(code)

st.text_area("输出", value=output, height=200, disabled=True)

# 下载按钮

st.download_button(

"下载代码",

data=code if code else "",

file_name="code.txt",

mime="text/plain"

)

其中，run_code函数用于执行代码并返回输出：

def run_code(code):

old_stdout = sys.stdout

sys.stdout = mystdout = StringIO()

try:

exec(code)

except Exception as e:

print(e)

finally:

sys.stdout = old_stdout

return mystdout.getvalue()

这样可能更清晰。

测试各个功能：

1. 当勾选“选择其它语言”时，显示下拉菜单，选项正确。

2. 输入框高度根据“停用分列”变化。

3. 高亮显示的语言正确。

4. 未选择其他语言时执行代码并显示输出。

5. 分列显示或下方显示结果。

6. 下载按钮正确生成。

可能遇到的问题：

- 语言文件路径是否正确？可能需要使用相对路径，或者使用__file__来定位。假设streamlit程序运行在项目根目录，tools/languages.txt存在。

- 执行代码时的安全性，但题目假设允许。

- 动态布局的处理，特别是分列和下方显示的逻辑是否正确。

综上，整合以上思路，编写最终的代码。

### 回答正文：

以下是实现所需功能的Streamlit代码：

```python
import streamlit as st
import os
from io import StringIO
import sys

def get_languages():
    file_path = os.path.join(os.getcwd(), 'tools', 'languages.txt')
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def run_code(code):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    try:
        exec(code)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdout = old_stdout
    return mystdout.getvalue()

def main():
    st.title("代码输入和运行程序")

    # 第一行顶部布局
    col1_top, col2_top = st.columns(2)
    with col1_top:
        disable_columns = st.checkbox("停用分列")
        select_other_lang = st.checkbox("选择其它语言")

    # 语言选择处理
    selected_lang = 'python'
    if select_other_lang:
        try:
            languages = get_languages()
            with col2_top:
                selected_lang = st.selectbox("选择语言", options=languages)
        except Exception as e:
            st.error(f"无法读取语言文件: {e}")

    # 主内容布局
    if not disable_columns:
        main_col1, main_col2 = st.columns(2)
    else:
        main_col1 = st.container()

    # 输入框设置
    with main_col1:
        code_height = 500 if disable_columns else 800
        code = st.text_area("输入代码", height=code_height, key="code_input")

    # 结果显示处理
    if code:
        lang = selected_lang.lower() if select_other_lang else 'python'
        
        # 代码高亮显示
        if not disable_columns:
            with main_col2:
                st.code(code, language=lang)
        else:
            st.code(code, language=lang)

        # 代码执行和输出
        if not select_other_lang:
            output = run_code(code)
            output_container = main_col2 if not disable_columns else st
            if not disable_columns:
                with output_container:
                    st.text_area("执行结果", value=output, height=200, disabled=True)
            else:
                st.text_area("执行结果", value=output, height=200, disabled=True)

    # 下载按钮
    st.download_button(
        label="下载代码",
        data=code if code else "",
        file_name="user_code.txt",
        mime="text/plain"
    )

if __name__ == "__main__":
    main()
```

使用说明：

1. 在项目根目录下创建`tools`文件夹，并在其中创建`languages.txt`文件，每行一个编程语言名称（例如：python、java、javascript等）

2. 安装依赖：
```bash
pip install streamlit
```

3. 运行程序：
```bash
streamlit run your_script_name.py
```

功能说明：

1. 顶部两个复选框控制布局和语言选择
2. 输入框高度根据"停用分列"状态动态调整（500/800像素）
3. 代码高亮显示支持多种编程语言
4. 自动执行Python代码并显示输出结果
5. 布局根据复选框状态动态切换（分列/上下布局）
6. 始终显示下载按钮可将代码保存为txt文件

注意事项：

1. 确保`tools/languages.txt`文件存在且格式正确
2. 执行代码时请确保输入安全的Python代码
3. 其他编程语言选项仅影响代码高亮显示，不影响实际执行
4. 实际代码执行仅支持Python语言（当不选择其他语言时）