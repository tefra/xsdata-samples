from dataclasses import dataclass, field
from typing import Optional
from autosar.models.integer import Integer
from autosar.models.lin_error_response import LinErrorResponse
from autosar.models.lin_slave_config_ident import LinSlaveConfigIdent
from autosar.models.lin_slave_subtypes_enum import LinSlaveSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref
from autosar.models.string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinSlaveConfig:
    """Node attributes of LIN slaves that are handled by the LinMaster.

    In the System Description LIN slaves may be described in the context of the Lin Master.

    In an ECU Extract of the LinMaster the LinSlave Ecus shall not be available.

    The information that is described here is necessary in the ECU Extract for the configuration of the LinMaster.

    The values of attributes of LinSlaveConfig and the corresponding LinSlave shall be identical (if both are defined in a System Description).

    :ivar configured_nad: To distinguish LIN slaves that are used twice
        or more within the same cluster.
    :ivar function_id: LIN function ID.
    :ivar ident: This adds the ability to become referrable to
        LinSlaveConfig.
    :ivar initial_nad: Initial NAD of the LIN slave.
    :ivar lin_error_response: Each slave node shall publish one response
        error in one of its transmitted unconditional frames.
    :ivar lin_slave_ecu_ref: Reference to the LinSlaveEcu.
    :ivar protocol_version: Version specifier for a communication
        protocol. Protocol version of the LinMaster and the LinSlaves
        may be different.
    :ivar supplier_id: LIN Supplier ID.
    :ivar variant_id: Specifies the Variant ID.
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
        name = "LIN-SLAVE-CONFIG"

    configured_nad: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "CONFIGURED-NAD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    function_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FUNCTION-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ident: Optional[LinSlaveConfigIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    initial_nad: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "INITIAL-NAD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    lin_error_response: Optional[LinErrorResponse] = field(
        default=None,
        metadata={
            "name": "LIN-ERROR-RESPONSE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    lin_slave_ecu_ref: Optional["LinSlaveConfig.LinSlaveEcuRef"] = field(
        default=None,
        metadata={
            "name": "LIN-SLAVE-ECU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    protocol_version: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    supplier_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SUPPLIER-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variant_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "VARIANT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class LinSlaveEcuRef(Ref):
        dest: Optional[LinSlaveSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
