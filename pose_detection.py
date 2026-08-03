import cv2
import mediapipe as mp
import math


def calculate_angle(a, b, c):
    """
    Calculate angle between three points.
    """
    a = [a.x, a.y]
    b = [b.x, b.y]
    c = [c.x, c.y]

    radians = math.atan2(c[1] - b[1], c[0] - b[0]) - \
              math.atan2(a[1] - b[1], a[0] - b[0])

    angle = abs(radians * 180.0 / math.pi)

    if angle > 180:
        angle = 360 - angle

    return angle


def run_pose_detection():

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    pose = mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "❌ Webcam could not be opened."

    squat_count = 0
    squat_state = "up"

    print("Webcam started. Press Q to stop.")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = pose.process(rgb_frame)

        if results.pose_landmarks:

            landmarks = results.pose_landmarks.landmark

            # Right side landmarks
            hip = landmarks[
                mp_pose.PoseLandmark.RIGHT_HIP
            ]

            knee = landmarks[
                mp_pose.PoseLandmark.RIGHT_KNEE
            ]

            ankle = landmarks[
                mp_pose.PoseLandmark.RIGHT_ANKLE
            ]

            angle = calculate_angle(
                hip,
                knee,
                ankle
            )

            # Draw pose
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            # Squat detection
            if angle > 160:

                squat_state = "up"

            elif angle < 100 and squat_state == "up":

                squat_count += 1
                squat_state = "down"

            # Display angle
            cv2.putText(
                frame,
                f"Knee Angle: {int(angle)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

        # Display squat count
        cv2.putText(
            frame,
            f"Squats: {squat_count}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )

        cv2.putText(
            frame,
            "Press Q to Stop",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

        cv2.imshow(
            "AI Gym - Squat Detection",
            frame
        )

        # Q = Stop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    pose.close()

    return f"🎉 Workout completed! Total squats: {squat_count}"