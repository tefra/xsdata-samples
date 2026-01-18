from __future__ import annotations

from dataclasses import dataclass, field

from .ecuc_affection_enum import EcucAffectionEnum
from .ecuc_common_attributes_subtypes_enum import (
    EcucCommonAttributesSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucConfigurationClassAffection:
    """
    Specifies in the "VendorSpecificModuleDefinition" whether changes on
    this parameter do affect other parameters in a later configuration
    step.

    This element is removed from the specifications and shall not be used.

    :ivar affected_refs: Optional reference to parameters or references
        which are affected by the ConfigurationClassAffection.
    :ivar affection_kind: Specifies which affect do changes in this
        parameter have on other parameters.  This attribute is
        deprecated and will be removed in future versions.
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
        name = "ECUC-CONFIGURATION-CLASS-AFFECTION"

    affected_refs: None | EcucConfigurationClassAffection.AffectedRefs = field(
        default=None,
        metadata={
            "name": "AFFECTED-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    affection_kind: None | EcucAffectionEnum = field(
        default=None,
        metadata={
            "name": "AFFECTION-KIND",
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

    @dataclass
    class AffectedRefs:
        affected_ref: list[
            EcucConfigurationClassAffection.AffectedRefs.AffectedRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "AFFECTED-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class AffectedRef(Ref):
            dest: None | EcucCommonAttributesSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
