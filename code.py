import streamlit as st

st.set_page_config(
    page_title="Healthy Aging Compass",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: 800;
    color: #2E7D32;
}
.card {
    padding: 18px;
    border-radius: 16px;
    background-color: #F5F7FA;
    margin-bottom: 14px;
}
.action-card {
    padding: 16px;
    border-radius: 14px;
    background-color: #E8F5E9;
    margin-bottom: 10px;
}
.warning-card {
    padding: 16px;
    border-radius: 14px;
    background-color: #FFF8E1;
    margin-bottom: 10px;
}
.passport {
    padding: 14px;
    border-radius: 14px;
    background-color: #EEF7FF;
    margin-bottom: 10px;
}
.future-card {
    padding: 18px;
    border-radius: 16px;
    background-color: #F3E5F5;
    margin-bottom: 14px;
}
.small-note {
    color: #666;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🌿 Healthy Aging Compass</div>', unsafe_allow_html=True)
st.write("A simple wellness guide to help older adults stay independent, active, and prepared.")

st.markdown("---")

st.markdown("## 🚀 Quick Start")
st.write("Answer a few simple questions to get your personalized wellness snapshot.")

nickname = st.text_input("What should we call you? Optional")
st.caption("Use a nickname only. Do not enter your full legal name.")

display_name = nickname.strip() if nickname.strip() else "there"

age_group = st.radio(
    "What is your age group?",
    ["65-74", "75-84", "85+"],
    horizontal=True
)

main_goal = st.radio(
    "What matters most to you right now?",
    [
        "Staying independent",
        "Avoiding falls",
        "Managing medications",
        "Staying active",
        "Supporting a loved one"
    ]
)

priority = st.selectbox(
    "Choose your top wellness priority",
    [
        "Stay in my home",
        "Walk more comfortably",
        "Avoid hospital visits",
        "Keep my medications organized",
        "Stay socially connected"
    ]
)

wellness_visit = st.radio(
    "Have you had a wellness visit in the last year?",
    ["Yes", "No", "Not sure"],
    horizontal=True
)

meds_5plus = st.radio(
    "Do you take 5 or more medications?",
    ["Yes", "No", "Not sure"],
    horizontal=True
)

fall_last_year = st.radio(
    "Have you fallen in the last year?",
    ["Yes", "No", "Not sure"],
    horizontal=True
)

exercise = st.radio(
    "Do you get regular physical activity?",
    ["Yes", "No", "Not sure"],
    horizontal=True
)

flu_shot = st.radio(
    "Have you received a flu shot this year?",
    ["Yes", "No", "Not sure"],
    horizontal=True
)

social_connection = st.radio(
    "Do you feel socially connected to family, friends, or community?",
    ["Yes", "No", "Not sure"],
    horizontal=True
)

if st.button("Show My Snapshot", use_container_width=True):

    score = 100

    if wellness_visit == "No":
        score -= 15
    elif wellness_visit == "Not sure":
        score -= 8

    if meds_5plus == "Yes":
        score -= 15
    elif meds_5plus == "Not sure":
        score -= 5

    if fall_last_year == "Yes":
        score -= 20
    elif fall_last_year == "Not sure":
        score -= 8

    if exercise == "No":
        score -= 15
    elif exercise == "Not sure":
        score -= 7

    if flu_shot == "No":
        score -= 10
    elif flu_shot == "Not sure":
        score -= 5

    if social_connection == "No":
        score -= 10
    elif social_connection == "Not sure":
        score -= 5

    score = max(score, 0)

    if score >= 85:
        status = "🟢 Strong"
        status_message = "You have several habits that support healthy aging."
    elif score >= 65:
        status = "🟡 Watch"
        status_message = "You are doing well in some areas, but a few things may need attention."
    else:
        status = "🔴 Action Needed"
        status_message = "A few simple actions may help support your independence and safety."

    st.markdown("---")
    st.markdown(f"## 🧭 {display_name}, here is your Healthy Aging Snapshot")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Healthy Aging Score", f"{score}/100")

    with col2:
        st.metric("Status", status)

    st.write(status_message)
    st.progress(score / 100)

    st.info(f"Your plan is focused on: **{priority}**")

    st.markdown("## 🏡 Age-in-Place Readiness")

    if score >= 85:
        readiness = "Strong"
        readiness_text = "Your current habits support staying independent."
    elif score >= 65:
        readiness = "Moderate"
        readiness_text = "You may benefit from a few preventive actions."
    else:
        readiness = "Needs Support"
        readiness_text = "Consider discussing your wellness plan with a doctor, caregiver, or trusted support person."

    st.markdown(
        f"""
        <div class="card">
        <h3>Readiness Level: {readiness}</h3>
        <p>{readiness_text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🎯 Your Next Best Action")

    actions = []

    if fall_last_year == "Yes":
        actions.append("Talk to your doctor about balance, fall prevention, and home safety.")
    if meds_5plus == "Yes":
        actions.append("Ask your doctor or pharmacist for a medication review.")
    if wellness_visit in ["No", "Not sure"]:
        actions.append("Schedule an annual wellness visit.")
    if exercise == "No":
        actions.append("Start light walking or chair exercises, if safe for you.")
    if flu_shot in ["No", "Not sure"]:
        actions.append("Ask about getting your flu shot.")
    if social_connection == "No":
        actions.append("Plan one social check-in this week with family, friends, or a community group.")

    if not actions:
        actions.append("Keep up your current healthy habits and check in again next month.")

    st.markdown(
        f"""
        <div class="action-card">
        <h3>✅ {actions[0]}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 📌 Top 3 Recommended Steps")

    for action in actions[:3]:
        st.success(action)

    st.markdown("## 🛂 Healthy Aging Passport")

    passport_stamps = []

    if wellness_visit == "Yes":
        passport_stamps.append("Annual Wellness Visit")
    if flu_shot == "Yes":
        passport_stamps.append("Flu Vaccine")
    if exercise == "Yes":
        passport_stamps.append("Staying Active")
    if fall_last_year == "No":
        passport_stamps.append("Fall-Free This Year")
    if meds_5plus == "No":
        passport_stamps.append("Medication Simplicity")
    if social_connection == "Yes":
        passport_stamps.append("Social Connection")

    total_possible = 6
    total_stamps = len(passport_stamps)

    st.progress(total_stamps / total_possible)
    st.write(f"Passport Progress: **{total_stamps} of {total_possible} milestones completed**")

    if passport_stamps:
        cols = st.columns(2)
        for i, stamp in enumerate(passport_stamps):
            with cols[i % 2]:
                st.markdown(
                    f"""
                    <div class="passport">
                    <h4>✅ {stamp}</h4>
                    <p class="small-note">Stamp earned</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.warning("No passport stamps yet. Start with one healthy aging action this month.")

    st.markdown("### Stamps Still Available")

    missing = []

    if wellness_visit != "Yes":
        missing.append("Annual Wellness Visit")
    if flu_shot != "Yes":
        missing.append("Flu Vaccine")
    if exercise != "Yes":
        missing.append("Staying Active")
    if fall_last_year != "No":
        missing.append("Fall-Free This Year")
    if meds_5plus != "No":
        missing.append("Medication Review")
    if social_connection != "Yes":
        missing.append("Social Connection")

    if missing:
        for item in missing:
            st.info(f"⬜ {item}")
    else:
        st.balloons()
        st.success("Amazing — you earned all available passport stamps!")

    st.markdown("## 🗓️ This Month's Personalized Wellness Mission")

    if priority == "Stay in my home":
        mission = "Check one room for tripping hazards this week, such as loose rugs, cords, or clutter."
    elif priority == "Walk more comfortably":
        mission = "Try a short, safe walk or chair exercise 3 times this week, if safe for you."
    elif priority == "Avoid hospital visits":
        mission = "Schedule or confirm your next wellness visit and write down questions for your doctor."
    elif priority == "Keep my medications organized":
        mission = "Create or update a simple medication list and bring it to your next doctor or pharmacy visit."
    else:
        mission = "Call, visit, or message one person you care about this week."

    st.markdown(
        f"""
        <div class="warning-card">
        <h3>🌟 {display_name}'s Monthly Mission</h3>
        <p>{mission}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 💌 A Message From Your Future Self")

    st.markdown(
        f"""
        <div class="future-card">
        <h3>Dear {display_name},</h3>
        <p>
        Thank you for focusing on <b>{priority.lower()}</b>.
        Small steps taken consistently can help support confidence,
        independence, and quality of life.
        </p>
        <p>
        Keep going — your future self is grateful for the care you are taking today.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## ❤️ Caregiver Snapshot")

    caregiver_notes = []

    if fall_last_year == "Yes":
        caregiver_notes.append("Mobility or fall prevention may need attention.")
    if meds_5plus == "Yes":
        caregiver_notes.append("Medication review may be helpful.")
    if wellness_visit in ["No", "Not sure"]:
        caregiver_notes.append("Preventive visit may need scheduling.")
    if social_connection == "No":
        caregiver_notes.append("Social support may be important.")

    if caregiver_notes:
        for note in caregiver_notes:
            st.warning(note)
    else:
        st.success("No major caregiver alerts based on these answers.")

    st.markdown("## 📊 Community Health Themes")

    st.write(
        f"For adults age **{age_group}**, common healthy aging focus areas include:"
    )

    st.write("- Fall prevention")
    st.write("- Medication safety")
    st.write("- Preventive care")
    st.write("- Staying active")
    st.write("- Social connection")

    st.markdown("---")
    st.caption(
        "This tool is for general wellness education only. It is not medical advice, diagnosis, or treatment. "
        "For personal medical concerns, talk with a doctor or qualified health professional."
    )
