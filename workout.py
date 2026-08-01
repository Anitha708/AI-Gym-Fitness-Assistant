import cv2
import mediapipe as mp


def run_pose_detection():

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    pose = mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Camera could not be opened."

    squat_count = 0

    # Start in standing position
    stage = "STANDING"

    # Prevent multiple counts during one movement
    can_count = False

    while cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = pose.process(rgb_frame)

        if results.pose_landmarks:

            landmarks = results.pose_landmarks.landmark

            # Left side
            left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
            left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]

            # Right side
            right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]
            right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE]

            # Average positions
            hip_y = (left_hip.y + right_hip.y) / 2
            knee_y = (left_knee.y + right_knee.y) / 2

            body_position = knee_y - hip_y

            # -------------------------
            # SQUAT DETECTION
            # -------------------------

            # Going down
            if body_position < 0.20 and stage == "STANDING":
                stage = "SQUAT"
                can_count = True

            # Coming back up
            elif body_position > 0.25 and stage == "SQUAT":

                stage = "STANDING"

                # Count only once
                if can_count:
                    squat_count += 1
                    can_count = False

            # Draw pose landmarks
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            # -------------------------
            # DISPLAY SQUAT COUNT
            # -------------------------

            cv2.putText(
                frame,
                f"Squats: {squat_count}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # -------------------------
            # DISPLAY POSITION
            # -------------------------

            cv2.putText(
                frame,
                f"Position: {stage}",
                (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            # -------------------------
            # FORM FEEDBACK
            # -------------------------

            if stage == "SQUAT":
                feedback = "Good! Keep your back straight."
            else:
                feedback = "Ready for next squat."

            cv2.putText(
                frame,
                feedback,
                (20, 170),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                (0, 255, 0),
                2
            )

            # -------------------------
            # DISPLAY POSITION VALUE
            # -------------------------

            cv2.putText(
                frame,
                f"Position Value: {body_position:.2f}",
                (20, 130),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

        # Display camera window
        cv2.imshow(
            "AI Gym Trainer - Squat Counter",
            frame
        )

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    pose.close()

    return f"Workout completed! Total squats: {squat_count}"