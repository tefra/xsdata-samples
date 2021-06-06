from dataclasses import dataclass
from .route_instruction_version_structure import RouteInstructionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteInstruction(RouteInstructionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
