from dataclasses import dataclass
from .additional_driver_option_version_structure import (
    AdditionalDriverOptionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AdditionalDriverOption(AdditionalDriverOptionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
