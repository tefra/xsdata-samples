from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .bsw_mgr_needs import BswMgrNeeds
from .bsw_module_description_ref_conditional import (
    BswModuleDescriptionRefConditional,
)
from .bsw_module_entry_ref_conditional import BswModuleEntryRefConditional
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
from .positive_integer import PositiveInteger
from .secure_on_board_communication_needs import (
    SecureOnBoardCommunicationNeeds,
)
from .short_name_fragment import ShortNameFragment
from .supervised_entity_checkpoint_needs import SupervisedEntityCheckpointNeeds
from .supervised_entity_needs import SupervisedEntityNeeds
from .sync_time_base_mgr_user_needs import SyncTimeBaseMgrUserNeeds
from .v_2_x_fac_user_needs import V2XFacUserNeeds
from .v_2_x_m_user_needs import V2XMUserNeeds
from .vendor_specific_service_needs import VendorSpecificServiceNeeds
from .warning_indicator_requested_bit_needs import (
    WarningIndicatorRequestedBitNeeds,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswModuleDependency:
    """
    This class collects the dependencies of a BSW module or cluster on a
    certain other BSW module.

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
    :ivar target_module_id: AUTOSAR identifier of the target module of
        which the dependencies are defined. This information is
        optional, because the target module may also be identified by
        targetModuleRef.
    :ivar target_module_refs: Reference to the target module. It is an
        &lt;&lt;atpUriDef&gt;&gt; because the reference shall be used to
        identify the target module without actually needing the
        description of that target module. This property was modified
        due to atpVariation (DirectedAssociationPattern).
    :ivar required_entrys: Indicates an entry into another modules which
        is required by this module. This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar expected_callbacks: Indicates a callback expected to be called
        from another module and implemented by this module. This
        property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar service_items: A single item (example: Nv block) for which the
        quality of a service is defined. The aggregation is marked as
        &lt;&lt;atpSplitable&gt;&gt; to allow for extension during the
        ECU configuration process. This association is deprecated since
        R4.0.3, since ServiceNeeds shall be associated with the new
        element BswServiceDependency within the BswInternalBehavior.
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
        name = "BSW-MODULE-DEPENDENCY"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: None | BswModuleDependency.ShortNameFragments = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: None | BswModuleDependency.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_module_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TARGET-MODULE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_module_refs: None | BswModuleDependency.TargetModuleRefs = field(
        default=None,
        metadata={
            "name": "TARGET-MODULE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_entrys: None | BswModuleDependency.RequiredEntrys = field(
        default=None,
        metadata={
            "name": "REQUIRED-ENTRYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    expected_callbacks: None | BswModuleDependency.ExpectedCallbacks = field(
        default=None,
        metadata={
            "name": "EXPECTED-CALLBACKS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_items: None | BswModuleDependency.ServiceItems = field(
        default=None,
        metadata={
            "name": "SERVICE-ITEMS",
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
    class TargetModuleRefs:
        bsw_module_description_ref_conditional: list[
            BswModuleDescriptionRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-DESCRIPTION-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredEntrys:
        bsw_module_entry_ref_conditional: list[
            BswModuleEntryRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-ENTRY-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExpectedCallbacks:
        bsw_module_entry_ref_conditional: list[
            BswModuleEntryRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-ENTRY-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ServiceItems:
        bsw_mgr_needs: list[BswMgrNeeds] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MGR-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_mgr_user_needs: list[ComMgrUserNeeds] = field(
            default_factory=list,
            metadata={
                "name": "COM-MGR-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_certificate_key_slot_needs: list[
            CryptoCertificateKeySlotNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-CERTIFICATE-KEY-SLOT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_key_management_needs: list[CryptoKeyManagementNeeds] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-KEY-MANAGEMENT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_service_job_needs: list[CryptoServiceJobNeeds] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-SERVICE-JOB-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_service_needs: list[CryptoServiceNeeds] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_condition_needs: list[
            DiagnosticClearConditionNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-CONDITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_communication_manager_needs: list[
            DiagnosticCommunicationManagerNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_component_needs: list[DiagnosticComponentNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-COMPONENT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_control_needs: list[DiagnosticControlNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CONTROL-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_enable_condition_needs: list[
            DiagnosticEnableConditionNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ENABLE-CONDITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_info_needs: list[DiagnosticEventInfoNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-INFO-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_manager_needs: list[DiagnosticEventManagerNeeds] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-EVENT-MANAGER-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_event_needs: list[DiagnosticEventNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_generic_uds_needs: list[DiagnosticGenericUdsNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-GENERIC-UDS-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_indicator_needs: list[DiagnosticIndicatorNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-INDICATOR-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_io_control_needs: list[DiagnosticIoControlNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-IO-CONTROL-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_operation_cycle_needs: list[
            DiagnosticOperationCycleNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-OPERATION-CYCLE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_file_transfer_needs: list[
            DiagnosticRequestFileTransferNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-FILE-TRANSFER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_response_on_event_needs: list[
            DiagnosticResponseOnEventNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-RESPONSE-ON-EVENT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_routine_needs: list[DiagnosticRoutineNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ROUTINE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_storage_condition_needs: list[
            DiagnosticStorageConditionNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-STORAGE-CONDITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_upload_download_needs: list[
            DiagnosticUploadDownloadNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-UPLOAD-DOWNLOAD-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_value_needs: list[DiagnosticValueNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-VALUE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostics_communication_security_needs: list[
            DiagnosticsCommunicationSecurityNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTICS-COMMUNICATION-SECURITY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dlt_user_needs: list[DltUserNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DLT-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_activation_line_needs: list[DoIpActivationLineNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-ACTIVATION-LINE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_gid_needs: list[DoIpGidNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-GID-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_gid_synchronization_needs: list[DoIpGidSynchronizationNeeds] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DO-IP-GID-SYNCHRONIZATION-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        do_ip_power_mode_status_needs: list[DoIpPowerModeStatusNeeds] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-POWER-MODE-STATUS-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_routing_activation_authentication_needs: list[
            DoIpRoutingActivationAuthenticationNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-ROUTING-ACTIVATION-AUTHENTICATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_routing_activation_confirmation_needs: list[
            DoIpRoutingActivationConfirmationNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dtc_status_change_notification_needs: list[
            DtcStatusChangeNotificationNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecu_state_mgr_user_needs: list[EcuStateMgrUserNeeds] = field(
            default_factory=list,
            metadata={
                "name": "ECU-STATE-MGR-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        error_tracer_needs: list[ErrorTracerNeeds] = field(
            default_factory=list,
            metadata={
                "name": "ERROR-TRACER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        function_inhibition_availability_needs: list[
            FunctionInhibitionAvailabilityNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "FUNCTION-INHIBITION-AVAILABILITY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        function_inhibition_needs: list[FunctionInhibitionNeeds] = field(
            default_factory=list,
            metadata={
                "name": "FUNCTION-INHIBITION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        further_action_byte_needs: list[FurtherActionByteNeeds] = field(
            default_factory=list,
            metadata={
                "name": "FURTHER-ACTION-BYTE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_supervision_needs: list[GlobalSupervisionNeeds] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-SUPERVISION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        hardware_test_needs: list[HardwareTestNeeds] = field(
            default_factory=list,
            metadata={
                "name": "HARDWARE-TEST-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ids_mgr_custom_timestamp_needs: list[IdsMgrCustomTimestampNeeds] = (
            field(
                default_factory=list,
                metadata={
                    "name": "IDS-MGR-CUSTOM-TIMESTAMP-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        ids_mgr_needs: list[IdsMgrNeeds] = field(
            default_factory=list,
            metadata={
                "name": "IDS-MGR-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        indicator_status_needs: list[IndicatorStatusNeeds] = field(
            default_factory=list,
            metadata={
                "name": "INDICATOR-STATUS-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_dcm_dm_19_support: list[J1939DcmDm19Support] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-DCM-DM-19-SUPPORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_rm_incoming_request_service_needs: list[
            J1939RmIncomingRequestServiceNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-RM-INCOMING-REQUEST-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_rm_outgoing_request_service_needs: list[
            J1939RmOutgoingRequestServiceNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-RM-OUTGOING-REQUEST-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nv_block_needs: list[NvBlockNeeds] = field(
            default_factory=list,
            metadata={
                "name": "NV-BLOCK-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_control_service_needs: list[ObdControlServiceNeeds] = field(
            default_factory=list,
            metadata={
                "name": "OBD-CONTROL-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_info_service_needs: list[ObdInfoServiceNeeds] = field(
            default_factory=list,
            metadata={
                "name": "OBD-INFO-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_monitor_service_needs: list[ObdMonitorServiceNeeds] = field(
            default_factory=list,
            metadata={
                "name": "OBD-MONITOR-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_pid_service_needs: list[ObdPidServiceNeeds] = field(
            default_factory=list,
            metadata={
                "name": "OBD-PID-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_ratio_denominator_needs: list[ObdRatioDenominatorNeeds] = field(
            default_factory=list,
            metadata={
                "name": "OBD-RATIO-DENOMINATOR-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        obd_ratio_service_needs: list[ObdRatioServiceNeeds] = field(
            default_factory=list,
            metadata={
                "name": "OBD-RATIO-SERVICE-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        secure_on_board_communication_needs: list[
            SecureOnBoardCommunicationNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURE-ON-BOARD-COMMUNICATION-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        supervised_entity_checkpoint_needs: list[
            SupervisedEntityCheckpointNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "SUPERVISED-ENTITY-CHECKPOINT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        supervised_entity_needs: list[SupervisedEntityNeeds] = field(
            default_factory=list,
            metadata={
                "name": "SUPERVISED-ENTITY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sync_time_base_mgr_user_needs: list[SyncTimeBaseMgrUserNeeds] = field(
            default_factory=list,
            metadata={
                "name": "SYNC-TIME-BASE-MGR-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        v_2_x_fac_user_needs: list[V2XFacUserNeeds] = field(
            default_factory=list,
            metadata={
                "name": "V-2-X-FAC-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        v_2_x_m_user_needs: list[V2XMUserNeeds] = field(
            default_factory=list,
            metadata={
                "name": "V-2-X-M-USER-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        vendor_specific_service_needs: list[VendorSpecificServiceNeeds] = (
            field(
                default_factory=list,
                metadata={
                    "name": "VENDOR-SPECIFIC-SERVICE-NEEDS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        warning_indicator_requested_bit_needs: list[
            WarningIndicatorRequestedBitNeeds
        ] = field(
            default_factory=list,
            metadata={
                "name": "WARNING-INDICATOR-REQUESTED-BIT-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
