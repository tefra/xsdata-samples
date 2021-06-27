from dataclasses import dataclass, field
from typing import Optional
from .annotation import DocumentationBlock
from .argument_data_prototype_subtypes_enum import ArgumentDataPrototypeSubtypesEnum
from .filter_debouncing_enum import FilterDebouncingEnum
from .float_mod import Float
from .multidimensional_time import MultidimensionalTime
from .multilanguage_long_name import MultilanguageLongName
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .pulse_test_enum import PulseTestEnum
from .ref import Ref
from .string import String
from .trigger_subtypes_enum import TriggerSubtypesEnum
from .variable_data_prototype_subtypes_enum import VariableDataPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IoHwAbstractionServerAnnotation:
    """The IoHwAbstractionServerAnnotation will only be used from a sensor- or
    an actuator component while interacting with the IoHwAbstraction layer.

    Note that the "server" in the name of this meta-class is not meant
    to restrict the usage to ClientServerInterfaces.

    :ivar label: This is the headline for the annotation.
    :ivar annotation_origin: This attribute identifies the origin of the
        annotation. It is an arbitrary string since it can be an
        individual's name as well as the name of a tool or even the name
        of a process step.
    :ivar annotation_text: This is the text of the annotation.
    :ivar age: In case of a SET operation, the age will be interpreted
        as Delay while in a GET operation (input) it specifies the
        Lifetime of the signal within the IoHwAbstraction Layer
    :ivar argument_ref: Reference to the corresponding
        ArgumentDataPrototype.
    :ivar bsw_resolution: This value is determined by an appropriate
        combination of the range, the unit as well as the data-elements
        type, i.e. (ecuSignalRange.upperLimit-ecuSignalRange.lowerLimit)
        / (2^datatypelength - 1)
    :ivar data_element_ref: Reference to the corresponding
        VariableDataPrototype.
    :ivar failure_monitoring_ref: This is only applicable in SET
        operations. If it is enabled, the IoHwAbstraction layer will
        monitor the result of the operation and issue an diagnostic
        signal. This means especially, that an additional client-server
        port has to be created. Tools can use this information to cross-
        check whether for each data-element in a SET operation with
        FailureMonitoring enabled an additional port is created The
        referenced port monitors a failure in the to be monitored
        VariableDataPrototype of the IoHwAbstraction layer. The
        referenced port has to be another port of the same Actuator or
        Sensor Component.
    :ivar filtering_debouncing: This attribute is used to indicate what
        kind of filtering/debouncing has been put to the signal in the
        IoHwAbstraction layer. rawData means that no modification of the
        signal has been applied. This is the default value debounceData
        means that the signal is a mean value waitTimeData means that
        the signal is delivered by a GET operation after a certain
        amount of time
    :ivar pulse_test: This attribute indicates to the connected
        SensorActuatorSwComponentType whether the VariableDataPrototype
        can be used to generate pulse test sequences using the
        IoHwAbstraction layer
    :ivar trigger_ref: Reference to the corresponding Trigger.
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
        name = "IO-HW-ABSTRACTION-SERVER-ANNOTATION"

    label: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotation_origin: Optional[String] = field(
        default=None,
        metadata={
            "name": "ANNOTATION-ORIGIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotation_text: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "ANNOTATION-TEXT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    age: Optional[MultidimensionalTime] = field(
        default=None,
        metadata={
            "name": "AGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    argument_ref: Optional["IoHwAbstractionServerAnnotation.ArgumentRef"] = field(
        default=None,
        metadata={
            "name": "ARGUMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    bsw_resolution: Optional[Float] = field(
        default=None,
        metadata={
            "name": "BSW-RESOLUTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_element_ref: Optional["IoHwAbstractionServerAnnotation.DataElementRef"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    failure_monitoring_ref: Optional["IoHwAbstractionServerAnnotation.FailureMonitoringRef"] = field(
        default=None,
        metadata={
            "name": "FAILURE-MONITORING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    filtering_debouncing: Optional[FilterDebouncingEnum] = field(
        default=None,
        metadata={
            "name": "FILTERING-DEBOUNCING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pulse_test: Optional[PulseTestEnum] = field(
        default=None,
        metadata={
            "name": "PULSE-TEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trigger_ref: Optional["IoHwAbstractionServerAnnotation.TriggerRef"] = field(
        default=None,
        metadata={
            "name": "TRIGGER-REF",
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
    class ArgumentRef(Ref):
        dest: Optional[ArgumentDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DataElementRef(Ref):
        dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class FailureMonitoringRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TriggerRef(Ref):
        dest: Optional[TriggerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
