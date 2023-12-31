from dataclasses import dataclass
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RentalOptionVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "RentalOption_VersionStructure"
