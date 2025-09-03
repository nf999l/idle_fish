import pygame
import os

class AssetManager:
    def __init__(self, base_path="assets/graphics/"):
        self.base_path = base_path
        self.cache = {}
    def load_image(self, filename):
        # Pfad zusammensetzen
        path = os.path.join(self.base_path, filename)

        # Falls schon geladen: zurückgeben
        if path in self.cache:
            return self.cache[path]

        # Bild laden
        image = pygame.image.load(path)

        # Cache speichern
        self.cache[path] = image
        return image    