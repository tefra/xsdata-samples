from dataclasses import dataclass, field

from ipxact.models.constraint_set import ConstraintSet

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ConstraintSets:
    """
    List of constraintSet elements for a component port.
    """

    class Meta:
        name = "constraintSets"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    constraint_set: list[ConstraintSet] = field(
        default_factory=list,
        metadata={
            "name": "constraintSet",
            "type": "Element",
            "min_occurs": 1,
        },
    )
