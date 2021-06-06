from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .component_in_composition_instance_ref import ComponentInCompositionInstanceRef
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .port_prototype_blueprint_subtypes_enum import PortPrototypeBlueprintSubtypesEnum
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .td_event_occurrence_expression import TdEventOccurrenceExpression
from .td_event_variable_data_prototype_type_enum import TdEventVariableDataPrototypeTypeEnum
from .variable_data_prototype_subtypes_enum import VariableDataPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TdEventVariableDataPrototype:
    """
    This is used to describe timing events related to sender-receiver
    communication at VFB level.

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
    :ivar occurrence_expression: The occurrence expression for this
        event.
    :ivar component_iref: The context for the scope of this timing
        event.
    :ivar is_external: This attribute is used to refer to external
        events that are related to hardware I/O, like physical sensors
        and actuators, at Virtual Functional Bus (VFB) level.
    :ivar port_prototype_blueprint_ref: The PortPrototypeBlueprint is
        the scope of the timing event.
    :ivar port_ref: The port scope of the timing event.
    :ivar data_element_ref: The referenced VariableDataPrototype
    :ivar td_event_variable_data_prototype_type: The specific type of
        this timing event.
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
        name = "TD-EVENT-VARIABLE-DATA-PROTOTYPE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["TdEventVariableDataPrototype.ShortNameFragments"] = field(
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
    annotations: Optional["TdEventVariableDataPrototype.Annotations"] = field(
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
    occurrence_expression: Optional[TdEventOccurrenceExpression] = field(
        default=None,
        metadata={
            "name": "OCCURRENCE-EXPRESSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    component_iref: Optional[ComponentInCompositionInstanceRef] = field(
        default=None,
        metadata={
            "name": "COMPONENT-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    is_external: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IS-EXTERNAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    port_prototype_blueprint_ref: Optional["TdEventVariableDataPrototype.PortPrototypeBlueprintRef"] = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-BLUEPRINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    port_ref: Optional["TdEventVariableDataPrototype.PortRef"] = field(
        default=None,
        metadata={
            "name": "PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_element_ref: Optional["TdEventVariableDataPrototype.DataElementRef"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    td_event_variable_data_prototype_type: Optional[TdEventVariableDataPrototypeTypeEnum] = field(
        default=None,
        metadata={
            "name": "TD-EVENT-VARIABLE-DATA-PROTOTYPE-TYPE",
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
    class PortPrototypeBlueprintRef(Ref):
        dest: Optional[PortPrototypeBlueprintSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PortRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
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
