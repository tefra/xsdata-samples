from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataTypePolicyEnumSimple(Enum):
    """
    :cvar LEGACY: In case the System Description doesn't use a complete
        Software Component Description (VFB View) this value can be
        chosen. This supports the inclusion of legacy signals. The
        aggregation of SwDataDefProps shall be used to configure the
        "ComSignalDataInvalidValue" and the Data Semantics.
    :cvar NETWORK_REPRESENTATION_FROM_COM_SPEC: Ignore any
        networkRepresentationProps of this ISignal and use the
        networkRepresentation from the ComSpec. Please note that the
        usage does not imply the existence of the SwDataDefProps in the
        role networkRepresentation aggregated by the SenderComSpec or
        ReceiverComSpec if an ImplementationDataType is defined.
    :cvar OVERRIDE: If this value is chosen the requirements specified
        in the ComSpec (networkRepresentationFromComSpec) are not
        fullfilled by the aggregated SwDataDefProps. In this case the
        networkRepresentation is specified by the aggregated
        swDataDefProps.
    :cvar PORT_INTERFACE_DEFINITION: This enumeration literal is
        deprecated and will be removed in future. Old description:
        Ignore any networkRepresentationProps of this ISignal and use
        the networkRepresentation specified in the
        VariableDataPrototypes owned by PortInterface
        (portInterfaceDefinition).
    :cvar TRANSFORMING_I_SIGNAL: This literal indicates that a
        transformer chain shall be used to communicate the ISignal as
        UINT8_N over the bus.
    """

    LEGACY = "LEGACY"
    NETWORK_REPRESENTATION_FROM_COM_SPEC = (
        "NETWORK-REPRESENTATION-FROM-COM-SPEC"
    )
    OVERRIDE = "OVERRIDE"
    PORT_INTERFACE_DEFINITION = "PORT-INTERFACE-DEFINITION"
    TRANSFORMING_I_SIGNAL = "TRANSFORMING-I-SIGNAL"
