import streamlit as st
import os
import random


#项目说明
with st.expander("Hunyuan Video Gallery Without Prompt（展开项目说明）"):
        st.write("本人近期在图片和视频生成均改用Hunyuan Video，考虑到分辨率不同以及要展示图片和视频内容就新建了项目。经测试能正常生成的最大分辨率约为1584x896，本项目中的图片和视频也使用这个分辨率，视频长度为21帧，帧率12fps。竖屏内容可用的最大分辨率为540x960，垂直分辨率相比横屏没有明显提升，出片率也较低。由于这个分辨率不明显高于streamlit的缩略图分辨率，相比之前的项目在页面上取消了下载按钮已提高外观一致性。由于Hunyuan Video在使用单个风格提示词时引导效果一般且无提示词基本不影响出片率，本项目取消风格选择。")
        st.write("由于实现流程可能较为复杂，本项目未添加预期的刷新按钮返回页面顶部以及翻页按钮功能（在页面顶部重新选中随机选项可以实现刷新，刷新网页会回到默认选项）。视频设为自动播放但在读取与上一次读取时重复的视频时无法自动播放。")
# 创建四个下拉菜单
cols = st.columns(4)

with cols[0]:
    media_type = st.selectbox("选择类型", ["图片", "视频"])

with cols[1]:
    aspect_ratio = st.selectbox("选择比例", ["16：9", "9：16"])

with cols[2]:
    num_items = st.selectbox("选择数量", [i for i in range(8, 33, 4)])

# 获取当前文件夹路径
current_dir = os.getcwd()

# 根据选择确定文件夹前缀和后缀
if media_type == "图片":
    prefix = "gallery1/pictures"
else:
    prefix = "gallery1/videos"

if aspect_ratio == "16：9":
    suffix = "1"
else:
    suffix = "2"

folder_path = os.path.join(current_dir, f"{prefix}{suffix}")

# 检查文件夹是否存在，如果不存在则显示错误信息
if not os.path.exists(folder_path):
    st.error(f"文件夹 {folder_path} 不存在")
else:
    # 获取文件列表
    if media_type == "图片":
        file_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    else:
        file_extensions = ['.mp4', '.avi', '.mkv', '.mov']

    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in file_extensions]
    total_files = len(file_list)

    if total_files == 0:
        st.warning("文件夹中没有文件")
    else:
        # 计算范围选项
        num_pages = total_files // num_items
        if total_files % num_items != 0:
            num_pages += 1
        range_options = ["随机"]
        for i in range(num_pages):
            start = i * num_items + 1
            end = min((i + 1) * num_items, total_files)
            range_options.append(f"{start}-{end}")

        with cols[3]:
            range_option = st.selectbox("选择范围", range_options)

        # 根据选择的范围获取文件
        if range_option == "随机":
            selected_files = random.sample(file_list, min(num_items, total_files))
            page_index = None  # 随机选择时没有页面索引
        else:
            # 解析范围，获取起始和结束索引
            start_end = range_option.split("-")
            start_index = int(start_end[0]) - 1  # 转换为0-based索引
            end_index = int(start_end[1])
            selected_files = file_list[start_index:end_index]
            # 计算当前页面索引
            page_size = num_items
            page_index = start_index // page_size

        # 根据选择的宽高比决定显示的列数
        if aspect_ratio == "16：9":
            cols_display = st.columns(2)
        else:
            cols_display = st.columns(4)

        # 显示选中的文件
        for i, file in enumerate(selected_files):
            col_idx = i % len(cols_display)
            with cols_display[col_idx]:
                file_path = os.path.join(folder_path, file)
                if media_type == "图片":
                    st.image(file_path)
                else:
                    st.video(file_path, format="video/mp4", start_time=0,loop=True, autoplay=True)

        # 根据选择的范围显示按钮
        if range_option == "随机":
            # 创建刷新按钮
            if st.button("刷新"):
                # 刷新页面，重新随机选择文件
                pass  # 需要进一步实现刷新功能
st.show()