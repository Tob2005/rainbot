# Stubs for bson.dbref (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Mapping, Optional

from bson.son import SON

class DBRef:
    def __init__(
        self,
        collection: str,
        id: Any, database: Optional[str] = ...,
        _extra: Mapping[str, Any] = ...,
        **kwargs: Any) -> None: ...
    @property
    def collection(self) -> str: ...
    @property
    def id(self) -> Any: ...
    @property
    def database(self) -> Optional[str]: ...
    def __getattr__(self, key: str) -> Any: ...
    def as_doc(self) -> SON[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __deepcopy__(self, memo: Any) -> DBRef: ...