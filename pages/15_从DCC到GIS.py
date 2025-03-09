import streamlit as st
st.set_page_config(layout="wide")
st.title("从DCC到GIS")
st.subheader("1.离线渲染", divider=True)
st.write("我接触DCC是在Windows系统自带的画图3D，功能比较少。为了进一步探索DCC，安装了相对热门的Blender，但因为不了解操作方法而弃用。后来偶然接触到Adobe Dimension，带有离线渲染引擎并且操作比较简单，当时因为一些项目接触了SolidWorks，部分作品是用SolidWorks建模的。为了探索更多功能，又接触了Substance 3D Stager，可以渲染视频，速度也明显优于Adobe Dimension。")
st.write("为了使用更多动画功能，我具体了解操作后正式入坑了Blender，在之前的软件了解PBR等知识后，入坑Blender也变得更容易。在Blender中，我重点探索了程序化建模等功能。这一部分和下一部分的视频发布在https://space.bilibili.com/478036060? ，Blender项目的工程文件发布在https://github.com/Willian7004/my_Blender_programs 。")
st.subheader("2.实时渲染", divider=True)
st.write("使用离线渲染软件能做出真实的渲染效果，但在PC上难以制作大场景，面数较多的场景预览也很慢，因此较多尝试实时渲染引擎。刚开始尝试虚幻5，由于操作上不习惯就改用基于虚幻引擎的Twinmotion。在Twinmotion做了不少建筑和园林题材的场景，其中使用路径追踪功能渲染的图片发布在https://www.xiaohongshu.com/user/profile/6605a535000000000b00c4d2? 。")
st.write("由于Twinmotion的草地清晰度一般，并且希望探索更多交互式内容的制作，具体了解相关操作后正式入坑虚幻5。在虚幻5使用Megascans模型的精度优于Twinmotion内置的模型，但空间占用也较大。由于虚幻5的Lumen渲染效果比较好并且稳定性强，我在虚幻5就没有继续制作图片内容。")
st.subheader("3.谷歌地球", divider=True)
st.write("使用DCC软件搭建接近现实的场景的流程比较复杂，并且制作面数多的场景时卡顿明显。对此我一方面逐步转向AI视频创作，另一方面使用谷歌地球来实现根据可视范围加载带光照的模型，即使在核显也可以流畅运行。")
st.write("谷歌地球可以直接预览，结合街景功能可以实现“云旅游”，这也是GIS的一个重要意义。我制作谷歌地球的视频一方面考虑到实时预览需要不少时间加载模型，另一方面方便跟其他人分享。此外，一些用户受网络限制难以获取国外区域的高分辨率卫星图等GIS数据，无法了解其它国家在住房等方面的真实情况。因此我制作了大量城市的视频，总计数十小时，发布在https://www.acfun.cn/u/76077623")

