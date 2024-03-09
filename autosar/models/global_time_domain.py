from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .can_global_time_domain_props import CanGlobalTimeDomainProps
from .category_string import CategoryString
from .communication_cluster_subtypes_enum import (
    CommunicationClusterSubtypesEnum,
)
from .eth_global_time_domain_props import EthGlobalTimeDomainProps
from .fr_global_time_domain_props import FrGlobalTimeDomainProps
from .general_purpose_pdu_subtypes_enum import GeneralPurposePduSubtypesEnum
from .global_time_can_master import GlobalTimeCanMaster
from .global_time_can_slave import GlobalTimeCanSlave
from .global_time_correction_props import GlobalTimeCorrectionProps
from .global_time_domain_ref_conditional import GlobalTimeDomainRefConditional
from .global_time_domain_subtypes_enum import GlobalTimeDomainSubtypesEnum
from .global_time_eth_master import GlobalTimeEthMaster
from .global_time_eth_slave import GlobalTimeEthSlave
from .global_time_fr_master import GlobalTimeFrMaster
from .global_time_fr_slave import GlobalTimeFrSlave
from .global_time_gateway import GlobalTimeGateway
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .network_segment_identification import NetworkSegmentIdentification
from .pdu_triggering_ref_conditional import PduTriggeringRefConditional
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue
from .user_defined_global_time_master import UserDefinedGlobalTimeMaster
from .user_defined_global_time_slave import UserDefinedGlobalTimeSlave

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class GlobalTimeDomain:
    """
    This represents the ability to define a global time domain.

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
    :ivar communication_cluster_refs: This represents the collection of
        CommunicationClusters that shall implement the GlobalTimeDomain
        in terms of communication of global time information.
    :ivar debounce_time: Defines the minimum amount of time between two
        time sync messages are transmitted.
    :ivar domain_id: This represents the ID of the GlobalTimeDomain used
        in the network messages sent on behalf of global time
        management.
    :ivar follow_up_timeout_value: Rx timeout for the follow-up message.
        This is only relevant for selected bus systems Unit:seconds
    :ivar gateways: A GlobalTimeGateway may exist in the context of a
        GlobalTimeDomain to actively update the global time information
        as it is routed from one GlobalTimeDomain to another. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar global_time_correction_props: Defintion of attributes for rate
        and offset correction.
    :ivar global_time_domain_propertys: Additional properties of the
        GlobalTimeDomain. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar global_time_domain_props: Additional properties of the
        GlobalTimeDomain
    :ivar global_time_masters: This represents the single master of a
        GlobalTimeDomain. A GlobalTimeDomain may have no
        GlobalTimeDomain.master, e.g. when it gets its time from a GPS
        receiver. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar global_time_pdu_ref: This PDU will be taken to transmit the
        global time information from a GlobalTimeMaster to a the
        associated GlobalTimeSlaves.
    :ivar global_time_pdu_triggering_ref: This PduTriggering will be
        taken to transmit the global time information from a
        GlobalTimeMaster to a the associated GlobalTimeSlaves.
    :ivar global_time_sub_domains: By this means it is possible to
        create a hierarchy of subDomains where one global time domain
        can declare one or more other global time domains as its
        subDomains. This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar master: This represents the single master of a
        GlobalTimeDomain. A GlobalTimeDomain may have no
        GlobalTimeDomain.master, e.g. when it gets its time from a GPS
        receiver.
    :ivar network_segment_id: Defines the numerical identification of a
        GlobalTime sub domain.
    :ivar offset_time_domain_ref: Reference to a synchronized time
        domain this offset time domain is based on. The reference source
        is the offset time domain. The reference target is the
        synchronized time domain.
    :ivar pdu_triggerings: This PduTriggering will be taken to transmit
        the global time information from a GlobalTimeMaster to a the
        associated GlobalTimeSlaves. This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar slaves: This represents the collections of slaves of the
        GlobalTimeDomain. A GlobalTimeDomain may have no
        GlobalTimeDomain.slaves, e.g. when it propagates its time
        directly to sub domains. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar sub_domain_refs: By this means it is possible to create a
        hierarchy of subDomains where one global time domain can declare
        one or more other global time domains as its subDomains.
    :ivar sync_loss_threshold: This represents the minimum delta between
        the time value in two sync messages for which the sync loss flag
        is set.
    :ivar sync_loss_timeout: This attribute describes the timeout for
        the situation that the time synchronization gets lost in the
        scope of the time domain.
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
        name = "GLOBAL-TIME-DOMAIN"

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
        "GlobalTimeDomain.ShortNameFragments"
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
    annotations: Optional["GlobalTimeDomain.Annotations"] = field(
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
    communication_cluster_refs: Optional[
        "GlobalTimeDomain.CommunicationClusterRefs"
    ] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CLUSTER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    debounce_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "DEBOUNCE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    domain_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DOMAIN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    follow_up_timeout_value: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "FOLLOW-UP-TIMEOUT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    gateways: Optional["GlobalTimeDomain.Gateways"] = field(
        default=None,
        metadata={
            "name": "GATEWAYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_correction_props: Optional[GlobalTimeCorrectionProps] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-CORRECTION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_domain_propertys: Optional[
        "GlobalTimeDomain.GlobalTimeDomainPropertys"
    ] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-DOMAIN-PROPERTYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_domain_props: Optional[
        "GlobalTimeDomain.GlobalTimeDomainProps"
    ] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-DOMAIN-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_masters: Optional[
        "GlobalTimeDomain.GlobalTimeMasters"
    ] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-MASTERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_pdu_ref: Optional["GlobalTimeDomain.GlobalTimePduRef"] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_pdu_triggering_ref: Optional[
        "GlobalTimeDomain.GlobalTimePduTriggeringRef"
    ] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-PDU-TRIGGERING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_sub_domains: Optional[
        "GlobalTimeDomain.GlobalTimeSubDomains"
    ] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-SUB-DOMAINS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    master: Optional["GlobalTimeDomain.Master"] = field(
        default=None,
        metadata={
            "name": "MASTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_segment_id: Optional[NetworkSegmentIdentification] = field(
        default=None,
        metadata={
            "name": "NETWORK-SEGMENT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    offset_time_domain_ref: Optional[
        "GlobalTimeDomain.OffsetTimeDomainRef"
    ] = field(
        default=None,
        metadata={
            "name": "OFFSET-TIME-DOMAIN-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_triggerings: Optional["GlobalTimeDomain.PduTriggerings"] = field(
        default=None,
        metadata={
            "name": "PDU-TRIGGERINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    slaves: Optional["GlobalTimeDomain.Slaves"] = field(
        default=None,
        metadata={
            "name": "SLAVES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sub_domain_refs: Optional["GlobalTimeDomain.SubDomainRefs"] = field(
        default=None,
        metadata={
            "name": "SUB-DOMAIN-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_loss_threshold: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "SYNC-LOSS-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_loss_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "SYNC-LOSS-TIMEOUT",
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
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CommunicationClusterRefs:
        communication_cluster_ref: List[
            "GlobalTimeDomain.CommunicationClusterRefs.CommunicationClusterRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "COMMUNICATION-CLUSTER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class CommunicationClusterRef(Ref):
            dest: Optional[CommunicationClusterSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class Gateways:
        global_time_gateway: List[GlobalTimeGateway] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-GATEWAY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class GlobalTimeDomainPropertys:
        can_global_time_domain_props: List[CanGlobalTimeDomainProps] = field(
            default_factory=list,
            metadata={
                "name": "CAN-GLOBAL-TIME-DOMAIN-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eth_global_time_domain_props: List[EthGlobalTimeDomainProps] = field(
            default_factory=list,
            metadata={
                "name": "ETH-GLOBAL-TIME-DOMAIN-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        fr_global_time_domain_props: List[FrGlobalTimeDomainProps] = field(
            default_factory=list,
            metadata={
                "name": "FR-GLOBAL-TIME-DOMAIN-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class GlobalTimeDomainProps:
        can_global_time_domain_props: Optional[
            CanGlobalTimeDomainProps
        ] = field(
            default=None,
            metadata={
                "name": "CAN-GLOBAL-TIME-DOMAIN-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eth_global_time_domain_props: Optional[
            EthGlobalTimeDomainProps
        ] = field(
            default=None,
            metadata={
                "name": "ETH-GLOBAL-TIME-DOMAIN-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        fr_global_time_domain_props: Optional[FrGlobalTimeDomainProps] = field(
            default=None,
            metadata={
                "name": "FR-GLOBAL-TIME-DOMAIN-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class GlobalTimeMasters:
        global_time_can_master: List[GlobalTimeCanMaster] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-CAN-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_time_eth_master: List[GlobalTimeEthMaster] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-ETH-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_time_fr_master: List[GlobalTimeFrMaster] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-FR-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_global_time_master: List[
            UserDefinedGlobalTimeMaster
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-GLOBAL-TIME-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class GlobalTimePduRef(Ref):
        dest: Optional[GeneralPurposePduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class GlobalTimePduTriggeringRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class GlobalTimeSubDomains:
        global_time_domain_ref_conditional: List[
            GlobalTimeDomainRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-DOMAIN-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Master:
        global_time_can_master: Optional[GlobalTimeCanMaster] = field(
            default=None,
            metadata={
                "name": "GLOBAL-TIME-CAN-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_time_eth_master: Optional[GlobalTimeEthMaster] = field(
            default=None,
            metadata={
                "name": "GLOBAL-TIME-ETH-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_time_fr_master: Optional[GlobalTimeFrMaster] = field(
            default=None,
            metadata={
                "name": "GLOBAL-TIME-FR-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_global_time_master: Optional[
            UserDefinedGlobalTimeMaster
        ] = field(
            default=None,
            metadata={
                "name": "USER-DEFINED-GLOBAL-TIME-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class OffsetTimeDomainRef(Ref):
        dest: Optional[GlobalTimeDomainSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class PduTriggerings:
        pdu_triggering_ref_conditional: List[
            PduTriggeringRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "PDU-TRIGGERING-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Slaves:
        global_time_can_slave: List[GlobalTimeCanSlave] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-CAN-SLAVE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_time_eth_slave: List[GlobalTimeEthSlave] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-ETH-SLAVE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_time_fr_slave: List[GlobalTimeFrSlave] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-FR-SLAVE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_global_time_slave: List[
            UserDefinedGlobalTimeSlave
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-GLOBAL-TIME-SLAVE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SubDomainRefs:
        sub_domain_ref: List[
            "GlobalTimeDomain.SubDomainRefs.SubDomainRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SUB-DOMAIN-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SubDomainRef(Ref):
            dest: Optional[GlobalTimeDomainSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
