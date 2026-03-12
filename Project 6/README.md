# Reeborg Maze Solution 🤖🧩

This repository contains my solution to a maze challenge from **Reeborg's World**. The goal of the challenge is to guide the robot through a maze and reach the goal using Python logic.

## 🧠 Problem

The robot starts somewhere in a maze and must reach the goal.
It can only use a limited set of commands such as:

* `move()`
* `turn_left()`
* `wall_in_front()`
* `right_is_clear()`
* `at_goal()`

Because the robot cannot turn right directly, we must create our own `turn_right()` function.

## ⚙️ Strategy

I used a variation of the **right-hand wall following algorithm**.

The idea is:

1. If the robot can move to the **right**, turn right and move.
2. If there is **no wall in front**, move forward.
3. If there **is a wall**, adjust direction.

This allows the robot to navigate through most maze layouts.

## 🔍 What I Learned

While solving this challenge I learned:

* How to break problems into smaller functions
* How conditional logic controls movement
* How maze-solving strategies like the **right-hand rule** work
* How algorithms can sometimes get stuck in loops depending on maze structure

This challenge took about **1.5 days to solve**, which made it a great exercise in persistence and debugging.

## 🚀 Future Improvements

Possible improvements could include:

* Detecting loops
* Tracking visited positions
* Implementing more advanced maze algorithms like DFS or BFS

## 📚 Platform

This challenge was completed on **Reeborg's World**, an educational platform for learning programming logic and Python.
