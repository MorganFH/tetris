class Tetromino:
    # Abstract base class?

    def __init__(self) -> None:
        self.piece_type = None
        self.orientations = []
        self.current_orientation = None
