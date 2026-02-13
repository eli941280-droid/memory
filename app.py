import streamlit as st
import datetime
import time
import os

# 1. 基础配置
st.set_page_config(page_title="26天，爱在跳动", page_icon="💖")

# 自定义样式：增加相册美化
st.markdown("""
    <style>
    .stApp { background-color: #fffafa; }
    .heart-timer { font-size: 2.2rem !important; color: #ff4b4b; font-weight: bold; text-align: center; margin: 10px 0; }
    .card { background: white; padding: 20px; border-radius: 20px; box-shadow: 0 4px 15px rgba(255, 75, 75, 0.1); margin-bottom: 20px; text-align: center; }
    .img-caption { font-size: 0.8rem; color: #888; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 身份验证 ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🔒 专属验证")
    ans = st.text_input("每天晚上都要干啥？")
    if st.button("进入时光机"):
        if ans.lower() == "video":
            st.session_state['auth'] = True
            st.balloons()
            st.rerun()
        else:
            st.error("暗号不对哦，再想想？")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. 主界面 (验证通过后显示) ---
else:
    # 恋爱起点：2026.1.18
    start_date = datetime.datetime(2026, 1, 18, 0, 0, 0)

    # 顶部实时计时
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("我们已经在一起")
    timer_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 📸 重点：聊天记录照片墙 ---
    st.markdown("### 🎞️ 那些心动瞬间")
    st.write("点击图片可以放大看我们的‘通话长跑’纪录")

    # 自动识别当前目录下的所有图片 (png, jpg, jpeg)
    valid_images = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if valid_images:
        # 每行放2张照片，手机端看起来比例最舒服
        cols = st.columns(2)
        for i, img_name in enumerate(sorted(valid_images)):
            with cols[i % 2]:
                st.image(img_name, use_container_width=True)
                st.markdown(f'<p class="img-caption">Moment {i + 1}</p>', unsafe_allow_html=True)
    else:
        st.warning("还没把照片放进文件夹哦！快把截图放进来~")

    st.markdown("""
    <div class="card">
        <p>✨ <b>统计笔记</b></p>
        <p style='font-size:0.9rem; color:#666;'>
            我们最久的一次聊了 <b>6小时58分</b><br>
            这26天里，每一个 Duration 都是陪伴的刻度。
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 刷新计时器
    while True:
        now = datetime.datetime.now()
        diff = now - start_date
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        with timer_placeholder.container():
            st.markdown(f'<p class="heart-timer">{days}天 {hours:02d}:{minutes:02d}:{seconds:02d}</p>',
                        unsafe_allow_html=True)
        time.sleep(1)