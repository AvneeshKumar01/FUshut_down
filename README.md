# 🖐 Hand Gesture Controlled Shutdown

This project lets you **shut down your computer using a hand gesture** detected via your webcam. Built with **Python**, **OpenCV**, and **MediaPipe**, it identifies a specific gesture (middle finger up, others folded) and executes an immediate shutdown.

---

## 📦 Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
opencv-python
mediapipe
numpy
```

---

## 🚀 How It Works

- Captures real-time hand landmarks using MediaPipe.
- Detects if:
  - Middle finger is **extended**.
  - Index, Ring, and Pinky fingers are **folded**.
- If the gesture matches, triggers a system **shutdown**.

⛘️ **Warning:** Shutdown is immediate once the gesture is recognized. Test carefully!

---

## 📋 Usage

1. Clone the repository and navigate into the project folder.
2. (Optional but recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate    # On Windows
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python main.py 
python3 main.py
```

5. Allow webcam access.
6. Make the **ultimate savage gesture**:
   - Raise your middle finger high like you're flipping off your PC ✌️.
   - Keep the rest of your fingers tucked down like they know who's boss.
7. Watch your computer surrender and **shut down immediately**.
8. Press `Q` if you want to exit like a "civilized" human without nuking your machine.

---

## 🛠 Developer Notes

- To **test without shutting down**, comment `shut_down_computer()` and uncomment `print("shutdown")`.
- Landmark detection follows MediaPipe's index for hand joints.

---

## 🧹 Extra Details

- **Image Flip:**
  - Makes webcam act like a mirror.

- **Y-Axis for Detection:**
  - In MediaPipe, `y` increases downward.
  - If fingertip `y` is higher (smaller) than the PIP joint `y`, the finger is pointing upward.

---

## 🧹 Author's Note

> "Left `# print("shutdown")` commented out... because I'm cool like that. 😎"

Stay savage. 👑

---

# 🔗 License

_GPL3.0_

