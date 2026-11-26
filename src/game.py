"""
Confoederatio Helvetica - Main Game Loop
Optimized for long sessions (50+ years) with efficient resource management.
Includes caching, incremental updates, and memory leak prevention.
"""

import time
from typing import Dict, List, Optional

from src.game_state import GameState
from src.utils.performance import (
    memoize,
    GameTimer,
    clear_all_caches,
    price_cache,
    troop_strength_cache,
)
from src.utils.graphics_manager import graphics


class Game:
    """Main game controller with optimized loop."""
    
    def __init__(self):
        self.state = GameState()
        self.running = False
        self.paused = False
        self.last_frame_time = 0
        self.frame_count = 0
        self.fps = 60
        self.target_fps = 30  # Lower target for strategy game
        
        # Performance tracking
        self.stats = {
            "total_frames": 0,
            "avg_frame_time_ms": 0.0,
            "cache_hits": 0,
            "cache_misses": 0,
        }
    
    def initialize(self) -> bool:
        """Initialize all game systems."""
        print("Initializing Confoederatio Helvetica...")
        
        # Initialize graphics
        if not graphics.initialize():
            print("Warning: Graphics initialization failed")
        
        # Load assets
        self._load_assets()
        
        # Reset performance stats
        clear_all_caches()
        self.stats = {
            "total_frames": 0,
            "avg_frame_time_ms": 0.0,
            "cache_hits": 0,
            "cache_misses": 0,
        }
        
        print("Game initialized successfully")
        return True
    
    def _load_assets(self) -> None:
        """Pre-load all game assets for better performance."""
        print("Loading game assets...")
        
        # Load city icons
        for city_id in ["zuerich", "basel", "geneva", "bern", "luzern"]:
            graphics.load_city_icon(city_id)
        
        # Load goods icons
        for goods_type in ["grain", "wine", "cheese", "wool", "iron", "silver"]:
            graphics.load_goods_icon(goods_type)
        
        # Load troop icons
        for troop_type in ["halberdier", "crossbowman", "cavalry"]:
            graphics.load_troop_icon(troop_type)
        
        # Load backgrounds
        graphics.load_title_screen()
        graphics.load_map_background()
        
        print("Assets loaded")
    
    def run(self) -> None:
        """Main game loop with performance optimization."""
        self.running = True
        clock_start = time.time()
        frame_times = []
        
        while self.running:
            frame_start = GameTimer.time_ms()
            
            # Handle events
            self._handle_events()
            
            # Update game state (only if not paused)
            if not self.paused:
                self._update()
            
            # Render
            self._render()
            
            # Performance tracking
            frame_end = GameTimer.time_ms()
            frame_time = frame_end - frame_start
            frame_times.append(frame_time)
            
            # Keep only last 60 frame times for average
            if len(frame_times) > 60:
                frame_times.pop(0)
            
            self.stats["total_frames"] += 1
            self.stats["avg_frame_time_ms"] = sum(frame_times) / len(frame_times)
            
            # Maintain target FPS
            elapsed = time.time() - clock_start
            expected = (self.frame_count + 1) / self.target_fps
            if elapsed < expected:
                time.sleep(expected - elapsed)
            
            self.frame_count += 1
        
        print(f"Game ended. Total frames: {self.stats['total_frames']}")
    
    def _handle_events(self) -> None:
        """Process input events."""
        try:
            import pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_p:
                        self.paused = not self.paused
        except ImportError:
            pass  # No Pygame, skip event handling
    
    def _update(self) -> None:
        """Update game state with optimized calculations."""
        # Update economy (uses cached price calculations)
        if hasattr(self.state, 'economy') and self.state.economy is not None:
            self.state.economy.update()
        
        # Update military
        if hasattr(self.state, 'military') and self.state.military is not None:
            self.state.military.update()
        
        # Check for events
        if hasattr(self.state, 'events') and self.state.events is not None:
            self.state.events.check_events()
    
    def _render(self) -> None:
        """Render game with efficient drawing."""
        try:
            import pygame
            screen = pygame.display.get_surface()
            if screen is None:
                return
            
            # Clear screen
            screen.fill((245, 230, 195))  # Parchment color
            
            # Draw game elements based on current state
            self._draw_game_elements(screen)
            
            pygame.display.flip()
        except ImportError:
            pass  # No Pygame, skip rendering
    
    def _draw_game_elements(self, screen) -> None:
        """Draw all game elements efficiently."""
        try:
            import pygame
            
            # Draw map background
            map_bg = graphics.load_map_background()
            if hasattr(map_bg, 'get_width'):
                screen.blit(map_bg, (0, 0))
            
            # Draw cities
            for city in self.state.cities.values():
                icon = graphics.load_city_icon(city.id)
                if hasattr(icon, 'get_width'):
                    screen.blit(icon, (city.x - 32, city.y - 32))
            
            # Draw UI overlay
            font = graphics.get_font(16)
            if font is not None:
                year_text = font.render(f"Year: {self.state.year}", True, (60, 40, 20))
                screen.blit(year_text, (10, 10))
        except ImportError:
            pass
    
    @memoize(max_size=512)
    def calculate_trade_price(self, goods_type: str, from_city: str, to_city: str) -> float:
        """Calculate trade price with caching for performance."""
        base_prices = {
            "grain": 10,
            "wine": 25,
            "cheese": 15,
            "wool": 20,
            "iron": 30,
            "silver": 50,
        }
        
        base = base_prices.get(goods_type, 10)
        # Distance factor (simplified)
        distance_factor = 1.0 + abs(hash(from_city) - hash(to_city)) % 100 / 1000.0
        return round(base * distance_factor, 2)
    
    @memoize(max_size=256)
    def calculate_troop_strength(self, troop_type: str, count: int) -> int:
        """Calculate troop combat strength with caching."""
        strengths = {
            "halberdier": 10,
            "crossbowman": 8,
            "cavalry": 15,
        }
        base = strengths.get(troop_type, 10)
        return base * count
    
    def save_game(self, filename: str) -> bool:
        """Save game state efficiently."""
        try:
            from src.utils.save_load import save_game as sl_save
            return sl_save(self.state, filename)
        except Exception as e:
            print(f"Error saving game: {e}")
            return False
    
    def load_game(self, filename: str) -> bool:
        """Load game state efficiently."""
        try:
            from src.utils.save_load import load_game as sl_load
            loaded_state = sl_load(filename)
            if loaded_state is not None:
                self.state = loaded_state
                # Clear caches after loading (state has changed)
                clear_all_caches()
                return True
            return False
        except Exception as e:
            print(f"Error loading game: {e}")
            return False
    
    def shutdown(self) -> None:
        """Clean up all resources."""
        print("Shutting down game...")
        graphics.shutdown()
        clear_all_caches()
        self.running = False
