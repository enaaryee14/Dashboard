import streamlit as st

def logout_button_top_right():
    # Create two columns: left (wide) + right (button)
    col1, col2 = st.columns([10, 2])

    with col2:
        logout_clicked = st.button("🚪 Logout")

    if logout_clicked:
        st.session_state.clear()
        st.switch_page("pages/1_welcome.py")

logout_button_top_right()


import streamlit as st
import pandas as pd

import streamlit as st

# -----------------------------
# PAGE PROTECTION
# -----------------------------
if "logged_in" not in st.session_state or st.session_state["logged_in"] != True:
    st.switch_page("Pages/2_login.py")

if st.session_state.get("user_role") != "commissioner":
    st.error("Access denied. Commissioner only.")
    st.stop()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Commissioner Dashboard | NIC", layout="wide")

st.title("Commissioner Dashboard")
st.markdown("### Overview of Departments and Task Management")

# -----------------------------------------------
# PLACEHOLDER DATA (Later this will come from a database)
# -----------------------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = pd.DataFrame([
        {"Department": "Finance", "Task": "Prepare Q1 budget", "Assigned To": "staff1", "Status": "In Progress"},
        {"Department": "IT", "Task": "Upgrade servers", "Assigned To": "staff2", "Status": "Not Started"},
        {"Department": "Claims", "Task": "Review pending claims", "Assigned To": "staff3", "Status": "Completed"},
    ])

tasks_df = st.session_state.tasks

# -----------------------------------------------
# OVERVIEW SECTION
# -----------------------------------------------
st.subheader("📊 Department Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Tasks", len(tasks_df))

with col2:
    st.metric("Completed", tasks_df[tasks_df["Status"] == "Completed"].shape[0])

with col3:
    st.metric("In Progress", tasks_df[tasks_df["Status"] == "In Progress"].shape[0])


# -----------------------------------------------
# VIEW TASK TABLE
# -----------------------------------------------
st.subheader("📁 All Tasks")
st.dataframe(tasks_df, use_container_width=True)


# -----------------------------------------------
# ADD NEW TASK (Commissioner Function)
# -----------------------------------------------
st.subheader("➕ Assign New Task")

with st.form("add_task_form"):
    department = st.selectbox("Select Department", ["Finance", "IT", "Claims", "Inspections", "Actuarial"])

    task_name = st.text_input("Task Title")

    assigned_to = st.text_input("Assign To (Staff Name)")

    status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])

    submitted = st.form_submit_button("Create Task")

    if submitted:
        new_row = {"Department": department, "Task": task_name, "Assigned To": assigned_to, "Status": status}
        st.session_state.tasks.loc[len(st.session_state.tasks)] = new_row
        st.success("Task added successfully!")
        st.experimental_rerun()


# -----------------------------------------------
# UPDATE TASK PROGRESS (Staff Action)
# -----------------------------------------------
st.subheader("🔄 Update Task Progress (Staff Updates Will Show Here)")

selected_index = st.number_input("Enter task index to update:", min_value=0, max_value=len(tasks_df)-1)

new_status = st.selectbox("Update Status", ["Not Started", "In Progress", "Completed"])

if st.button("Update Task"):
    st.session_state.tasks.loc[selected_index, "Status"] = new_status
    st.success("Task status updated.")
    st.experimental_rerun()

# -----------------------------------------------
# REAL-TIME CHAT SYSTEM (Commissioner <-> Staff)
# -----------------------------------------------
st.subheader("💬 Chat With Staff")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Display chat messages
chat_box = st.container()
with chat_box:
    st.markdown(
        """
        <div style='height: 300px; overflow-y: scroll; padding: 10px; border: 1px solid #cccccc; border-radius: 6px; background-color: #f7f7f7;'>
        """,
        unsafe_allow_html=True
    )

    for msg in st.session_state.chat:
        st.markdown(
            f"""
            <div style='margin-bottom: 8px;'>
                <b>{msg['sender']}:</b> {msg['message']}  
                <span style='color: gray; font-size: 12px;'>({msg['time']})</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

# Message input area
st.markdown("### Send a Message")

new_message = st.text_input("Type your message here:")

if st.button("Send Message"):
    if new_message.strip() != "":
        from datetime import datetime
        
        st.session_state.chat.append({
            "sender": "Commissioner",
            "message": new_message,
            "time": datetime.now().strftime("%H:%M")
        })
        st.experimental_rerun()



