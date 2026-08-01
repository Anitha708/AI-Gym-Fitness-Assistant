def get_gym_buddy_response(message):

    message = message.lower().strip()

    # Motivation
    if any(word in message for word in [
        "motivat",
        "lazy",
        "give up",
        "can't",
        "tired"
    ]):
        return (
            "💪 Don't give up! Small consistent efforts lead to "
            "big results. Take a short break if needed and keep going!"
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
            "Start with a comfortable number of repetitions and increase "
            "gradually."
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

    # Rest
    elif any(word in message for word in [
        "rest",
        "sleep",
        "recover",
        "recovery"
    ]):
        return (
            "😴 Recovery is an important part of fitness. Get enough "
            "sleep, stay hydrated, and allow your body to recover "
            "between intense workouts."
        )

    # Greeting
    elif any(word in message for word in [
        "hello",
        "hi",
        "hey"
    ]):
        return (
            "👋 Hey! I'm your Virtual Gym Buddy. "
            "Ask me about workouts, nutrition, motivation, or recovery!"
        )

    # Default
    else:
        return (
            "🤖 I'm here to support your fitness journey! "
            "You can ask me about workouts, diet, motivation, "
            "or recovery."
        )