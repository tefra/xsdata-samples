from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .constant_specification_mapping_set_subtypes_enum import (
    ConstantSpecificationMappingSetSubtypesEnum,
)
from .data_type_mapping_set_subtypes_enum import DataTypeMappingSetSubtypesEnum
from .identifier import Identifier
from .instantiation_data_def_props import InstantiationDataDefProps
from .mode_switch_event_triggered_activity import (
    ModeSwitchEventTriggeredActivity,
)
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nv_block_data_mapping import NvBlockDataMapping
from .nv_block_needs import NvBlockNeeds
from .parameter_data_prototype import ParameterDataPrototype
from .ref import Ref
from .role_based_data_assignment import RoleBasedDataAssignment
from .role_based_port_assignment import RoleBasedPortAssignment
from .short_name_fragment import ShortNameFragment
from .timing_event_subtypes_enum import TimingEventSubtypesEnum
from .variable_data_prototype import VariableDataPrototype

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NvBlockDescriptor:
    """
    Specifies the properties of exactly on NVRAM Block.

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
    :ivar client_server_ports: The RoleBasedPortAssignement defines
        which client server port of the NvBlockSwComponentType serves
        for which kind of service or notification. In case of
        notifications one common callback function is provided by the
        RTE for each individual kind of notification defined by the
        "role". The aggregation of RoleBasedPortAssignment is subject to
        variability with the purpose to support the conditional
        existence of ports. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar constant_value_mapping_refs: Reference to the
        ConstanSpecificationMapping to be applied for the particular
        NVRAM Block
    :ivar data_type_mapping_refs: Reference to the DataTypeMapping to be
        applied for the particular NVRAM Block.
    :ivar instantiation_data_def_propss: The purpose of
        InstantiationDataDefProps are the refinement of some data def
        properties of individual instantiations within the context of a
        NvBlockSwComponentType. The aggregation of
        InstantiationDataDefProps is subject to variability with the
        purpose to support the conditional existence of ports, component
        internal memory objects and those attributes. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar mode_switch_event_triggered_activitys: This represents the
        collection of ModeSwitchEventTriggeredActivities related to the
        enclosing NvBlockDescriptor. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar nv_block_data_mappings: Defines the mapping between the
        VariableDataPrototypes in the NvBlockComponents ports and the
        VariableDataPrototypes of the RAM Block. The aggregation of
        NvBlockDataMapping is subject to variability with the purpose to
        support the conditional existence of nv data ports. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar nv_block_needs: Specifies the abstract needs on the
        configuration of the NVRAM Manager for the single NVRAM Block
        described by this NvBlockDescriptor. In addition, it may define
        requirements for writing strategies in an implementation of an
        NvBlockSwComponentType by the RTE. Please note that the
        attributes nDataSets and nRomBlocks are not relevant for this
        aggregation because the RTE will allocate just one block anyway.
        In a different context, however, they do make sense.
    :ivar ram_block: Defines the RAM Block of the NVRAM Block provided
        by NvBlockSwComponentType.
    :ivar rom_block: Defines the ROM Block of the NVRAM Block provided
        by NvBlockSwComponentType.
    :ivar support_dirty_flag: Specifies whether calling of NvM functions
        for writing and/or status control of potentially modified RAM
        Blocks to NV memory shall be controlled by the RTE.
    :ivar timing_event_ref: this reference can be taken to identify the
        TimingEvent to be used by the RTE for implementing a cyclic
        writing strategy for this block
    :ivar writing_strategy_role: This attribute allows for assigning a
        specific writing strategy for an incoming AutosarDataPrototype.
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
        name = "NV-BLOCK-DESCRIPTOR"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: NvBlockDescriptor.ShortNameFragments | None = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: NvBlockDescriptor.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_server_ports: NvBlockDescriptor.ClientServerPorts | None = (
        field(
            default=None,
            metadata={
                "name": "CLIENT-SERVER-PORTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    constant_value_mapping_refs: NvBlockDescriptor.ConstantValueMappingRefs | None = field(
        default=None,
        metadata={
            "name": "CONSTANT-VALUE-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_type_mapping_refs: NvBlockDescriptor.DataTypeMappingRefs | None = field(
        default=None,
        metadata={
            "name": "DATA-TYPE-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    instantiation_data_def_propss: NvBlockDescriptor.InstantiationDataDefPropss | None = field(
        default=None,
        metadata={
            "name": "INSTANTIATION-DATA-DEF-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_switch_event_triggered_activitys: NvBlockDescriptor.ModeSwitchEventTriggeredActivitys | None = field(
        default=None,
        metadata={
            "name": "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nv_block_data_mappings: NvBlockDescriptor.NvBlockDataMappings | None = field(
        default=None,
        metadata={
            "name": "NV-BLOCK-DATA-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nv_block_needs: NvBlockNeeds | None = field(
        default=None,
        metadata={
            "name": "NV-BLOCK-NEEDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ram_block: VariableDataPrototype | None = field(
        default=None,
        metadata={
            "name": "RAM-BLOCK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rom_block: ParameterDataPrototype | None = field(
        default=None,
        metadata={
            "name": "ROM-BLOCK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    support_dirty_flag: Boolean | None = field(
        default=None,
        metadata={
            "name": "SUPPORT-DIRTY-FLAG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timing_event_ref: NvBlockDescriptor.TimingEventRef | None = field(
        default=None,
        metadata={
            "name": "TIMING-EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    writing_strategy_role: RoleBasedDataAssignment | None = field(
        default=None,
        metadata={
            "name": "WRITING-STRATEGY-ROLE",
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
    class ClientServerPorts:
        role_based_port_assignment: list[RoleBasedPortAssignment] = field(
            default_factory=list,
            metadata={
                "name": "ROLE-BASED-PORT-ASSIGNMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ConstantValueMappingRefs:
        constant_value_mapping_ref: list[
            NvBlockDescriptor.ConstantValueMappingRefs.ConstantValueMappingRef
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
            dest: ConstantSpecificationMappingSetSubtypesEnum | None = (
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
            NvBlockDescriptor.DataTypeMappingRefs.DataTypeMappingRef
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
            dest: DataTypeMappingSetSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class InstantiationDataDefPropss:
        instantiation_data_def_props: list[InstantiationDataDefProps] = field(
            default_factory=list,
            metadata={
                "name": "INSTANTIATION-DATA-DEF-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ModeSwitchEventTriggeredActivitys:
        mode_switch_event_triggered_activity: list[
            ModeSwitchEventTriggeredActivity
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class NvBlockDataMappings:
        nv_block_data_mapping: list[NvBlockDataMapping] = field(
            default_factory=list,
            metadata={
                "name": "NV-BLOCK-DATA-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TimingEventRef(Ref):
        dest: TimingEventSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
