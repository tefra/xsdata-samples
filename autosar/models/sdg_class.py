from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.identifier import Identifier
from autosar.models.meta_class_name import MetaClassName
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.nmtoken_string import NmtokenString
from autosar.models.ref import Ref
from autosar.models.sdg_aggregation_with_variation import SdgAggregationWithVariation
from autosar.models.sdg_foreign_reference import SdgForeignReference
from autosar.models.sdg_foreign_reference_with_variation import SdgForeignReferenceWithVariation
from autosar.models.sdg_primitive_attribute import SdgPrimitiveAttribute
from autosar.models.sdg_primitive_attribute_with_variation import SdgPrimitiveAttributeWithVariation
from autosar.models.sdg_reference import SdgReference
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.traceable_text_subtypes_enum import TraceableTextSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SdgClass:
    """An SdgClass specifies the name and structure of the SDG that may be used
    to store proprietary data in an AUTOSAR model.

    The SdgClass is similar to an UML stereotype.

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
    :ivar gid: Specifies the name that identifies the element.
    :ivar extends_meta_class: The AUTOSAR Meta-Class that may be
        extended by this SdgClass.
    :ivar caption: Specifies if a caption is required. Note: only Sdgs
        that have a caption can be referenced
    :ivar attributes: Defintion of the structure of the Sdg
    :ivar sdg_constraint_refs: Semantic constraints that restrict the
        structure of the special data group.
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
        name = "SDG-CLASS"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SdgClass.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["SdgClass.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    gid: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "GID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    extends_meta_class: Optional[MetaClassName] = field(
        default=None,
        metadata={
            "name": "EXTENDS-META-CLASS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    caption: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CAPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    attributes: Optional["SdgClass.Attributes"] = field(
        default=None,
        metadata={
            "name": "ATTRIBUTES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sdg_constraint_refs: Optional["SdgClass.SdgConstraintRefs"] = field(
        default=None,
        metadata={
            "name": "SDG-CONSTRAINT-REFS",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Attributes:
        sdg_aggregation_with_variation: List[SdgAggregationWithVariation] = field(
            default_factory=list,
            metadata={
                "name": "SDG-AGGREGATION-WITH-VARIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sdg_foreign_reference: List[SdgForeignReference] = field(
            default_factory=list,
            metadata={
                "name": "SDG-FOREIGN-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sdg_foreign_reference_with_variation: List[SdgForeignReferenceWithVariation] = field(
            default_factory=list,
            metadata={
                "name": "SDG-FOREIGN-REFERENCE-WITH-VARIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sdg_primitive_attribute: List[SdgPrimitiveAttribute] = field(
            default_factory=list,
            metadata={
                "name": "SDG-PRIMITIVE-ATTRIBUTE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sdg_primitive_attribute_with_variation: List[SdgPrimitiveAttributeWithVariation] = field(
            default_factory=list,
            metadata={
                "name": "SDG-PRIMITIVE-ATTRIBUTE-WITH-VARIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sdg_reference: List[SdgReference] = field(
            default_factory=list,
            metadata={
                "name": "SDG-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SdgConstraintRefs:
        sdg_constraint_ref: List["SdgClass.SdgConstraintRefs.SdgConstraintRef"] = field(
            default_factory=list,
            metadata={
                "name": "SDG-CONSTRAINT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class SdgConstraintRef(Ref):
            dest: Optional[TraceableTextSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
