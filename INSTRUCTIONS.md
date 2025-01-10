# INSTRUCTIONS: Customize Your Love Choice Game!

Welcome to the Love Choice Game Template! This guide will walk you through the steps of customizing the game with your own story, choices, and endings using **Python and the Pygame library**.

These instructions are designed for beginners, so don't worry if you don't have much programming experience. I'll break down each part step-by-step.

## Getting Started

1. **Download/Clone:** You should have already downloaded or cloned this project from GitHub. If not, go back to the main repository page and follow the instructions there.
2. **Install Pygame:**
    *   This game uses the `pygame` library. If you don't have it installed, open your terminal or command prompt and type:
        ```bash
        pip install pygame
        ```
3. **Install Assets:**
    *   This game uses assets such as images and fonts. Make sure you have downloaded these and put them in the correct folders as laid out in the code
    *   The code will try to use a font file named `better-together.ttf`. If you don't have this font or want to use a different one, update this in the code

## Understanding the Code Structure (Python/Pygame)

The game is built using Python and Pygame. Here's a simplified overview of the important parts:

*   **`story` Dictionary:** This is the heart of your game! It's a Python dictionary that holds the entire story's structure.
    *   **Scenes:** Each entry in the `story` dictionary represents a scene (e.g., "start", "park", "cafe").
    *   **Scene Content:** Each scene has:
        *   `text`: The text displayed on the screen for that scene.
        *   `choices`: A list of `Button` objects representing the choices the player can make.
        *   `image`: The name of the image to display for that scene (make sure this image is in your `images` folder).
        *   `sound`: The name of the sound effect to play (optional, put sounds in the `sounds` folder).
        *   `hidden_area`: (Optional) Defines a clickable area on the screen that plays a sound.
*   **`Button` Class:** Defines how buttons look and behave. You don't need to change the code here, but you'll use it to create choices.
*   **`load_assets()` Function:** Loads images and sounds. You'll need to update the file paths here if you use your own assets.
*   **`draw_text()` Function:** A helper function to draw text on the screen.
*   **Game Loop:** The `while running:` loop is the main part of the game. It handles events (like button clicks), updates the game state, and draws everything on the screen.

## Customizing the Game

Now comes the fun part - making the game your own!

### 1. Modify the Story

Open the Python file (it might be named `main.py` or `game.py`). Find the `story` dictionary. This is where you'll edit the story.

#### Changing Text

*   **Scene Text:** In each scene, change the text within the double quotes (`""`) to whatever you want to be displayed.
    *   Example:

    ```python
    "start": {
        "text": "Welcome, [Partner's Name]! Where should our journey begin?",
        # ... other parts of the scene
    },
    ```

#### Changing Images

*   **Replace Images:** Put your own images in the `images` folder. Make sure they are `.jpg` or `.png` files.
*   **Update Image Names:** In each scene, change the `"image"` value to the name of your image file.
    *   Example:

    ```python
    "park": {
        # ... other parts of the scene
        "image": "my_park_image.jpg",  # Your image file name
    },
    ```

#### Changing Sounds

*   **Replace Sounds:** Put your own sound files in the `sounds` folder. Make sure they are `.wav` files.
*   **Update Sound Names:** In each scene, change or add the `"sound"` value with the name of your sound file.
    *   Example:

    ```python
    "cafe": {
        # ... other parts of the scene
        "sound": "my_cafe_sound.wav",
    },
    ```

#### Modifying Choices

*   **Button Text:** Change the text within the double quotes when creating a `Button` object.
*   **Destination Scene:** The last argument when creating a `Button` is the name of the scene it leads to. Change this to create different story paths.
    *   Example:

    ```python
    "choices": [
        Button("Go to the Beach", 50, 150, 300, 50, FONT, LIGHT_BLUE, PINK, WHITE, "beach_scene"),
        Button("Stay Home", 450, 150, 300, 50, FONT, LIGHT_BLUE, PINK, WHITE, "home_scene")
    ],
    ```

#### Adding/Removing Scenes

*   **Add a Scene:** Copy an existing scene's structure, give it a new name, and customize the text, image, choices, etc.
*   **Remove a Scene:** Carefully delete the entire entry for a scene from the `story` dictionary. Make sure no choices point to a deleted scene!

### 2. The Love Meter

*   **`love_meter` Variable:** This variable keeps track of the player's "score." You can change the starting value (currently 50).
*   **Modifying the Love Meter:** In the game loop, there's a section that updates `love_meter` based on choices. You can change how much each choice affects the score.
    *   Example:

    ```python
    if current_scene == "walk":
        love_meter += 5  # Increase by 5 if they choose "walk"
    elif current_scene == "chat":
        love_meter -= 2  # Decrease by 2 if they choose "chat"
    ```

### 3. (Optional) Hidden Area

*   **`hidden_area`:** In some scenes, there might be a `hidden_area` defined. This creates a secret clickable area on the screen.
*   **Customize:** You can change the `rect` (position and size) and the `sound` played when it's clicked. You can also add `hidden_area` to other scenes.

## Testing and Sharing

1. **Run the Game:**
    *   Open your terminal or command prompt.
    *   Navigate to your project folder using the `cd` command (e.g., `cd path/to/your/project`).
    *   Type `python your_game_file.py` (replace `your_game_file.py` with the name of your Python file) and press Enter.
2. **Test Thoroughly:** Play through the entire game, trying out different choices to make sure everything works correctly and there are no errors.
3. **Share with Your Loved One:**
    *   **Executable (Advanced):** If you want to create an executable file that your loved one can run without needing Python installed, you can use tools like `py2app` (for macOS), `py2exe` (for Windows), or `PyInstaller` (cross-platform). This is a more advanced step, so you might want to search for tutorials on how to do this.
    *   **Send the Files:** The simplest way is to just send them the entire project folder. They will need to have Python and Pygame installed on their computer to run it.

## Troubleshooting

*   **Font Error:** If you get an error about the font file, make sure `better-together.ttf` (or your chosen font file) is in the same folder as your script. You can also replace `"better-together.ttf"` with `None` in the `FONT` variable to use the default font.
*   **Image/Sound Errors:** Double-check that your image and sound files are in the correct folders (`images` and `sounds`) and that the file names in the code match exactly (including capitalization).
*   **Game Not Running:** If the game doesn't run at all, carefully check your terminal for error messages. These messages will usually give you clues about what went wrong.

## Have Fun!

This is just a basic template, so feel free to get creative and add your own unique touches! If you have any questions or run into problems, feel free to ask for help online (Stack Overflow is a great resource).

Enjoy creating your personalized love choice game, and I hope your special someone loves it!
