from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .buffer_properties import BufferProperties
from .category_string import CategoryString
from .end_to_end_transformation_description import (
    EndToEndTransformationDescription,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .short_name_fragment import ShortNameFragment
from .someip_transformation_description import SomeipTransformationDescription
from .string import String
from .transformer_class_enum import TransformerClassEnum
from .user_defined_transformation_description import (
    UserDefinedTransformationDescription,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class TransformationTechnology:
    """
    A TransformationTechnology is a transformer inside a transformer chain.

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
    :ivar buffer_properties: Aggregation of the mandatory
        BufferProperties.
    :ivar has_internal_state: This attribute defines whether the
        Transformer has an internal state or not.
    :ivar needs_original_data: Specifies whether this transformer gets
        access to the SWC's original data.
    :ivar protocol: Specifies the protocol that is implemented by this
        transformer.
    :ivar transformation_descriptions: The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was 1.
    :ivar transformer_class: Specifies to which transformer class this
        transformer belongs.
    :ivar version: Version of the implemented protocol.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "TRANSFORMATION-TECHNOLOGY"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: (
        None | TransformationTechnology.ShortNameFragments
    ) = field(
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
    annotations: None | TransformationTechnology.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    buffer_properties: None | BufferProperties = field(
        default=None,
        metadata={
            "name": "BUFFER-PROPERTIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    has_internal_state: None | Boolean = field(
        default=None,
        metadata={
            "name": "HAS-INTERNAL-STATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    needs_original_data: None | Boolean = field(
        default=None,
        metadata={
            "name": "NEEDS-ORIGINAL-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol: None | String = field(
        default=None,
        metadata={
            "name": "PROTOCOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformation_descriptions: (
        None | TransformationTechnology.TransformationDescriptions
    ) = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-DESCRIPTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformer_class: None | TransformerClassEnum = field(
        default=None,
        metadata={
            "name": "TRANSFORMER-CLASS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    version: None | String = field(
        default=None,
        metadata={
            "name": "VERSION",
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
    class TransformationDescriptions:
        end_to_end_transformation_description: list[
            EndToEndTransformationDescription
        ] = field(
            default_factory=list,
            metadata={
                "name": "END-TO-END-TRANSFORMATION-DESCRIPTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_transformation_description: list[
            SomeipTransformationDescription
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-TRANSFORMATION-DESCRIPTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_transformation_description: list[
            UserDefinedTransformationDescription
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-TRANSFORMATION-DESCRIPTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
