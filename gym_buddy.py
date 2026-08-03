def gym_buddy_response(message):
    message = message.lower().strip()

    if any(word in message for word in [
        "hi", "hii", "hiii", "hello", "hey"
    ]):
        return (
            "👋 Hey! I'm your Virtual Gym Buddy! "
            "I'm ready to support your fitness journey. 💪"
        )

    elif any(phrase in message for phrase in [
        "nice to meet you",
        "good to meet you",
        "pleased to meet you",
        "glad to meet you"
    ]):
        return (
            "😊 Nice to meet you too! I'm happy to be your "
            "Virtual Gym Buddy. 💪 I can help you with workouts, "
            "fitness goals, nutrition, motivation and recovery."
        )

    elif any(phrase in message for phrase in [
        "how are you",
        "how are u",
        "how r you",
        "how r u"
    ]):
        return (
            "😊 I'm doing great and ready to help! 💪 "
            "What would you like to work on today — workouts, "
            "fitness goals, nutrition or motivation?"
        )

    elif any(word in message for word in [
        "fitness", "healthy", "health", "fit"
    ]):
        return (
            "💪 Fitness is about building a healthy and active lifestyle. "
            "Try to combine regular exercise, balanced nutrition, "
            "proper hydration, good sleep and consistency."
        )

    elif any(phrase in message for phrase in [
        "fitness goal",
        "fitness goals",
        "my goal",
        "my goals",
        "goal for fitness",
        "goals for fitness",
        "fitness target"
    ]):
        return (
            "🎯 Great fitness goals should be realistic and measurable.\n\n"
            "• Weight loss\n"
            "• Muscle building\n"
            "• Improving strength\n"
            "• Increasing endurance\n"
            "• Improving overall fitness\n\n"
            "Choose one main goal and track your progress consistently. 💪"
        )

    elif any(phrase in message for phrase in [
        "gym tips",
        "tips about gym",
        "tips for gym",
        "gym advice",
        "gym guidance",
        "beginner gym"
    ]):
        return (
            "🏋️ Here are some useful gym tips:\n\n"
            "• Warm up before exercising\n"
            "• Focus on proper form\n"
            "• Start with manageable weights\n"
            "• Increase intensity gradually\n"
            "• Stay hydrated\n"
            "• Get enough recovery\n"
            "• Track your workouts\n"
            "• Stay consistent"
        )

    elif any(phrase in message for phrase in [
        "give me tips",
        "some tips",
        "fitness tips",
        "tips for fitness",
        "fitness advice",
        "help with fitness"
    ]):
        return (
            "💪 Here are some fitness tips:\n\n"
            "🏋️ Exercise regularly and focus on proper form.\n"
            "🥗 Eat balanced meals with enough protein.\n"
            "💧 Stay hydrated.\n"
            "😴 Get enough sleep and recovery.\n"
            "🎯 Set realistic fitness goals.\n"
            "🔥 Stay consistent!"
        )

    elif any(word in message for word in [
        "workout",
        "exercise",
        "squat",
        "pushup",
        "push-up",
        "training"
    ]):
        return (
            "🏋️ Start your workout with a warm-up and focus on "
            "proper form. Begin with comfortable repetitions and "
            "gradually increase the intensity."
        )

    elif any(phrase in message for phrase in [
        "build muscle",
        "building muscle",
        "muscle gain",
        "gain muscle",
        "muscle building"
    ]):
        return (
            "💪 For muscle building, focus on strength training, "
            "progressive overload, enough protein, balanced meals "
            "and proper recovery."
        )

    elif any(phrase in message for phrase in [
        "lose weight",
        "weight loss",
        "lose fat",
        "fat loss"
    ]):
        return (
            "🔥 For healthy weight management, combine regular "
            "physical activity with balanced nutrition. Focus on "
            "whole foods, vegetables, fruits and adequate protein."
        )

    elif any(word in message for word in [
        "diet",
        "food",
        "eat",
        "nutrition",
        "meal",
        "calorie",
        "protein"
    ]):
        return (
            "🥗 Focus on balanced meals containing vegetables, "
            "fruits, whole grains and protein-rich foods. "
            "Stay hydrated and limit highly processed foods."
        )

    elif any(word in message for word in [
        "motivat",
        "lazy",
        "give up",
        "can't",
        "tired",
        "unmotivated"
    ]):
        return (
            "💪 Don't give up! Progress takes time. "
            "Even a short workout is better than doing nothing. "
            "Set a small goal for today and stay consistent! 🔥"
        )

    elif any(word in message for word in [
        "rest",
        "sleep",
        "recover",
        "recovery"
    ]):
        return (
            "😴 Recovery is an important part of fitness. "
            "Get enough sleep, stay hydrated and allow your body "
            "to recover between intense workouts."
        )

    elif any(phrase in message for phrase in [
        "thank you",
        "thanks",
        "thank u"
    ]):
        return (
            "😊 You're very welcome! Keep working toward your "
            "fitness goals. I'm always here to support you! 💪"
        )

    elif any(phrase in message for phrase in [
        "bye",
        "goodbye",
        "see you"
    ]):
        return (
            "👋 Bye! Take care and keep working toward your "
            "fitness goals. 💪🔥"
        )

    else:
        return (
            "🤖 I'm here to support your fitness journey! 💪\n\n"
            "You can ask me:\n"
            "• Give me gym tips\n"
            "• Tell me about fitness\n"
            "• Give me fitness goal tips\n"
            "• How can I build muscle?\n"
            "• How can I lose weight?\n"
            "• Give me workout tips\n"
            "• Give me diet tips\n"
            "• How important is recovery?"
        )