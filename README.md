# 📊 BDS - Basic Day Scorer
Basic Day Scorer is a simple daily scoring system written in Python. It uses Python, json, and os.

## Requirements:

An up-to-date version of Python must be installed on your computer.

## How to Run?

Download the program.

Double-click on the program.

## How to Use?
First, let's assume you did something bad that day. You will select that you did something bad.
After that, you will enter more points depending on how bad that thing was for you. One-fourth of the points you entered will be added to the bad bar. If your good bar is above 5 points or equal to 5 points, 5 points will be deducted from the good bar. If you enter something good, all of the points you entered will be added to the good bar, and again, if the bad bar is greater than 5 or equal to 5, then 5 will be subtracted from the bad bar.

## Features:

After each action, your good bar and bad bar values are written to a json file. Each value is not saved individually; the latest value remains saved. This way, it both does not take up much space and allows you to continue from where you left off even if you close and reopen it.

The bad bar increases slower than the good bar.

Even if you mess with or corrupt your save file, the program will not give an error.
