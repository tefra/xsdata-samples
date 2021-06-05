from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.communication_controller_subtypes_enum import CommunicationControllerSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.integer import Integer
from autosar.models.machine_design_subtypes_enum import MachineDesignSubtypesEnum
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.nm_coordinator_role_enum import NmCoordinatorRoleEnum
from autosar.models.nm_ecu_subtypes_enum import NmEcuSubtypesEnum
from autosar.models.nm_pdu_subtypes_enum import NmPduSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayNmNode:
    """
    FlexRay specific NM Node attributes.

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
    :ivar controller_ref: Association to an CommunicationController in
        the topology description.
    :ivar machine_ref: Reference to the machine that contains the
        NmNode.
    :ivar nm_coord_cluster: NmCoordinationCluster identification number.
    :ivar nm_coordinator_role: This attribute indicates the role the NM
        Coordinator will have on this channel.
    :ivar nm_if_ecu_ref: Reference to the NmEcu that contains this
        NmNode. (CommunicationController that is referenced by the
        NmNode shall be contained in the EcuInstance that is referenced
        by the NmEcu).
    :ivar nm_node_id: Node identifier of local NmNode. Shall be unique
        in the NmCluster.
    :ivar nm_passive_mode_enabled: Enables support of the Passive Mode.
        The passive mode is configurable per channel.
    :ivar rx_nm_pdu_refs: receive NM Pdu.
    :ivar tx_nm_pdu_refs: transmit NM Pdu
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar nm_instance_id: The NM instance identifier is used for
        reporting of development errors to DET. It must be unique for
        each NM instance within one ECU.
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
        name = "FLEXRAY-NM-NODE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["FlexrayNmNode.ShortNameFragments"] = field(
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
    annotations: Optional["FlexrayNmNode.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    controller_ref: Optional["FlexrayNmNode.ControllerRef"] = field(
        default=None,
        metadata={
            "name": "CONTROLLER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    machine_ref: Optional["FlexrayNmNode.MachineRef"] = field(
        default=None,
        metadata={
            "name": "MACHINE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_coord_cluster: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NM-COORD-CLUSTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_coordinator_role: Optional[NmCoordinatorRoleEnum] = field(
        default=None,
        metadata={
            "name": "NM-COORDINATOR-ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_if_ecu_ref: Optional["FlexrayNmNode.NmIfEcuRef"] = field(
        default=None,
        metadata={
            "name": "NM-IF-ECU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_node_id: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "NM-NODE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_passive_mode_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-PASSIVE-MODE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rx_nm_pdu_refs: Optional["FlexrayNmNode.RxNmPduRefs"] = field(
        default=None,
        metadata={
            "name": "RX-NM-PDU-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tx_nm_pdu_refs: Optional["FlexrayNmNode.TxNmPduRefs"] = field(
        default=None,
        metadata={
            "name": "TX-NM-PDU-REFS",
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
    nm_instance_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NM-INSTANCE-ID",
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
    class ControllerRef(Ref):
        dest: Optional[CommunicationControllerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class MachineRef(Ref):
        dest: Optional[MachineDesignSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class NmIfEcuRef(Ref):
        dest: Optional[NmEcuSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RxNmPduRefs:
        rx_nm_pdu_ref: List["FlexrayNmNode.RxNmPduRefs.RxNmPduRef"] = field(
            default_factory=list,
            metadata={
                "name": "RX-NM-PDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class RxNmPduRef(Ref):
            dest: Optional[NmPduSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TxNmPduRefs:
        tx_nm_pdu_ref: List["FlexrayNmNode.TxNmPduRefs.TxNmPduRef"] = field(
            default_factory=list,
            metadata={
                "name": "TX-NM-PDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class TxNmPduRef(Ref):
            dest: Optional[NmPduSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
