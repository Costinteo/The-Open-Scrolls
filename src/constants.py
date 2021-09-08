# Screen Size and others
WIDTH, HEIGHT = 1280, 720
PADDING = 60
FPS = 60

# Colours and aesthetics
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
NAVY = (10, 10, 80)
FONT = "dejavusans"


# Game related
# unused
MAX_ATTRIBUTES = 3

# class used to draw levels and entities
# its static variables are updated when a level is loaded
class DrawInfo:

    ROWS = 0
    COLS = 0
    X_OFFSET = 0
    Y_OFFSET = 0

    CELL_WIDTH = 0
    CELL_HEIGHT = 0

    ENTITY_WIDTH = 0
    ENTITY_HEIGHT = 0

    @staticmethod
    def update(height, width):
        DrawInfo.ROWS = height
        DrawInfo.COLS = width

        DrawInfo.X_OFFSET = ((WIDTH - PADDING * 2) // DrawInfo.COLS)
        DrawInfo.Y_OFFSET = ((HEIGHT - PADDING * 2) // DrawInfo.ROWS)

        DrawInfo.CELL_WIDTH = DrawInfo.X_OFFSET + 1
        DrawInfo.CELL_HEIGHT = DrawInfo.Y_OFFSET + 1

        # 10 represents how many pixels smaller the entity is
        # compared to a cell (static tiles)
        DrawInfo.ENTITY_WIDTH = DrawInfo.X_OFFSET - 10
        DrawInfo.ENTITY_HEIGHT = DrawInfo.Y_OFFSET - 10
