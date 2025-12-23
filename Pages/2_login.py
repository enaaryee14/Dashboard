import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Login | NIC Dashboard", page_icon="🔐")

# --- Custom CSS to style login box ---
page_bg = """
<style>
.stApp {
    background-color: #f5f5f5;
}

.login-box {
    padding: 30px;
    background: white;
    width: 350px;
    margin: auto;
    margin-top: 80px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.18);
}

.login-title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 10px;
    font-weight: 600;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# --- Login Form ---
with st.container():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown('<p class="login-title">NIC Login</p>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    login_btn = st.button("Login")

    st.markdown("</div>", unsafe_allow_html=True)


# --- Simple Authentication Logic ---
if login_btn:
    # Hardcoded credentials for now — later we will connect a database
    if username == "admin" and password == "1234":
        st.success("Login successful! Welcome Commissioner.")
        st.session_state["user_role"] = "commissioner"
        st.session_state["logged_in"] = True
        st.switch_page("pages/3_commissioner.py")

    elif username == "staffadd" and password == "1234":
        st.success("Login successful! Welcome Staff Member.")
        st.session_state["user_role"] = "staff"
        st.session_state["logged_in"] = True
        st.switch_page("pages/4_staff.py")

    else:
        st.error("Invalid username or password.")

st.session_state["username"] = username
