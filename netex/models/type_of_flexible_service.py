from dataclasses import dataclass
from .type_of_flexible_service_value_structure import (
    TypeOfFlexibleServiceValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFlexibleService(TypeOfFlexibleServiceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
