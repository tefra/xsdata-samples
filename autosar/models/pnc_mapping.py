from dataclasses import dataclass, field
from typing import List, Optional
from .adaptive_platform_service_instance_subtypes_enum import (
    AdaptivePlatformServiceInstanceSubtypesEnum,
)
from .admin_data import (
    AdminData,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .consumed_provided_service_instance_group_ref_conditional import (
    ConsumedProvidedServiceInstanceGroupRefConditional,
)
from .ecu_instance_subtypes_enum import EcuInstanceSubtypesEnum
from .frame_triggering_subtypes_enum import FrameTriggeringSubtypesEnum
from .i_signal_i_pdu_group_subtypes_enum import ISignalIPduGroupSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .pdur_i_pdu_group_subtypes_enum import PdurIPduGroupSubtypesEnum
from .physical_channel_subtypes_enum import PhysicalChannelSubtypesEnum
from .pnc_mapping_ident import PncMappingIdent
from .port_group_in_system_instance_ref import PortGroupInSystemInstanceRef
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PncMapping:
    """@RESTRICT_TO_STANDARD:CP!
    Describes a mapping between one or several Virtual Function Clusters onto Partial Network Clusters. A Virtual Function Cluster is realized by a PortGroup. A Partial Network Cluster is realized by one or more IPduGroups.
    @END_RESTRICT_TO_STANDARD!
    @RESTRICT_TO_STANDARD:AP!
    Describes a mapping between one or several Virtual Function Clusters onto Partial Network Clusters. A Virtual Function Cluster is realized by a PortGroup. A Partial Network Cluster is realized by one or more ServiceInstances.
    @END_RESTRICT_TO_STANDARD!

    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particlar
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Describable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar admin_data: This represents the administrative data for the
        describable object.
    :ivar dynamic_pnc_mapping_pdu_group_refs: Reference to an
        ISignalIPduGroup that allows mapping of this PNC without
        statically mapping this PNC directly to a channel. This is
        needed to describe dynamic PNCs that can be learned only at run-
        time and which have also a relation to an ISignalIPduGroup.
    :ivar ident: This adds the ability to become referrable to
        PncMapping.
    :ivar physical_channel_refs: This reference maps the partial network
        to a communication channel.
    :ivar pnc_consumed_provided_service_instance_groups:
        ConsumedProvidedServiceInstanceGroup used in a Partial Network
        Cluster. This reference is optional, since this could be used
        for starting and stopping ConsumedProvidedServiceInstanceGroup
        according the requested partial network, but is not necessarily
        needed. This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar pnc_group_refs: IPduGroup participating in a Partial Network
        Cluster. This reference is optional in case an ecu extract has
        only indirect pnc access, i.e. ecu is not directly connected to
        a network which supports partial network.
    :ivar pnc_identifier: Identifer of the Partial Network Cluster. This
        number represents the absolute bit position of this Partial
        Network Cluster in the NM Pdu.
    :ivar pnc_pdur_group_refs: This reference maps the Partial Network
        Cluster to a set of PdurIpduGroups.
    :ivar pnc_wakeup_enable: If this parameter is available and set to
        true then this PNC will be woken up as soon as a channel wakeup
        occurs on a channel where this PNC is assigned to. This is
        ensured by adding this PNC to the corresponding channel wakeup
        sources during upstream mapping.
    :ivar relevant_for_dynamic_pnc_mapping_refs: Reference to a PNC
        Gateway ECU for PNCs which do not have a static channel mapping.
        This is needed to describe dynamic PNCs that can be learned only
        at run-time and which have no relation to an ISignalIPduGroup.
    :ivar service_instance_refs: Reference to ServiceInstances that are
        participating in a Partial Network Cluster.
    :ivar short_label: This attribute specifies an identifying shortName
        for the PncMapping. It shall be unique in the System scope.
    :ivar vfc_irefs: Virtual Function Cluster to be mapped onto a
        Partial Network Cluster. This reference is optional in case that
        the System Description doesn't use a complete Software Component
        Description (VFB View). This supports the inclusion of legacy
        systems.
    :ivar wakeup_frame_refs: Reference to collection of FrameTriggerings
        that are used for the wakeup of this PNC (Application Frames or
        Nm Frames can be used). This reference is only valid if this
        EcuExtract represents an ECU which has direct PNC access, i.e.
        ECU is directly connected to a network which supports partial
        network.
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
    """

    class Meta:
        name = "PNC-MAPPING"

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
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
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
    dynamic_pnc_mapping_pdu_group_refs: Optional[
        "PncMapping.DynamicPncMappingPduGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "DYNAMIC-PNC-MAPPING-PDU-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ident: Optional[PncMappingIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    physical_channel_refs: Optional["PncMapping.PhysicalChannelRefs"] = field(
        default=None,
        metadata={
            "name": "PHYSICAL-CHANNEL-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_consumed_provided_service_instance_groups: Optional[
        "PncMapping.PncConsumedProvidedServiceInstanceGroups"
    ] = field(
        default=None,
        metadata={
            "name": "PNC-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_group_refs: Optional["PncMapping.PncGroupRefs"] = field(
        default=None,
        metadata={
            "name": "PNC-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_identifier: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PNC-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_pdur_group_refs: Optional["PncMapping.PncPdurGroupRefs"] = field(
        default=None,
        metadata={
            "name": "PNC-PDUR-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_wakeup_enable: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PNC-WAKEUP-ENABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    relevant_for_dynamic_pnc_mapping_refs: Optional[
        "PncMapping.RelevantForDynamicPncMappingRefs"
    ] = field(
        default=None,
        metadata={
            "name": "RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_instance_refs: Optional["PncMapping.ServiceInstanceRefs"] = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vfc_irefs: Optional["PncMapping.VfcIrefs"] = field(
        default=None,
        metadata={
            "name": "VFC-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_frame_refs: Optional["PncMapping.WakeupFrameRefs"] = field(
        default=None,
        metadata={
            "name": "WAKEUP-FRAME-REFS",
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

    @dataclass
    class DynamicPncMappingPduGroupRefs:
        dynamic_pnc_mapping_pdu_group_ref: List[
            "PncMapping.DynamicPncMappingPduGroupRefs.DynamicPncMappingPduGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DYNAMIC-PNC-MAPPING-PDU-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DynamicPncMappingPduGroupRef(Ref):
            dest: Optional[ISignalIPduGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PhysicalChannelRefs:
        physical_channel_ref: List[
            "PncMapping.PhysicalChannelRefs.PhysicalChannelRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "PHYSICAL-CHANNEL-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PhysicalChannelRef(Ref):
            dest: Optional[PhysicalChannelSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PncConsumedProvidedServiceInstanceGroups:
        consumed_provided_service_instance_group_ref_conditional: List[
            ConsumedProvidedServiceInstanceGroupRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PncGroupRefs:
        pnc_group_ref: List["PncMapping.PncGroupRefs.PncGroupRef"] = field(
            default_factory=list,
            metadata={
                "name": "PNC-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PncGroupRef(Ref):
            dest: Optional[ISignalIPduGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PncPdurGroupRefs:
        pnc_pdur_group_ref: List[
            "PncMapping.PncPdurGroupRefs.PncPdurGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "PNC-PDUR-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PncPdurGroupRef(Ref):
            dest: Optional[PdurIPduGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RelevantForDynamicPncMappingRefs:
        relevant_for_dynamic_pnc_mapping_ref: List[
            "PncMapping.RelevantForDynamicPncMappingRefs.RelevantForDynamicPncMappingRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RelevantForDynamicPncMappingRef(Ref):
            dest: Optional[EcuInstanceSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ServiceInstanceRefs:
        service_instance_ref: List[
            "PncMapping.ServiceInstanceRefs.ServiceInstanceRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ServiceInstanceRef(Ref):
            dest: Optional[
                AdaptivePlatformServiceInstanceSubtypesEnum
            ] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class VfcIrefs:
        vfc_iref: List[PortGroupInSystemInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "VFC-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class WakeupFrameRefs:
        wakeup_frame_ref: List[
            "PncMapping.WakeupFrameRefs.WakeupFrameRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "WAKEUP-FRAME-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class WakeupFrameRef(Ref):
            dest: Optional[FrameTriggeringSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
