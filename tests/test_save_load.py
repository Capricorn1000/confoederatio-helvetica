"""
Confoederatio Helvetica - Save/Load Tests
Tests for efficient serialization, compression, and large game states.
"""

import unittest
import os
import json
from src.utils.save_load import (
    save_game,
    load_game,
    list_saves,
    delete_save,
)


class TestSaveLoad(unittest.TestCase):
    """Test save/load functionality."""
    
    def setUp(self):
        self.test_dir = "test_saves"
        os.makedirs(self.test_dir, exist_ok=True)
    
    def tearDown(self):
        # Clean up test saves
        for filename in os.listdir(self.test_dir):
            filepath = os.path.join(self.test_dir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
    
    def test_save_and_load_basic(self):
        """Test basic save and load."""
        state = {"year": 1500, "player_name": "Hans", "wealth": 1000}
        filename = os.path.join(self.test_dir, "test_save.json")
        
        # Save
        result = save_game(state, filename)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(filename))
        
        # Load
        loaded = load_game(filename)
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded["year"], 1500)
        self.assertEqual(loaded["player_name"], "Hans")
    
    def test_compressed_save(self):
        """Test gzip compressed saves."""
        state = {"year": 1550, "cities": ["Zürich", "Basel", "Genf"]}
        filename = os.path.join(self.test_dir, "test_save.gz")
        
        result = save_game(state, filename)
        self.assertTrue(result)
        
        loaded = load_game(filename)
        self.assertIsNotNone(loaded)
        self.assertEqual(len(loaded["cities"]), 3)
    
    def test_large_state(self):
        """Test saving large game state (simulating long session)."""
        # Create a large state with many years of data
        state = {
            "year": 1600,
            "history": [],
            "cities": {},
            "trades": []
        }
        
        # Add 100 years of trade history
        for year in range(1500, 1600):
            state["history"].append({
                "year": year,
                "events": [f"Event {i}" for i in range(10)]
            })
            state["trades"].extend([
                {"from": "Zürich", "to": "Basel", "goods": "grain", "year": year},
                {"from": "Basel", "to": "Genf", "goods": "wine", "year": year}
            ])
        
        filename = os.path.join(self.test_dir, "large_save.json")
        result = save_game(state, filename)
        self.assertTrue(result)
        
        # Verify file is reasonably sized (compression helps)
        file_size = os.path.getsize(filename)
        print(f"Large save size: {file_size} bytes")
        
        loaded = load_game(filename)
        self.assertIsNotNone(loaded)
        self.assertEqual(len(loaded["history"]), 100)
    
    def test_list_saves(self):
        """Test listing save files."""
        # Create some saves
        for i in range(3):
            filename = os.path.join(self.test_dir, f"save_{i}.json")
            save_game({"index": i}, filename)
        
        saves = list_saves(self.test_dir)
        self.assertEqual(len(saves), 3)
    
    def test_delete_save(self):
        """Test deleting a save file."""
        filename = os.path.join(self.test_dir, "to_delete.json")
        save_game({"test": True}, filename)
        
        result = delete_save(filename)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(filename))


if __name__ == '__main__':
    unittest.main()
