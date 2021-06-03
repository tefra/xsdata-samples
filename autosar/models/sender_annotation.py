from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import DocumentationBlock
from autosar.models.boolean import Boolean
from autosar.models.data_limit_kind_enum import DataLimitKindEnum
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.processing_kind_enum import ProcessingKindEnum
from autosar.models.ref import Ref
from autosar.models.string import String
from autosar.models.variable_data_prototype_subtypes_enum import VariableDataPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SenderAnnotation:
    """
    Annotation of a sender port, specifying properties of data elements that
    don't affect communication or generation of the RTE.

    :ivar label: This is the headline for the annotation.
    :ivar annotation_origin: This attribute identifies the origin of the
        annotation. It is an arbitrary string since it can be an
        individual's name as well as the name of a tool or even the name
        of a process step.
    :ivar annotation_text: This is the text of the annotation.
    :ivar computed: Flag whether this data element was not measured
        directly but instead was calculated from possibly several other
        measured or calculated values.
    :ivar data_element_ref: The instance of VariableDataPrototype
        annotated.
    :ivar limit_kind: This min or max has not to be mismatched with the
        min- and max for data-value in a compu-method. For example, this
        annotation shows when the result of the calculation performed in
        a RunnableEntity owned by one AtomicSwComponentType is
        transmitted to another AtomicSwComponentType whose
        RunnableEntity will use this value as a limit, e.g. the
        max.power which can be used by that software-component, or the
        current min. slip.
    :ivar processing_kind: This attribute controls how data is processed
        according to the possible values of ProcessingKindEnum.
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
        name = "SENDER-ANNOTATION"

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
    computed: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "COMPUTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_element_ref: Optional["SenderAnnotation.DataElementRef"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    limit_kind: Optional[DataLimitKindEnum] = field(
        default=None,
        metadata={
            "name": "LIMIT-KIND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    processing_kind: Optional[ProcessingKindEnum] = field(
        default=None,
        metadata={
            "name": "PROCESSING-KIND",
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
    class DataElementRef(Ref):
        dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
