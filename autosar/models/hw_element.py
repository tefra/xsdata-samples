from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.category_string import CategoryString
from autosar.models.hw_attribute_value import HwAttributeValue
from autosar.models.hw_category_subtypes_enum import HwCategorySubtypesEnum
from autosar.models.hw_element_connector import HwElementConnector
from autosar.models.hw_element_ref_conditional import HwElementRefConditional
from autosar.models.hw_pin_group_content import HwPinGroup
from autosar.models.hw_type_subtypes_enum import HwTypeSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class HwElement:
    """This represents the ability to describe Hardware Elements on an instance
    level.

    The particular types of hardware are distinguished by the category.
    This category determines the applicable attributes. The possible
    categories and attributes are defined in HwCategory.

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
        object in question.  More elaborate documentation, (in
        particular how the object is built or used) should go to
        "introduction".
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
    :ivar hw_type_ref: This association is used to assign an optional
        HwType which contains the common attribute values for all
        occurences of this HwDescriptionEntity.  Note that HwTypes can
        not be redefined and therefore shall not have a hwType
        reference.
    :ivar hw_category_refs: One of the associations representing one
        particular category of the hardware entity.
    :ivar hw_attribute_values: This aggregation represents a particular
        hardware attribute value. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar nested_elements: This association is used to establish
        hierarchies of hw elements. Note that one particular HwElement
        can be target of this association only once. I.e. multiple
        instantiation of the same HwElement is not supported (at any
        hierarchy level). This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar hw_pin_groups: This aggregation is used to describe the
        connection facilities of a hardware element. Note that hardware
        element has no pins but only pingroups.  The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar hw_element_connections: This represents one particular
        connection between two hardware elements. The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
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
        different AUTOSAR models.  The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed.  An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "HW-ELEMENT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["HwElement.ShortNameFragments"] = field(
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
    annotations: Optional["HwElement.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    hw_type_ref: Optional["HwElement.HwTypeRef"] = field(
        default=None,
        metadata={
            "name": "HW-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    hw_category_refs: Optional["HwElement.HwCategoryRefs"] = field(
        default=None,
        metadata={
            "name": "HW-CATEGORY-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    hw_attribute_values: Optional["HwElement.HwAttributeValues"] = field(
        default=None,
        metadata={
            "name": "HW-ATTRIBUTE-VALUES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nested_elements: Optional["HwElement.NestedElements"] = field(
        default=None,
        metadata={
            "name": "NESTED-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    hw_pin_groups: Optional["HwElement.HwPinGroups"] = field(
        default=None,
        metadata={
            "name": "HW-PIN-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    hw_element_connections: Optional["HwElement.HwElementConnections"] = field(
        default=None,
        metadata={
            "name": "HW-ELEMENT-CONNECTIONS",
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
    class HwTypeRef(Ref):
        dest: Optional[HwTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HwCategoryRefs:
        hw_category_ref: List["HwElement.HwCategoryRefs.HwCategoryRef"] = field(
            default_factory=list,
            metadata={
                "name": "HW-CATEGORY-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class HwCategoryRef(Ref):
            dest: Optional[HwCategorySubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class HwAttributeValues:
        hw_attribute_value: List[HwAttributeValue] = field(
            default_factory=list,
            metadata={
                "name": "HW-ATTRIBUTE-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class NestedElements:
        hw_element_ref_conditional: List[HwElementRefConditional] = field(
            default_factory=list,
            metadata={
                "name": "HW-ELEMENT-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class HwPinGroups:
        hw_pin_group: List[HwPinGroup] = field(
            default_factory=list,
            metadata={
                "name": "HW-PIN-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class HwElementConnections:
        hw_element_connector: List[HwElementConnector] = field(
            default_factory=list,
            metadata={
                "name": "HW-ELEMENT-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )