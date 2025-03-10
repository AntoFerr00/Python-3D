# 3D Solar System

A Python project using VPython that simulates a solar system in 3D with:
- Planets orbiting the Sun.
- A flickering starfield backdrop.
- A comet with an elliptical orbit.
- An interactive spaceship you can control with arrow keys.
- Collision detection with asteroids.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [License](#license)
- [Contributing](#contributing)

## Features

1. **Realistic Planetary Orbits**  
   Each planet orbits at different speeds and spins on its axis.
2. **Comet**  
   Moves in an elliptical orbit around the Sun.
3. **Flickering Starfield**  
   Randomly placed stars that flicker for a more engaging visual.
4. **Saturn's Ring**  
   A ring object that follows Saturn's position.
5. **Asteroid Belt**  
   An asteroid ring that sits between Mars and Jupiter.
6. **Interactive Spaceship**  
   Control a spaceship to explore the solar system and dodge asteroids.
7. **Collision Detection**  
   Spaceship turns red if it intersects with an asteroid.

## Installation

1. **Clone or download** this repository.
2. Install [Python 3](https://www.python.org/downloads/).
3. Install the `vpython` package (if not already installed):
   ```bash
   pip install vpython
   ```
4. Navigate to the project folder in your terminal/command prompt.

## Usage
Run the Python script:
   ```bash
    python main.py
   ```
A new window (or browser tab) will open displaying the 3D simulation.
Move your mouse to rotate and zoom the view.

## Controls
Use your arrow keys:

Up: Accelerate forward
Down: Accelerate backward
Left: Rotate left
Right: Rotate right
The spaceship has simple physics with a small friction factor.
Watch for collisions with asteroids (ship turns red upon collision).

## License
This project is licensed under the MIT License.

## Contributing
Contributions, bug reports, and feature requests are welcome!

1. Fork the repository
2. Create a new branch for your feature/fix
3. Commit your changes
4. Push to your branch
5. Create a Pull Request