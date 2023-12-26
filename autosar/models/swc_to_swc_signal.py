from dataclasses import dataclass, field
from typing import List, Optional
from .variable_data_prototype_in_system_instance_ref import (
    VariableDataPrototypeInSystemInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcToSwcSignal:
    """The SwcToSwcSignal describes the information (data element) that is
    exchanged between two SW Components.

    On the SWC Level it is possible that a SW Component sends one data
    element from one P-Port to two different SW Components (1:n
    Communication). The SwcToSwcSignal describes exactly the information
    which is exchanged between one P-Port of a SW Component and one
    R-Port of another SW Component.

    :ivar data_element_irefs: Reference to a data element on the
        PPortPrototype and to the same data element on the
        RPortPrototype.
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
        name = "SWC-TO-SWC-SIGNAL"

    data_element_irefs: Optional["SwcToSwcSignal.DataElementIrefs"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-IREFS",
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

    @dataclass
    class DataElementIrefs:
        data_element_iref: List[
            VariableDataPrototypeInSystemInstanceRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-ELEMENT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            },
        )
