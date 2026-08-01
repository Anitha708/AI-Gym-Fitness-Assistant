import pandas as pd
import os


FILE_NAME = "workout_history.csv"


def load_workout_data():

    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)

    return pd.DataFrame(
        columns=[
            "Date",
            "Exercise",
            "Repetitions",
            "Duration",
            "Calories"
        ]
    )


def save_workout(
    date,
    exercise,
    repetitions,
    duration,
    calories
):

    df = load_workout_data()

    new_workout = pd.DataFrame({
        "Date": [date],
        "Exercise": [exercise],
        "Repetitions": [repetitions],
        "Duration": [duration],
        "Calories": [calories]
    })

    df = pd.concat(
        [df, new_workout],
        ignore_index=True
    )

    df.to_csv(
        FILE_NAME,
        index=False
    )

    return df