"""
Confoederatio Helvetica - Performance Optimization & Caching
Provides memoization, resource management, and efficient serialization.
Optimized for long game sessions (50+ years of gameplay).
"""

import time
import json
import weakref
from functools import wraps
from typing import Any, Callable, Dict, Optional, Tuple


class LRUCache:
    """Least Recently Used cache with configurable size."""
    
    def __init__(self, max_size: int = 128):
        self.max_size = max_size
        self.cache: Dict[Any, Any] = {}
        self.order: list = []
    
    def get(self, key: Any) -> Optional[Any]:
        if key in self.cache:
            # Move to end (most recently used)
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None
    
    def set(self, key: Any, value: Any) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.max_size:
            # Evict least recently used
            lru_key = self.order.pop(0)
            del self.cache[lru_key]
        
        self.cache[key] = value
        self.order.append(key)
    
    def clear(self) -> None:
        self.cache.clear()
        self.order.clear()
    
    def __len__(self) -> int:
        return len(self.cache)


def memoize(max_size: int = 256):
    """Memoization decorator with LRU cache."""
    def decorator(func: Callable) -> Callable:
        cache = LRUCache(max_size)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create hashable key
            key = (args, tuple(sorted(kwargs.items())))
            result = cache.get(key)
            if result is not None:
                return result
            
            result = func(*args, **kwargs)
            cache.set(key, result)
            return result
        
        wrapper.cache_clear = cache.clear
        wrapper.cache_info = lambda: {"size": len(cache)}
        return wrapper
    
    return decorator


class ResourcePool:
    """Object pool for reusing expensive objects."""
    
    def __init__(self, factory: Callable, max_size: int = 50):
        self.factory = factory
        self.max_size = max_size
        self.pool: list = []
        self.in_use: set = set()
    
    def acquire(self) -> Any:
        if self.pool:
            obj = self.pool.pop()
        else:
            obj = self.factory()
        self.in_use.add(id(obj))
        return obj
    
    def release(self, obj: Any) -> None:
        obj_id = id(obj)
        if obj_id in self.in_use:
            self.in_use.discard(obj_id)
            if len(self.pool) < self.max_size:
                self.pool.append(obj)
    
    def clear(self) -> None:
        self.pool.clear()
        self.in_use.clear()


class GameTimer:
    """High-resolution timer for performance measurement."""
    
    @staticmethod
    def time_ms() -> float:
        return time.time() * 1000.0
    
    @staticmethod
    def benchmark(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
        """Measure execution time of a function."""
        start = GameTimer.time_ms()
        result = func(*args, **kwargs)
        elapsed = GameTimer.time_ms() - start
        return result, elapsed


class EfficientSerializer:
    """Optimized serialization for large game states."""
    
    @staticmethod
    def serialize(state: Dict) -> bytes:
        """Serialize game state to compact binary format."""
        # Use JSON with separators for compactness
        return json.dumps(state, separators=(',', ':')).encode('utf-8')
    
    @staticmethod
    def deserialize(data: bytes) -> Dict:
        """Deserialize game state from binary format."""
        return json.loads(data.decode('utf-8'))
    
    @staticmethod
    def serialize_incremental(full_state: Dict, changes: Dict) -> bytes:
        """Serialize only changed portions of state."""
        return EfficientSerializer.serialize(changes)


class MemoryManager:
    """Track and manage memory usage for long sessions."""
    
    def __init__(self):
        self.allocated: Dict[str, Any] = {}
        self.total_bytes = 0
    
    def register(self, name: str, obj: Any) -> None:
        """Register an object for memory tracking."""
        self.allocated[name] = weakref.ref(obj)
    
    def unregister(self, name: str) -> None:
        """Unregister an object."""
        if name in self.allocated:
            del self.allocated[name]
    
    def cleanup_dead_refs(self) -> int:
        """Remove references to garbage-collected objects."""
        dead = [name for name, ref in self.allocated.items() if ref() is None]
        for name in dead:
            del self.allocated[name]
        return len(dead)
    
    def get_live_count(self) -> int:
        """Count objects still alive."""
        return sum(1 for ref in self.allocated.values() if ref() is not None)


# Global caches for frequently used calculations
price_cache = LRUCache(max_size=512)
troop_strength_cache = LRUCache(max_size=256)
distance_cache = LRUCache(max_size=128)


def clear_all_caches() -> None:
    """Clear all global caches (useful between game sessions)."""
    price_cache.clear()
    troop_strength_cache.clear()
    distance_cache.clear()
