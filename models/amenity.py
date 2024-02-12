from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize Amenity class."""
        super().__init__(*args, **kwargs)
        self.name = ""
