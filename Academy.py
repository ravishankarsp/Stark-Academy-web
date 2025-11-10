import streamlit as s
from datetime import date
import pandas as pd

s.set_page_config(page_title="Stark Academy",layout="wide")

s.sidebar.title("Navigation")
page = s.sidebar.radio("Go to", ["Home", "Courses", "Faculty", "Dashboard", "Feedback"])


if page == "Home":
   s.title("Home Page")
   s.header("🎓 Welcome to Stark Academy")
   s.write("Empowering learners to build their future through knowledge, skills, and innovation.")
   s.image("https://imgs.search.brave.com/RFt7CVPUdxSHecSteceJZM2P3fnRiTwvK0dqYrLUJ6A/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA1LzMyLzYzLzA3/LzM2MF9GXzUzMjYz/MDc0OF9Ccm1RUlo0/QkZJcjRPb0VnRm9y/czRJc1FtZTVPSFJu/OC5qcGc",width=800)
   s.write("At Stark Academy, we believe education should be accessible, practical, and inspiring. Our mission is to help students, professionals, and lifelong learners gain the confidence and expertise to achieve their goals.")
   s.header("🔍 What You Can Do Here")
   s.markdown("""
    - 📚 Explore **Departments & Courses**  
    - 🧑‍🎓 Check **Student Services**  
    - 🗓️ Stay updated with **College Events**  
    - 📞 Visit the **Contact Page** for inquiries
    """)
   s.markdown("---")
   s.markdown(
        f"""
           Created by Stark Academy {date.today().year} | All Rights Reserved
        """
     )


elif page == "Courses":
    s.title("Courses Page")
    s.header("Courses Avaliable")
    courses = [
    {
        "name": "Python Programming",
        "instructor": "Dr. Ravi Kumar",
        "duration": "6 weeks",
        "desc": "Learn Python from basics to advanced with practical projects."
    },
    {
        "name": "Data Science Basics",
        "instructor": "Prof. Meena R.",
        "duration": "8 weeks",
        "desc": "Understand data cleaning, analysis, and visualization."
    },
    {
        "name": "Web Development",
        "instructor": "Mr. Karthik S.",
        "duration": "10 weeks",
        "desc": "Create responsive websites using HTML, CSS, and JavaScript."
    },
    {
        "name": "AI Fundamentals",
        "instructor": "Dr. Anjali Tiwari",
        "duration": "12 weeks",
        "desc": "Dive into the world of Artificial Intelligence and Machine Learning."
    }
]


    for course in courses:
       with s.container():
                s.subheader(course["name"])
                s.write(f"👨‍🏫 **Instructor:** {course['instructor']}")
                s.write(f"⏳ **Duration:** {course['duration']}")
                s.write(f"📖 {course['desc']}")
                s.button("Enroll Now", key=course["name"])  # non-functional placeholder
                s.markdown("---")


elif page == "Faculty":
    Facutly = [
    {
        "instructorname": "Dr. Ravi Kumar",
        "Department": "Artifical Intelligence",
        "Email": "kumarravi@gmail.com",
        "Contact": 9898683287
        },
    {
        "instructorname": "Prof. Meena R.",
        "Department": "Data Science",
         "Email": "meenar@gmail.com",
        "Contact": 8195194519
    },
    {
        "instructorname": "Mr. Karthik S.",
        "Department": "Developer",
        "Email": "karthiks@gmail.com",
        "Contact": 8529631472
    },
    {
        "instructorname": "Dr. Anjali Tiwari",
        "Department" : "Data Science",
        "Email": "anjalit@gmail.com",
        "Contact": 9638521472
    }
]
    for fact in Facutly:
       with s.container():
                s.subheader(fact["instructorname"])
                s.write(f"Department : {fact['Department']}")
                s.write(f"Email : {fact['Email']}")
                s.write(f"Contact : {fact['Contact']}")
                s.markdown("---")

elif page == "Dashboard":
    pass


elif page == "Feedback":
    s.title("Feedback")
    s.subheader("Submit your Feedback")
    name = s.text_input("Your Name")
    score = s.number_input("Your score")
    s.text_area("Comments")
    button = s.button("Submit")

    if button and name and score:
        s.success("Thanks for submitting your feedback")
    else:
        s.error("Please fill the Name and Score input")
