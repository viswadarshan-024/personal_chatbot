import streamlit as st
from chatbot_core import generate_response, create_new_session, list_sessions, get_chat_history, get_session_name
from datetime import datetime

if "current_session" not in st.session_state:
    st.session_state["current_session"] = create_new_session()

st.sidebar.title("Chat Sessions")
st.sidebar.subheader("Manage your chat sessions")

sessions = list_sessions()
for session in sessions:
    session_name = get_session_name(session)
    if st.sidebar.button(f"Switch to: {session_name}", key=session):
        st.session_state["current_session"] = session

if st.sidebar.button("New Chat"):
    new_session_id = create_new_session()
    st.session_state["current_session"] = new_session_id

current_session = st.session_state["current_session"]
st.sidebar.write(f"Current Session: {get_session_name(current_session)}")

st.title("🤖 Personal Chatbot")
st.subheader(f"Chatting in: {get_session_name(current_session)}")

chat_container = st.container()
with chat_container:
    chat_history = get_chat_history(current_session)
    for message in chat_history:
        if message["type"] == "human":
            st.markdown(
                f"""
                <div style='text-align: right; padding: 10px; margin: 5px; border: 1px solid #3498db; border-radius: 5px; background-color: #2c3e50; color: #ecf0f1;'>
                    <b>You:</b> {message['content']} <i style='color: gray;'>{message.get('timestamp', '')}</i>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif message["type"] == "ai":
            st.markdown(
                f"""
                <div style='text-align: left; padding: 10px; margin: 5px; border: 1px solid #2ecc71; border-radius: 5px; background-color: #34495e; color: #ecf0f1;'>
                    <b>AI:</b> {message['content']} <i style='color: gray;'>{message.get('timestamp', '')}</i>
                </div>
                """,
                unsafe_allow_html=True
            )

st.write("---")  

input_container = st.container()
with input_container:
    with st.form(key='input_form', clear_on_submit=True):
        user_input = st.text_input("Enter your message:", key="user_input", label_visibility="collapsed")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            if user_input.strip():
                response = generate_response(current_session, user_input)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                with chat_container:
                    st.markdown(
                        f"""
                        <div style='text-align: right; padding: 10px; margin: 5px; border: 1px solid #3498db; border-radius: 5px; background-color: #2c3e50; color: #ecf0f1;'>
                            <b>You:</b> {user_input} <i style='color: gray;'>{timestamp}</i>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f"""
                        <div style='text-align: left; padding: 10px; margin: 5px; border: 1px solid #2ecc71; border-radius: 5px; background-color: #34495e; color: #ecf0f1;'>
                            <b>AI:</b> {response} <i style='color: gray;'>{timestamp}</i>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.warning("Please enter a message.")

st.write("---")
st.markdown("<div style='text-align: center; color: #bdc3c7;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
