import streamlit as st
import random
from fractions import Fraction

st.set_page_config(page_title="Limit Practice", page_icon="📐", layout="centered")

def generate_problem():
    """
    Generate b and c such that:
    1. (x + 1) / (x² + cx + b) = 0/0 at x = -1
    2. lim (x→-1) √((x + 1) / (x² + cx + b)) = 1/a for some integer a
    
    For 0/0 at x = -1:
    - Numerator: x + 1 = 0 at x = -1 ✓
    - Denominator: x² + cx + b = 0 at x = -1
      => 1 - c + b = 0
      => b = c - 1
    
    So (x + 1) must be a factor of (x² + cx + b)
    x² + cx + b = x² + cx + (c-1) = (x + 1)(x + c - 1)
    
    The expression becomes:
    √((x + 1) / ((x + 1)(x + c - 1))) = √(1 / (x + c - 1))
    
    At x = -1: lim = √(1 / (c - 2)) = 1/√(c - 2)
    
    For this to equal 1/a (integer a), we need c - 2 = a²
    So c = a² + 2
    """
    # Choosing a random integer a between 2 and 100 for our application
    a = random.randint(2, 100)
    
    # Calculate c and b
    c = a * a + 2
    b = c - 1
    
    # The answer is 1/a
    answer = Fraction(1, a)
    
    return b, c, answer, a

def evaluate_answer(user_input, correct_answer):
    """Evaluate if user's answer matches the correct answer"""
    try:
        # parse user input as fraction
        if '/' in user_input:
            user_answer = Fraction(user_input)
        else:
            user_answer = float(user_input)
            correct_float = float(correct_answer)
            # improvised acceptable margin of error. but can be changed for a more
            # or lesser margin of accuracy
            return abs(user_answer - correct_float) < 0.0001
        
        return user_answer == correct_answer
    except:
        return False

def show_solution(b, c, a):
    st.markdown("### Solution Explanation")
    
    st.markdown(f"""
    **Given**: $\\lim_{{x \\to -1}} \\sqrt{{\\frac{{x + 1}}{{x^2 + {c}x + {b}}}}}$
    
    **Step 1**: Check if this is an indeterminate form
    - At $x = -1$: numerator = $(-1) + 1 = 0$
    - At $x = -1$: denominator = $(-1)^2 + {c}(-1) + {b} = 1 - {c} + {b} = 0$
    - This gives us $0/0$ indeterminate form ✓
    
    **Step 2**: Factor the denominator
    - Since $(x + 1)$ is a factor: $x^2 + {c}x + {b} = (x + 1)(x + {c-1})$
    
    **Step 3**: Simplify the expression
    $$\\sqrt{{\\frac{{x + 1}}{{(x + 1)(x + {c-1})}}}} = \\sqrt{{\\frac{{1}}{{x + {c-1}}}}}$$
    
    **Step 4**: Evaluate the limit
    $$\\lim_{{x \\to -1}} \\sqrt{{\\frac{{1}}{{x + {c-1}}}}} = \\sqrt{{\\frac{{1}}{{-1 + {c-1}}}}} = \\sqrt{{\\frac{{1}}{{{c-2}}}}} = \\frac{{1}}{{\\sqrt{{{c-2}}}}} = \\frac{{1}}{{{a}}}$$
    
    **Answer**: $\\boxed{{\\frac{{1}}{{{a}}}}}$
    """)

# Initialize session state
if 'problem' not in st.session_state:
    st.session_state.problem = generate_problem()
    st.session_state.submitted = False
    st.session_state.show_explanation = False

# Main UI
st.title(" Limit Practice: Square Roots & Rational Expressions")
st.markdown("Practice evaluating limits involving indeterminate forms!")

# Display the problem
b, c, answer, a = st.session_state.problem

st.markdown("### Problem")
st.latex(f"\\lim_{{x \\to -1}} \\sqrt{{\\frac{{x + 1}}{{x^2 + {c}x + {b}}}}}")

# User input
st.markdown("### Your Answer")
user_input = st.text_input(
    "Enter your answer (as a fraction like '1/3' or decimal like '0.333'):",
    key="answer_input",
    disabled=st.session_state.submitted
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Submit Answer", disabled=st.session_state.submitted):
        if user_input:
            st.session_state.submitted = True
            st.session_state.is_correct = evaluate_answer(user_input, answer)
        else:
            st.warning("Please enter your answer!")

with col2:
    if st.button("New Problem"):
        st.session_state.problem = generate_problem()
        st.session_state.submitted = False
        st.session_state.show_explanation = False
        st.rerun()

# Feedback
if st.session_state.submitted:
    if st.session_state.is_correct:
        st.success("Correct! Well done!")
    else:
        st.error(f"Not quite. The correct answer is {answer} (or {float(answer):.4f})")
        st.info("check the explanation below!")
    
    # Show explanation button
    if st.button("Show Explanation" if not st.session_state.show_explanation else "Hide Explanation"):
        st.session_state.show_explanation = not st.session_state.show_explanation
        st.rerun()
    
    if st.session_state.show_explanation:
        show_solution(b, c, a)
