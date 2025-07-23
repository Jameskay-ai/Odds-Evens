# Core components for Streamlit / pandas / numpy
import streamlit as st

# Custom CSS styling
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #001f3f !important;
            color: white;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        .main, .block-container {
            background-color: #ffffff;
            color: #001f3f !important;
        }
        .block-container h1, 
        .block-container h2,
        .block-container h3,
        .block-container h4,
        .block-container h5,
        .block-container h6,
        .block-container p,
        .block-container li {
            color: #001f3f !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with explanation
with st.sidebar:
     # Button to redirect to Python Landing page
    st.caption("To view other projects click here")
    st.markdown(
        """
        <a href="https://jameskay-ai.github.io/" target="_blank">
            <button style="background-color:#004080; color:white; padding:10px; border:none; border-radius:5px;">
                Back to main
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.header("PROJECT DETAILS:")
    st.markdown("""
    This app takes a number and checks whether it's **even** or **odd** using basic Python logic.
    ### 📘 Real-World Applications
    - Detecting even/odd IDs
    - Alternating logic in games or automation
    - Basic input validation logic

    ### 🧾 Code Breakdown
    ```python
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
    ```
    - `%` checks the remainder of `number ÷ 2`.
    - If remainder is 0 → **even**.
    - Otherwise → **odd**.

    ### 💡 Key Concepts
    - Modulo operator (`%`)
    - Conditional logic (`if-else`)
    - Input/output interaction
    """)

# Main title and description
st.title("Welcome to the Python Porfolio")
st.subheader("🔢 Even or Odd Checker")
st.markdown("##### By: James Kay")
st.write("Enter a number below and find out if it's even or odd!")

# Input
number = st.number_input("Choose a number:", step=1, format="%d")

# Result logic
if number % 2 == 0:
    st.success(f"✅ The number **{number}** is even! 🎉")
else:
    st.info(f"ℹ️ The number **{number}** is odd! 🤓")
