import streamlit as st
import base64
import os

st.set_page_config(page_title="うたボタン", layout="wide")

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

bg_base64 = get_base64_image("static/background.jpg")

# ボタン位置パラメータ
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 130
LEFT_START = 40
TOP_START = 40
X_SPACING = 165
Y_SPACING = 155

buttons = [
    {"title": "いぬのおまわりさん", "sound": "inu.mp3"},
    {"title": "どんぐりころころ", "sound": "donguri.mp3"},
    {"title": "うさぎ", "sound": "usagi.mp3"},
    {"title": "あめふり", "sound": "amefuri.mp3"},
    {"title": "きんたろう", "sound": "kintaro.mp3"},
    {"title": "あかいとりことり", "sound": "あかいとりことり.mp3"},
    {"title": "こいのぼり", "sound": "koinobori.mp3"},
    {"title": "たこのうた", "sound": "tako.mp3"},
    {"title": "しゃぼんだま", "sound": "shabon.mp3"},
    {"title": "アルプス", "sound": "alps.mp3"},
    {"title": "うらしま", "sound": "urashima.mp3"},
    {"title": "むしのこえ", "sound": "mushi.mp3"},
    {"title": "あたまポン", "sound": "atamapon.mp3"},
    {"title": "しょうじょうじ", "sound": "tanuki.mp3"},
    {"title": "きらきらぼし", "sound": "kirakira.mp3"},
    {"title": "アンパンマン", "sound": "anpanman.mp3"},
]

# ボタンHTMLを全部まとめる
button_html = ""
for i, btn in enumerate(buttons):
    row = i // 4
    col = i % 4
    top = TOP_START + row * Y_SPACING
    left = LEFT_START + col * X_SPACING
    button_html += f"""
    <button onclick="window.location.search='?play={btn['sound']}'"
            class="button"
            style="top: {top}px; left: {left}px;">
    </button>
    """

# 背景とボタン
st.markdown(f"""
<style>
.container {{
    position: relative;
    width: 768px;
    height: 1024px;
    background-image: url("data:image/jpeg;base64,{bg_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    border: 2px solid #ccc;
    margin: 0 auto;
}}

.button {{
    position: absolute;
    background-color: rgba(100, 100, 255, 0.3);  /* 半透明で見える */
    border: 2px solid rgba(0, 0, 0, 0.2);
    border-radius: 12px;
    width: {BUTTON_WIDTH}px;
    height: {BUTTON_HEIGHT}px;
    cursor: pointer;
}}
</style>
<div class="container">
{button_html}
</div>
""", unsafe_allow_html=True)

# 音声再生
query_params = st.query_params
if "play" in query_params:
    sound_file = query_params["play"][0]
    sound_path = f"static/sounds/{sound_file}"
    if os.path.exists(sound_path):
        st.audio(sound_path, format="audio/mp3")
    else:
        st.warning(f"音声ファイルが見つかりません: {sound_file}")
