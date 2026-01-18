from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .data_transformation_ref_conditional import (
    DataTransformationRefConditional,
)
from .end_to_end_transformation_i_signal_props import (
    EndToEndTransformationISignalProps,
)
from .i_signal_subtypes_enum import ISignalSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .someip_transformation_i_signal_props import (
    SomeipTransformationISignalProps,
)
from .system_signal_group_subtypes_enum import SystemSignalGroupSubtypesEnum
from .user_defined_transformation_i_signal_props import (
    UserDefinedTransformationISignalProps,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ISignalGroup:
    """
    SignalGroup of the Interaction Layer.

    The RTE supports a "signal fan-out" where the same System Signal Group
    is sent in different SignalIPdus to multiple receivers. An ISignalGroup
    refers to a set of ISignals that shall always be kept together. A
    ISignalGroup represents a COM Signal Group. Therefore it is recommended
    to put the ISignalGroup in the same Package as ISignals (see
    atp.recommendedPackage).

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
    :ivar com_based_signal_group_transformations: This property was
        modified due to atpVariation (DirectedAssociationPattern).
    :ivar i_signal_refs: Reference to a set of ISignals that shall
        always be kept together.
    :ivar system_signal_group_ref: Reference to the SystemSignalGroup
        that is defined on VFB level and that is supposed to be
        transmitted in the ISignalGroup.
    :ivar transformation_i_signal_propss: A transformer chain consists
        of an ordered list of transformers. The ISignalGroup specific
        configuration properties for each transformer are defined in the
        TransformationISignalProps class. The transformer configuration
        properties that are common for all ISignalGroups are described
        in the TransformationTechnology class.
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
        name = "I-SIGNAL-GROUP"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: ISignalGroup.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: ISignalGroup.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    com_based_signal_group_transformations: (
        ISignalGroup.ComBasedSignalGroupTransformations | None
    ) = field(
        default=None,
        metadata={
            "name": "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_refs: ISignalGroup.ISignalRefs | None = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_signal_group_ref: ISignalGroup.SystemSignalGroupRef | None = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformation_i_signal_propss: (
        ISignalGroup.TransformationISignalPropss | None
    ) = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-I-SIGNAL-PROPSS",
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
    uuid: str | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ComBasedSignalGroupTransformations:
        data_transformation_ref_conditional: list[
            DataTransformationRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TRANSFORMATION-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ISignalRefs:
        i_signal_ref: list[ISignalGroup.ISignalRefs.ISignalRef] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ISignalRef(Ref):
            dest: ISignalSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SystemSignalGroupRef(Ref):
        dest: SystemSignalGroupSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TransformationISignalPropss:
        end_to_end_transformation_i_signal_props: list[
            EndToEndTransformationISignalProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_transformation_i_signal_props: list[
            SomeipTransformationISignalProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_transformation_i_signal_props: list[
            UserDefinedTransformationISignalProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
