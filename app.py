import streamlit as st
import pandas as pd

from habit_tracker import load_workout_data, save_workout
from gym_buddy import get_gym_buddy_response


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Gym & Fitness Assistant",
    page_icon="🏋️",
    layout="wide"
)


# ============================================================
# VIRTUAL GYM BUDDY FUNCTION
# ============================================================

def get_gym_buddy_response(message):

    message = message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii", "hiii"]:
        return (
            "👋 Hey! I'm your Virtual Gym Buddy! "
            "I'm doing great and I'm ready to support your fitness journey. 💪"
        )

    # How are you?
    elif any(phrase in message for phrase in [
        "how are you",
        "how r you",
        "how are u",
        "how r u"
    ]):
        return (
            "😊 I'm doing great! Thanks for asking. "
            "I'm always ready to motivate you and help with "
            "workouts, nutrition, and fitness goals. 💪"
        )

    # Name / identity
    elif any(phrase in message for phrase in [
        "who are you",
        "what are you",
        "what is your name",
        "what's your name",
        "your name"
    ]):
        return (
            "🤖 I'm your AI Gym Buddy! "
            "You can call me Gym Buddy. 💪 "
            "I help you with workouts, nutrition, motivation, "
            "recovery, and fitness tracking."
        )

    # Do you know me?
    elif any(phrase in message for phrase in [
        "you know me",
        "do you know me",
        "know about me"
    ]):
        return (
            "😊 I know that you're using me as your Virtual Gym Buddy! "
            "I can respond based on our current conversation, "
            "but I don't automatically know your personal information."
        )

    # Thanks
    elif any(phrase in message for phrase in [
        "thank you",
        "thanks",
        "thank u"
    ]):
        return (
            "You're very welcome! 😊 "
            "Keep going with your fitness journey. 💪"
        )

    # Motivation
    elif any(word in message for word in [
        "motivat",
        "lazy",
        "give up",
        "can't",
        "tired",
        "sad"
    ]):
        return (
            "💪 Don't give up! Progress takes time. "
            "Even a small workout today is better than doing nothing. "
            "Take a short rest if you're tired and continue when you're ready."
        )

    # Workout
    elif any(word in message for word in [
        "workout",
        "exercise",
        "squat",
        "pushup",
        "push-up",
        "training"
    ]):
        return (
            "🏋️ Try to maintain proper form and controlled movements. "
            "Start with a comfortable number of repetitions and "
            "increase gradually."
        )

    # Nutrition
    elif any(word in message for word in [
        "diet",
        "food",
        "eat",
        "nutrition",
        "meal",
        "calorie"
    ]):
        return (
            "🥗 Focus on balanced meals with vegetables, fruits, "
            "whole grains, and protein. Stay hydrated and avoid "
            "excessively processed foods."
        )

    # Recovery
    elif any(word in message for word in [
        "rest",
        "sleep",
        "recover",
        "recovery"
    ]):
        return (
            "😴 Recovery is an important part of fitness. "
            "Get enough sleep, stay hydrated, and give your body "
            "time to recover between intense workouts."
        )

    # Goodbye
    elif any(word in message for word in [
        "bye",
        "goodbye",
        "see you"
    ]):
        return (
            "👋 Bye! Keep taking care of yourself and stay consistent "
            "with your fitness goals. See you soon! 💪"
        )

    # Default
    else:
        return (
            "🤖 I'm still learning! You can ask me about workouts, "
            "nutrition, motivation, recovery, or your fitness goals. 💪"
        )


# ============================================================
# TITLE
# ============================================================

st.title("🏋️ AI Gym & Fitness Assistant")

st.write(
    "Your intelligent fitness companion for workouts, nutrition, "
    "fitness tracking, and personalized guidance."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📋 Fitness Menu")

option = st.sidebar.radio(
    "Choose a module:",
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
# HOME
# ============================================================

if option == "🏠 Home":

    st.header("Welcome to your AI Fitness Assistant! 💪")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Workout Status", "Ready")

    with col2:
        st.metric("Fitness Goal", "Not Set")

    with col3:
        st.metric("Performance", "0%")

    st.info(
        "Select a module from the sidebar to begin your fitness journey."
    )


# ============================================================
# AI GYM TRAINER
# ============================================================

elif option == "🏋️ AI Gym Trainer":

    from workout import run_pose_detection

    st.header("🏋️ AI Gym Trainer")

    st.write(
        "Use your camera to detect squats, count repetitions, "
        "and receive basic workout feedback."
    )

    st.info(
        "The webcam workout feature is designed for local execution. "
        "The deployed cloud version does not directly access your computer's webcam."
    )

    if st.button("▶️ Start Workout"):

        st.write("🏋️ Workout started!")

        result = run_pose_detection()

        st.success(result)


# ============================================================
# DIET & NUTRITION
# ============================================================

elif option == "🥗 Diet & Nutrition":

    st.header("🥗 AI Diet & Nutrition Assistant")

    st.write(
        "Get a basic BMI assessment, estimated calorie requirement, "
        "and goal-based nutrition recommendations."
    )

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            value=21
        )

        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=165.0
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=30.0,
            max_value=200.0,
            value=60.0
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        goal = st.selectbox(
            "Fitness Goal",
            [
                "Weight Loss",
                "Weight Gain",
                "Maintain Weight",
                "Muscle Building"
            ]
        )

        activity = st.selectbox(
            "Activity Level",
            [
                "Sedentary",
                "Lightly Active",
                "Moderately Active",
                "Very Active"
            ]
        )

    if st.button("Calculate Fitness Plan"):

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

        calories = bmr * activity_multiplier[activity]

        if goal == "Weight Loss":
            target_calories = calories - 300

        elif goal == "Weight Gain":
            target_calories = calories + 300

        else:
            target_calories = calories

        st.divider()

        st.subheader("📊 Your Fitness Assessment")

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

            st.success(
                """
                **Weight Loss Focus**

                • Choose vegetables and fruits regularly  
                • Include lean protein in meals  
                • Prefer whole grains  
                • Limit highly processed foods  
                • Drink enough water  
                • Maintain regular physical activity
                """
            )

        elif goal == "Weight Gain":

            st.success(
                """
                **Healthy Weight Gain Focus**

                • Include protein-rich foods  
                • Add nuts and seeds  
                • Include milk/curd or suitable alternatives  
                • Eat balanced carbohydrate sources  
                • Have regular meals and snacks  
                • Combine nutrition with strength training
                """
            )

        elif goal == "Muscle Building":

            st.success(
                """
                **Muscle Building Focus**

                • Include adequate protein  
                • Eat balanced carbohydrates  
                • Include healthy fats  
                • Stay hydrated  
                • Combine nutrition with resistance training  
                • Get adequate rest and recovery
                """
            )

        else:

            st.success(
                """
                **Maintenance Focus**

                • Maintain a balanced diet  
                • Include fruits and vegetables  
                • Choose whole grains  
                • Include adequate protein  
                • Stay hydrated  
                • Continue regular physical activity
                """
            )

        st.info(
            "💡 These recommendations are general fitness guidance "
            "and should not replace advice from a qualified "
            "healthcare professional."
        )


# ============================================================
# FITNESS HABIT TRACKER
# ============================================================

elif option == "📊 Fitness Habit Tracker":

    st.header("📊 AI Fitness Habit Tracker")

    st.write(
        "Track your workouts and monitor your fitness progress over time."
    )

    st.subheader("➕ Add Workout")

    workout_date = st.date_input("Workout Date")

    exercise = st.selectbox(
        "Exercise",
        [
            "Squats",
            "Push-ups",
            "Lunges",
            "Plank",
            "Running",
            "Other"
        ]
    )

    repetitions = st.number_input(
        "Repetitions",
        min_value=0,
        max_value=1000,
        value=10
    )

    duration = st.number_input(
        "Duration (minutes)",
        min_value=0,
        max_value=300,
        value=10
    )

    calories = st.number_input(
        "Calories Burned",
        min_value=0,
        max_value=5000,
        value=50
    )

    if st.button("💾 Save Workout"):

        save_workout(
            workout_date,
            exercise,
            repetitions,
            duration,
            calories
        )

        st.success("Workout saved successfully! 🎉")

    st.divider()

    st.subheader("📋 Workout History")

    df = load_workout_data()

    if len(df) > 0:

        st.dataframe(
            df,
            use_container_width=True
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

    st.header("🤖 Virtual Gym Buddy")

    st.write(
        "Your personal fitness companion for motivation, "
        "workout guidance, nutrition tips, and recovery."
    )

    st.info(
        "Ask your Gym Buddy anything about your fitness journey! 💪"
    )

    # Create chat history only once
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # --------------------------------------------------------
    # Display previous conversation
    # --------------------------------------------------------

    st.subheader("💬 Conversation")

    if len(st.session_state.chat_history) > 0:

        for sender, message in st.session_state.chat_history:

            if sender == "You":

                st.markdown(
                    f"**👤 You:** {message}"
                )

            else:

                st.markdown(
                    f"**🤖 Gym Buddy:** {message}"
                )

    else:

        st.info(
            "👋 Start the conversation by asking me something!"
        )

    st.divider()

    # --------------------------------------------------------
    # Message input
    # --------------------------------------------------------

    user_message = st.text_input(
        "💬 Your message",
        placeholder="Example: Give me diet tips",
        key="gym_buddy_input"
    )

    # --------------------------------------------------------
    # Send button
    # --------------------------------------------------------

    if st.button("Send 💬"):

        if user_message.strip():

            response = get_gym_buddy_response(
                user_message
            )

            # Save BOTH user message and AI response
            st.session_state.chat_history.append(
                ("You", user_message)
            )

            st.session_state.chat_history.append(
                ("Gym Buddy", response)
            )

            # Rerun page so the new conversation appears
            st.rerun()

        else:

            st.warning(
                "Please type a message first."
            )

    # --------------------------------------------------------
    # Clear conversation
    # --------------------------------------------------------

    if st.button("🗑️ Clear Conversation"):

        st.session_state.chat_history = []

        st.rerun()


# ============================================================
# PERFORMANCE ANALYZER
# ============================================================


elif option == "📈 Performance Analyzer":

    st.header("📈 Pose-to-Performance Analyzer")

    st.write(
        "Analyze your workout performance and generate "
        "a simple performance score."
    )

    st.subheader("🏋️ Enter Workout Results")

    col1, col2 = st.columns(2)

    with col1:
        squat_count = st.number_input(
            "Squats Completed",
            min_value=0,
            max_value=200,
            value=20
        )

        pushups = st.number_input(
            "Push-ups Completed",
            min_value=0,
            max_value=200,
            value=10
        )

    with col2:
        duration = st.number_input(
            "Workout Duration (minutes)",
            min_value=0,
            max_value=300,
            value=30
        )

        consistency = st.slider(
            "Workout Consistency (%)",
            min_value=0,
            max_value=100,
            value=70
        )

    if st.button("📊 Analyze Performance"):

        # ----------------------------------------------------
        # SCORE CALCULATION
        # ----------------------------------------------------

        squat_score = min(squat_count / 50 * 100, 100)
        pushup_score = min(pushups / 30 * 100, 100)
        duration_score = min(duration / 60 * 100, 100)

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

        # ----------------------------------------------------
        # PERFORMANCE LEVEL
        # ----------------------------------------------------

        if performance_score >= 80:
            level = "Excellent 🏆"
            message = (
                "Excellent performance! Keep maintaining "
                "your consistency and form."
            )

        elif performance_score >= 60:
            level = "Good 💪"
            message = (
                "Good progress! Continue training consistently "
                "to improve your performance."
            )

        elif performance_score >= 40:
            level = "Average 👍"
            message = (
                "You're making progress. Try gradually "
                "increasing your workout intensity."
            )

        else:
            level = "Beginner 🌱"
            message = (
                "Everyone starts somewhere! Focus on consistency "
                "and gradually increase your activity."
            )

        # ----------------------------------------------------
        # DISPLAY RESULTS
        # ----------------------------------------------------

        st.divider()

        st.subheader("📊 Performance Results")

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

        # ----------------------------------------------------
        # PERFORMANCE BREAKDOWN
        # ----------------------------------------------------

        st.subheader("📋 Performance Breakdown")

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

        st.dataframe(
            performance_data,
            use_container_width=True
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

    st.header("🔌 Smart Gym Assistant")

    st.write(
        "AI-powered gym equipment monitoring and "
        "workout intensity recommendation."
    )

    st.subheader("🏋️ Equipment Settings")

    col1, col2 = st.columns(2)

    with col1:

        equipment = st.selectbox(
            "Select Equipment",
            [
                "Treadmill",
                "Exercise Bike",
                "Leg Press",
                "Chest Press",
                "Rowing Machine"
            ]
        )

        intensity = st.slider(
            "Current Intensity (%)",
            min_value=0,
            max_value=100,
            value=50
        )

    with col2:

        heart_rate = st.number_input(
            "Heart Rate (BPM)",
            min_value=40,
            max_value=220,
            value=80
        )

        workout_time = st.number_input(
            "Workout Time (minutes)",
            min_value=0,
            max_value=300,
            value=20
        )

    if st.button("🤖 Analyze Equipment"):

        # ----------------------------------------------------
        # AI-BASED INTENSITY RECOMMENDATION
        # ----------------------------------------------------

        if heart_rate > 160:

            recommendation = (
                "⚠️ High intensity detected. "
                "Consider reducing the workout intensity "
                "and taking a rest."
            )

            status = "High Intensity"

        elif heart_rate > 130:

            recommendation = (
                "💪 Moderate intensity detected. "
                "Maintain your current pace and monitor "
                "your energy level."
            )

            status = "Moderate Intensity"

        else:

            recommendation = (
                "✅ Low to moderate intensity detected. "
                "You can gradually increase the intensity "
                "if you feel comfortable."
            )

            status = "Low Intensity"

        # ----------------------------------------------------
        # DISPLAY RESULTS
        # ----------------------------------------------------

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

        # ----------------------------------------------------
        # SIMULATED IoT DATA
        # ----------------------------------------------------

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
            use_container_width=True
        )

        st.success(
            "🔌 Smart Gym equipment successfully monitored!"
        )

        st.info(
            "💡 This project uses simulated IoT sensor data. "
            "Real gym equipment can be connected using MQTT, "
            "Node-RED, or other IoT communication protocols."
        )


# ============================================================
# GYM RECOMMENDER
# ============================================================


elif option == "📍 Gym Recommender":

    st.header("📍 AI Gym Recommender")

    st.write(
        "Get personalized gym, workout program, and fitness "
        "challenge recommendations based on your goals."
    )

    st.subheader("🎯 Your Fitness Preferences")

    col1, col2 = st.columns(2)

    with col1:

        goal = st.selectbox(
            "Fitness Goal",
            [
                "Weight Loss",
                "Muscle Building",
                "General Fitness",
                "Strength Training",
                "Flexibility"
            ]
        )

        experience = st.selectbox(
            "Experience Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    with col2:

        workout_type = st.selectbox(
            "Preferred Workout",
            [
                "Gym Training",
                "Home Workout",
                "Cardio",
                "Strength Training",
                "Yoga"
            ]
        )

        location = st.text_input(
            "Enter Your City",
            placeholder="Example: Hyderabad"
        )

    if st.button("🔍 Get Recommendations"):

        # ----------------------------------------------------
        # RECOMMENDATION LOGIC
        # ----------------------------------------------------

        if goal == "Weight Loss":

            program = (
                "🏃 Cardio + Full Body Training"
            )

            challenge = (
                "🔥 30-Day Fitness Consistency Challenge"
            )

        elif goal == "Muscle Building":

            program = (
                "🏋️ Strength Training + Progressive Overload"
            )

            challenge = (
                "💪 30-Day Strength Building Challenge"
            )

        elif goal == "Strength Training":

            program = (
                "🏋️ Compound Exercises + Strength Program"
            )

            challenge = (
                "⚡ Progressive Strength Challenge"
            )

        elif goal == "Flexibility":

            program = (
                "🧘 Yoga + Mobility Training"
            )

            challenge = (
                "🌿 21-Day Flexibility Challenge"
            )

        else:

            program = (
                "🏋️ Balanced Full Body Fitness Program"
            )

            challenge = (
                "💪 30-Day General Fitness Challenge"
            )

        # ----------------------------------------------------
        # RESULTS
        # ----------------------------------------------------

        st.divider()

        st.subheader("🎯 Your Personalized Recommendations")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Fitness Goal",
                goal
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

        # ----------------------------------------------------
        # GYM RECOMMENDATION
        # ----------------------------------------------------

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

        
# ============================================================
# PERFORMANCE ANALYZER
# ============================================================

elif option == "📈 Performance Analyzer":

    st.header("📈 Pose-to-Performance Analyzer")

    st.write(
        "Analyze your workout performance and generate "
        "a simple performance score."
    )

    st.subheader("🏋️ Enter Workout Results")

    col1, col2 = st.columns(2)

    with col1:

        squat_count = st.number_input(
            "Squats Completed",
            min_value=0,
            max_value=200,
            value=20
        )

        pushups = st.number_input(
            "Push-ups Completed",
            min_value=0,
            max_value=200,
            value=10
        )

    with col2:

        duration = st.number_input(
            "Workout Duration (minutes)",
            min_value=0,
            max_value=300,
            value=30
        )

        consistency = st.slider(
            "Workout Consistency (%)",
            min_value=0,
            max_value=100,
            value=70
        )

    if st.button("📊 Analyze Performance"):

        squat_score = min(squat_count / 50 * 100, 100)
        pushup_score = min(pushups / 30 * 100, 100)
        duration_score = min(duration / 60 * 100, 100)

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
                "Good progress! Continue training consistently "
                "to improve your performance."
            )

        elif performance_score >= 40:

            level = "Average 👍"

            message = (
                "You're making progress. Try gradually "
                "increasing your workout intensity."
            )

        else:

            level = "Beginner 🌱"

            message = (
                "Everyone starts somewhere! Focus on consistency "
                "and gradually increase your activity."
            )

        st.divider()

        st.subheader("📊 Performance Results")

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

        st.subheader("📋 Performance Breakdown")

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

        st.dataframe(
            performance_data,
            use_container_width=True
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

    st.header("🔌 Smart Gym Assistant")

    st.write(
        "AI-powered gym equipment monitoring and "
        "workout intensity recommendation."
    )

    st.subheader("🏋️ Equipment Settings")

    col1, col2 = st.columns(2)

    with col1:

        equipment = st.selectbox(
            "Select Equipment",
            [
                "Treadmill",
                "Exercise Bike",
                "Leg Press",
                "Chest Press",
                "Rowing Machine"
            ]
        )

        intensity = st.slider(
            "Current Intensity (%)",
            min_value=0,
            max_value=100,
            value=50
        )

    with col2:

        heart_rate = st.number_input(
            "Heart Rate (BPM)",
            min_value=40,
            max_value=220,
            value=80
        )

        workout_time = st.number_input(
            "Workout Time (minutes)",
            min_value=0,
            max_value=300,
            value=20
        )

    if st.button("🤖 Analyze Equipment"):

        if heart_rate > 160:

            recommendation = (
                "⚠️ High intensity detected. "
                "Consider reducing the workout intensity "
                "and taking a rest."
            )

            status = "High Intensity"

        elif heart_rate > 130:

            recommendation = (
                "💪 Moderate intensity detected. "
                "Maintain your current pace and monitor "
                "your energy level."
            )

            status = "Moderate Intensity"

        else:

            recommendation = (
                "✅ Low to moderate intensity detected. "
                "You can gradually increase the intensity "
                "if you feel comfortable."
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
            use_container_width=True
        )

        st.success(
            "🔌 Smart Gym equipment successfully monitored!"
        )

        st.info(
            "💡 This project uses simulated IoT sensor data. "
            "Real gym equipment can be connected using MQTT "
            "or Node-RED."
        )


# ============================================================
# GYM RECOMMENDER
# ============================================================

    elif option == "📍 Gym Recommender":

      st.header("📍 AI Gym Recommender")

    st.write(
        "Get personalized gym, workout program, and fitness "
        "challenge recommendations."
    )

    st.subheader("🎯 Your Fitness Preferences")

    col1, col2 = st.columns(2)

    with col1:

        gym_goal = st.selectbox(
            "Fitness Goal",
            [
                "Weight Loss",
                "Muscle Building",
                "General Fitness",
                "Strength Training",
                "Flexibility"
            ]
        )

        experience = st.selectbox(
            "Experience Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    with col2:

        workout_type = st.selectbox(
            "Preferred Workout",
            [
                "Gym Training",
                "Home Workout",
                "Cardio",
                "Strength Training",
                "Yoga"
            ]
        )

        location = st.text_input(
            "Enter Your City",
            placeholder="Example: Hyderabad"
        )

    if st.button("🔍 Get Recommendations"):

        if gym_goal == "Weight Loss":

            program = (
                "🏃 Cardio + Full Body Training"
            )

            challenge = (
                "🔥 30-Day Fitness Consistency Challenge"
            )

        elif gym_goal == "Muscle Building":

            program = (
                "🏋️ Strength Training + Progressive Overload"
            )

            challenge = (
                "💪 30-Day Strength Building Challenge"
            )

        elif gym_goal == "Strength Training":

            program = (
                "🏋️ Compound Exercises + Strength Program"
            )

            challenge = (
                "⚡ Progressive Strength Challenge"
            )

        elif gym_goal == "Flexibility":

            program = (
                "🧘 Yoga + Mobility Training"
            )

            challenge = (
                "🌿 21-Day Flexibility Challenge"
            )

        else:

            program = (
                "🏋️ Balanced Full Body Fitness Program"
            )

            challenge = (
                "💪 30-Day General Fitness Challenge"
            )

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
            use_container_width=True
        )

        st.success(
            "🤖 AI recommendation generated successfully!"
        )

        st.info(
            "💡 This prototype uses rule-based recommendation "
            "logic. A production version could use machine "
            "learning, location APIs, and historical user data."
        ) 