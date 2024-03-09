from dataclasses import dataclass

from .connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultConnectionRefStructure(ConnectionRefStructure):
    pass
