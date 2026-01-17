from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.delay_value_type import DelayValueType
from ipxact.models.edge_value_type import EdgeValueType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class TimingConstraint:
    """
    Defines a timing constraint for the associated port.

    The constraint is relative to the clock specified by the clockName
    attribute. The clockEdge indicates which clock edge the constraint is
    associated with (default is rising edge). The delayType attribute can
    be specified to further refine the constraint.

    :ivar value:
    :ivar clock_edge: Indicates the clock edge that a timing constraint
        is relative to.
    :ivar delay_type: Indicates the type of delay in a timing constraint
        - minimum or maximum.
    :ivar clock_name: Indicates the name of the clock to which this
        constraint applies.
    :ivar id:
    """

    class Meta:
        name = "timingConstraint"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        },
    )
    clock_edge: Optional[EdgeValueType] = field(
        default=None,
        metadata={
            "name": "clockEdge",
            "type": "Attribute",
        },
    )
    delay_type: Optional[DelayValueType] = field(
        default=None,
        metadata={
            "name": "delayType",
            "type": "Attribute",
        },
    )
    clock_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "clockName",
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
