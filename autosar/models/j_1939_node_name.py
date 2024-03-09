from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class J1939NodeName:
    """
    This element contains attributes to configure the J1939NmNode NAME.

    :ivar arbitrary_address_capable: Arbitrary Address Capable field of
        the NAME of this node.
    :ivar ecu_instance: ECU Instance field of the NAME of this node.
    :ivar function: Function field of the NAME of this node.
    :ivar function_instance: Function Instance field of the NAME of this
        node.
    :ivar identitiy_number: Identity Number field of the NAME of this
        node.
    :ivar industry_group: Industry Group field of the NAME of this node.
    :ivar manufacturer_code: Manufacturer Code field of the NAME of this
        node.
    :ivar vehicle_system: Vehicle System field of the NAME of this node.
    :ivar vehicle_system_instance: Vehicle System Instance field of the
        NAME of this node.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "J-1939-NODE-NAME"

    arbitrary_address_capable: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ARBITRARY-ADDRESS-CAPABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_instance: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    function: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "FUNCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    function_instance: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "FUNCTION-INSTANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    identitiy_number: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "IDENTITIY-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    industry_group: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "INDUSTRY-GROUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    manufacturer_code: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MANUFACTURER-CODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vehicle_system: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "VEHICLE-SYSTEM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vehicle_system_instance: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "VEHICLE-SYSTEM-INSTANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
