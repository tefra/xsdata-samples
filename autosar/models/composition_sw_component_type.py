from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .assembly_sw_connector import AssemblySwConnector
from .blueprint_policy_list import BlueprintPolicyList
from .blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from .blueprint_policy_single import BlueprintPolicySingle
from .category_string import CategoryString
from .consistency_needs import ConsistencyNeeds
from .constant_specification_mapping_set_subtypes_enum import (
    ConstantSpecificationMappingSetSubtypesEnum,
)
from .data_type_mapping_set_subtypes_enum import DataTypeMappingSetSubtypesEnum
from .delegation_sw_connector import DelegationSwConnector
from .identifier import Identifier
from .instantiation_timing_event_props import InstantiationTimingEventProps
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .p_port_prototype import PPortPrototype
from .pass_through_sw_connector import PassThroughSwConnector
from .port_group import PortGroup
from .pr_port_prototype import PrPortPrototype
from .r_port_prototype import RPortPrototype
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String
from .sw_component_documentation import SwComponentDocumentation
from .sw_component_prototype import SwComponentPrototype
from .unit_group_subtypes_enum import UnitGroupSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompositionSwComponentType:
    """
    A CompositionSwComponentType aggregates SwComponentPrototypes (that in
    turn are typed by SwComponentTypes) as well as SwConnectors for
    primarily connecting SwComponentPrototypes among each others and
    towards the surface of the CompositionSwComponentType.

    By this means hierarchical structures of software-components can be
    created.

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
    :ivar blueprint_policys: This role indicates whether the
        blueprintable element will be modifiable or not motifiable.
    :ivar short_name_pattern: This attribute represents the pattern
        which shall be used to build the shortName of the derived
        elements. As of now it is modeled as a String.  In general it
        should follow the pattern: pattern = (placeholder | namePart)*
        placeholder = "{" namePart "}" namePart = identifier | "_" This
        is subject to be refined in subsequent versions. Note that this
        is marked as obsolete. Use the xml attribute namePattern instead
        as it applies to Identifier and CIdentifier (shortName, symbol
        etc.)
    :ivar sw_component_documentations: This adds a documentation to the
        SwComponentType. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar consistency_needss: This represents the collection of
        ConsistencyNeeds owned by the enclosing SwComponentType. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar ports: The PortPrototypes through which this SwComponentType
        can communicate. The aggregation of PortPrototype is subject to
        variability with the purpose to support the conditional
        existence of PortPrototypes. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar port_groups: A port group being part of this component. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar unit_group_refs: This allows for the specification of which
        UnitGroups are relevant in the context of referencing
        SwComponentType.
    :ivar components: @RESTRICT_TO_STANDARD:CP! The instantiated
        components that are part of this composition. The aggregation of
        SwComponentPrototype is subject to variability with the purpose
        to support the conditional existence of a SwComponentPrototype.
        Please be aware: if the conditional existence of
        SwComponentPrototypes is resolved post-build the deselected
        SwComponentPrototypes are still contained in the ECUs build but
        the instances are inactive in in that they are not scheduled by
        the RTE. The aggregation is marked as atpSplitable in order to
        allow the addition of service components to the ECU extract
        during the ECU integration. The use case for having 0 components
        owned by the CompositionSwComponentType could be to deliver an
        empty CompositionSwComponentType to e.g. a supplier for filling
        the internal structure. @END_RESTRICT_TO_STANDARD!
        @RESTRICT_TO_STANDARD:AP! The instantiated components that are
        part of this composition. @END_RESTRICT_TO_STANDARD! The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar connectors: SwConnectors have the principal ability to
        establish a connection among PortPrototypes. They can have many
        roles in the context of a CompositionSwComponentType. Details
        are refined by subclasses. The aggregation of SwConnectors is
        subject to variability with the purpose to support variant data
        flow. @RESTRICT_TO_STANDARD:CP:AP! The aggregation is marked as
        atpSplitable in order to allow the extension of the ECU extract
        with AssemblySwConnectors between ApplicationSwComponentTypes
        and ServiceSwComponentTypes during the ECU integration.
        @END_RESTRICT_TO_STANDARD! The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar constant_value_mapping_refs: Reference to the
        ConstantSpecificationMapping to be applied for initValues of
        PPortComSpecs and RPortComSpec.
    :ivar data_type_mapping_refs: @RESTRICT_TO_STANDARD:CP! Reference to
        the DataTypeMapping to be applied for the used
        ApplicationDataTypes in PortInterfaces. Background: when
        developing subsystems it may happen that ApplicationDataTypes
        are used on the surface of CompositionSwComponentTypes. In this
        case it would be reasonable to be able to also provide the
        intended mapping to the ImplementationDataTypes. However, this
        mapping shall be informal and not technically binding for the
        implementors mainly because the RTE generator is not concerned
        about the CompositionSwComponentTypes. Rationale: if the mapping
        of ApplicationDataTypes on the delegated and inner PortPrototype
        matches then the mapping to ImplementationDataTypes is not
        impacting compatibility. @END_RESTRICT_TO_STANDARD!
        @RESTRICT_TO_STANDARD:AP! Reference to the DataTypeMapping to be
        applied for the used ApplicationDataTypes in ServiceInterfaces.
        @END_RESTRICT_TO_STANDARD!
    :ivar instantiation_rte_event_propss: This allows to define
        instantiation specific properties for RTE Events, in particular
        for instance specific scheduling. The upper multiplicity of this
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
        name = "COMPOSITION-SW-COMPONENT-TYPE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "CompositionSwComponentType.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["CompositionSwComponentType.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blueprint_policys: Optional[
        "CompositionSwComponentType.BlueprintPolicys"
    ] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    short_name_pattern: Optional[String] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_component_documentations: Optional[
        "CompositionSwComponentType.SwComponentDocumentations"
    ] = field(
        default=None,
        metadata={
            "name": "SW-COMPONENT-DOCUMENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    consistency_needss: Optional[
        "CompositionSwComponentType.ConsistencyNeedss"
    ] = field(
        default=None,
        metadata={
            "name": "CONSISTENCY-NEEDSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ports: Optional["CompositionSwComponentType.Ports"] = field(
        default=None,
        metadata={
            "name": "PORTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_groups: Optional["CompositionSwComponentType.PortGroups"] = field(
        default=None,
        metadata={
            "name": "PORT-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unit_group_refs: Optional["CompositionSwComponentType.UnitGroupRefs"] = (
        field(
            default=None,
            metadata={
                "name": "UNIT-GROUP-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    components: Optional["CompositionSwComponentType.Components"] = field(
        default=None,
        metadata={
            "name": "COMPONENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    connectors: Optional["CompositionSwComponentType.Connectors"] = field(
        default=None,
        metadata={
            "name": "CONNECTORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    constant_value_mapping_refs: Optional[
        "CompositionSwComponentType.ConstantValueMappingRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONSTANT-VALUE-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_type_mapping_refs: Optional[
        "CompositionSwComponentType.DataTypeMappingRefs"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-TYPE-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    instantiation_rte_event_propss: Optional[
        "CompositionSwComponentType.InstantiationRteEventPropss"
    ] = field(
        default=None,
        metadata={
            "name": "INSTANTIATION-RTE-EVENT-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: Optional[str] = field(
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
    class BlueprintPolicys:
        blueprint_policy_list: list[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_not_modifiable: list[BlueprintPolicyNotModifiable] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        blueprint_policy_single: list[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SwComponentDocumentations:
        sw_component_documentation: list[SwComponentDocumentation] = field(
            default_factory=list,
            metadata={
                "name": "SW-COMPONENT-DOCUMENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ConsistencyNeedss:
        consistency_needs: list[ConsistencyNeeds] = field(
            default_factory=list,
            metadata={
                "name": "CONSISTENCY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Ports:
        p_port_prototype: list[PPortPrototype] = field(
            default_factory=list,
            metadata={
                "name": "P-PORT-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        pr_port_prototype: list[PrPortPrototype] = field(
            default_factory=list,
            metadata={
                "name": "PR-PORT-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        r_port_prototype: list[RPortPrototype] = field(
            default_factory=list,
            metadata={
                "name": "R-PORT-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PortGroups:
        port_group: list[PortGroup] = field(
            default_factory=list,
            metadata={
                "name": "PORT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class UnitGroupRefs:
        unit_group_ref: list[
            "CompositionSwComponentType.UnitGroupRefs.UnitGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "UNIT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class UnitGroupRef(Ref):
            dest: Optional[UnitGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class Components:
        sw_component_prototype: list[SwComponentPrototype] = field(
            default_factory=list,
            metadata={
                "name": "SW-COMPONENT-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Connectors:
        assembly_sw_connector: list[AssemblySwConnector] = field(
            default_factory=list,
            metadata={
                "name": "ASSEMBLY-SW-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        delegation_sw_connector: list[DelegationSwConnector] = field(
            default_factory=list,
            metadata={
                "name": "DELEGATION-SW-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        pass_through_sw_connector: list[PassThroughSwConnector] = field(
            default_factory=list,
            metadata={
                "name": "PASS-THROUGH-SW-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ConstantValueMappingRefs:
        constant_value_mapping_ref: list[
            "CompositionSwComponentType.ConstantValueMappingRefs.ConstantValueMappingRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSTANT-VALUE-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ConstantValueMappingRef(Ref):
            dest: Optional[ConstantSpecificationMappingSetSubtypesEnum] = (
                field(
                    default=None,
                    metadata={
                        "name": "DEST",
                        "type": "Attribute",
                        "required": True,
                    },
                )
            )

    @dataclass
    class DataTypeMappingRefs:
        data_type_mapping_ref: list[
            "CompositionSwComponentType.DataTypeMappingRefs.DataTypeMappingRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TYPE-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DataTypeMappingRef(Ref):
            dest: Optional[DataTypeMappingSetSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class InstantiationRteEventPropss:
        instantiation_timing_event_props: list[
            InstantiationTimingEventProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "INSTANTIATION-TIMING-EVENT-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
