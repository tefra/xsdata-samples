from dataclasses import dataclass

from .usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameterRef(UsageParameterRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
