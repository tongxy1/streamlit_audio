import streamlit as st
import base64
import streamlit.components.v1 as components

def main():
    st.title("音频文件上传并播放")

    # 文件上传
    uploaded_file = st.file_uploader("请选择一个音频文件", type=["mp3", "wav", "ogg"])

    if uploaded_file is not None:
        # 将文件转换为 base64 编码
        audio_bytes = uploaded_file.read()
        audio_b64 = base64.b64encode(audio_bytes).decode()

        # 使用 HTML 和 <audio> 标签嵌入播放器
        audio_html = f"""
        <audio id="audioPlayer" controls>
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
            您的浏览器不支持音频播放。
        </audio>
        <br>
        
        <script>
            var audio = document.getElementById("audioPlayer");
            // 回放指定秒数的函数
            function rewindAudio(seconds) {{
                audio.currentTime = Math.max(0, audio.currentTime - seconds);
            }}
            // 快进指定秒数的函数
            function fowardAudio(seconds) {{
                audio.currentTime = Math.min(audio.duration, audio.currentTime + seconds);
            }}
        </script>
        <button onclick="rewindAudio(1)">回放 1 秒</button>
        <button onclick="rewindAudio(2)">回放 2 秒</button>
        <button onclick="rewindAudio(3)">回放 3 秒</button>
        <button onclick="rewindAudio(4)">回放 4 秒</button> 
        <button onclick="rewindAudio(5)">回放 5 秒</button>
        <button onclick="rewindAudio(6)">回放 6 秒</button>
        <br>
        <br>
        <button onclick="fowardAudio(1)">快进 1 秒</button>
        <button onclick="fowardAudio(2)">快进 2 秒</button>
        <button onclick="fowardAudio(3)">快进 3 秒</button>
        <button onclick="fowardAudio(4)">快进 4 秒</button> 
        <button onclick="fowardAudio(5)">快进 5 秒</button>
        <button onclick="fowardAudio(6)">快进 6 秒</button>

        """
        # 使用 st.markdown 渲染 HTML
        # st.markdown(audio_html, unsafe_allow_html=True)
        components.html(audio_html)
        #st.components.v1.html(audio_html)

if __name__ == "__main__":
    main()
