import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    menu = option_menu(
        menu_title = "My Project",
        options = ["Home", "About", "Contact"],
        icons = ['house-door-fill', 'file-person', 'person-lines-fill']
    )

if menu == "Home":
    st.title("Bhunaya Group of Enterprises")
    st.image("https://th.bing.com/th/id/R.d68e3c4d65551a8a20d61bf68b7a6599?rik=AjPoqJy7lnFeOQ&riu=http%3a%2f%2fcdn.wallpapersafari.com%2f8%2f35%2fWEGgt5.jpeg&ehk=i5r7GsvthzeUlLOKuQXDFJ7ernumJggjvTBCpfEroiA%3d&risl=&pid=ImgRaw&r=0")
    
    st.write("An enterprise is a large organization, usually engaged in commercial, industrial, or professional activities. Enterprises can range from multinational corporations to regional businesses and may operate in various industries such as technology, finance, healthcare, manufacturing, and more.")



elif menu == "About":
    st.title("About Us")
    st.write("Welcome to Bhunaya innovation meets excellence. Established in 2023 have been at the forefront of marketing, delivering top-tier solutions that drive success.")
    st.divider()
    st.title("Our Mission")
    st.write("At [Enterprise Name], we are committed to [core mission—e.g., empowering businesses, enhancing technology, delivering quality products]. Our goal is to [key objective—e.g., redefine industry standards, create sustainable solutions, build long-term partnerships].")
    st.divider()
    st.title("Our Vision")
    st.write("We envision a future where [enterprise’s future goals—e.g., businesses operate seamlessly with technology, healthcare becomes more accessible, sustainability leads industries]. Our team of experts works tirelessly to turn that vision into reality.")
    st.divider()
    



elif menu == "Contact":
    st.title("Contact Form")
    name = st.text_input("Enter Your Name:")
    age = st.number_input("Enter Your Age:")
    gender = st.radio("Select Your Gender:", ["Male","Female"])
    doorno = st.number_input("Enter your Door Number: ")
    street = st.text_input("Enter Your Street Name: ")
    city = st.selectbox("Select Your District",["Theni","Madurai","Dindigul","Sivakasi"])
    email = st.text_input("Enter Your E-mail Id")
    st.button("Submit")

    st.table({

        "Name" : name,
        "Age" : age,
        "Gender" : gender,
        "City" : city,
        "Email" : email
    })



