"""
Confoederatio Helvetica - Graphics Manager
Manages all game graphics, textures, and visual assets.
Uses Pygame for rendering with Pillow-generated Renaissance-style assets.
"""

import os
from typing import Dict, Optional

try:
    import pygame
except ImportError:
    pygame = None


class GraphicsManager:
    """Centralized graphics management with caching and error handling."""
    
    def __init__(self, assets_dir: str = "assets"):
        self.assets_dir = assets_dir
        self.images: Dict[str, object] = {}
        self.fonts: Dict[str, object] = {}
        self.initialized = False
    
    def initialize(self) -> bool:
        """Initialize graphics system."""
        if pygame is None:
            print("Warning: Pygame not available, using fallback graphics")
            return False
        
        try:
            pygame.init()
            self.initialized = True
            print("Graphics initialized successfully")
            return True
        except Exception as e:
            print(f"Error initializing graphics: {e}")
            return False
    
    def load_image(self, path: str, key: Optional[str] = None) -> object:
        """Load and cache an image."""
        if key is None:
            key = path
        
        if key in self.images:
            return self.images[key]
        
        full_path = os.path.join(self.assets_dir, path)
        try:
            if pygame is not None and os.path.exists(full_path):
                img = pygame.image.load(full_path).convert_alpha()
            else:
                # Fallback: create placeholder
                img = self._create_placeholder(64, 64, (200, 180, 150))
            
            self.images[key] = img
            return img
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            img = self._create_placeholder(64, 64, (200, 180, 150))
            self.images[key] = img
            return img
    
    def load_city_icon(self, city_id: str) -> object:
        """Load city icon with fallback."""
        path = f"cities/{city_id}.png"
        key = f"city_{city_id}"
        return self.load_image(path, key)
    
    def load_goods_icon(self, goods_type: str) -> object:
        """Load goods icon with fallback."""
        path = f"goods/{goods_type}.png"
        key = f"goods_{goods_type}"
        return self.load_image(path, key)
    
    def load_troop_icon(self, troop_type: str) -> object:
        """Load troop icon with fallback."""
        path = f"troops/{troop_type}.png"
        key = f"troop_{troop_type}"
        return self.load_image(path, key)
    
    def load_title_screen(self) -> object:
        """Load title screen image."""
        path = "title_screen.png"
        return self.load_image(path, "title")
    
    def load_map_background(self) -> object:
        """Load map background image."""
        path = "map_background.png"
        return self.load_image(path, "map_bg")
    
    def get_font(self, size: int = 16, bold: bool = False) -> object:
        """Get or create a font with caching."""
        key = f"font_{size}_{bold}"
        if key in self.fonts:
            return self.fonts[key]
        
        try:
            if pygame is not None:
                font = pygame.font.Font(None, size)
                if bold:
                    font.set_bold(True)
            else:
                font = None
            
            self.fonts[key] = font
            return font
        except Exception as e:
            print(f"Error loading font: {e}")
            return None
    
    def _create_placeholder(self, width: int, height: int, color) -> object:
        """Create a placeholder image when assets are unavailable."""
        if pygame is not None:
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            surface.fill(color + (255,))
            return surface
        else:
            # Return a simple dict as fallback
            return {"type": "placeholder", "size": (width, height), "color": color}
    
    def render_text(self, text: str, size: int = 16, color=(60, 40, 20)) -> object:
        """Render text to a surface."""
        font = self.get_font(size)
        if pygame is not None and font is not None:
            return font.render(text, True, color)
        else:
            return {"type": "text", "text": text, "size": size, "color": color}
    
    def clear_cache(self) -> None:
        """Clear all cached images and fonts."""
        self.images.clear()
        self.fonts.clear()
    
    def shutdown(self) -> None:
        """Clean up graphics resources."""
        self.clear_cache()
        if pygame is not None and self.initialized:
            pygame.quit()


# Global instance
graphics = GraphicsManager()
