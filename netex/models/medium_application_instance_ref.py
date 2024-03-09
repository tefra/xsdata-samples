from dataclasses import dataclass

from .medium_application_instance_ref_structure import (
    MediumApplicationInstanceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumApplicationInstanceRef(MediumApplicationInstanceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
