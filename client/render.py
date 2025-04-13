import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class ImageSwitcher:
    def __init__(self):
        # List to store our images
        self.images = []
        # Track current image index
        self.current_index = 0
        
    def load_images(self, *image_paths):
        """Load multiple images from file paths"""
        for path in image_paths:
            try:
                # Convert images to optimize performance
                img = pygame.image.load(path).convert_alpha()
                self.images.append(img)
            except Exception as e:
                print(f"Error loading {path}: {str(e)}")
        
    def get_current_image(self):
        """Return the currently selected image"""
        return self.images[self.current_index] if self.images else None
        
    def next_image(self):
        """Move to the next image in sequence"""
        if len(self.images) > 1:
            self.current_index = (self.current_index + 1) % len(self.images)
            
    def previous_image(self):
        """Move to the previous image in sequence"""
        if len(self.images) > 1:
            self.current_index = (self.current_index - 1) % len(self.images)

def main(images):
    # Create instance of our image switcher
    switcher = ImageSwitcher()
    
    # Load your images here - replace with your actual image paths
    switcher.load_images(
        images
    )
    
    # Set up game loop variables
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    switcher.next_image()
                elif event.key == pygame.K_LEFT:
                    switcher.previous_image()
        
        # Draw current frame
        screen.fill((0, 0, 0))  # Clear screen with black
        
        # Get and draw current image
        current_image = switcher.get_current_image()
        if current_image:
            # Calculate position to center the image
            rect = current_image.get_rect()
            pos_x = (SCREEN_WIDTH - rect.width) // 2
            pos_y = (SCREEN_HEIGHT - rect.height) // 2
            
            # Draw the image
            screen.blit(current_image, (pos_x, pos_y))
        
        # Update display
        pygame.display.flip()
        
        # Cap framerate
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()