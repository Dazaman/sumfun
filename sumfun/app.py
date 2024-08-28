import streamlit as st
import random

# Initialize session state for the score if it doesn't exist
if "score" not in st.session_state:
    st.session_state["score"] = 0


def refresh_problems():
    # Clear all problem-related session state variables
    for key in list(st.session_state.keys()):
        if key.startswith(("num", "sub_num", "mul_num", "div_num")):
            del st.session_state[key]


def main():
    st.title("Arithmetic Practice")

    if "score" not in st.session_state:
        st.session_state["score"] = 0

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    with tab1:
        addition()
    with tab2:
        subtraction()
    with tab3:
        multiplication()
    with tab4:
        division()

    # Add refresh button to sidebar
    st.sidebar.header("Controls")
    if st.sidebar.button("Refresh All Problems"):
        refresh_problems()

    st.sidebar.header("Score")
    st.sidebar.write(f"Your score: {st.session_state['score']}")


def addition():
    def check_answer():  # Callback function
        user_input = st.session_state[
            f"addition_input_{st.session_state.num1}_{st.session_state.num2}"
        ]
        try:
            ans = int(user_input)
            if ans == st.session_state.num1 + st.session_state.num2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(
                    f"Incorrect. The answer is {st.session_state.num1 + st.session_state.num2}"
                )
        except ValueError:
            st.error("Please enter a valid integer.")

    if "num1" not in st.session_state or "num2" not in st.session_state:
        st.session_state.num1 = random.randint(1, 100)
        st.session_state.num2 = random.randint(1, 100)

    with st.form(key="addition_form"):
        st.write(f"What is {st.session_state.num1} + {st.session_state.num2}?")
        answer = st.number_input(
            "Enter your answer:",
            value=0,
            step=1,
            key=f"addition_input_{st.session_state.num1}_{st.session_state.num2}",
        )
        _ = st.form_submit_button("Check Answer", on_click=check_answer)


def subtraction():
    def check_answer():  # Callback function
        user_input = st.session_state[
            f"subtraction_input_{st.session_state.sub_num1}_{st.session_state.sub_num2}"
        ]
        try:
            ans = int(user_input)
            if ans == st.session_state.sub_num1 - st.session_state.sub_num2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(
                    f"Incorrect. The answer is {st.session_state.sub_num1 - st.session_state.sub_num2}"
                )
        except ValueError:
            st.error("Please enter a valid integer.")

    if "sub_num1" not in st.session_state or "sub_num2" not in st.session_state:
        st.session_state.sub_num1 = random.randint(1, 100)
        st.session_state.sub_num2 = random.randint(1, 100)
        # Ensure num1 >= num2 for simple subtraction
        if st.session_state.sub_num1 < st.session_state.sub_num2:
            st.session_state.sub_num1, st.session_state.sub_num2 = (
                st.session_state.sub_num2,
                st.session_state.sub_num1,
            )

    with st.form(key="subtraction_form"):
        st.write(f"What is {st.session_state.sub_num1} - {st.session_state.sub_num2}?")
        answer = st.number_input(
            "Enter your answer:",
            value=0,
            step=1,
            key=f"subtraction_input_{st.session_state.sub_num1}_{st.session_state.sub_num2}",
        )
        _ = st.form_submit_button("Check Answer", on_click=check_answer)


def multiplication():
    def check_answer():  # Callback function
        user_input = st.session_state[
            f"multiplication_input_{st.session_state.mul_num1}_{st.session_state.mul_num2}"
        ]
        try:
            ans = int(user_input)
            if ans == st.session_state.mul_num1 * st.session_state.mul_num2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(
                    f"Incorrect. The answer is {st.session_state.mul_num1 * st.session_state.mul_num2}"
                )
        except ValueError:
            st.error("Please enter a valid integer.")

    if "mul_num1" not in st.session_state or "mul_num2" not in st.session_state:
        st.session_state.mul_num1 = random.randint(1, 12)
        st.session_state.mul_num2 = random.randint(1, 12)

    with st.form(key="multiplication_form"):
        st.write(f"What is {st.session_state.mul_num1} * {st.session_state.mul_num2}?")
        answer = st.number_input(
            "Enter your answer:",
            value=0,
            step=1,
            key=f"multiplication_input_{st.session_state.mul_num1}_{st.session_state.mul_num2}",
        )
        _ = st.form_submit_button("Check Answer", on_click=check_answer)


def division():
    def check_answer():  # Callback function
        user_input = st.session_state[
            f"division_input_{st.session_state.div_num1}_{st.session_state.div_num2}"
        ]
        try:
            ans = int(user_input)
            if ans == st.session_state.div_num1 // st.session_state.div_num2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(
                    f"Incorrect. The answer is {st.session_state.div_num1 // st.session_state.div_num2}"
                )
        except ValueError:
            st.error("Please enter a valid integer.")

    if "div_num1" not in st.session_state or "div_num2" not in st.session_state:
        st.session_state.div_num2 = random.randint(1, 12)
        st.session_state.div_num1 = st.session_state.div_num2 * random.randint(1, 12)

    with st.form(key="division_form"):
        st.write(f"What is {st.session_state.div_num1} / {st.session_state.div_num2}?")
        answer = st.number_input(
            "Enter your answer:",
            value=0,
            step=1,
            key=f"division_input_{st.session_state.div_num1}_{st.session_state.div_num2}",
        )
        _ = st.form_submit_button("Check Answer", on_click=check_answer)


st.sidebar.header("Score")
st.sidebar.write(f"Your score: {st.session_state['score']}")

if __name__ == "__main__":
    main()
