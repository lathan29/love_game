import pygame
import sys
import os

# --- Initialize Pygame ---
pygame.init()
pygame.mixer.init()

# --- Screen Settings ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Our Adventure")  # Replace with your game's title

# --- Colors ---
WHITE = (255, 255, 255)
PINK = (255, 182, 193)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)

# --- Fonts ---
FONT_SIZE = 30
try:
    FONT = pygame.font.Font("better-together.ttf", FONT_SIZE)  # Optional: Add your own font or use None for default
except FileNotFoundError:
    print("Error: Could not find the font file 'better-together.ttf'. Using default font.")
    FONT = pygame.font.Font(None, FONT_SIZE)

# --- Load Assets ---
def load_assets():
    """Loads images and sounds with error handling."""
    assets = {}
    assets["font"] = FONT

    # Load images
    image_paths = {
        "start_image": "images/start_image.jpg",  # Replace with your image paths
        "park_image": "images/park_image.jpg",
        "cafe_image": "images/cafe_image.jpg",
        "walk_image": "images/walk_image.jpg",
        "chat_image": "images/chat_image.jpg",
        "coffee_image": "images/coffee_image.jpg",
        "cake_image": "images/cake_image.jpg",
        "italian_image": "images/italian_image.jpg",
        "pizza_image": "images/pizza_image.jpg",
        "movie_image": "images/movie_image.jpg",
        "surprise_image": "images/surprise_image.jpg",
        "future_image": "images/future_image.jpg",
    }
    for key, path in image_paths.items():
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Image file not found at: {path}")

            if not os.path.isfile(path):
                raise ValueError(f"Path is not a valid file: {path}")

            assets[key] = pygame.image.load(path)

        except FileNotFoundError as e:
            print(f"Error loading image '{key}': {e}")
            sys.exit()
        except ValueError as e:
            print(f"Error with path for image '{key}': {e}")
            sys.exit()
        except pygame.error as e:
            print(f"Error loading image '{key}' from '{path}': {e} - Check if it's a valid image file.")
            sys.exit()

    # Load sounds
    sound_paths = {
        "choice_sound": "sounds/choice.wav",  # Replace with your sound paths
        "special_sound": "sounds/special.wav",
    }
    assets["sounds"] = {}
    for key, path in sound_paths.items():
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Sound file not found at: {path}")
            if not os.path.isfile(path):
                raise ValueError(f"Sound path is not a valid file: {path}")
            assets["sounds"][key] = pygame.mixer.Sound(path)
        except FileNotFoundError as e:
            print(f"Error loading image '{key}': {e}")
            sys.exit()
        except ValueError as e:
            print(f"Error with path for image '{key}': {e}")
            sys.exit()
        except pygame.error as e:
            print(f"Error loading sound '{key}' from '{path}': {e} - Check if it's a valid image file.")
            sys.exit()

    return assets

# --- Helper Function to Draw Text ---
def draw_text(screen, text, font, color, x, y, center=False):
    """Draws text to the screen."""
    text_surface = font.render(text, True, color)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
    else:
        text_rect = text_surface.get_rect(topleft=(x, y))
    screen.blit(text_surface, text_rect)

# --- Button Class ---
class Button:
    """Represents a clickable button."""

    def __init__(self, text, x, y, width, height, font, color, hover_color, text_color, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        """Draws the button, changing color on hover."""
        mouse_pos = pygame.mouse.get_pos()
        button_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, button_color, self.rect)
        draw_text(screen, self.text, self.font, self.text_color, self.rect.centerx, self.rect.centery, True)

    def check_click(self, event):
        """Checks if the button was clicked and returns its action."""
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return self.action
        return None

# --- Story Data ---
story = {
    "start": {
        "text": "Welcome, Player! Where should our journey begin?",  # Customize the starting text
        "choices": [
            # Customize the choices and their destination scenes
            Button("The Cafe", 50, 150, 300, 50, FONT, LIGHT_BLUE, PINK, WHITE, "cafe"),
            Button("The Park", 450, 150, 300, 50, FONT, LIGHT_BLUE, PINK, WHITE, "park"),
            Button("Movie Night", 50, 220, 300, 50, FONT, LIGHT_BLUE, PINK, WHITE, "movie")
        ],
        "image": "start_image",  # Use the keys from your image_paths
        "sound": None  # Use the keys from your sound_paths, or None
    },
    "park": {
        "text": "What a lovely park! What should we do here?",
        "choices": [
            Button("Take a Walk", 50, 150, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "walk"),
            Button("Sit and Chat", 50, 220, 450, 50, FONT, LIGHT_BLUE, PINK, WHITE, "chat"),
            Button("Have a Picnic", 50, 290, 400, 50, FONT, LIGHT_BLUE, PINK, WHITE, "surprise_picnic")
        ],
        "image": "park_image",
        "sound": "choice_sound",  # Example sound
        "hidden_area": {  # Optional hidden area
            "rect": pygame.Rect(500, 300, 100, 100),
            "sound": "special_sound"
        }
    },
    "cafe": {
        "text": "The aroma of coffee fills the air! What shall we order?",
        "choices": [
            Button("Coffee", 50, 150, 400, 50, FONT, LIGHT_BLUE, PINK, WHITE, "coffee"),
            Button("Cake", 50, 220, 500, 50, FONT, LIGHT_BLUE, PINK, WHITE, "cake"),
            Button("Go to Italian Place", 50, 290, 550, 50, FONT, LIGHT_BLUE, PINK, WHITE, "italian_restaurant")
        ],
        "image": "cafe_image",
        "sound": "choice_sound"
    },
    "walk": {
        "text": "We took a leisurely walk and enjoyed the scenery. The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "walk_image",
        "sound": "choice_sound"
    },
    "chat": {
        "text": "We sat on a bench, talked, and laughed. The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "chat_image",
        "sound": "choice_sound"
    },
    "coffee": {
        "text": "We enjoyed a warm cup of coffee. The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "coffee_image",
        "sound": "choice_sound"
    },
    "cake": {
        "text": "The cake was delicious! The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "cake_image",
        "sound": "choice_sound"
    },
    "italian_restaurant": {
        "text": "This Italian place is great! What should we get?",
        "choices": [
            Button("Spaghetti", 50, 150, 400, 50, FONT, LIGHT_BLUE, PINK, WHITE, "spaghetti"),
            Button("Pizza", 50, 220, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "pizza")
        ],
        "image": "italian_image",
        "sound": "choice_sound"
    },
    "pizza": {
        "text": "The pizza was a great choice! The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "pizza_image",
        "sound": "choice_sound"
    },
    "spaghetti": {
        "text": "The spaghetti was delicious! The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "italian_image",
        "sound": "choice_sound"
    },
    "movie": {
        "text": "What movie should we watch tonight?",
        "choices": [
            Button("Action Movie", 50, 150, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "fav_movie"),
            Button("Rom-Com", 50, 220, 400, 50, FONT, LIGHT_BLUE, PINK, WHITE, "new_movie")
        ],
        "image": "movie_image",
        "sound": None
    },
    "fav_movie": {
        "text": "We watched an awesome action movie! The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "movie_image",
        "sound": "choice_sound"
    },
    "new_movie": {
        "text": "That romantic comedy was so funny! The end (for now!).",
        "choices": [
            Button("Think About Future", 50, 400, 350, 50, FONT, LIGHT_BLUE, PINK, WHITE, "future")
        ],
        "image": "movie_image",
        "sound": "choice_sound"
    },
    "surprise_picnic": {
        "text": "Surprise! Let's have a picnic!",
        "choices": [
            Button("That's Awesome!", 50, 220, 450, 50, FONT, LIGHT_BLUE, PINK, WHITE, "surprise")
        ],
        "image": "park_image",  # Or a specific picnic image
        "sound": "choice_sound"
    },
    "surprise": {
        "text": "This is the end of our adventure. I hope you enjoyed it!",
        "choices": [],
        "image": "surprise_image",
        "sound": "choice_sound"
    },
    "future": {
        "text": "What a wonderful journey! Let's make many more memories together. The end.",
        "choices": [],
        "image": "future_image",
        "sound": "choice_sound"
    }
}

# --- Game Variables ---
current_scene = "start"
love_meter = 50  # You can adjust the starting value

# --- Load Assets ---
assets = load_assets()

# --- Music ---
# Use background music (optional)
pygame.mixer.music.load("sounds/background_music.mp3")  # Replace with your music file
pygame.mixer.music.set_volume(0.5) # Set to 0 to mute
pygame.mixer.music.play(-1)  # Loop indefinitely

# --- Function to draw the love meter ---
def draw_love_meter(screen, love_meter, x, y):
    """Draws a heart-shaped love meter."""
    pygame.draw.polygon(screen, PINK, [(x, y - 15), (x - 15, y - 30), (x, y), (x + 15, y - 30)])
    pygame.draw.circle(screen, PINK, (x - 8, y - 25), 8)
    pygame.draw.circle(screen, PINK, (x + 8, y - 25), 8)

    fill = int((love_meter / 100) * 30)
    pygame.draw.rect(screen, PINK, (x - 15, y - 30, fill, 15))

# --- Main Game Loop ---
running = True
while running:
    screen.fill(WHITE)

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            # Handle hidden area click
            if "hidden_area" in story[current_scene]:
                hidden_area = story[current_scene]["hidden_area"]
                if event.type == pygame.MOUSEBUTTONDOWN and hidden_area["rect"].collidepoint(event.pos):
                    if hidden_area["sound"] in assets["sounds"]:
                        assets["sounds"][hidden_area["sound"]].play()

            # Handle button clicks
            for choice_button in story[current_scene]["choices"]:
                next_scene = choice_button.check_click(event)
                if next_scene:
                    current_scene = next_scene

                    # Modify love_meter based on choice
                    if current_scene == "walk":
                        love_meter += 5
                    elif current_scene == "chat":
                        love_meter += 10
                    elif current_scene == "surprise_picnic":
                        love_meter += 15
                    elif current_scene == "coffee":
                        love_meter += 8
                    elif current_scene == "cake":
                        love_meter += 12
                    elif current_scene == "italian_restaurant":
                        love_meter += 7
                    elif current_scene == "pizza":
                        love_meter += 11
                    elif current_scene == "spaghetti":
                        love_meter += 9
                    elif current_scene == "fav_movie":
                        love_meter += 6
                    elif current_scene == "new_movie":
                        love_meter += 10
                    elif current_scene == "future":
                        love_meter = 100

                    # Clamp love_meter to 0-100
                    love_meter = max(0, min(love_meter, 100))

                    # Play sound for the new scene
                    if story[current_scene].get("sound") in assets["sounds"]:
                        assets["sounds"][story[current_scene]["sound"]].play()

    # --- Draw Scene ---
    screen.blit(assets[story[current_scene]["image"]], (0, 0))
    draw_text(screen, story[current_scene]["text"], assets["font"], DARK_BLUE, 50, 50)

    # --- Draw Buttons ---
    for choice_button in story[current_scene]["choices"]:
        choice_button.draw(screen)

    # --- Draw Love Meter ---
    draw_love_meter(screen, love_meter, 750, 30)

    pygame.display.flip()

pygame.quit()
sys.exit()