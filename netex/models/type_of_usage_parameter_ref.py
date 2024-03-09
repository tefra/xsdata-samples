from dataclasses import dataclass

from .type_of_usage_parameter_ref_structure import (
    TypeOfUsageParameterRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfUsageParameterRef(TypeOfUsageParameterRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
