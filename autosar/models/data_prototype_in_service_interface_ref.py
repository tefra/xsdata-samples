from dataclasses import dataclass, field

from .data_prototype_in_service_interface_instance_ref import (
    DataPrototypeInServiceInterfaceInstanceRef,
)
from .port_interface_element_in_implementation_datatype_ref import (
    PortInterfaceElementInImplementationDatatypeRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataPrototypeInServiceInterfaceRef:
    """
    This meta-class represents the ability to refer to an AUTOSAR
    DataPrototype in the context of a ServiceInterface.

    :ivar data_prototype_iref: This element represents the ability to: *
        refer to a DataPrototype in the context of a ServiceInterface. *
        refer to the internal structure of a DataPrototype in which is
        typed by an ApplicationDatatype the context of a
        ServiceInterface.
    :ivar element_in_impl_datatype: This element represents the ability
        to refer to the internal structure of an AutosarDataPrototype
        which is typed by an ImplementationDatatype in the context of a
        ServiceInterface.
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
        name = "DATA-PROTOTYPE-IN-SERVICE-INTERFACE-REF"

    data_prototype_iref: DataPrototypeInServiceInterfaceInstanceRef | None = (
        field(
            default=None,
            metadata={
                "name": "DATA-PROTOTYPE-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    element_in_impl_datatype: (
        PortInterfaceElementInImplementationDatatypeRef | None
    ) = field(
        default=None,
        metadata={
            "name": "ELEMENT-IN-IMPL-DATATYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
