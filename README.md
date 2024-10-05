 # Balloon Pop Game

## Overview

This is a simple interactive game called **Balloon Pop**, developed using Python and Pygame, with hand tracking capabilities provided by OpenCV and the **cvzone** Hand Tracking Module. In this game, a balloon appears on the screen, and the player can "pop" the balloon by pointing their finger at it via a webcam. The objective is to pop as many balloons as possible within a limited time, and the player's score increases with each successful pop.

## Features

- **Hand Tracking**: Detects hand gestures using a webcam to interact with the game.
- **Balloon Animation**: A balloon that moves up the screen and resets position upon being "popped."
- **Score System**: Players earn points for each balloon they pop.
- **Time Limit**: The game runs for 30 seconds, after which the player's score is displayed.

## Prerequisites

To run the game, you need the following:

- Python 3.x
- Required libraries:
  - `pygame`
  - `opencv-python`
  - `cvzone`
  - `numpy`

Install the required dependencies using pip:

```bash
pip install pygame opencv-python cvzone numpy
```

## Game Instructions

1. **Game Objective**: Pop the balloons by pointing your finger at them before they float off the screen. The goal is to achieve the highest score possible within the given 30 seconds.
2. **Hand Tracking**: The game uses your webcam to detect your hand, specifically the index finger. The position of your finger is used to interact with the balloon on the screen.

## How to Run

1. Make sure your webcam is connected and working.
2. Run the Python script:

   ```bash
   python balloon_pop.py
   ```

3. The game window will open. You will see the balloon moving up the screen.
4. Use your hand to interact with the balloon. When your finger "touches" the balloon, it pops, and a new balloon appears at a random location.
5. Try to pop as many balloons as possible within 30 seconds.

6. Once the game ends, your final score will be displayed.

## How It Works

- **Webcam Integration**: The script captures real-time video from your webcam and uses OpenCV and the cvzone HandDetector module to track your hand movements.
- **Balloon Movement**: The balloon moves upward at a certain speed. If the balloon reaches the top of the screen without being popped, its speed increases and it reappears at the bottom.
- **Score Tracking**: Each time you pop a balloon, your score increases by 10 points and the balloon's speed increases.

## Game Assets

- The balloon image is loaded from a file (`BalloonRed.png`).
- Fonts used for displaying the score and time are loaded from a specified path. If the font file is missing, the default font will be used.

## Extracting Zipped Files

The project has been compressed using **7-Zip** into parts, each of 10 MB size, as shown in the image (e.g., `ai.zip.001`, `ai.zip.002`, etc.). To extract the files from these multiple parts after downloading them from GitHub, follow these steps:

1. **Download all parts**: Ensure you have downloaded all parts (e.g., `ai.zip.001`, `ai.zip.002`, and so on) from the GitHub repository.
2. **Install 7-Zip**: If you don't already have it, download and install [7-Zip](https://www.7-zip.org/).
3. **Extract the files**:
   - Right-click on the first part (`ai.zip.001`).
   - Select **7-Zip > Extract Here** or **Extract to "ai.zip/"** (if you want to extract the contents into a separate folder).
   - 7-Zip will automatically combine all parts and extract the files.
4. **Move the Extracted Files**: After extracting the files:
   - **Cut and paste** the extracted `ai` folder into the **Virtual Keyboard** project folder, the one that contains the `.main` file. This ensures that the virtual keyboard can correctly access the extracted files and run smoothly.

## Customization

- **Balloon Image**: You can replace the balloon image (`BalloonRed.png`) with any other image by updating the file path in the script.
- **Font Style**: The font used to display the score and time can be changed by specifying a different font file in the `font_path` variable.

## Notes

- Ensure that your webcam is functioning correctly before running the game.
- If the balloon does not pop when you point your finger at it, adjust the position of your hand to ensure better detection.
- The balloon speed increases each time you miss popping a balloon, making the game progressively harder.

## Ending the Game

- The game will automatically end after 30 seconds, and the final score will be displayed.
- You can also quit the game manually by pressing the `Quit` button in the window or closing the game window.
