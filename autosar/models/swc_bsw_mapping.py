from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .bsw_internal_behavior_subtypes_enum import (
    BswInternalBehaviorSubtypesEnum,
)
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .swc_bsw_runnable_mapping import SwcBswRunnableMapping
from .swc_bsw_synchronized_mode_group_prototype import (
    SwcBswSynchronizedModeGroupPrototype,
)
from .swc_bsw_synchronized_trigger import SwcBswSynchronizedTrigger
from .swc_internal_behavior_subtypes_enum import (
    SwcInternalBehaviorSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SwcBswMapping:
    """
    Maps an SwcInternalBehavior to an BswInternalBehavior.

    This is required to coordinate the API generation and the scheduling
    for AUTOSAR Service Components, ECU Abstraction Components and Complex
    Driver Components by the RTE and the BSW scheduling mechanisms.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar bsw_behavior_ref: The mapped BswInternalBehavior
    :ivar runnable_mappings: A mapping between a pair of SWC and BSW
        runnables. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar swc_behavior_ref: The mapped SwcInternalBehavior.
    :ivar synchronized_mode_groups: A pair of SWC and BSW mode group
        prototypes to be synchronized by the scheduler. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar synchronized_triggers: A pair of SWC and BSW Triggers to be
        synchronized by the scheduler. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "SWC-BSW-MAPPING"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | SwcBswMapping.ShortNameFragments = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | SwcBswMapping.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_behavior_ref: None | SwcBswMapping.BswBehaviorRef = field(
        default=None,
        metadata={
            "name": "BSW-BEHAVIOR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    runnable_mappings: None | SwcBswMapping.RunnableMappings = field(
        default=None,
        metadata={
            "name": "RUNNABLE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    swc_behavior_ref: None | SwcBswMapping.SwcBehaviorRef = field(
        default=None,
        metadata={
            "name": "SWC-BEHAVIOR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    synchronized_mode_groups: None | SwcBswMapping.SynchronizedModeGroups = (
        field(
            default=None,
            metadata={
                "name": "SYNCHRONIZED-MODE-GROUPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    synchronized_triggers: None | SwcBswMapping.SynchronizedTriggers = field(
        default=None,
        metadata={
            "name": "SYNCHRONIZED-TRIGGERS",
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
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class BswBehaviorRef(Ref):
        dest: BswInternalBehaviorSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class RunnableMappings:
        swc_bsw_runnable_mapping: list[SwcBswRunnableMapping] = field(
            default_factory=list,
            metadata={
                "name": "SWC-BSW-RUNNABLE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class SwcBehaviorRef(Ref):
        dest: SwcInternalBehaviorSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SynchronizedModeGroups:
        swc_bsw_synchronized_mode_group_prototype: list[
            SwcBswSynchronizedModeGroupPrototype
        ] = field(
            default_factory=list,
            metadata={
                "name": "SWC-BSW-SYNCHRONIZED-MODE-GROUP-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class SynchronizedTriggers:
        swc_bsw_synchronized_trigger: list[SwcBswSynchronizedTrigger] = field(
            default_factory=list,
            metadata={
                "name": "SWC-BSW-SYNCHRONIZED-TRIGGER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
