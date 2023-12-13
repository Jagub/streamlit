import streamlit as st

# Define the Streamlit app
def main():
    st.title("Find the Largest Among Three Numbers")

    # Get input from the user
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Find the largest number
    largest_number = find_largest(num1, num2, num3)

    # Display the result
    st.write("The largest number is:", largest_number)

# Function to find the largest number among three
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)
