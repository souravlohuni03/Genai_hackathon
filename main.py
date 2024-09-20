import streamlit as st
import datetime

def main():
    # Set page config
    st.set_page_config(page_title="Credit Application Form", layout="wide")

    # Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #4CAF50;
        border-radius: 5px;
        height: 3em;
        width: 100%;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stSelectbox>div>div>select {
        border-radius: 5px;
    }
    .stDateInput>div>div>input {
        border-radius: 5px;
    }
    .stNumberInput>div>div>input {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Credit Application Form</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please fill out all required fields below</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p class="big-font">Personal Information</p>', unsafe_allow_html=True)
        st.text_input("First name")
        st.text_input("Middle name (optional)")
        st.text_input("Last name")
        st.text_input("Suffix (optional)")
        
        st.markdown('<p class="big-font">Residential Address</p>', unsafe_allow_html=True)
        st.text_input("Address line 1")
        st.text_input("Address line 2 (optional)")
        st.text_input("City")
        st.selectbox("State", ["Select State"] + ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"])
        st.text_input("ZIP code")
        st.checkbox("Send my statement to a different address")

    with col2:
        st.markdown('<p class="big-font">Contact Information</p>', unsafe_allow_html=True)
        st.radio("Primary phone number", ["Mobile phone", "Home phone"])
        st.text_input("Phone number")
        st.text_input("Email address")
        
        st.markdown('<p class="big-font">Citizenship</p>', unsafe_allow_html=True)
        st.radio("Are you a U.S. citizen?", ["Yes", "No"])
        st.radio("Do you have a dual citizenship?", ["Yes", "No"])
        st.text_input("Country of residence")
        
        st.markdown('<p class="big-font">Personal Details</p>', unsafe_allow_html=True)
        st.date_input("Date of birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
        st.selectbox("Employment status", ["Select status", "Employed", "Homemaker", "Retired", "Self-Employed", "Student", "Unemployed"])
        st.number_input("Total gross annual income ($)", min_value=0, step=1000)
        st.selectbox("Primary source of income", ["Select source", "Employment", "Inheritance", "Trust Investment Income", "Retirement Income", "Social Security", "Unemployment", "Other Income"])
        st.number_input("Monthly housing payment ($)", min_value=0, step=100)

    st.markdown("---")
    if st.button("Submit Application"):
        st.success("Application submitted successfully!")

if __name__ == "__main__":
    main()
