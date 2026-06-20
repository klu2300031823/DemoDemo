import streamlit as st
import time

st.set_page_config(
    page_title="Cricket Quiz Challenge",
    page_icon="🏏",
    layout="centered"
)

# ===================== HELPERS =====================

def clean(text):
    return " ".join(str(text).lower().strip().split())

# ===================== QUESTIONS =====================

questions = [

# ================= IPL (30) =================

{"q":"Who scored the first century in IPL history?","a":"brendon mccullum"},
{"q":"Which team won the inaugural IPL season in 2008?","a":"rajasthan royals"},
{"q":"Who captained Rajasthan Royals to the IPL 2008 title?","a":"shane warne"},
{"q":"Who has scored the highest individual score in IPL history?","a":"chris gayle"},
{"q":"Who scored 973 runs in IPL 2016?","a":"virat kohli"},
{"q":"Which team defeated RCB in the IPL 2016 Final?","a":"sunrisers hyderabad"},
{"q":"Who won the Orange Cap in IPL 2023?","a":"shubman gill"},
{"q":"Who has taken the most wickets in IPL history?","a":"yuzvendra chahal"},
{"q":"Which bowler took the first IPL hat-trick?","a":"lakshmipathy balaji"},
{"q":"Who hit 175* in an IPL innings?","a":"chris gayle"},
{"q":"Which team won IPL 2022?","a":"gujarat titans"},
{"q":"Who captained Gujarat Titans in their debut season?","a":"hardik pandya"},
{"q":"Who was the first Indian to score an IPL century?","a":"manish pandey"},
{"q":"Which stadium is the home ground of Chennai Super Kings?","a":"chepauk"},
{"q":"Who won the Purple Cap in IPL 2024?","a":"harshal patel"},
{"q":"Who was Mumbai Indians' first captain?","a":"sachin tendulkar"},
{"q":"Which team was suspended along with CSK for two seasons?","a":"rajasthan royals"},
{"q":"Who won the MVP award in IPL 2020?","a":"jofra archer"},
{"q":"Who holds the record for fastest IPL fifty in 14 balls?","a":"yashasvi jaiswal"},
{"q":"Who captained Deccan Chargers to the IPL title?","a":"adam gilchrist"},
{"q":"Which IPL team was based in Kochi?","a":"kochi tuskers kerala"},
{"q":"Who won Emerging Player of IPL 2023?","a":"yashasvi jaiswal"},
{"q":"Which player has the most IPL centuries?","a":"virat kohli"},
{"q":"Who was the first overseas player to win an Orange Cap?","a":"shaun marsh"},
{"q":"Who took 6 wickets for 12 runs against SRH in IPL 2021?","a":"harshal patel"},
{"q":"Which team won IPL 2014?","a":"kolkata knight riders"},
{"q":"Which team won IPL 2019?","a":"mumbai indians"},
{"q":"Who has played the most IPL matches?","a":"ms dhoni"},
{"q":"Which franchise won back-to-back IPL titles in 2020 and 2021?","a":"chennai super kings"},
{"q":"Who took 6 wickets for 14 runs in IPL for Mumbai Indians?","a":"alzarri joseph"},

# ================= INTERNATIONAL (20) =================

{"q":"Who scored the first ODI double century?","a":"sachin tendulkar"},
{"q":"Which country won the 2019 ODI World Cup?","a":"england"},
{"q":"Who scored 400* in a Test innings?","a":"brian lara"},
{"q":"Who was Player of the Tournament in the 2011 ODI World Cup?","a":"yuvraj singh"},
{"q":"Which bowler took all 10 wickets in a Test innings for India?","a":"anil kumble"},
{"q":"Who scored the fastest ODI century in 31 balls?","a":"ab de villiers"},
{"q":"Who captained India in the 2007 T20 World Cup?","a":"ms dhoni"},
{"q":"Which country won the first Cricket World Cup?","a":"west indies"},
{"q":"Who has the most wickets in Test cricket history?","a":"muttiah muralitharan"},
{"q":"Who hit six sixes in an over in a T20 World Cup match?","a":"yuvraj singh"},
{"q":"Which country won the 2023 ODI World Cup?","a":"australia"},
{"q":"Who scored 264 in an ODI innings?","a":"rohit sharma"},
{"q":"Who was Player of the Tournament in the 2023 ODI World Cup?","a":"virat kohli"},
{"q":"Who hit the winning six in the 2011 World Cup Final?","a":"ms dhoni"},
{"q":"Which bowler dismissed Sachin Tendulkar the most times internationally?","a":"glenn mcgrath"},
{"q":"Who was the first cricketer to score 100 international centuries?","a":"sachin tendulkar"},
{"q":"Which country won the World Test Championship 2023?","a":"australia"},
{"q":"Who scored the first T20I century?","a":"chris gayle"},
{"q":"Who has the highest ODI score by an individual batsman?","a":"rohit sharma"},
{"q":"Who has the most international centuries?","a":"sachin tendulkar"}

]

TOTAL = len(questions)

# ===================== SESSION =====================

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = [""] * TOTAL

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

current = st.session_state.current
# ===================== CURRENT QUESTION =====================

question = questions[current]

st.title("🏏 Cricket Quiz Challenge")

st.write(f"### Question {current + 1} of {TOTAL}")

st.progress((current + 1) / TOTAL)

# ===================== TIMER =====================

elapsed = int(time.time() - st.session_state.start_time)
remaining = max(0, 30 - elapsed)

st.error(f"⏳ Time Left: {remaining} seconds")

# Auto move to next question when timer ends
if remaining <= 0:

    if current < TOTAL - 1:
        st.session_state.current += 1
        st.session_state.start_time = time.time()
        st.rerun()

# ===================== QUESTION =====================

st.write("###")
st.write(question["q"])

answer = st.text_input(
    "Type your answer:",
    value=st.session_state.answers[current],
    key=f"q_{current}"
)

st.session_state.answers[current] = answer

# ===================== SAVE & NEXT =====================

if current < TOTAL - 1:

    if st.button("💾 Save & Next"):
        st.session_state.current += 1
        st.session_state.start_time = time.time()
        st.rerun()

# ===================== AUTO NEXT WHEN TIME ENDS =====================

if remaining <= 0:

    if current < TOTAL - 1:
        st.session_state.current += 1
        st.session_state.start_time = time.time()
        st.rerun()

# ===================== LAST QUESTION =====================
if current == TOTAL - 1:

    st.write("---")

    if st.button("🏆 Submit Quiz"):

        score = 0

        for i in range(TOTAL):

            user_answer = clean(st.session_state.answers[i])
            correct_answer = clean(questions[i]["a"])

            if user_answer == correct_answer:
                score += 1

        st.session_state.clear()

        st.title("🏆 Quiz Completed")
        st.success(f"Your Score: {score}/{TOTAL}")

        percentage = (score / TOTAL) * 100

        if percentage >= 80:
            st.balloons()
            st.success("Excellent Cricket Knowledge! 🔥")
        elif percentage >= 60:
            st.success("Very Good Performance! 👍")
        elif percentage >= 40:
            st.warning("Good Attempt!")
        else:
            st.error("Need More Cricket Watching 😄")

        st.stop()

# ===================== AUTO REFRESH TIMER =====================

time.sleep(1)
st.rerun()
