# Snake Game (Python)

## Overview
Snake Game is a classic arcade game developed using Python and the Pygame library. The objective of the game is to control a snake and eat food while avoiding collisions with the walls and itself. The game increases in difficulty as the snake grows, requiring strategic movement to maximize the score.

## Features
- Classic snake movement where the player controls the snake using keyboard inputs.
- Food spawns at random locations, and consuming it increases the snake's length and score.
- The game includes boundary detection, ensuring that the snake cannot move beyond the screen.
- The snake's movement speed increases as the game progresses, adding an extra challenge.
- Score tracking allows players to monitor their progress.
- The game over condition is triggered when the snake collides with itself or the boundary.
- Simple but engaging graphical elements are created using the Pygame library.

## Technologies Used
- Python: The programming language used for implementing the logic of the game.
- Pygame Library: A library used for rendering graphics, handling events, and managing game mechanics.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Markhasmukh/Snake-Game_Python.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Snake-Game_Python
   ```
3. Install the required dependencies:
   ```sh
   pip install pygame
   ```

## Usage
1. Run the game script by executing:
   ```sh
   python snake.py
   ```
2. Use the arrow keys to control the snake's movement.
3. Consume food to grow the snake and increase the score.
4. Avoid hitting the walls or colliding with the snake's body to prevent a game over.
5. The game will continue until the snake collides with itself or a boundary, at which point the final score will be displayed.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improving the game, feel free to submit an issue or a pull request. Enhancements such as adding new game modes, improving the UI, or optimizing performance are encouraged.

## License
This project is licensed under the MIT License.

## Additional Details
The game follows a simple event-driven loop where the player's inputs dictate the snake's direction. The game checks for collisions at every frame update and determines whether the game should continue or end. The increasing speed mechanism ensures that the difficulty level gradually rises, making the game more engaging. Future improvements may include implementing different difficulty modes, adding background music, and introducing power-ups for more dynamic gameplay.

---

### How the Snake Game Works
1. **Game Initialization:** The game initializes with a set screen size, a snake of initial length, and a food item placed randomly on the screen.
2. **Movement Handling:** The player's inputs control the direction of the snake. Movement is continuous, meaning the snake moves in the chosen direction until a new input is provided.
3. **Food Consumption:** When the snake's head touches the food, the score increases, the snake grows, and a new food item is placed randomly.
4. **Collision Detection:** The game continuously checks if the snake has hit a wall or itself. If a collision occurs, the game ends, and the final score is displayed.
5. **Game Loop:** The game runs in a loop where it updates the screen, processes user input, and checks for win/loss conditions in real time.

This implementation ensures a fun and challenging experience for users looking to play a nostalgic game built with Python.

