"""Content formatter init."""

from abc import ABC, abstractmethod
from typing import List


class ContentFormatter(ABC):
    """Abstract class for content formatter."""

    @abstractmethod
    def format(self, *args, **kwargs) -> List[str]:
        """Abstract method definition."""
        pass
