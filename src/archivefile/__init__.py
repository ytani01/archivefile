#
# (c) 2025 Yoichi Tanibayashi
#
from importlib.metadata import version

from .archivefiles import ArchiveFiles

if __package__:
    __version__ = version(__package__)
else:
    __version__ = "_._._"

__all__ = [
    "__version__",
    "ArchiveFiles",
]
