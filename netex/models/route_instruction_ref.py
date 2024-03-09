from dataclasses import dataclass

from .route_instruction_ref_structure import RouteInstructionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteInstructionRef(RouteInstructionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
