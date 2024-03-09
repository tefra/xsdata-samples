from dataclasses import dataclass

from .conventional_mode_of_operation_ref_structure import (
    ConventionalModeOfOperationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConventionalModeOfOperationRef(ConventionalModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
