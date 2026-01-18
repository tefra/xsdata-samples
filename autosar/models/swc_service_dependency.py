from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .bsw_mgr_needs import BswMgrNeeds
from .category_string import CategoryString
from .com_mgr_user_needs import ComMgrUserNeeds
from .crypto_certificate_key_slot_needs import CryptoCertificateKeySlotNeeds
from .crypto_key_management_needs import CryptoKeyManagementNeeds
from .crypto_service_job_needs import CryptoServiceJobNeeds
from .crypto_service_needs import CryptoServiceNeeds
from .diagnostic_clear_condition_needs import DiagnosticClearConditionNeeds
from .diagnostic_communication_manager_needs import (
    DiagnosticCommunicationManagerNeeds,
)
from .diagnostic_component_needs import DiagnosticComponentNeeds
from .diagnostic_control_needs import DiagnosticControlNeeds
from .diagnostic_enable_condition_needs import DiagnosticEnableConditionNeeds
from .diagnostic_event_info_needs import DiagnosticEventInfoNeeds
from .diagnostic_event_manager_needs import DiagnosticEventManagerNeeds
from .diagnostic_event_needs import DiagnosticEventNeeds
from .diagnostic_generic_uds_needs import DiagnosticGenericUdsNeeds
from .diagnostic_indicator_needs import DiagnosticIndicatorNeeds
from .diagnostic_io_control_needs import DiagnosticIoControlNeeds
from .diagnostic_operation_cycle_needs import DiagnosticOperationCycleNeeds
from .diagnostic_request_file_transfer_needs import (
    DiagnosticRequestFileTransferNeeds,
)
from .diagnostic_response_on_event_needs import DiagnosticResponseOnEventNeeds
from .diagnostic_routine_needs import DiagnosticRoutineNeeds
from .diagnostic_storage_condition_needs import DiagnosticStorageConditionNeeds
from .diagnostic_upload_download_needs import DiagnosticUploadDownloadNeeds
from .diagnostic_value_needs import DiagnosticValueNeeds
from .diagnostics_communication_security_needs import (
    DiagnosticsCommunicationSecurityNeeds,
)
from .dlt_user_needs import DltUserNeeds
from .do_ip_activation_line_needs import DoIpActivationLineNeeds
from .do_ip_gid_needs import DoIpGidNeeds
from .do_ip_gid_synchronization_needs import DoIpGidSynchronizationNeeds
from .do_ip_power_mode_status_needs import DoIpPowerModeStatusNeeds
from .do_ip_routing_activation_authentication_needs import (
    DoIpRoutingActivationAuthenticationNeeds,
)
from .do_ip_routing_activation_confirmation_needs import (
    DoIpRoutingActivationConfirmationNeeds,
)
from .dtc_status_change_notification_needs import (
    DtcStatusChangeNotificationNeeds,
)
from .ecu_state_mgr_user_needs import EcuStateMgrUserNeeds
from .error_tracer_needs import ErrorTracerNeeds
from .function_inhibition_availability_needs import (
    FunctionInhibitionAvailabilityNeeds,
)
from .function_inhibition_needs import FunctionInhibitionNeeds
from .further_action_byte_needs import FurtherActionByteNeeds
from .global_supervision_needs import GlobalSupervisionNeeds
from .hardware_test_needs import HardwareTestNeeds
from .identifier import Identifier
from .ids_mgr_custom_timestamp_needs import IdsMgrCustomTimestampNeeds
from .ids_mgr_needs import IdsMgrNeeds
from .indicator_status_needs import IndicatorStatusNeeds
from .j_1939_dcm_dm_19_support import J1939DcmDm19Support
from .j_1939_rm_incoming_request_service_needs import (
    J1939RmIncomingRequestServiceNeeds,
)
from .j_1939_rm_outgoing_request_service_needs import (
    J1939RmOutgoingRequestServiceNeeds,
)
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nv_block_needs import NvBlockNeeds
from .obd_control_service_needs import ObdControlServiceNeeds
from .obd_info_service_needs import ObdInfoServiceNeeds
from .obd_monitor_service_needs import ObdMonitorServiceNeeds
from .obd_pid_service_needs import ObdPidServiceNeeds
from .obd_ratio_denominator_needs import ObdRatioDenominatorNeeds
from .obd_ratio_service_needs import ObdRatioServiceNeeds
from .port_group_subtypes_enum import PortGroupSubtypesEnum
from .ref import Ref
from .role_based_data_assignment import RoleBasedDataAssignment
from .role_based_data_type_assignment import RoleBasedDataTypeAssignment
from .role_based_port_assignment import RoleBasedPortAssignment
from .secure_on_board_communication_needs import (
    SecureOnBoardCommunicationNeeds,
)
from .short_name_fragment import ShortNameFragment
from .supervised_entity_checkpoint_needs import SupervisedEntityCheckpointNeeds
from .supervised_entity_needs import SupervisedEntityNeeds
from .symbolic_name_props import SymbolicNameProps
from .sync_time_base_mgr_user_needs import SyncTimeBaseMgrUserNeeds
from .v_2_x_fac_user_needs import V2XFacUserNeeds
from .v_2_x_m_user_needs import V2XMUserNeeds
from .vendor_specific_service_needs import VendorSpecificServiceNeeds
from .warning_indicator_requested_bit_needs import (
    WarningIndicatorRequestedBitNeeds,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcServiceDependency:
    """
    Specialization of ServiceDependency in the context of an
    SwcInternalBehavior.

    It allows to associate ports, port groups and (in special cases) data
    defined for an atomic software component to a given ServiceNeeds
    element.

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
    :ivar assigned_data_types: This is the role of the assignment data
        type in the given context. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was 1.
    :ivar symbolic_name_props: This attribute can be taken to contribute
        to the creation of symbolic name values.
    :ivar assigned_datas: Defines the role of an associated data object
        of the same component. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar assigned_ports: Defines the role of an associated port of the
        same component. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar represented_port_group_ref: This reference specifies an
        association between the ServiceNeeeds and a PortGroup, for
        example to request a communication mode which applies for
        communication via these ports. The referred PortGroup shall be
        local to this atomic SWC, but via the links between the
        PortGroups, a tool can evaluate this information such that all
        the ports linked via this port group on the same ECU can be
        found.
    :ivar service_needs: The associated ServiceNeeds.
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
        name = "SWC-SERVICE-DEPENDENCY"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: SwcServiceDependency.ShortNameFragments | None = field(
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
    annotations: SwcServiceDependency.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    assigned_data_types: SwcServiceDependency.AssignedDataTypes | None = (
        field(
            default=None,
            metadata={
                "name": "ASSIGNED-DATA-TYPES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    symbolic_name_props: SymbolicNameProps | None = field(
        default=None,
        metadata={
            "name": "SYMBOLIC-NAME-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    assigned_datas: SwcServiceDependency.AssignedDatas | None = field(
        default=None,
        metadata={
            "name": "ASSIGNED-DATAS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    assigned_ports: SwcServiceDependency.AssignedPorts | None = field(
        default=None,
        metadata={
            "name": "ASSIGNED-PORTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    represented_port_group_ref: SwcServiceDependency.RepresentedPortGroupRef | None = field(
        default=None,
        metadata={
            "name": "REPRESENTED-PORT-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_needs: SwcServiceDependency.ServiceNeeds | None = field(
        default=None,
        metadata={
            "name": "SERVICE-NEEDS",
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
    class AssignedDataTypes:
        role_based_data_type_assignment: list[RoleBasedDataTypeAssignment] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ROLE-BASED-DATA-TYPE-ASSIGNMENT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class AssignedDatas:
        role_based_data_assignment: list[RoleBasedDataAssignment] = field(
            default_factory=list,
            metadata={
                "name": "ROLE-BASED-DATA-ASSIGNMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class AssignedPorts:
        role_based_port_assignment: list[RoleBasedPortAssignment] = field(
            default_factory=list,
            metadata={
                "name": "ROLE-BASED-PORT-ASSIGNMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RepresentedPortGroupRef(Ref):
        dest: PortGroupSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ServiceNeeds:
        bsw_mgr_needs: BswMgrNeeds | None = field(
            default=None,
            metadata={
                "name": "BSW-MGR-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_mgr_user_needs: ComMgrUserNeeds | None = field(
            default=None,
            metadata={
                "name": "COM-MGR-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_certificate_key_slot_needs: CryptoCertificateKeySlotNeeds | None = field(
            default=None,
            metadata={
                "name": "CRYPTO-CERTIFICATE-KEY-SLOT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_key_management_needs: CryptoKeyManagementNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "CRYPTO-KEY-MANAGEMENT-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        crypto_service_job_needs: CryptoServiceJobNeeds | None = field(
            default=None,
            metadata={
                "name": "CRYPTO-SERVICE-JOB-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_service_needs: CryptoServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "CRYPTO-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_condition_needs: DiagnosticClearConditionNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-CONDITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_communication_manager_needs: DiagnosticCommunicationManagerNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_component_needs: DiagnosticComponentNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-COMPONENT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_control_needs: DiagnosticControlNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-CONTROL-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_enable_condition_needs: DiagnosticEnableConditionNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-ENABLE-CONDITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_info_needs: DiagnosticEventInfoNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "DIAGNOSTIC-EVENT-INFO-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_event_manager_needs: DiagnosticEventManagerNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-EVENT-MANAGER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_needs: DiagnosticEventNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-EVENT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_generic_uds_needs: DiagnosticGenericUdsNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "DIAGNOSTIC-GENERIC-UDS-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_indicator_needs: DiagnosticIndicatorNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-INDICATOR-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_io_control_needs: DiagnosticIoControlNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "DIAGNOSTIC-IO-CONTROL-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_operation_cycle_needs: DiagnosticOperationCycleNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-OPERATION-CYCLE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_file_transfer_needs: DiagnosticRequestFileTransferNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-FILE-TRANSFER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_response_on_event_needs: DiagnosticResponseOnEventNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-RESPONSE-ON-EVENT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_routine_needs: DiagnosticRoutineNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-ROUTINE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_storage_condition_needs: DiagnosticStorageConditionNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-STORAGE-CONDITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_upload_download_needs: DiagnosticUploadDownloadNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-UPLOAD-DOWNLOAD-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_value_needs: DiagnosticValueNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-VALUE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostics_communication_security_needs: DiagnosticsCommunicationSecurityNeeds | None = field(
            default=None,
            metadata={
                "name": "DIAGNOSTICS-COMMUNICATION-SECURITY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dlt_user_needs: DltUserNeeds | None = field(
            default=None,
            metadata={
                "name": "DLT-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_activation_line_needs: DoIpActivationLineNeeds | None = field(
            default=None,
            metadata={
                "name": "DO-IP-ACTIVATION-LINE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_gid_needs: DoIpGidNeeds | None = field(
            default=None,
            metadata={
                "name": "DO-IP-GID-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_gid_synchronization_needs: DoIpGidSynchronizationNeeds | None = field(
            default=None,
            metadata={
                "name": "DO-IP-GID-SYNCHRONIZATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_power_mode_status_needs: DoIpPowerModeStatusNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "DO-IP-POWER-MODE-STATUS-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        do_ip_routing_activation_authentication_needs: DoIpRoutingActivationAuthenticationNeeds | None = field(
            default=None,
            metadata={
                "name": "DO-IP-ROUTING-ACTIVATION-AUTHENTICATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_routing_activation_confirmation_needs: DoIpRoutingActivationConfirmationNeeds | None = field(
            default=None,
            metadata={
                "name": "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dtc_status_change_notification_needs: DtcStatusChangeNotificationNeeds | None = field(
            default=None,
            metadata={
                "name": "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecu_state_mgr_user_needs: EcuStateMgrUserNeeds | None = field(
            default=None,
            metadata={
                "name": "ECU-STATE-MGR-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        error_tracer_needs: ErrorTracerNeeds | None = field(
            default=None,
            metadata={
                "name": "ERROR-TRACER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        function_inhibition_availability_needs: FunctionInhibitionAvailabilityNeeds | None = field(
            default=None,
            metadata={
                "name": "FUNCTION-INHIBITION-AVAILABILITY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        function_inhibition_needs: FunctionInhibitionNeeds | None = field(
            default=None,
            metadata={
                "name": "FUNCTION-INHIBITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        further_action_byte_needs: FurtherActionByteNeeds | None = field(
            default=None,
            metadata={
                "name": "FURTHER-ACTION-BYTE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_supervision_needs: GlobalSupervisionNeeds | None = field(
            default=None,
            metadata={
                "name": "GLOBAL-SUPERVISION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        hardware_test_needs: HardwareTestNeeds | None = field(
            default=None,
            metadata={
                "name": "HARDWARE-TEST-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ids_mgr_custom_timestamp_needs: IdsMgrCustomTimestampNeeds | None = field(
            default=None,
            metadata={
                "name": "IDS-MGR-CUSTOM-TIMESTAMP-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ids_mgr_needs: IdsMgrNeeds | None = field(
            default=None,
            metadata={
                "name": "IDS-MGR-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        indicator_status_needs: IndicatorStatusNeeds | None = field(
            default=None,
            metadata={
                "name": "INDICATOR-STATUS-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_dcm_dm_19_support: J1939DcmDm19Support | None = field(
            default=None,
            metadata={
                "name": "J-1939-DCM-DM-19-SUPPORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_rm_incoming_request_service_needs: J1939RmIncomingRequestServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "J-1939-RM-INCOMING-REQUEST-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_rm_outgoing_request_service_needs: J1939RmOutgoingRequestServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "J-1939-RM-OUTGOING-REQUEST-SERVICE-NEEDS",
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
        obd_control_service_needs: ObdControlServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "OBD-CONTROL-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_info_service_needs: ObdInfoServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "OBD-INFO-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_monitor_service_needs: ObdMonitorServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "OBD-MONITOR-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_pid_service_needs: ObdPidServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "OBD-PID-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_ratio_denominator_needs: ObdRatioDenominatorNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "OBD-RATIO-DENOMINATOR-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        obd_ratio_service_needs: ObdRatioServiceNeeds | None = field(
            default=None,
            metadata={
                "name": "OBD-RATIO-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        secure_on_board_communication_needs: SecureOnBoardCommunicationNeeds | None = field(
            default=None,
            metadata={
                "name": "SECURE-ON-BOARD-COMMUNICATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        supervised_entity_checkpoint_needs: SupervisedEntityCheckpointNeeds | None = field(
            default=None,
            metadata={
                "name": "SUPERVISED-ENTITY-CHECKPOINT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        supervised_entity_needs: SupervisedEntityNeeds | None = field(
            default=None,
            metadata={
                "name": "SUPERVISED-ENTITY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sync_time_base_mgr_user_needs: SyncTimeBaseMgrUserNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "SYNC-TIME-BASE-MGR-USER-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        v_2_x_fac_user_needs: V2XFacUserNeeds | None = field(
            default=None,
            metadata={
                "name": "V-2-X-FAC-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        v_2_x_m_user_needs: V2XMUserNeeds | None = field(
            default=None,
            metadata={
                "name": "V-2-X-M-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        vendor_specific_service_needs: VendorSpecificServiceNeeds | None = (
            field(
                default=None,
                metadata={
                    "name": "VENDOR-SPECIFIC-SERVICE-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        warning_indicator_requested_bit_needs: WarningIndicatorRequestedBitNeeds | None = field(
            default=None,
            metadata={
                "name": "WARNING-INDICATOR-REQUESTED-BIT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
