from .color import *
import rand

class Palette:
    def __init__(self):
        self.colors = []

    def size(self):
        return len(self.colors)

    def get(self, index):
        if index >= self.size() or index < 0:
            index = 0
        return self.colors(index)

    def add(self, color):
        self.colors.append(color)

    def add_rgb(self, r, g, b):
        self.add(rgb(r, g, b))

    def add_rgba(self, r, g, b, a):
        self.add(rgba(r, g, b, a))

    def get_random(self):
        index = rand.int_range(0, self.size() - 1)
        return self.get(index)

    def sort(self):
        self.colors = sorted(self.colors, key = lambda color: color.luminance())

