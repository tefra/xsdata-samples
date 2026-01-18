from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import DocumentationBlock
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ModePortAnnotation:
    """
    Annotation to a port used for calibration regarding a certain
    ModeDeclarationGroupPrototype.

    :ivar label: This is the headline for the annotation.
    :ivar annotation_origin: This attribute identifies the origin of the
        annotation. It is an arbitrary string since it can be an
        individual's name as well as the name of a tool or even the name
        of a process step.
    :ivar annotation_text: This is the text of the annotation.
    :ivar mode_group_ref: The instance of annotated
        ModeDeclarationGroupPrototype.
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
        name = "MODE-PORT-ANNOTATION"

    label: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotation_origin: None | String = field(
        default=None,
        metadata={
            "name": "ANNOTATION-ORIGIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotation_text: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "ANNOTATION-TEXT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_group_ref: None | ModePortAnnotation.ModeGroupRef = field(
        default=None,
        metadata={
            "name": "MODE-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
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

    @dataclass(kw_only=True)
    class ModeGroupRef(Ref):
        dest: ModeDeclarationGroupPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
