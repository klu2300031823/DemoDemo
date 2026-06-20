import streamlit as st
import time

st.set_page_config(
    page_title="Java Quiz",
    page_icon="",
    layout="centered"
)

# ===================== HELPERS =====================

def clean(text):
    return " ".join(str(text).lower().strip().split())

# ===================== QUESTIONS =====================

# questions = [

# # ================= IPL (30) =================

# {"q":"Who scored the first century in IPL history?","a":"brendon mccullum"},
# {"q":"Which team won the inaugural IPL season in 2008?","a":"rajasthan royals"},
# {"q":"Who captained Rajasthan Royals to the IPL 2008 title?","a":"shane warne"},
# {"q":"Who has scored the highest individual score in IPL history?","a":"chris gayle"},
# {"q":"Who scored 973 runs in IPL 2016?","a":"virat kohli"},
# {"q":"Which team defeated RCB in the IPL 2016 Final?","a":"sunrisers hyderabad"},
# {"q":"Who won the Orange Cap in IPL 2023?","a":"shubman gill"},
# {"q":"Who has taken the most wickets in IPL history?","a":"yuzvendra chahal"},
# {"q":"Which bowler took the first IPL hat-trick?","a":"lakshmipathy balaji"},
# {"q":"Who hit 175* in an IPL innings?","a":"chris gayle"},
# {"q":"Which team won IPL 2022?","a":"gujarat titans"},
# {"q":"Who captained Gujarat Titans in their debut season?","a":"hardik pandya"},
# {"q":"Who was the first Indian to score an IPL century?","a":"manish pandey"},
# {"q":"Which stadium is the home ground of Chennai Super Kings?","a":"chepauk"},
# {"q":"Who won the Purple Cap in IPL 2024?","a":"harshal patel"},
# {"q":"Who was Mumbai Indians' first captain?","a":"sachin tendulkar"},
# {"q":"Which team was suspended along with CSK for two seasons?","a":"rajasthan royals"},
# {"q":"Who won the MVP award in IPL 2020?","a":"jofra archer"},
# {"q":"Who holds the record for fastest IPL fifty in 14 balls?","a":"yashasvi jaiswal"},
# {"q":"Who captained Deccan Chargers to the IPL title?","a":"adam gilchrist"},
# {"q":"Which IPL team was based in Kochi?","a":"kochi tuskers kerala"},
# {"q":"Who won Emerging Player of IPL 2023?","a":"yashasvi jaiswal"},
# {"q":"Which player has the most IPL centuries?","a":"virat kohli"},
# {"q":"Who was the first overseas player to win an Orange Cap?","a":"shaun marsh"},
# {"q":"Who took 6 wickets for 12 runs against SRH in IPL 2021?","a":"harshal patel"},
# {"q":"Which team won IPL 2014?","a":"kolkata knight riders"},
# {"q":"Which team won IPL 2019?","a":"mumbai indians"},
# {"q":"Who has played the most IPL matches?","a":"ms dhoni"},
# {"q":"Which franchise won back-to-back IPL titles in 2020 and 2021?","a":"chennai super kings"},
# {"q":"Who took 6 wickets for 14 runs in IPL for Mumbai Indians?","a":"alzarri joseph"},

# # ================= INTERNATIONAL (20) =================

# {"q":"Who scored the first ODI double century?","a":"sachin tendulkar"},
# {"q":"Which country won the 2019 ODI World Cup?","a":"england"},
# {"q":"Who scored 400* in a Test innings?","a":"brian lara"},
# {"q":"Who was Player of the Tournament in the 2011 ODI World Cup?","a":"yuvraj singh"},
# {"q":"Which bowler took all 10 wickets in a Test innings for India?","a":"anil kumble"},
# {"q":"Who scored the fastest ODI century in 31 balls?","a":"ab de villiers"},
# {"q":"Who captained India in the 2007 T20 World Cup?","a":"ms dhoni"},
# {"q":"Which country won the first Cricket World Cup?","a":"west indies"},
# {"q":"Who has the most wickets in Test cricket history?","a":"muttiah muralitharan"},
# {"q":"Who hit six sixes in an over in a T20 World Cup match?","a":"yuvraj singh"},
# {"q":"Which country won the 2023 ODI World Cup?","a":"australia"},
# {"q":"Who scored 264 in an ODI innings?","a":"rohit sharma"},
# {"q":"Who was Player of the Tournament in the 2023 ODI World Cup?","a":"virat kohli"},
# {"q":"Who hit the winning six in the 2011 World Cup Final?","a":"ms dhoni"},
# {"q":"Which bowler dismissed Sachin Tendulkar the most times internationally?","a":"glenn mcgrath"},
# {"q":"Who was the first cricketer to score 100 international centuries?","a":"sachin tendulkar"},
# {"q":"Which country won the World Test Championship 2023?","a":"australia"},
# {"q":"Who scored the first T20I century?","a":"chris gayle"},
# {"q":"Who has the highest ODI score by an individual batsman?","a":"rohit sharma"},
# {"q":"Who has the most international centuries?","a":"sachin tendulkar"}

# ]

questions = [

{"q":"Keyword used to inherit a class?","a":"extends"},
{"q":"Keyword used to create an object?","a":"new"},
{"q":"Root class of Java?","a":"object"},
{"q":"Package automatically imported in Java?","a":"java.lang"},
{"q":"Keyword to prevent inheritance?","a":"final"},
{"q":"Keyword used for abstraction?","a":"abstract"},
{"q":"Keyword used to handle exceptions?","a":"catch"},
{"q":"Keyword used to throw exception?","a":"throw"},
{"q":"Keyword used to declare exception?","a":"throws"},
{"q":"Keyword used for inheritance constructor call?","a":"super"},

{"q":"Parent of all exceptions?","a":"throwable"},
{"q":"Keyword for current object?","a":"this"},
{"q":"Method called automatically on object creation?","a":"constructor"},
{"q":"Keyword used to implement interface?","a":"implements"},
{"q":"Collection that stores key-value pairs?","a":"map"},
{"q":"Ordered collection with duplicates?","a":"list"},
{"q":"Collection without duplicates?","a":"set"},
{"q":"Class used for dynamic arrays?","a":"arraylist"},
{"q":"FIFO data structure?","a":"queue"},
{"q":"LIFO data structure?","a":"stack"},

{"q":"Method used to compare strings?","a":"equals"},
{"q":"Method returning string length?","a":"length"},
{"q":"Package containing collections?","a":"java.util"},
{"q":"Keyword for thread creation alternative?","a":"runnable"},
{"q":"Method to start thread?","a":"start"},
{"q":"Method executed by thread?","a":"run"},
{"q":"Default value of boolean?","a":"false"},
{"q":"Default value of int?","a":"0"},
{"q":"Default value of object reference?","a":"null"},
{"q":"Keyword used for synchronization?","a":"synchronized"},

{"q":"Interface used for sorting custom objects?","a":"comparable"},
{"q":"Interface for custom comparison?","a":"comparator"},
{"q":"Class used for immutable strings?","a":"string"},
{"q":"Mutable string class?","a":"stringbuilder"},
{"q":"Keyword for package declaration?","a":"package"},
{"q":"Keyword to access package classes?","a":"import"},
{"q":"Access modifier visible everywhere?","a":"public"},
{"q":"Access modifier visible only in class?","a":"private"},
{"q":"Access modifier visible in package?","a":"default"},
{"q":"Access modifier visible in subclasses?","a":"protected"},

{"q":"Exception occurring when dividing by zero?","a":"arithmeticexception"},
{"q":"Exception for invalid array index?","a":"arrayindexoutofboundsexception"},
{"q":"Exception for null reference access?","a":"nullpointerexception"},
{"q":"Exception checked at compile time?","a":"checked"},
{"q":"Exception checked at runtime?","a":"unchecked"},
{"q":"Keyword for multiple cases?","a":"switch"},
{"q":"Loop guaranteed to run once?","a":"dowhile"},
{"q":"Keyword to skip iteration?","a":"continue"},
{"q":"Keyword to exit loop?","a":"break"},
{"q":"Method converting string to int?","a":"parseint"},

{"q":"Wrapper class of int?","a":"integer"},
{"q":"Wrapper class of double?","a":"double"},
{"q":"Wrapper class of char?","a":"character"},
{"q":"Wrapper class of boolean?","a":"boolean"},
{"q":"Process of converting primitive to object?","a":"autoboxing"},
{"q":"Process of converting object to primitive?","a":"unboxing"},
{"q":"Keyword used for constant variable?","a":"final"},
{"q":"Keyword for static members?","a":"static"},
{"q":"Keyword used to inherit interfaces?","a":"extends"},
{"q":"Method used by garbage collector?","a":"finalize"},

{"q":"Java is platform ___ ?","a":"independent"},
{"q":"JVM stands for?","a":"jvm"},
{"q":"JRE stands for?","a":"jre"},
{"q":"JDK stands for?","a":"jdk"},
{"q":"Java source file extension?","a":"java"},
{"q":"Java bytecode file extension?","a":"class"},
{"q":"Collection framework interface parent?","a":"collection"},
{"q":"Method used to insert into ArrayList?","a":"add"},
{"q":"Method used to remove element?","a":"remove"},
{"q":"Method used to find size?","a":"size"},

{"q":"Keyword used for polymorphism runtime?","a":"override"},
{"q":"Keyword used for polymorphism compile time?","a":"overload"},
{"q":"Class used for input from keyboard?","a":"scanner"},
{"q":"Package containing Scanner?","a":"java.util"},
{"q":"Method to read integer in Scanner?","a":"nextint"},
{"q":"Method to read string line?","a":"nextline"},
{"q":"Keyword used for interface default implementation?","a":"default"},
{"q":"Keyword used for enum declaration?","a":"enum"},
{"q":"Keyword for nested class object access?","a":"outer"},
{"q":"Memory area storing objects?","a":"heap"},

{"q":"Memory area storing method calls?","a":"stack"},
{"q":"Process of hiding implementation?","a":"abstraction"},
{"q":"Process of binding data and methods?","a":"encapsulation"},
{"q":"Ability to take many forms?","a":"polymorphism"},
{"q":"Mechanism of acquiring properties?","a":"inheritance"},
{"q":"Class cannot be instantiated?","a":"abstract"},
{"q":"Method without body?","a":"abstract"},
{"q":"Interface methods are by default?","a":"public"},
{"q":"Java supports multiple inheritance through?","a":"interface"},
{"q":"Most important OOP feature for reuse?","a":"inheritance"},

{"q":"HashMap allows ___ keys?","a":"null"},
{"q":"TreeMap stores data in ___ order?","a":"sorted"},
{"q":"PriorityQueue is based on?","a":"heap"},
{"q":"ArrayList internally uses?","a":"array"},
{"q":"LinkedList internally uses?","a":"list"},
{"q":"Keyword used for lambda expressions?","a":"lambda"},
{"q":"Java version introducing streams?","a":"8"},
{"q":"Method to print output?","a":"println"},
{"q":"Entry point method of Java?","a":"main"},
{"q":"Keyword used to create package hierarchy?","a":"package"}

]

TOTAL = len(questions)

# ===================== SESSION =====================

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = [""] * TOTAL

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "submitted" not in st.session_state:
    st.session_state.submitted = False

current = st.session_state.current

if st.session_state.submitted:

    score = st.session_state.score

    st.title("🏆 Quiz Completed")
    st.success(f"Your Score: {score}/{TOTAL}")

    percentage = (score / TOTAL) * 100

    if percentage >= 80:
        st.balloons()
        #st.success("Excellent Cricket Knowledge! 🔥")
        st.success("Excellent Knowledge! 🔥")
    elif percentage >= 60:
        st.success("Very Good Performance! 👍")
    elif percentage >= 40:
        st.warning("Good Attempt!")
    else:
        #st.error("Need More Cricket Watching 😄")
        st.error("Need More Practice 😄")

    st.stop()
# ===================== CURRENT QUESTION =====================

question = questions[current]

st.title("Java Quiz Challenge")

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

        st.session_state.score = score
        st.session_state.submitted = True

        st.rerun()

time.sleep(1)
st.rerun()
