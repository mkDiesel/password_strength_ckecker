import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker",page_icon="🔒")

st.title("🔐Password Strength Checker")
st.markdown("""
🔐 Welcome to Your Ultimate Password Strength Buddy! 🚀
Worried if your password is strong enough? No stress!
Just pop it in — we'll analyze it and let you know how safe it really is.
Plus, get pro tips to craft a rock-solid password that'll keep the hackers at bay! 💪""")

password = st.text_input("Enter your password",type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be atleast 8 characters long.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")
    
    if re.search(r"[0-9]",password):
        score += 1
    else:
        feedback.append("❌Password should contain atleast one digit.")
        
    if re.search(r"[!@#$%&*]",password):
        score += 1
    else:
         feedback.append("❌Password should contain atleast special characters(!@#$%&*).")
         
    if score == 4:
        feedback.append("✅Your password is strong!🎉")    
    elif score == 3:
        feedback.append("🟢Your password is medium strength. It could be stronger!")    
    else: 
         feedback.append("🔴Your password is weak. Please make it stronger.") 
    
    if feedback:
        st.markdown("## 🛡️ Password Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
            
else:
    st.info("""🔑 Enter your password to kick things off!
Let’s see how strong your secret really is. 😉""")