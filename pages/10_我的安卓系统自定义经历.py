import streamlit as st
st.set_page_config(layout="wide")
st.title("我的安卓系统自定义经历")
st.subheader("1.儿时的root", divider=True)
st.write("小时候家长有一台三星手机，印象中是安卓4.2系统，当时安卓系统的功能不完善，有第三方的root管理工具可以通过系统的一些漏洞获取root权限。由于系统自带的管理功能不完善，在root后通过第三方工具可以实现自启动管理和权限管理等功能，其它功能当时没有接触。后来家长用了系统新一些的手机，这种root方式就失效了。")
st.subheader("2.错选的adb", divider=True)
st.write("我在选择自己的第一台手机时，比较注重在摄影上的表现，没有留意能否root，选了OPPO Find X5 Pro。早期使用正常，使用两年后不少程序流畅度低、续航明显下降并且系统自带的相机程序卡顿。就卸载了不必要的程序，把剩余的大部分程序换成优化更好的play版，达到了比较好的流畅度表现，但续航表现仍然不好。又了解了相关知识，安装了Scene用于性能监测，发现不少程序后台能耗较高，并且手动关闭后改善有限。又安装了黑域，借助无线调试自动关闭后台程序，只有必要的程序允许后台运行或定时启动接收消息，续航也得到改善。另外使用了洪图标包以改善大部分程序的图标外观。")
st.subheader("3.现在的刷机", divider=True)
st.write("虽然更换程序和使用adb后改善了主力机的表现，但能对系统自定义的程度还是远小于root。考虑到不更换主力机要控制预算，同时尝试LCD屏幕和平板电脑，就入手了无锁小米平板4。上一任机主安装的是Pixel Experience，感觉通知栏外观不太好，就参考网友的一些测试查找外观比较好的系统。这部分大部分没有适配小米平板4或者适配的版本外观优化幅度比较小。就尝试用LineageOS+Iconify方案。开始时用了整合KernelSU的LineageOS21,流畅度表现不好，换成LineageOS19后流畅度正常。使用Iconify进行外观自定义改善了通知栏和设置图标外观。由于系统自带桌面启动器在连续添加图标时有bug，就改用Lawnchair桌面启动器和洪图标包。")
st.write("以下是进行外观自定义后的效果（Iconify有大量自定义模块，也会不定期进行更换，这里只展示了第一版和创作本段使用的共两版）：")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("通知栏1")
    st.image("files/iconify_1.jpg")
with col2:
    st.subheader("快速设置面板1")
    st.image("files/iconify_2.jpg")
with col3:
    st.subheader("设置图标1")
    st.image("files/iconify_3.jpg")
col4, col5, col6 = st.columns(3)
with col4:
    st.subheader("通知栏2")
    st.image("files/iconify_4.jpg")
with col5:
    st.subheader("快速设置面板2")
    st.image("files/iconify_5.jpg")
with col6:
    st.subheader("设置图标2")
    st.image("files/iconify_6.jpg")
st.write("除了外观自定义外，运行Scene同样使用了root，后台程序管理使用了NoActive，可以实现墓碑机制。")
st.write("以后选择下一台主力机时还是会优先选择能root的手机。我目前用的OPPO的深度测试在上一代结束；小米从小米14开始是出厂澎湃系统，需要社区等级以及答题，root门槛提高；努比亚在Z60/红魔9一代后也取消了root；国外的三星等品牌能root但性价比低。如果要选新的手机，能考虑的就只有一加了。")

