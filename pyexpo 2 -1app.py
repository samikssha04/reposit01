import streamlit as st
import random
import math
st.title("Portfolio")
st.markdown(" <p style = 'color: black;font-family:lucida comsole;'> NAME:SREE SOUJANYA  K</p>",unsafe_allow_html=True)
st.markdown("<p style = 'color: black;font-family:lucida console;'> COLLEGE : KGISL Institute of Technology </p>",unsafe_allow_html=True)
st.markdown("<p style = 'color: black;font-family:lucida console;'>DEPARTMENT: B.E. Computer Science and Engineering</p>",unsafe_allow_html=True)
st.markdown("<p style = 'color : black; font-family:lucida console';>ROLL NO: 24UCS243</p>",unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://img.freepik.com/freevector/abstractbackground-design-dark-green_53876-59276.jpg');
        background-size:cover;
        background-repeat:no-repeat;
    
      }
    </style>
    """,
    unsafe_allow_html=True
          
)

st.image('https://c0.wallpaperflare.com/preview/920/519/697/abstract-php-c-analytics.jpg',width=900)




def display_rules(mode):
    if mode == "User Guessing":
        st.subheader("User Guessing Rules")
        st.write("""
        1. The computer has randomly selected a number within your specified range.
        2. Your task is to guess this number.
        3. You will receive feedback on whether your guess is too high or too low.
        4. Try to guess the number within the maximum attempts you set!
        """)
    elif mode == "Machine Guessing":
        st.subheader("Machine Guessing Rules")
        st.write("" "
        1. Think of a number within the range you specify.
        2. The machine will attempt to guess your number using a binary search strategy.
        3. You will provide feedback on whether the guess is too low, too high, or correct.
        4. The machine will aim to guess your number in the fewest attempts possible!
        """)

def user_guessing_game():
    st.title("User Guessing Game")

    # Inputs for range and max attempts
    lower_bound = st.number_input("Enter the lower bound:", value=1, key="user_lower")
    upper_bound = st.number_input("Enter the upper bound:", value=100, key="user_upper")
    max_attempts = st.number_input("Set maximum attempts:", min_value=1, value=5, key="max_attempts")

    if lower_bound >= upper_bound:
        st.warning("Please ensure the upper bound is greater than the lower bound.")
        return

    if 'secret_number' not in st.session_state or st.session_state.get('is_new_game', True):
        st.session_state.secret_number = random.randint(lower_bound, upper_bound)
        st.session_state.attempts = 0
        st.session_state.is_new_game = False

    if st.button("Start Game"):
        st.session_state.secret_number = random.randint(lower_bound, upper_bound)
        st.session_state.attempts = 0
        st.session_state.is_new_game = False
        st.success("Game has started! Make your guess.")

    guess = st.number_input(f"Guess a number between {lower_bound} and {upper_bound}:",
                             min_value=lower_bound, max_value=upper_bound, key="guess_input")

    if st.button("Submit Guess", key="submit_guess"):
        if guess is not None:
            st.session_state.attempts += 1
            if guess < st.session_state.secret_number:
                st.write("Too low! Try again.")
            elif guess > st.session_state.secret_number:
                st.write("Too high! Try again.")
            else:
                st.success(f"Congratulations! You've guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts.")
                st.session_state.is_new_game = True  # Use a different key here
                st.balloons()

            if st.session_state.attempts >= max_attempts:
                st.error("You've reached the maximum number of attempts! Game over.")
                st.write(f"The number was {st.session_state.secret_number}.")
                st.session_state.is_new_game = True

    if st.session_state.get('is_new_game', False):
        if st.button("Start New Game", key="new_game"):
            st.session_state.secret_number = None  # Reset just this key
            st.session_state.attempts = 0
            st.session_state.is_new_game = False

def machine_guessing_game():
    st.title("Machine Guessing Game")

    # Initialize session state for bounds and attempts if not already set
    if 'machine_lower' not in st.session_state:
        st.session_state.machine_lower = 1
    if 'machine_upper' not in st.session_state:
        st.session_state.machine_upper = 100
    if 'max_attempts' not in st.session_state:
        st.session_state.max_attempts = 5  # Default maximum attempts
    if 'machine_attempts' not in st.session_state:
        st.session_state.machine_attempts = 0
    if 'is_machine_new_game' not in st.session_state:
        st.session_state.is_machine_new_game = True

    # Only allow setting of input fields when starting a new game
    if st.session_state.is_machine_new_game:
        # Inputs for range and maximum attempts
        lower_bound = st.number_input("Enter the lower bound:", value=st.session_state.machine_lower, key="machine_lower_input")
        upper_bound = st.number_input("Enter the upper bound:", value=st.session_state.machine_upper, key="machine_upper_input")
        max_attempts = st.number_input("Set maximum attempts:", min_value=1, value=st.session_state.max_attempts, key="max_attempts_input")

        if lower_bound >= upper_bound:
            st.warning("Please ensure the upper bound is greater than the lower bound.")
            return

        if st.button("Start Game", key="start_machine_game"):
            # Set session state values for the game
            st.session_state.machine_lower = lower_bound
            st.session_state.machine_upper = upper_bound
            st.session_state.max_attempts = max_attempts
            st.session_state.machine_attempts = 0  # Reset attempts
            st.session_state.is_machine_new_game = False
            st.write("Think of a number between {} and {}.".format(st.session_state.machine_lower, st.session_state.machine_upper))
            st.write("Press 'Submit Guess' once you have your number in mind.")

    else:
        # Game logic
        if st.session_state.machine_attempts < st.session_state.max_attempts:
            guess = (st.session_state.machine_lower + st.session_state.machine_upper) // 2
            st.write(f"My guess is: {guess}")

            feedback = st.radio("Is my guess too low, too high, or correct?", 
                                ("Too Low", "Too High", "Correct"), key=f"feedback_{st.session_state.machine_attempts}")

            if st.button("Submit Guess", key="submit_machine_guess"):
                st.session_state.machine_attempts += 1  # Increment attempts
                if feedback == "Too Low":
                    st.session_state.machine_lower = guess + 1
                elif feedback == "Too High":
                    st.session_state.machine_upper = guess - 1
                elif feedback == "Correct":
                    st.success(f"I guessed your number {guess} in {st.session_state.machine_attempts} attempts!")
                    st.session_state.is_machine_new_game = True  # Start a new game
                    st.balloons()  # Celebration effect

                # Check if maximum attempts have been reached
                if st.session_state.machine_attempts >= st.session_state.max_attempts:
                    st.error("You've reached the maximum number of attempts! Game over.")
                    st.session_state.is_machine_new_game = True  # Start a new game

        if st.session_state.is_machine_new_game:
            if st.button("Start New Game", key="start_new_machine_game"):
                st.session_state.machine_attempts = 0  # Reset attempts for a new game
                st.session_state.is_machine_new_game = True



def main():
    st.title("Guessing Game Modes")
    mode = st.radio("Choose a mode:", ("User Guessing", "Machine Guessing"))

    display_rules(mode)

    if mode == "User Guessing":
        user_guessing_game()
    elif mode == "Machine Guessing":
        machine_guessing_game()

if _name_ == "_main_":
    main()
