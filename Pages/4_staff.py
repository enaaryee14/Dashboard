import streamlit as st
import pandas as pd

def logout_button_top_right():
    # Two columns → left (wide), right (logout button)
    col1, col2 = st.columns([10, 2])

    with col2:
        logout_clicked = st.button("🚪Logout")

    if logout_clicked:
        st.session_state.clear()
        st.switch_page("pages/1_welcome.py")
logout_button_top_right()

# -----------------------------
# PAGE PROTECTION
# -----------------------------
if "logged_in" not in st.session_state or st.session_state["logged_in"] != True:
    st.switch_page("1_Login.py")

if st.session_state.get("user_role") != "staff":
    st.error("Access denied. Staff only.")
    st.stop()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Staff Dashboard | NIC", layout="wide")

st.title("Staff Dashboard")
st.markdown("### Welcome! Here are the tasks assigned to you.")

# -----------------------------------------------
# PLACEHOLDER TASK DATA (shared with commissioner)
# -----------------------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = pd.DataFrame([
        {"Department": "Finance", "Task": "Prepare Q1 budget", "Assigned To": "staff1", "Status": "In Progress"},
        {"Department": "IT", "Task": "Upgrade servers", "Assigned To": "staff2", "Status": "Not Started"},
        {"Department": "Claims", "Task": "Review pending claims", "Assigned To": "staff3", "Status": "Completed"},
    ])

tasks_df = st.session_state.tasks

# Identify logged-in staff user
current_staff = st.session_state.get("username", "Unknown")

# -----------------------------------------------
# FILTER TASKS FOR THIS STAFF MEMBER
# -----------------------------------------------
my_tasks = tasks_df[tasks_df["Assigned To"] == current_staff]

st.subheader("📌 My Tasks")

if my_tasks.empty:
    st.info("You currently have no tasks assigned.")
else:
    st.dataframe(my_tasks, use_container_width=True)

# -----------------------------------------------
# UPDATE TASK PROGRESS
# -----------------------------------------------
st.subheader("🔄 Update Task Status")

if not my_tasks.empty:
    task_names = my_tasks["Task"].tolist()
    selected_task = st.selectbox("Select task to update", task_names)

    new_status = st.selectbox("New Status", ["Not Started", "In Progress", "Completed"])

    if st.button("Update Task"):
        task_index = tasks_df[tasks_df["Task"] == selected_task].index[0]
        st.session_state.tasks.loc[task_index, "Status"] = new_status

        st.success(f"Status updated successfully for '{selected_task}'")
        st.experimental_rerun()
else:
    st.write("No task available for update.")

# REAL-TIME CHAT SYSTEM (Staff <-> Commissioner)

st.subheader("💬 Chat With Commissioner")

# Initialize shared chat history
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
            "sender": st.session_state.get("username", "Staff"),
            "message": new_message,
            "time": datetime.now().strftime("%H:%M")
        })
        st.experimental_rerun()

