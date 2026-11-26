"""
Confoederatio Helvetica - Save/Load System
Optimized for large game states (50+ years of gameplay).
Uses efficient JSON serialization with compression support.
"""

import json
import os
import gzip
from typing import Any, Dict, Optional


def save_game(state: Any, filename: str) -> bool:
    """Save game state to file with optimization."""
    try:
        # Convert state to serializable dict
        data = _serialize_state(state)
        
        # Use gzip compression for large saves
        if filename.endswith('.gz'):
            with gzip.open(filename, 'wt', encoding='utf-8') as f:
                json.dump(data, f, separators=(',', ':'))
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, separators=(',', ':'))
        
        print(f"Game saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False


def load_game(filename: str) -> Optional[Any]:
    """Load game state from file."""
    try:
        if not os.path.exists(filename):
            print(f"Save file not found: {filename}")
            return None
        
        # Detect compression
        if filename.endswith('.gz'):
            with gzip.open(filename, 'rt', encoding='utf-8') as f:
                data = json.load(f)
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        
        # Reconstruct state
        state = _deserialize_state(data)
        print(f"Game loaded from {filename}")
        return state
    except Exception as e:
        print(f"Error loading game: {e}")
        return None


def list_saves(directory: str = "saves") -> list:
    """List all save files."""
    try:
        if not os.path.exists(directory):
            return []
        
        saves = []
        for filename in os.listdir(directory):
            if filename.endswith('.json') or filename.endswith('.gz'):
                filepath = os.path.join(directory, filename)
                save_time = os.path.getmtime(filepath)
                saves.append({
                    "filename": filename,
                    "path": filepath,
                    "timestamp": save_time
                })
        
        # Sort by timestamp (newest first)
        saves.sort(key=lambda x: x["timestamp"], reverse=True)
        return saves
    except Exception as e:
        print(f"Error listing saves: {e}")
        return []


def delete_save(filename: str) -> bool:
    """Delete a save file."""
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Save deleted: {filename}")
            return True
        return False
    except Exception as e:
        print(f"Error deleting save: {e}")
        return False


def _serialize_state(state) -> Dict:
    """Convert game state to serializable dictionary."""
    # Handle GameState object
    if hasattr(state, '__dict__'):
        data = {}
        for key, value in state.__dict__.items():
            if not key.startswith('_'):
                data[key] = _serialize_value(value)
        return data
    
    return _serialize_value(state)


def _serialize_value(value) -> Any:
    """Serialize a single value."""
    if isinstance(value, dict):
        return {k: _serialize_value(v) for k, v in value.items()}
    elif isinstance(value, (list, tuple)):
        return [_serialize_value(item) for item in value]
    elif hasattr(value, '__dict__'):
        # Nested object
        data = {}
        for key, val in value.__dict__.items():
            if not key.startswith('_'):
                data[key] = _serialize_value(val)
        return data
    else:
        return value


def _deserialize_state(data: Dict) -> Any:
    """Reconstruct game state from dictionary."""
    # Import GameState here to avoid circular imports
    try:
        from src.game_state import GameState
        
        if isinstance(data, dict):
            # Try to reconstruct as GameState
            if 'year' in data or 'cities' in data:
                state = GameState()
                for key, value in data.items():
                    if hasattr(state, key):
                        setattr(state, key, _deserialize_value(value))
                return state
        
        return _deserialize_value(data)
    except ImportError:
        return _deserialize_value(data)


def _deserialize_value(value) -> Any:
    """Deserialize a single value."""
    if isinstance(value, dict):
        return {k: _deserialize_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [_deserialize_value(item) for item in value]
    else:
        return value
