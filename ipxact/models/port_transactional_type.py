from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.bus_width import BusWidth
from ipxact.models.initiative import Initiative
from ipxact.models.kind import Kind
from ipxact.models.protocol import Protocol
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.trans_type_defs import TransTypeDefs
from ipxact.models.transactional_power_constraint_type import (
    TransactionalPowerConstraintType,
)
from ipxact.models.unsigned_int_expression import UnsignedIntExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PortTransactionalType:
    """
    Transactional port type.

    :ivar initiative: Defines how the port accesses this service.
    :ivar kind: Define the kind of transactional port
    :ivar bus_width: Defines the bus width in bits.This can be the
        result of an expression.
    :ivar qualifier: The type of information this port carries A
        transactional port can carry both address and data information.
    :ivar protocol: Defines the protocol type. Defaults to
        tlm_base_protocol_type for TLM sockets
    :ivar trans_type_defs: Definition of the port type expressed in the
        default language for this port (i.e. SystemC or SystemV).
    :ivar connection: Bounds number of legal connections.
    :ivar power_constraints: Wire port power constraints.
    :ivar all_logical_initiatives_allowed: True if logical ports with
        different initiatives from the physical port initiative may be
        mapped onto this port. Forbidden for phantom ports, which always
        allow logical ports with all initiatives value to be mapped onto
        the physical port. Also ignored for "both" ports, since any
        logical port may be mapped to a physical "both" port.
    """

    class Meta:
        name = "portTransactionalType"

    initiative: Initiative | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    kind: Kind | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bus_width: BusWidth | None = field(
        default=None,
        metadata={
            "name": "busWidth",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    qualifier: QualifierType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    protocol: Protocol | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    trans_type_defs: TransTypeDefs | None = field(
        default=None,
        metadata={
            "name": "transTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    connection: PortTransactionalType.Connection | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    power_constraints: PortTransactionalType.PowerConstraints | None = field(
        default=None,
        metadata={
            "name": "powerConstraints",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    all_logical_initiatives_allowed: bool = field(
        default=False,
        metadata={
            "name": "allLogicalInitiativesAllowed",
            "type": "Attribute",
        },
    )

    @dataclass
    class Connection:
        """
        :ivar max_connections: Indicates the maximum number of
            connections this port supports. If this element is not
            present or set to 0 it implies an unbounded number of
            allowed connections.
        :ivar min_connections: Indicates the minimum number of
            connections this port supports. If this element is not
            present, the minimum number of allowed connections is 1.
        """

        max_connections: UnsignedIntExpression | None = field(
            default=None,
            metadata={
                "name": "maxConnections",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        min_connections: UnsignedIntExpression | None = field(
            default=None,
            metadata={
                "name": "minConnections",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

    @dataclass
    class PowerConstraints:
        """
        :ivar power_constraint: Single wire port set of power
            constraints.
        """

        power_constraint: list[TransactionalPowerConstraintType] = field(
            default_factory=list,
            metadata={
                "name": "powerConstraint",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )
