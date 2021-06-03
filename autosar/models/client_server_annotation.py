from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import DocumentationBlock
from autosar.models.client_server_operation_subtypes_enum import ClientServerOperationSubtypesEnum
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.ref import Ref
from autosar.models.string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ClientServerAnnotation:
    """
    Annotation to a port regarding a certain Operation.

    :ivar label: This is the headline for the annotation.
    :ivar annotation_origin: This attribute identifies the origin of the
        annotation. It is an arbitrary string since it can be an
        individual's name as well as the name of a tool or even the name
        of a process step.
    :ivar annotation_text: This is the text of the annotation.
    :ivar operation_ref: This represents the ClientServerOperation that
        the ClientServerAnnotation corresponds to.
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
        name = "CLIENT-SERVER-ANNOTATION"

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
    operation_ref: Optional["ClientServerAnnotation.OperationRef"] = field(
        default=None,
        metadata={
            "name": "OPERATION-REF",
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
    class OperationRef(Ref):
        dest: Optional[ClientServerOperationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
