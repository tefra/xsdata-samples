from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import Sdg
from .build_engineering_object import BuildEngineeringObject
from .ecuc_definition_element_subtypes_enum import (
    EcucDefinitionElementSubtypesEnum,
)
from .foreign_model_reference import ForeignModelReference
from .generic_model_reference import GenericModelReference
from .identifier import Identifier
from .nmtoken_string import NmtokenString
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BuildActionIoElement:
    """
    This meta-class represents the ability to specify the input/output
    entities of a BuildAction.

    :ivar category: This element assigns a category to the parent
        element. It is intended to specialize the usage and/or the
        content of the object. Such a specialization may also impose
        particular semantic constraints on the entire substructure. See
        also Identifiable.
    :ivar sdgs: This special data group allows to denote specific data.
        The structure is subject of mutual agreement.
    :ivar ecuc_definition_ref: This association denotes an ECUC
        parameter definition. The such referenced parameters are subject
        of the build action input/ouptut. Note that the reference to the
        definition denotes the right for a build action to read and/or
        write values for the given defintion and all contained
        definitions.
    :ivar engineering_object: This represents an artifact applicable to
        the build action.
    :ivar foreign_model_reference: This is a reference to a foreign
        model element. Note that it is not modeled as an association
        because it should also be able to refer also to non AUTOSAR
        models.
    :ivar model_object_reference: This is a reference to a generic model
        element. Note that it is not modeled as an association because
        it should also be able to refer also to non AUTOSAR models.
    :ivar role: This attribute allows to denote a particular role of the
        collection. Note that the applicable semantics shall be mutually
        agreed between the two parties.
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
        name = "BUILD-ACTION-IO-ELEMENT"

    category: NmtokenString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdgs: BuildActionIoElement.Sdgs | None = field(
        default=None,
        metadata={
            "name": "SDGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecuc_definition_ref: BuildActionIoElement.EcucDefinitionRef | None = (
        field(
            default=None,
            metadata={
                "name": "ECUC-DEFINITION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    engineering_object: BuildEngineeringObject | None = field(
        default=None,
        metadata={
            "name": "ENGINEERING-OBJECT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    foreign_model_reference: ForeignModelReference | None = field(
        default=None,
        metadata={
            "name": "FOREIGN-MODEL-REFERENCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    model_object_reference: GenericModelReference | None = field(
        default=None,
        metadata={
            "name": "MODEL-OBJECT-REFERENCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    role: Identifier | None = field(
        default=None,
        metadata={
            "name": "ROLE",
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

    @dataclass
    class Sdgs:
        sdg: list[Sdg] = field(
            default_factory=list,
            metadata={
                "name": "SDG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EcucDefinitionRef(Ref):
        dest: EcucDefinitionElementSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
