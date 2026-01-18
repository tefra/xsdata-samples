from __future__ import annotations

from dataclasses import dataclass, field

from .rte_event_in_ecu_instance_ref import RteEventInEcuInstanceRef
from .variable_access_in_ecu_instance_ref import VariableAccessInEcuInstanceRef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McDataAccessDetails:
    """
    This meta-class allows to attach detailed information about the usage
    of a data buffer by the RTE to a corresponding McDataInstance.

    Use Case: Direct memory access to RTE internal buffers for rapid
    prototyping. In case of implicit communication, the various task local
    buffers need to be identified in relation to RTE events and variable
    access points. Note that the SwComponentPrototype, the RunnableEntity
    and the VariableDataPrototype are implicitly given be the referred
    instances of RTEEvent and VariableAccess.

    :ivar rte_event_irefs: The RTE event used to receive the data via
        this buffer.
    :ivar variable_access_irefs: The VariableAccess for which the data
        buffer is used.
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
        name = "MC-DATA-ACCESS-DETAILS"

    rte_event_irefs: None | McDataAccessDetails.RteEventIrefs = field(
        default=None,
        metadata={
            "name": "RTE-EVENT-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variable_access_irefs: None | McDataAccessDetails.VariableAccessIrefs = (
        field(
            default=None,
            metadata={
                "name": "VARIABLE-ACCESS-IREFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class RteEventIrefs:
        rte_event_iref: list[RteEventInEcuInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "RTE-EVENT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class VariableAccessIrefs:
        variable_access_iref: list[VariableAccessInEcuInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
