import streamlit as st
import datetime
import time

# 页面基础设置
st.set_page_config(page_title="我们的时光机", page_icon="💖", layout="centered")

# 自定义 CSS 样式，让手机端看起来更高级
st.markdown("""
    <style>
    .stApp { background-color: #fff5f5; }
    .main-card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(255,105,180,0.2); text-align: center; }
    .heart-timer { font-size: 2.2rem !important; color: #ff4b4b; font-weight: bold; margin: 20px 0; }
    .stat-text { color: #666; font-size: 1rem; line-height: 1.6; }
    .error-text { color: #ff4b4b; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 暗号校验逻辑 ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("🔒 身份验证")
    st.write("输入我们的专属暗号才能进入时光机")

    answer = st.text_input("每天晚上都要干啥？", placeholder="请输入暗号...")

    if st.button("确定"):
        if answer.lower() == "video":
            st.session_state['authenticated'] = True
            st.balloons()
            st.rerun()
        else:
            st.error("哼，答错了！再仔细想想？")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. 主界面逻辑 ---
else:
    # 恋爱起点：2026.1.18
    start_date = datetime.datetime(2026, 1, 18, 0, 0, 0)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("💌 属于我们的 26 天")

    # 动态计时占位符
    placeholder = st.empty()

    # 底部走心文案
    st.markdown("---")
    st.markdown(f"""
    <div class="stat-text">
        📸 <b>累计视频陪伴：</b> 超过 1260 分钟<br>
        🏆 <b>最长纪录：</b> 那一晚，我们聊了 6小时58分<br>
        ✨ <b>碎碎念：</b> 从 1 月 18 日相识到现在，<br>
        每一张视频截图都是我最宝贵的收藏。
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 实时刷新循环
    while True:
        now = datetime.datetime.now()
        diff = now - start_date

        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        with placeholder.container():
            st.markdown(f"""
                <p class="stat-text">我们已经在一起</p>
                <div class="heart-timer">
                    {days}天 {hours:02d}:{minutes:02d}:{seconds:02d}
                </div>
            """, unsafe_allow_html=True)

        time.sleep(1)