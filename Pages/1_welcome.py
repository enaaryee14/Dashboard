import streamlit as st

# --- PAGE CONFIG --- #
st.set_page_config(
    page_title="Welcome | Taskboard",
    page_icon="📊",
    layout="wide"
)

# --- CUSTOM CSS FOR CORPORATE LOOK --- #
st.markdown("""
    <style>
        body {
            background-color: #f4f6f9;
        }
        .welcome-box {
            background: white;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            width: 60%;
            margin: auto;
        }
        .title {
            font-size: 40px;
            font-weight: 800;
            margin-bottom: 10px;
            color: #003366;
        }
        .subtitle {
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            color: #777;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# --- MAIN LAYOUT --- #
st.markdown("<div class='welcome-box'>", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Coat_of_arms_of_Ghana.svg/640px-Coat_of_arms_of_Ghana.svg.png",
         width=120)

st.markdown("<div class='title'>Commissioner’s Task Management System</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>A centralized platform for tracking departmental activities, monitoring staff performance, and managing tasks across the Commission.</div>",
    unsafe_allow_html=True
)

# --- BUTTONS --- #
col1, col2, col3 = st.columns([1,2,1])

with col2:
    login = st.button("🔐 Proceed to Login", use_container_width=True)
    about = st.button("ℹ️ About the System", use_container_width=True)

# Redirect to login when clicked
if login:
    st.switch_page("Pages/2_login.py")

if about:
    st.info("""
    ### About This System  
    This platform enables the Commissioner of Insurance to:
    - Monitor activities across departments  
    - Track staff performance  
    - Assign, review and delete tasks  
    - Generate reports and dashboards  
    - Maintain transparency and accountability  
    """)

# --- FOOTER --- #
st.markdown("<div class='footer'>© 2025 National Insurance Commission — All Rights Reserved</div>", unsafe_allow_html=True)
