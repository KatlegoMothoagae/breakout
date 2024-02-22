import pygame
import os

pygame.init()

def sprite_sheet(size, file_name, pos=(0, 0), output_dir="sprites"):
    """Loads a sprite sheet and saves individual sprites as image files.
    (tuple(num, num), string, tuple(num, num), string -> list)

    This function cuts the given image into pieces(sprites) and saves them as individual image files.
    size is the size in pixels of the sprite. eg. (64, 64) sprite size of 64 pixels, by 64 pixels.
    file_name is the file name that contains the sprite sheet. preferable format is png.
    pos is the starting point on the image. eg. (10, 10) think about it as an offset.
    output_dir is the directory where the individual sprite images will be saved.
    """
    len_sprt_x, len_sprt_y = size  # sprite size
    sprt_rect_x, sprt_rect_y = pos  # where to find first sprite on sheet
    sheet = pygame.image.load(file_name).convert_alpha()  # Load the sheet
    sheet_rect = sheet.get_rect()  # assign a rect of the sheet's size
    sprites = []  # make a list of sprites
    for i in range(0, sheet_rect.height, size[1]):  # rows
        for ii in range(0, sheet_rect.width, size[0]):  # columns
            sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y))  # clip the sprite
            sprite = sheet.subsurface(sheet.get_clip())  # grab the sprite from the clipped area
            sprite_name = f"sprite_{len(sprites)}.png"  # generate sprite name
            sprite_path = os.path.join(output_dir, sprite_name)  # generate sprite path
            pygame.image.save(sprite, sprite_path)  # save the sprite as an image file
            sprites.append(sprite_path)  # append the sprite path to the list
            sprt_rect_x += len_sprt_x  # go to the next sprite on the x axis
        sprt_rect_y += len_sprt_y  # go to the next row (y axis)
        sprt_rect_x = 0  # reset the sprite on the x axis back to 0
    return sprites  # return the list of sprite paths

# Example usage:
# sprite_size = (32, 32)
# sprite_sheet_file = "spritesheet.png"
# sprites = sprite_sheet(sprite_size, sprite_sheet_file)
# print("Sprites saved at:", sprites)


