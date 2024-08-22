import streamlit as st
import random

# Initialize session state for the score if it doesn't exist
if "score" not in st.session_state:
    st.session_state["score"] = 0


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


def addition():
    def check_answer(n1, n2, user_input):  # Callback function
        try:
            ans = int(user_input)  # Convert to integer inside the callback
            if ans == n1 + n2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(f"Incorrect. The answer is {n1 + n2}")
        except ValueError:
            st.error("Please enter a valid integer.")

    with st.form(key="addition_form"):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        st.write(f"What is {num1} + {num2}?")
        answer = st.number_input(
            "Enter your answer:", value=0, key=f"addition_input_{num1}_{num2}"
        )
        submitted = st.form_submit_button(
            "Check Answer", on_click=check_answer, args=(num1, num2, answer)
        )


def subtraction():
    def check_answer(n1, n2, user_input):  # Callback function
        try:
            ans = int(user_input)
            if ans == n1 - n2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(f"Incorrect. The answer is {n1 + n2}")
        except ValueError:
            st.error("Please enter a valid integer.")

    with st.form(key="subtraction_form"):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        # Ensure num1 >= num2 for simple subtraction
        if num1 < num2:
            num1, num2 = num2, num1
        st.write(f"What is {num1} - {num2}?")
        answer = st.number_input(
            "Enter your answer:", value=0, key=f"subtraction_input_{num1}_{num2}"
        )
        submitted = st.form_submit_button(
            "Check Answer", on_click=check_answer, args=(num1, num2, answer)
        )


def multiplication():
    def check_answer(n1, n2, user_input):  # Callback function
        try:
            ans = int(user_input)
            if ans == n1 * n2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(f"Incorrect. The answer is {n1 + n2}")
        except ValueError:
            st.error("Please enter a valid integer.")

    with st.form(key="multiplication_form"):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        st.write(f"What is {num1} * {num2}?")
        answer = st.number_input(
            "Enter your answer:", value=0, key=f"multiplication_input_{num1}_{num2}"
        )
        submitted = st.form_submit_button(
            "Check Answer", on_click=check_answer, args=(num1, num2, answer)
        )


def division():
    def check_answer(n1, n2, user_input):  # Callback function
        try:
            ans = int(user_input)
            if ans == n1 / n2:
                st.success("Correct!")
                st.session_state["score"] += 1
            else:
                st.error(f"Incorrect. The answer is {n1 + n2}")
        except ValueError:
            st.error("Please enter a valid integer.")

    with st.form(key="division_form"):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        # Ensure division results in a whole number
        num1 = num1 * num2
        st.write(f"What is {num1} / {num2}?")
        answer = st.number_input(
            "Enter your answer:", value=0, key=f"division_input_{num1}_{num2}"
        )
        submitted = st.form_submit_button(
            "Check Answer", on_click=check_answer, args=(num1, num2, answer)
        )


st.sidebar.header("Score")
st.sidebar.write(f"Your score: {st.session_state['score']}")

if __name__ == "__main__":
    main()
