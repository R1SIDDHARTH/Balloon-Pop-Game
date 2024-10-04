# Import necessary modules

import random
import pygame
import cv2
import numpy as np
import os
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize Pygame
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Initialize Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

# Load Balloon Image
imgBalloon = pygame.image.load('C:\\ALL folder in dexstop\\PycharmProjects\\AI game\\BalloonRed.png').convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = random.randint(100, width - 100), height + 50

# Variables
speed = 15
score = 0
startTime = time.time()
totalTime = 30

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

def resetBalloon():
    rectBalloon.x = random.randint(100, width - 100)
    rectBalloon.y = height + 50

# Main Loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            break

    if not start:
        break

    # Apply Logic
    timeRemain = int(totalTime - (time.time() - startTime))
    if timeRemain < 0:
        window.fill((255, 255, 255))

        font_path = os.path.join('C:\\ALL folder in dexstop\\PycharmProjects\\AI game\\Project - GUI', 'Marcellus-Regular.ttf')
        try:
            font = pygame.font.Font(font_path, 50)
        except FileNotFoundError:
            print(f"Font file not found at {font_path}")
            font = pygame.font.Font(None, 50)  # Use default font if the specified font file is not found

        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time UP', True, (50, 50, 255))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))

    else:
        # OpenCV
        ret, img = cap.read()
        if not ret:
            continue
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        rectBalloon.y -= speed  # Move the balloon up
        # Check if balloon has reached the top without pop
        if rectBalloon.y < 0:
            resetBalloon()
            speed += 1

        if hands:
            hand = hands[0]
            lmList = hand['lmList']
            if lmList:
                # Get the tip of the index finger
                x, y = lmList[8][0], lmList[8][1]
                if rectBalloon.collidepoint(x, y):
                    resetBalloon()
                    score += 10
                    speed += 1

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))
        window.blit(imgBalloon, rectBalloon)

        font_path = os.path.join('C:\\ALL folder in dexstop\\PycharmProjects\\AI game\\Project - GUI', 'Marcellus-Regular.ttf')
        try:
            font = pygame.font.Font(font_path, 50)
        except FileNotFoundError:
            print(f"Font file not found at {font_path}")
            font = pygame.font.Font(None, 50)  # Use default font if the specified font file is not found

        textScore = font.render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)

# Release the webcam and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()