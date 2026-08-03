import streamlit as st
import pandas as pd

from habit_tracker import load_workout_data, save_workout
from gym_buddy import gym_buddy_response


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Gym & Fitness Assistant",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ============================================================
# PROFESSIONAL FITNESS UI
# ============================================================

st.markdown("""
<style>

/* MAIN APP */
.stApp {
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
    color: #111827;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}


/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f172a 0%,
        #1e1b4b 55%,
        #312e81 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-weight: 800;
}


/* HERO */
.hero {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #312e81 50%,
        #4f46e5 100%
    );

    padding: 45px 40px;
    border-radius: 24px;
    color: white;
    margin-bottom: 30px;

    box-shadow: 0 20px 45px rgba(49, 46, 129, 0.25);
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
    line-height: 1.6;
}


/* BADGE */
.badge {
    display: inline-block;
    padding: 7px 15px;
    border-radius: 50px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    color: white;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 12px;
}


/* FEATURE CARDS */
.feature-card {
    background: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 20px;
    min-height: 180px;
    margin-bottom: 20px;
    border: 1px solid #e2e8f0;

    box-shadow: 0 10px 30px rgba(15,23,42,0.07);

    transition: all 0.25s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 18px 40px rgba(79,70,229,0.15);
    border-color: #c7d2fe;
}

.feature-icon {
    font-size: 36px;
    margin-bottom: 10px;
}

.feature-card h3 {
    color: #111827;
    margin-bottom: 8px;
    font-weight: 750;
}

.feature-card p {
    color: #64748b;
    line-height: 1.6;
}


/* SECTION CARDS */
.section-card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 10px 30px rgba(15,23,42,0.06);
    margin-bottom: 25px;
}


/* TITLES */
.page-title {
    font-size: 34px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
}

.page-subtitle {
    color: #64748b;
    font-size: 17px;
    margin-bottom: 25px;
}


/* METRICS */
div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 8px 25px rgba(15,23,42,0.06);
}

div[data-testid="stMetricLabel"] {
    color: #64748b !important;
}

div[data-testid="stMetricValue"] {
    color: #312e81 !important;
    font-weight: 800;
}


/* BUTTONS */
.stButton > button {
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );

    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    padding: 0.7rem 1.3rem;

    box-shadow: 0 6px 15px rgba(79,70,229,0.2);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(79,70,229,0.3);
}


/* INPUTS */
.stTextInput input,
.stNumberInput input {
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
    background: white !important;
}

.stTextInput input:focus,
.stNumberInput input:focus {
    border-color: #6366f1 !important;
}


/* ALERTS */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: none;
}


/* DATAFRAME */
div[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
}


/* FOOTER */
.footer {
    text-align: center;
    padding: 30px 10px;
    margin-top: 40px;
    color: #64748b;
    font-size: 14px;
}

.footer b {
    color: #312e81;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏋️ Gym AI")
st.sidebar.caption("Your Personal Fitness Assistant")

st.sidebar.markdown("---")

option = st.sidebar.radio(
    "📋 Fitness Menu",
    [
        "🏠 Home",
        "🏋️ AI Gym Trainer",
        "🥗 Diet & Nutrition",
        "📊 Fitness Habit Tracker",
        "🤖 Virtual Gym Buddy",
        "📈 Performance Analyzer",
        "🔌 Smart Gym Assistant",
        "📍 Gym Recommender"
    ]
)


# ============================================================
# HERO
# ============================================================
st.markdown("""
<div class="hero">

    <div class="badge">AI FITNESS PLATFORM</div>

    <h1>🏋️ AI Gym & Fitness Assistant</h1>

    <p>
        Your intelligent fitness companion for workouts,
        nutrition, progress tracking and personalized guidance.
    </p>

</div>
""", unsafe_allow_html=True)

# ============================================================
# HOME
# ============================================================

if option == "🏠 Home":

    st.markdown(
        '<div class="page-title">Welcome to Your Fitness Hub 👋</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Everything you need to support your fitness journey in one place.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏋️ Workout Status", "Ready")

    with col2:
        st.metric("🎯 Fitness Goal", "Not Set")

    with col3:
        st.metric("📈 Performance", "0%")


    st.markdown("<br>", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🏋️</div>
            <h3>AI Gym Trainer</h3>
            <p>
                Exercise guidance and repetition tracking
                for your training sessions.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🥗</div>
            <h3>AI Nutrition</h3>
            <p>
                BMI assessment, calorie estimation and
                goal-based nutrition guidance.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Habit Tracker</h3>
            <p>
                Record workouts and monitor your fitness
                activity over time.
            </p>
        </div>
        """, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>Virtual Gym Buddy</h3>
            <p>
                Get motivation, workout tips, nutrition
                guidance and recovery suggestions.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3>Performance Analyzer</h3>
            <p>
                Calculate a simple workout performance
                score from your training results.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔌</div>
            <h3>Smart Gym</h3>
            <p>
                Simulated equipment monitoring and
                workout intensity recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "💡 Select a module from the sidebar to begin your fitness journey."
    )


# ============================================================
# AI GYM TRAINER
# ============================================================

elif option == "🏋️ AI Gym Trainer":

    st.markdown(
        '<div class="page-title">🏋️ AI Gym Trainer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'AI-assisted squat workout and repetition tracking.'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("🎯 Workout Assistant")

    st.write(
        "Use this module to record a squat workout and "
        "receive basic training guidance."
    )

    st.info(
        "☁️ Cloud Deployment Mode: Webcam-based pose detection "
        "is designed for local execution. This deployed version "
        "uses manual workout input so the application works reliably "
        "on Streamlit Cloud."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏋️ Exercise", "Squats")

    with col2:
        st.metric("🔍 Tracking", "Manual")

    with col3:
        st.metric("🟢 Status", "Ready")

    st.divider()

    st.subheader("🏋️ Record Your Squat Workout")

    squat_reps = st.number_input(
        "🔢 Squats Completed",
        min_value=0,
        max_value=1000,
        value=10,
        step=1
    )

    workout_minutes = st.number_input(
        "⏱️ Workout Duration (minutes)",
        min_value=0,
        max_value=300,
        value=10,
        step=1
    )

    if st.button(
        "📊 Analyze Squat Workout",
        use_container_width=True,
        key="analyze_squat_workout"
    ):

        if squat_reps == 0:

            st.warning(
                "Please enter at least one completed squat."
            )

        else:

            if squat_reps >= 50:
                level = "Excellent 🏆"

            elif squat_reps >= 30:
                level = "Great 💪"

            elif squat_reps >= 15:
                level = "Good 👍"

            else:
                level = "Beginner 🌱"

            st.success(
                f"Workout recorded successfully! {level}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Squats",
                    squat_reps
                )

            with col2:
                st.metric(
                    "Duration",
                    f"{workout_minutes} min"
                )

            with col3:
                st.metric(
                    "Workout Level",
                    level
                )

            st.info(
                "💡 Focus on controlled movements, proper posture "
                "and comfortable range of motion."
            )


# ============================================================
# DIET & NUTRITION
# ============================================================

elif option == "🥗 Diet & Nutrition":

    st.markdown(
        '<div class="page-title">🥗 AI Diet & Nutrition Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'BMI assessment, calorie estimation and goal-based nutrition guidance.'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            value=21,
            key="nutrition_age"
        )

        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=165.0,
            key="nutrition_height"
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=30.0,
            max_value=200.0,
            value=60.0,
            key="nutrition_weight"
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"],
            key="nutrition_gender"
        )

        goal = st.selectbox(
            "Fitness Goal",
            [
                "Weight Loss",
                "Weight Gain",
                "Maintain Weight",
                "Muscle Building"
            ],
            key="nutrition_goal"
        )

        activity = st.selectbox(
            "Activity Level",
            [
                "Sedentary",
                "Lightly Active",
                "Moderately Active",
                "Very Active"
            ],
            key="nutrition_activity"
        )

    if st.button(
        "📊 Calculate Fitness Plan",
        use_container_width=True,
        key="calculate_fitness_plan"
    ):

        height_m = height / 100

        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        if gender == "Female":

            bmr = (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                - 161
            )

        else:

            bmr = (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                + 5
            )

        activity_multiplier = {
            "Sedentary": 1.2,
            "Lightly Active": 1.375,
            "Moderately Active": 1.55,
            "Very Active": 1.725
        }

        calories = (
            bmr * activity_multiplier[activity]
        )

        if goal == "Weight Loss":
            target_calories = calories - 300

        elif goal == "Weight Gain":
            target_calories = calories + 300

        else:
            target_calories = calories

        st.divider()

        st.subheader("📊 Fitness Assessment")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("BMI", f"{bmi:.1f}")

        with col2:
            st.metric("BMI Category", category)

        with col3:
            st.metric(
                "Estimated Calories",
                f"{target_calories:.0f} kcal/day"
            )

        st.subheader("🥗 Nutrition Recommendations")

        if goal == "Weight Loss":

            st.success("""
**Weight Loss Focus**

• Choose vegetables and fruits regularly  
• Include lean protein  
• Prefer whole grains  
• Limit highly processed foods  
• Stay hydrated  
• Maintain regular physical activity
""")

        elif goal == "Weight Gain":

            st.success("""
**Healthy Weight Gain Focus**

• Include protein-rich foods  
• Add nuts and seeds  
• Include balanced carbohydrates  
• Eat regular meals and snacks  
• Combine nutrition with strength training
""")

        elif goal == "Muscle Building":

            st.success("""
**Muscle Building Focus**

• Include adequate protein  
• Eat balanced carbohydrates  
• Include healthy fats  
• Stay hydrated  
• Combine nutrition with resistance training  
• Get adequate rest and recovery
""")

        else:

            st.success("""
**Maintenance Focus**

• Maintain a balanced diet  
• Include fruits and vegetables  
• Choose whole grains  
• Include adequate protein  
• Stay hydrated  
• Continue regular physical activity
""")

        st.info(
            "💡 These are general fitness estimates and should not "
            "replace advice from a qualified healthcare professional."
        )


# ============================================================
# FITNESS HABIT TRACKER
# ============================================================

elif option == "📊 Fitness Habit Tracker":

    st.markdown(
        '<div class="page-title">📊 Fitness Habit Tracker</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Track your workouts and monitor your fitness progress.'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("➕ Add Workout")

    col1, col2 = st.columns(2)

    with col1:

        workout_date = st.date_input(
            "Workout Date",
            key="tracker_date"
        )

        exercise = st.selectbox(
            "Exercise",
            [
                "Squats",
                "Push-ups",
                "Lunges",
                "Plank",
                "Running",
                "Other"
            ],
            key="tracker_exercise"
        )

        repetitions = st.number_input(
            "Repetitions",
            min_value=0,
            max_value=1000,
            value=10,
            key="tracker_reps"
        )

    with col2:

        duration = st.number_input(
            "Duration (minutes)",
            min_value=0,
            max_value=300,
            value=10,
            key="tracker_duration"
        )

        calories = st.number_input(
            "Calories Burned",
            min_value=0,
            max_value=5000,
            value=50,
            key="tracker_calories"
        )

    if st.button(
        "💾 Save Workout",
        use_container_width=True,
        key="save_workout_button"
    ):

        save_workout(
            workout_date,
            exercise,
            repetitions,
            duration,
            calories
        )

        st.success(
            "Workout saved successfully! 🎉"
        )

    st.divider()

    st.subheader("📋 Workout History")

    df = load_workout_data()

    if len(df) > 0:

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("📊 Fitness Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Workouts",
                len(df)
            )

        with col2:
            st.metric(
                "Total Repetitions",
                int(df["Repetitions"].sum())
            )

        with col3:
            st.metric(
                "Total Calories",
                int(df["Calories"].sum())
            )

        st.subheader("📈 Repetition Progress")

        chart_data = df[
            ["Date", "Repetitions"]
        ].copy()

        chart_data["Date"] = pd.to_datetime(
            chart_data["Date"]
        )

        chart_data = chart_data.set_index("Date")

        st.line_chart(
            chart_data["Repetitions"]
        )

    else:

        st.info(
            "No workouts recorded yet. Add your first workout! 💪"
        )


# ============================================================
# VIRTUAL GYM BUDDY
# ============================================================

elif option == "🤖 Virtual Gym Buddy":

    st.markdown(
        '<div class="page-title">🤖 Virtual Gym Buddy</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Your personal fitness chatbot for motivation, workouts, '
        'nutrition and recovery.'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("💬 Chat with your Virtual Gym Buddy")

    if len(st.session_state.chat_history) == 0:

        st.info(
            "👋 Start a conversation with your Virtual Gym Buddy!"
        )

    else:

        for sender, message in st.session_state.chat_history:

            if sender == "You":

                st.markdown(
                    f"""
                    <div style="
                        background:#e8f0fe;
                        padding:12px 16px;
                        border-radius:12px;
                        margin:8px 0;
                    ">
                        <b>👤 You</b><br>
                        {message}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div style="
                        background:#f3f4f6;
                        padding:12px 16px;
                        border-radius:12px;
                        margin:8px 0;
                    ">
                        <b>🤖 Gym Buddy</b><br>
                        {message}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.divider()

    with st.form(
        key="gym_buddy_form",
        clear_on_submit=True
    ):

        user_message = st.text_input(
            "💬 Your message",
            placeholder="Example: Give me diet tips",
            key="gym_buddy_input"
        )

        send_message = st.form_submit_button(
            "💬 Send Message",
            use_container_width=True
        )

    if send_message:

        if user_message.strip():

            response = gym_buddy_response(
                user_message
            )

            st.session_state.chat_history.append(
                ("You", user_message)
            )

            st.session_state.chat_history.append(
                ("Gym Buddy", response)
            )

            st.rerun()

        else:

            st.warning(
                "⚠️ Please type a message first."
            )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True,
        key="clear_gym_buddy"
    ):

        st.session_state.chat_history = []

        st.rerun()


# ============================================================
# PERFORMANCE ANALYZER
# ============================================================

elif option == "📈 Performance Analyzer":

    st.markdown(
        '<div class="page-title">📈 Performance Analyzer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Analyze your workout performance and calculate a fitness score.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        squat_count = st.number_input(
            "Squats Completed",
            min_value=0,
            max_value=200,
            value=20,
            key="performance_squats"
        )

        pushups = st.number_input(
            "Push-ups Completed",
            min_value=0,
            max_value=200,
            value=10,
            key="performance_pushups"
        )

    with col2:

        duration = st.number_input(
            "Workout Duration (minutes)",
            min_value=0,
            max_value=300,
            value=30,
            key="performance_duration"
        )

        consistency = st.slider(
            "Workout Consistency (%)",
            min_value=0,
            max_value=100,
            value=70,
            key="performance_consistency"
        )

    if st.button(
        "📊 Analyze Performance",
        use_container_width=True,
        key="analyze_performance"
    ):

        squat_score = min(
            squat_count / 50 * 100,
            100
        )

        pushup_score = min(
            pushups / 30 * 100,
            100
        )

        duration_score = min(
            duration / 60 * 100,
            100
        )

        performance_score = (
            squat_score * 0.30
            + pushup_score * 0.25
            + duration_score * 0.20
            + consistency * 0.25
        )

        performance_score = round(
            performance_score,
            1
        )

        if performance_score >= 80:

            level = "Excellent 🏆"
            message = (
                "Excellent performance! Keep maintaining "
                "your consistency and form."
            )

        elif performance_score >= 60:

            level = "Good 💪"
            message = (
                "Good progress! Continue training consistently."
            )

        elif performance_score >= 40:

            level = "Average 👍"
            message = (
                "You're making progress. Gradually increase "
                "your workout intensity."
            )

        else:

            level = "Beginner 🌱"
            message = (
                "Everyone starts somewhere! Focus on consistency."
            )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Performance Score",
                f"{performance_score}%"
            )

        with col2:
            st.metric(
                "Performance Level",
                level
            )

        with col3:
            st.metric(
                "Workout Duration",
                f"{duration} min"
            )

        st.success(message)

        performance_data = pd.DataFrame({
            "Activity": [
                "Squats",
                "Push-ups",
                "Workout Duration",
                "Consistency"
            ],
            "Score": [
                round(squat_score, 1),
                round(pushup_score, 1),
                round(duration_score, 1),
                consistency
            ]
        })

        st.subheader("📋 Performance Breakdown")

        st.dataframe(
            performance_data,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("📈 Performance Chart")

        chart_data = performance_data.set_index(
            "Activity"
        )

        st.bar_chart(
            chart_data["Score"]
        )

        st.info(
            "💡 This is a basic performance scoring system "
            "for educational/project demonstration purposes."
        )


# ============================================================
# SMART GYM ASSISTANT
# ============================================================

elif option == "🔌 Smart Gym Assistant":

    st.markdown(
        '<div class="page-title">🔌 Smart Gym Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Simulated smart equipment monitoring and workout intensity analysis.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        equipment = st.selectbox(
            "🏋️ Select Equipment",
            [
                "Treadmill",
                "Exercise Bike",
                "Leg Press",
                "Chest Press",
                "Rowing Machine"
            ],
            key="smart_equipment"
        )

        intensity = st.slider(
            "Current Intensity (%)",
            min_value=0,
            max_value=100,
            value=50,
            key="smart_intensity"
        )

    with col2:

        heart_rate = st.number_input(
            "❤️ Heart Rate (BPM)",
            min_value=40,
            max_value=220,
            value=80,
            key="smart_heart_rate"
        )

        workout_time = st.number_input(
            "⏱️ Workout Time (minutes)",
            min_value=0,
            max_value=300,
            value=20,
            key="smart_workout_time"
        )

    if st.button(
        "🤖 Analyze Equipment",
        use_container_width=True,
        key="analyze_equipment"
    ):

        if heart_rate > 160:

            recommendation = (
                "⚠️ High intensity detected. Consider reducing "
                "the workout intensity and taking a rest."
            )

            status = "High Intensity"

        elif heart_rate > 130:

            recommendation = (
                "💪 Moderate intensity detected. Maintain your "
                "current pace and monitor your energy level."
            )

            status = "Moderate Intensity"

        else:

            recommendation = (
                "✅ Low to moderate intensity detected. You can "
                "gradually increase intensity if comfortable."
            )

            status = "Low Intensity"

        st.divider()

        st.subheader("📡 Smart Equipment Status")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Equipment",
                equipment
            )

        with col2:
            st.metric(
                "Heart Rate",
                f"{heart_rate} BPM"
            )

        with col3:
            st.metric(
                "Intensity",
                f"{intensity}%"
            )

        st.subheader("🤖 AI Recommendation")

        if heart_rate > 160:
            st.warning(recommendation)

        elif heart_rate > 130:
            st.info(recommendation)

        else:
            st.success(recommendation)

        st.subheader("📡 IoT Sensor Data")

        sensor_data = pd.DataFrame({
            "Sensor": [
                "Heart Rate Sensor",
                "Intensity Sensor",
                "Workout Timer"
            ],
            "Value": [
                f"{heart_rate} BPM",
                f"{intensity}%",
                f"{workout_time} minutes"
            ],
            "Status": [
                status,
                "Active",
                "Connected"
            ]
        })

        st.dataframe(
            sensor_data,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            "🔌 Smart Gym equipment successfully monitored!"
        )

        st.info(
            "💡 This project uses simulated IoT sensor data. "
            "A real implementation could use MQTT, Node-RED "
            "or other IoT protocols."
        )


# ============================================================
# GYM RECOMMENDER
# ============================================================

elif option == "📍 Gym Recommender":

    st.markdown(
        '<div class="page-title">📍 AI Gym Recommender</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Get personalized workout programs and fitness challenge recommendations.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        gym_goal = st.selectbox(
            "🎯 Fitness Goal",
            [
                "Weight Loss",
                "Muscle Building",
                "General Fitness",
                "Strength Training",
                "Flexibility"
            ],
            key="gym_goal"
        )

        experience = st.selectbox(
            "📚 Experience Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ],
            key="gym_experience"
        )

    with col2:

        workout_type = st.selectbox(
            "🏋️ Preferred Workout",
            [
                "Gym Training",
                "Home Workout",
                "Cardio",
                "Strength Training",
                "Yoga"
            ],
            key="gym_workout_type"
        )

        location = st.text_input(
            "📍 Enter Your City",
            placeholder="Example: Hyderabad",
            key="gym_location"
        )

    if st.button(
        "🔍 Get Recommendations",
        use_container_width=True,
        key="get_gym_recommendations"
    ):

        if gym_goal == "Weight Loss":

            program = "🏃 Cardio + Full Body Training"
            challenge = "🔥 30-Day Fitness Consistency Challenge"

        elif gym_goal == "Muscle Building":

            program = "🏋️ Strength Training + Progressive Overload"
            challenge = "💪 30-Day Strength Building Challenge"

        elif gym_goal == "Strength Training":

            program = "🏋️ Compound Exercises + Strength Program"
            challenge = "⚡ Progressive Strength Challenge"

        elif gym_goal == "Flexibility":

            program = "🧘 Yoga + Mobility Training"
            challenge = "🌿 21-Day Flexibility Challenge"

        else:

            program = "🏋️ Balanced Full Body Fitness Program"
            challenge = "💪 30-Day General Fitness Challenge"

        st.divider()

        st.subheader("🎯 Your Personalized Recommendations")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Fitness Goal",
                gym_goal
            )

        with col2:
            st.metric(
                "Experience",
                experience
            )

        with col3:
            st.metric(
                "Workout Type",
                workout_type
            )

        st.subheader("🏋️ Recommended Program")

        st.success(program)

        st.subheader("🔥 Recommended Fitness Challenge")

        st.info(challenge)

        st.subheader("📍 Gym Recommendation")

        if location.strip():

            st.success(
                f"Based on your preferences, look for a "
                f"{workout_type.lower()} gym or fitness center "
                f"near **{location}**."
            )

        else:

            st.warning(
                "Enter your city to receive a location-based "
                "gym recommendation."
            )

        recommendation_data = pd.DataFrame({
            "Category": [
                "Fitness Goal",
                "Experience Level",
                "Workout Preference",
                "Recommended Program",
                "Fitness Challenge"
            ],
            "Recommendation": [
                gym_goal,
                experience,
                workout_type,
                program,
                challenge
            ]
        })

        st.subheader("📋 Recommendation Summary")

        st.dataframe(
            recommendation_data,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            "🤖 AI recommendation generated successfully!"
        )

        st.info(
            "💡 This prototype uses rule-based recommendation logic. "
            "A production version could use machine learning, "
            "location APIs and historical user data."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    <b>🏋️ AI Gym & Fitness Assistant</b><br>
    AI-powered fitness companion • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)