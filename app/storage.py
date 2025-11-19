"""
app/storage.py
--------------
Purpose:
    Provide a consistent interface for storing and retrieving state.

Sprint 1 Goals:
    - You DO NOT implement real storage.
    - Provide an in-memory placeholder class for future integration.
    - Keep method signatures minimal so later sprints can expand on them.
"""


class InMemoryStorage:
    """
    Simple dictionary-based storage for Sprint 1.

    Usage:
        storage = InMemoryStorage()
        storage.save("last_query", {"query": "Hello"})
        result = storage.load("last_query")

    """

    def __init__(self):
        # TODO:
        #   - initialize a simple internal dictionary
        #   - consider adding a 'demo_mode' flag for consistent behavior
        self.demo_mode: bool
        self.internal_dict: dict

    def save(self, key: str, value: dict):
        """
        Save arbitrary value under a string key.

        Args:
            key: Unique identifier name.
            value: Any JSON-serializable Python object.

        TODO:
            - store value in internal dictionary
        """
        if self.demo_mode:
            self.internal_dict[key] = value

    def load(self, key: str):
        """
        Retrieve stored object.

        Args:
            key: Key used during save().

        TODO:
            - return the value if it exists
            - return None (or raise KeyError) if it doesn’t
        """
        if self.demo_mode:
            return self.internal_dict[key]

    def clear(self):
        """
        Remove all stored values.

        TODO:
            - reset internal dictionary to empty
        """
        if self.demo_mode:
            self.internal_dict.clear


# --- Future Notes ---------------------------------------------------------
# In Sprint 2+ you will implement:
#
#   class RedisStorage(...)
#   class SQLiteStorage(...)
#
# with methods like:
#   - save_plan(session_id, plan)
#   - load_plan(session_id)
#   - append_result(...)
#
# Sprint 1 intentionally avoids all of this.
