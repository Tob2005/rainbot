from typing import Callable, Dict, List, Mapping, NamedTuple, Optional, Tuple, Union

from pymongo.read_preferences import _ServerMode
from pymongo.server import Server
from pymongo.server_description import ServerDescription
from pymongo.server_selectors import Selection
from pymongo.settings import TopologySettings


TopologyType = NamedTuple('TopologyType', [
    ('Single', int),
    ('ReplicaSetNoPrimary', int),
    ('ReplicaSetWithPrimary', int),
    ('Sharded', int),
    ('Unknown', int),
])
TOPOLOGY_TYPE: TopologyType = ...

class TopologyDescription(object):
    def __init__(
        self,
        topology_type: int,
        server_descriptions: Mapping[Tuple[str, int],
        ServerDescription],
        replica_set_name: Optional[str],
        max_set_version: Optional[int],
        max_election_id: Optional[int],
        topology_settings: TopologySettings) -> None: ...
    def check_compatible(self) -> None: ...
    def has_server(self, address: Tuple[str, int]) -> bool: ...
    def reset_server(self, address: Tuple[str, int]) -> 'TopologyDescription': ...
    def reset(self) -> 'TopologyDescription': ...
    def server_descriptions(self) -> Dict[Tuple[str, int], ServerDescription]: ...
    @property
    def topology_type(self) -> int: ...
    @property
    def topology_type_name(self) -> str: ...
    @property
    def replica_set_name(self) -> str: ...
    @property
    def max_set_version(self) -> int: ...
    @property
    def max_election_id(self) -> int: ...
    @property
    def known_servers(self) -> List[Server]: ...
    @property
    def common_wire_version(self) -> Optional[int]: ...
    @property
    def heartbeat_frequency(self) -> int: ...
    def apply_selector(
        self,
        selector: Union[Selection, Callable[[Selection], Selection], _ServerMode],
        address: Tuple[str, int]) -> List[ServerDescription]: ...
    def has_readable_server(self, read_preference: _ServerMode = ...) -> bool: ...
    def has_writable_server(self) -> bool: ...

def updated_topology_description(
    topology_description: TopologyDescription,
    server_description: ServerDescription) -> TopologyDescription: ...