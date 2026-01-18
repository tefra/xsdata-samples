from __future__ import annotations

from dataclasses import dataclass

from .validity_parameter_assignment_ref_structure import (
    ValidityParameterAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecificParameterAssignmentRefStructure(
    ValidityParameterAssignmentRefStructure
):
    pass
