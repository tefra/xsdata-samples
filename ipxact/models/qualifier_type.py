from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.is_clock_en_level import IsClockEnLevel
from ipxact.models.is_flow_control_flow_type import IsFlowControlFlowType
from ipxact.models.is_power_en_level import IsPowerEnLevel
from ipxact.models.is_reset_level import IsResetLevel

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class QualifierType:
    """
    :ivar is_address: If this element is present, the port contains
        address information.
    :ivar is_data: If this element is present, the port contains data
        information.
    :ivar is_clock: If this element is present, the port contains only
        clock information.
    :ivar is_reset: If this element is present, the port contains only
        reset information.
    :ivar is_valid: If this element is present, the port signifies that
        the data on the interface is currently valid
    :ivar is_interrupt: If this element is present, the port contains
        only interrupt information.
    :ivar is_clock_en: If this element is present, the port indicates
        that an associated conditional clock should be turned on.
    :ivar is_power_en: If this element is present, the port indicates
        that an associated power domain should be activated.
    :ivar is_opcode: If this element is present, the port determines the
        interpretation of other signals in the interface.
    :ivar is_protection: If this element is present, the port implements
        a protection signal.
    :ivar is_flow_control: If this element is present, the port is used
        by the interface’s flow control mechanism.
    :ivar is_user: If this element is present, the port is used for user
        defined behavior.
    :ivar is_request: If this element is present, the port implements a
        request signal.
    :ivar is_response: If this element is present, the port implements a
        response signal.
    :ivar id:
    """

    class Meta:
        name = "qualifierType"

    is_address: bool | None = field(
        default=None,
        metadata={
            "name": "isAddress",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_data: bool | None = field(
        default=None,
        metadata={
            "name": "isData",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_clock: bool | None = field(
        default=None,
        metadata={
            "name": "isClock",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_reset: QualifierType.IsReset | None = field(
        default=None,
        metadata={
            "name": "isReset",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_valid: bool | None = field(
        default=None,
        metadata={
            "name": "isValid",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_interrupt: bool | None = field(
        default=None,
        metadata={
            "name": "isInterrupt",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_clock_en: QualifierType.IsClockEn | None = field(
        default=None,
        metadata={
            "name": "isClockEn",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_power_en: QualifierType.IsPowerEn | None = field(
        default=None,
        metadata={
            "name": "isPowerEn",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_opcode: bool | None = field(
        default=None,
        metadata={
            "name": "isOpcode",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_protection: bool | None = field(
        default=None,
        metadata={
            "name": "isProtection",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_flow_control: QualifierType.IsFlowControl | None = field(
        default=None,
        metadata={
            "name": "isFlowControl",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_user: QualifierType.IsUser | None = field(
        default=None,
        metadata={
            "name": "isUser",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_request: bool | None = field(
        default=None,
        metadata={
            "name": "isRequest",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_response: bool | None = field(
        default=None,
        metadata={
            "name": "isResponse",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class IsReset:
        """
        :ivar value:
        :ivar level: Assertion level
        """

        value: bool | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        level: IsResetLevel | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class IsClockEn:
        """
        :ivar value:
        :ivar level: Assertion level
        """

        value: bool | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        level: IsClockEnLevel | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class IsPowerEn:
        """
        :ivar value:
        :ivar level: Assertion level
        :ivar power_domain_ref: PowerDomain references
        """

        value: bool | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        level: IsPowerEnLevel | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        power_domain_ref: str | None = field(
            default=None,
            metadata={
                "name": "powerDomainRef",
                "type": "Attribute",
            },
        )

    @dataclass
    class IsFlowControl:
        """
        :ivar value:
        :ivar flow_type: Controlled flow type
        :ivar user: User flow type information
        """

        value: bool | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        flow_type: IsFlowControlFlowType | None = field(
            default=None,
            metadata={
                "name": "flowType",
                "type": "Attribute",
            },
        )
        user: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class IsUser:
        """
        :ivar value:
        :ivar user: User behaviour
        """

        value: bool | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        user: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
