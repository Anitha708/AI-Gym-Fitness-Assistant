import os
import pandas as pd


FILE_NAME = "workout_history.csv"

COLUMNS = [
    "Date",
    "Exercise",
    "Repetitions",
    "Duration",
    "Calories"
]


def load_workout_data():

    if os.path.exists(FILE_NAME):

        df = pd.read_csv(FILE_NAME)

        # Make sure the expected columns exist
        for column in COLUMNS:
            if column not in df.columns:
                df[column] = None

        return df[COLUMNS]

    return pd.DataFrame(columns=COLUMNS)


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