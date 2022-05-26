import pygame
import pytmx


class Level:

    def __init__(self):
        self.tmx_file = pytmx.util_pygame.load_pygame('assets/levels/lvl1.tmx')
        self.tiles_ground = []
        self.image_ground = {
            "images" : [],
            "coordinates": []
        }
        self.tiles_liquid = {
            "images" : [],
            "coordinates": []
        }
        self.tiles_other = {
            "images" : [],
            "coordinates": []
        }

        self.x = 0
        self.y = 0

    def load_tmx_data(self):

        for obj in self.tmx_file.objects:
            if obj.type == "ground":
                self.tiles_ground.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        layer_id = 0
        for types in self.tmx_file:

            if types.name == "Sol":
                for x, y, gid in self.tmx_file.layers[layer_id]:
                    image = self.tmx_file.get_tile_image(x, y, layer_id)
                    if image:
                        self.image_ground["images"].append(image)
                        self.image_ground["coordinates"].append((x, y))

            elif types.name == "Liquides":
                for x, y, gid in self.tmx_file.layers[layer_id]:
                    image = self.tmx_file.get_tile_image(x, y, layer_id)
                    if image:
                        self.tiles_liquid["images"].append(image)
                        self.tiles_liquid["coordinates"].append((x, y))

            elif types.name == "Autre":
                for x, y, gid in self.tmx_file.layers[layer_id]:
                    image = self.tmx_file.get_tile_image(x, y, layer_id)
                    if image:
                        self.tiles_other["images"].append(image)
                        self.tiles_other["coordinates"].append((x, y))
            layer_id += 1
