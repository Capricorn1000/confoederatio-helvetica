"""
Confoederatio Helvetica - Performance & Caching Tests
Tests for LRU cache, memoization, resource pooling, and serialization.
"""

import unittest
import time
from src.utils.performance import (
    LRUCache,
    memoize,
    ResourcePool,
    GameTimer,
    EfficientSerializer,
)


class TestLRUCache(unittest.TestCase):
    """Test LRU cache implementation."""
    
    def test_basic_operations(self):
        cache = LRUCache(max_size=3)
        cache.set("a", 1)
        cache.set("b", 2)
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
    
    def test_eviction(self):
        cache = LRUCache(max_size=3)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        # Access 'a' to make it recently used
        cache.get("a")
        # Add new item, should evict 'b'
        cache.set("d", 4)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("c"), 3)
        self.assertEqual(cache.get("d"), 4)
    
    def test_clear(self):
        cache = LRUCache(max_size=3)
        cache.set("a", 1)
        cache.clear()
        self.assertIsNone(cache.get("a"))
        self.assertEqual(len(cache), 0)


class TestMemoize(unittest.TestCase):
    """Test memoization decorator."""
    
    def test_caching(self):
        call_count = [0]
        
        @memoize(max_size=10)
        def expensive_calc(x, y):
            call_count[0] += 1
            return x + y
        
        result1 = expensive_calc(2, 3)
        result2 = expensive_calc(2, 3)  # Should use cache
        self.assertEqual(result1, 5)
        self.assertEqual(result2, 5)
        self.assertEqual(call_count[0], 1)  # Only called once
    
    def test_different_args(self):
        call_count = [0]
        
        @memoize(max_size=10)
        def calc(x):
            call_count[0] += 1
            return x * 2
        
        calc(5)
        calc(10)
        self.assertEqual(call_count[0], 2)  # Called twice for different args
    
    def test_cache_clear(self):
        call_count = [0]
        
        @memoize(max_size=10)
        def calc(x):
            call_count[0] += 1
            return x * 2
        
        calc(5)
        calc.cache_clear()
        calc(5)  # Should call again after clear
        self.assertEqual(call_count[0], 2)


class TestResourcePool(unittest.TestCase):
    """Test resource pooling."""
    
    def test_acquire_release(self):
        pool = ResourcePool(lambda: {"value": 1}, max_size=5)
        obj = pool.acquire()
        self.assertIsNotNone(obj)
        pool.release(obj)
    
    def test_reuse(self):
        objects_created = [0]
        
        def factory():
            objects_created[0] += 1
            return {"id": objects_created[0]}
        
        pool = ResourcePool(factory, max_size=5)
        obj1 = pool.acquire()
        pool.release(obj1)
        obj2 = pool.acquire()  # Should reuse obj1
        self.assertEqual(objects_created[0], 1)  # Only one object created
    
    def test_max_size(self):
        pool = ResourcePool(lambda: {}, max_size=3)
        for i in range(5):
            obj = pool.acquire()
            pool.release(obj)
        self.assertLessEqual(len(pool.pool), 3)


class TestEfficientSerializer(unittest.TestCase):
    """Test efficient serialization."""
    
    def test_roundtrip(self):
        data = {"year": 1500, "cities": ["Zürich", "Basel"]}
        serialized = EfficientSerializer.serialize(data)
        deserialized = EfficientSerializer.deserialize(serialized)
        self.assertEqual(data, deserialized)
    
    def test_compact_format(self):
        data = {"a": 1, "b": 2}
        serialized = EfficientSerializer.serialize(data)
        # Should not have extra spaces
        self.assertNotIn(b' ', serialized)
        self.assertNotIn(b': ', serialized)


class TestGameTimer(unittest.TestCase):
    """Test game timer."""
    
    def test_time_ms(self):
        t = GameTimer.time_ms()
        self.assertIsInstance(t, float)
        self.assertGreater(t, 0)
    
    def test_benchmark(self):
        def slow_func():
            time.sleep(0.01)
            return "done"
        
        result, elapsed = GameTimer.benchmark(slow_func)
        self.assertEqual(result, "done")
        self.assertGreater(elapsed, 5)  # At least 5ms


if __name__ == '__main__':
    unittest.main()
