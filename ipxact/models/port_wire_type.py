from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.component_port_direction_type import (
    ComponentPortDirectionType,
)
from ipxact.models.constraint_sets import ConstraintSets
from ipxact.models.domain_type_defs import DomainTypeDefs
from ipxact.models.drivers import Drivers
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.signal_type_defs import SignalTypeDefs
from ipxact.models.wire_power_constraint_type import WirePowerConstraintType
from ipxact.models.wire_type_defs import WireTypeDefs

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PortWireType:
    """
    Wire port type for a component.

    :ivar direction: The direction of a wire style port. The basic
        directions for a port are 'in' for input ports, 'out' for output
        port and 'inout' for bidirectional and tristate ports. A value
        of 'phantom' is also allowed and define a port that exist on the
        IP-XACT component but not on the HDL model.
    :ivar qualifier: The type of information this port carries a wire
        port can carry both address and data, but may not mix this with
        a clock or reset.
    :ivar vectors: Vectored information.
    :ivar wire_type_defs:
    :ivar domain_type_defs:
    :ivar signal_type_defs:
    :ivar drivers:
    :ivar constraint_sets:
    :ivar power_constraints: Wire port power constraints.
    :ivar all_logical_directions_allowed: True if logical ports with
        different directions from the physical port direction may be
        mapped onto this port. Forbidden for phantom ports, which always
        allow logical ports with all direction value to be mapped onto
        the physical port. Also ignored for inout ports, since any
        logical port maybe mapped to a physical inout port.
    """

    class Meta:
        name = "portWireType"

    direction: ComponentPortDirectionType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    qualifier: QualifierType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vectors: ExtendedVectorsType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    wire_type_defs: WireTypeDefs | None = field(
        default=None,
        metadata={
            "name": "wireTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    domain_type_defs: DomainTypeDefs | None = field(
        default=None,
        metadata={
            "name": "domainTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    signal_type_defs: SignalTypeDefs | None = field(
        default=None,
        metadata={
            "name": "signalTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    drivers: Drivers | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    constraint_sets: ConstraintSets | None = field(
        default=None,
        metadata={
            "name": "constraintSets",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    power_constraints: PortWireType.PowerConstraints | None = field(
        default=None,
        metadata={
            "name": "powerConstraints",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    all_logical_directions_allowed: bool = field(
        default=False,
        metadata={
            "name": "allLogicalDirectionsAllowed",
            "type": "Attribute",
        },
    )

    @dataclass
    class PowerConstraints:
        """
        :ivar power_constraint: Single wire port set of power
            constraints.
        """

        power_constraint: list[WirePowerConstraintType] = field(
            default_factory=list,
            metadata={
                "name": "powerConstraint",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )
