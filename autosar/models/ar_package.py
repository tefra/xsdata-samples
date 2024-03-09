from dataclasses import dataclass, field
from typing import List, Optional

from .acl_object_set import AclObjectSet
from .acl_operation import AclOperation
from .acl_permission import AclPermission
from .acl_role import AclRole
from .adaptive_application_sw_component_type import (
    AdaptiveApplicationSwComponentType,
)
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .alias_name_set import AliasNameSet
from .allocator import Allocator
from .ap_application_error import ApApplicationError
from .ap_application_error_domain import ApApplicationErrorDomain
from .ap_application_error_set import ApApplicationErrorSet
from .application_array_data_type import ApplicationArrayDataType
from .application_assoc_map_data_type import ApplicationAssocMapDataType
from .application_deferred_data_type import ApplicationDeferredDataType
from .application_partition import ApplicationPartition
from .application_primitive_data_type import ApplicationPrimitiveDataType
from .application_record_data_type import ApplicationRecordDataType
from .application_sw_component_type import ApplicationSwComponentType
from .blueprint_mapping_set import BlueprintMappingSet
from .blueprint_policy_list import BlueprintPolicyList
from .blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from .blueprint_policy_single import BlueprintPolicySingle
from .bsw_composition_timing import BswCompositionTiming
from .bsw_entry_relationship_set import BswEntryRelationshipSet
from .bsw_implementation import BswImplementation
from .bsw_module_description import BswModuleDescription
from .bsw_module_entry import BswModuleEntry
from .bsw_module_timing import BswModuleTiming
from .build_action_manifest import BuildActionManifest
from .bus_mirror_channel_mapping_can import BusMirrorChannelMappingCan
from .bus_mirror_channel_mapping_flexray import BusMirrorChannelMappingFlexray
from .bus_mirror_channel_mapping_ip import BusMirrorChannelMappingIp
from .bus_mirror_channel_mapping_user_defined import (
    BusMirrorChannelMappingUserDefined,
)
from .calibration_parameter_value_set import CalibrationParameterValueSet
from .can_cluster import CanCluster
from .can_frame import CanFrame
from .can_tp_config import CanTpConfig
from .category_string import CategoryString
from .client_id_definition_set import ClientIdDefinitionSet
from .client_server_interface import ClientServerInterface
from .client_server_interface_to_bsw_module_entry_blueprint_mapping import (
    ClientServerInterfaceToBswModuleEntryBlueprintMapping,
)
from .collection import Collection
from .com_certificate_to_crypto_certificate_mapping import (
    ComCertificateToCryptoCertificateMapping,
)
from .com_event_grant import ComEventGrant
from .com_event_grant_design import ComEventGrantDesign
from .com_field_grant import ComFieldGrant
from .com_field_grant_design import ComFieldGrantDesign
from .com_find_service_grant import ComFindServiceGrant
from .com_find_service_grant_design import ComFindServiceGrantDesign
from .com_key_to_crypto_key_slot_mapping import ComKeyToCryptoKeySlotMapping
from .com_method_grant import ComMethodGrant
from .com_method_grant_design import ComMethodGrantDesign
from .com_offer_service_grant import ComOfferServiceGrant
from .com_offer_service_grant_design import ComOfferServiceGrantDesign
from .com_sec_oc_to_crypto_key_slot_mapping import (
    ComSecOcToCryptoKeySlotMapping,
)
from .complex_device_driver_sw_component_type import (
    ComplexDeviceDriverSwComponentType,
)
from .composite_interface import CompositeInterface
from .composition_p_port_to_executable_p_port_mapping import (
    CompositionPPortToExecutablePPortMapping,
)
from .composition_r_port_to_executable_r_port_mapping import (
    CompositionRPortToExecutableRPortMapping,
)
from .composition_sw_component_type import CompositionSwComponentType
from .compu_method import CompuMethod
from .consistency_needs_blueprint_set import ConsistencyNeedsBlueprintSet
from .constant_specification import ConstantSpecification
from .constant_specification_mapping_set import ConstantSpecificationMappingSet
from .consumed_provided_service_instance_group import (
    ConsumedProvidedServiceInstanceGroup,
)
from .container_i_pdu import ContainerIPdu
from .coupling_element import CouplingElement
from .cp_software_cluster import CpSoftwareCluster
from .cp_software_cluster_binary_manifest_descriptor import (
    CpSoftwareClusterBinaryManifestDescriptor,
)
from .cp_software_cluster_mapping_set import CpSoftwareClusterMappingSet
from .cp_software_cluster_resource_pool import CpSoftwareClusterResourcePool
from .crypto_certificate_interface import CryptoCertificateInterface
from .crypto_certificate_to_port_prototype_mapping import (
    CryptoCertificateToPortPrototypeMapping,
)
from .crypto_key_slot_interface import CryptoKeySlotInterface
from .crypto_key_slot_to_port_prototype_mapping import (
    CryptoKeySlotToPortPrototypeMapping,
)
from .crypto_need_to_port_prototype_mapping import (
    CryptoNeedToPortPrototypeMapping,
)
from .crypto_provider_interface import CryptoProviderInterface
from .crypto_provider_to_port_prototype_mapping import (
    CryptoProviderToPortPrototypeMapping,
)
from .crypto_service_certificate import CryptoServiceCertificate
from .crypto_service_key import CryptoServiceKey
from .crypto_service_primitive import CryptoServicePrimitive
from .crypto_service_queue import CryptoServiceQueue
from .crypto_trust_master_interface import CryptoTrustMasterInterface
from .custom_cpp_implementation_data_type import (
    CustomCppImplementationDataType,
)
from .data_constr import DataConstr
from .data_exchange_point import DataExchangePoint
from .data_transformation_set import DataTransformationSet
from .data_type_mapping_set import DataTypeMappingSet
from .dcm_i_pdu import DcmIPdu
from .dds_provided_service_instance import DdsProvidedServiceInstance
from .dds_required_service_instance import DdsRequiredServiceInstance
from .dds_service_instance_to_machine_mapping import (
    DdsServiceInstanceToMachineMapping,
)
from .dds_service_interface_deployment import DdsServiceInterfaceDeployment
from .deterministic_client import DeterministicClient
from .diagnostic_access_permission import DiagnosticAccessPermission
from .diagnostic_aging import DiagnosticAging
from .diagnostic_clear_condition import DiagnosticClearCondition
from .diagnostic_clear_condition_group import DiagnosticClearConditionGroup
from .diagnostic_clear_condition_port_mapping import (
    DiagnosticClearConditionPortMapping,
)
from .diagnostic_clear_diagnostic_information import (
    DiagnosticClearDiagnosticInformation,
)
from .diagnostic_clear_diagnostic_information_class import (
    DiagnosticClearDiagnosticInformationClass,
)
from .diagnostic_clear_reset_emission_related_info import (
    DiagnosticClearResetEmissionRelatedInfo,
)
from .diagnostic_clear_reset_emission_related_info_class import (
    DiagnosticClearResetEmissionRelatedInfoClass,
)
from .diagnostic_com_control import DiagnosticComControl
from .diagnostic_com_control_class import DiagnosticComControlClass
from .diagnostic_condition_interface import DiagnosticConditionInterface
from .diagnostic_connection import DiagnosticConnection
from .diagnostic_contribution_set import DiagnosticContributionSet
from .diagnostic_control_dtc_setting import DiagnosticControlDtcSetting
from .diagnostic_control_dtc_setting_class import (
    DiagnosticControlDtcSettingClass,
)
from .diagnostic_custom_service_class import DiagnosticCustomServiceClass
from .diagnostic_custom_service_instance import DiagnosticCustomServiceInstance
from .diagnostic_data_element_interface import DiagnosticDataElementInterface
from .diagnostic_data_identifier import DiagnosticDataIdentifier
from .diagnostic_data_identifier_generic_interface import (
    DiagnosticDataIdentifierGenericInterface,
)
from .diagnostic_data_identifier_interface import (
    DiagnosticDataIdentifierInterface,
)
from .diagnostic_data_identifier_set import DiagnosticDataIdentifierSet
from .diagnostic_data_transfer import DiagnosticDataTransfer
from .diagnostic_data_transfer_class import DiagnosticDataTransferClass
from .diagnostic_dem_provided_data_mapping import (
    DiagnosticDemProvidedDataMapping,
)
from .diagnostic_do_ip_activation_line_interface import (
    DiagnosticDoIpActivationLineInterface,
)
from .diagnostic_do_ip_group_identification_interface import (
    DiagnosticDoIpGroupIdentificationInterface,
)
from .diagnostic_do_ip_power_mode_interface import (
    DiagnosticDoIpPowerModeInterface,
)
from .diagnostic_do_ip_trigger_vehicle_announcement_interface import (
    DiagnosticDoIpTriggerVehicleAnnouncementInterface,
)
from .diagnostic_download_interface import DiagnosticDownloadInterface
from .diagnostic_dtc_information_interface import (
    DiagnosticDtcInformationInterface,
)
from .diagnostic_dynamic_data_identifier import DiagnosticDynamicDataIdentifier
from .diagnostic_dynamically_define_data_identifier import (
    DiagnosticDynamicallyDefineDataIdentifier,
)
from .diagnostic_dynamically_define_data_identifier_class import (
    DiagnosticDynamicallyDefineDataIdentifierClass,
)
from .diagnostic_ecu_instance_props import DiagnosticEcuInstanceProps
from .diagnostic_ecu_reset import DiagnosticEcuReset
from .diagnostic_ecu_reset_class import DiagnosticEcuResetClass
from .diagnostic_ecu_reset_interface import DiagnosticEcuResetInterface
from .diagnostic_enable_condition import DiagnosticEnableCondition
from .diagnostic_enable_condition_group import DiagnosticEnableConditionGroup
from .diagnostic_enable_condition_port_mapping import (
    DiagnosticEnableConditionPortMapping,
)
from .diagnostic_environmental_condition import (
    DiagnosticEnvironmentalCondition,
)
from .diagnostic_event import DiagnosticEvent
from .diagnostic_event_interface import DiagnosticEventInterface
from .diagnostic_event_port_mapping import DiagnosticEventPortMapping
from .diagnostic_event_to_debounce_algorithm_mapping import (
    DiagnosticEventToDebounceAlgorithmMapping,
)
from .diagnostic_event_to_enable_condition_group_mapping import (
    DiagnosticEventToEnableConditionGroupMapping,
)
from .diagnostic_event_to_operation_cycle_mapping import (
    DiagnosticEventToOperationCycleMapping,
)
from .diagnostic_event_to_security_event_mapping import (
    DiagnosticEventToSecurityEventMapping,
)
from .diagnostic_event_to_storage_condition_group_mapping import (
    DiagnosticEventToStorageConditionGroupMapping,
)
from .diagnostic_event_to_trouble_code_j_1939_mapping import (
    DiagnosticEventToTroubleCodeJ1939Mapping,
)
from .diagnostic_event_to_trouble_code_uds_mapping import (
    DiagnosticEventToTroubleCodeUdsMapping,
)
from .diagnostic_extended_data_record import DiagnosticExtendedDataRecord
from .diagnostic_fim_alias_event import DiagnosticFimAliasEvent
from .diagnostic_fim_alias_event_group import DiagnosticFimAliasEventGroup
from .diagnostic_fim_alias_event_group_mapping import (
    DiagnosticFimAliasEventGroupMapping,
)
from .diagnostic_fim_alias_event_mapping import DiagnosticFimAliasEventMapping
from .diagnostic_fim_event_group import DiagnosticFimEventGroup
from .diagnostic_fim_function_mapping import DiagnosticFimFunctionMapping
from .diagnostic_freeze_frame import DiagnosticFreezeFrame
from .diagnostic_function_identifier import DiagnosticFunctionIdentifier
from .diagnostic_function_identifier_inhibit import (
    DiagnosticFunctionIdentifierInhibit,
)
from .diagnostic_generic_uds_interface import DiagnosticGenericUdsInterface
from .diagnostic_indicator import DiagnosticIndicator
from .diagnostic_indicator_interface import DiagnosticIndicatorInterface
from .diagnostic_indicator_port_mapping import DiagnosticIndicatorPortMapping
from .diagnostic_info_type import DiagnosticInfoType
from .diagnostic_inhibit_source_event_mapping import (
    DiagnosticInhibitSourceEventMapping,
)
from .diagnostic_io_control import DiagnosticIoControl
from .diagnostic_io_control_class import DiagnosticIoControlClass
from .diagnostic_iumpr import DiagnosticIumpr
from .diagnostic_iumpr_denominator_group import DiagnosticIumprDenominatorGroup
from .diagnostic_iumpr_group import DiagnosticIumprGroup
from .diagnostic_j_1939_expanded_freeze_frame import (
    DiagnosticJ1939ExpandedFreezeFrame,
)
from .diagnostic_j_1939_freeze_frame import DiagnosticJ1939FreezeFrame
from .diagnostic_j_1939_node import DiagnosticJ1939Node
from .diagnostic_j_1939_spn import DiagnosticJ1939Spn
from .diagnostic_j_1939_spn_mapping import DiagnosticJ1939SpnMapping
from .diagnostic_j_1939_sw_mapping import DiagnosticJ1939SwMapping
from .diagnostic_master_to_slave_event_mapping import (
    DiagnosticMasterToSlaveEventMapping,
)
from .diagnostic_master_to_slave_event_mapping_set import (
    DiagnosticMasterToSlaveEventMappingSet,
)
from .diagnostic_measurement_identifier import DiagnosticMeasurementIdentifier
from .diagnostic_memory_destination_mirror import (
    DiagnosticMemoryDestinationMirror,
)
from .diagnostic_memory_destination_port_mapping import (
    DiagnosticMemoryDestinationPortMapping,
)
from .diagnostic_memory_destination_primary import (
    DiagnosticMemoryDestinationPrimary,
)
from .diagnostic_memory_destination_user_defined import (
    DiagnosticMemoryDestinationUserDefined,
)
from .diagnostic_memory_identifier import DiagnosticMemoryIdentifier
from .diagnostic_monitor_interface import DiagnosticMonitorInterface
from .diagnostic_operation_cycle import DiagnosticOperationCycle
from .diagnostic_operation_cycle_interface import (
    DiagnosticOperationCycleInterface,
)
from .diagnostic_operation_cycle_port_mapping import (
    DiagnosticOperationCyclePortMapping,
)
from .diagnostic_parameter_identifier import DiagnosticParameterIdentifier
from .diagnostic_powertrain_freeze_frame import DiagnosticPowertrainFreezeFrame
from .diagnostic_protocol import DiagnosticProtocol
from .diagnostic_provided_data_mapping import DiagnosticProvidedDataMapping
from .diagnostic_read_data_by_identifier import DiagnosticReadDataByIdentifier
from .diagnostic_read_data_by_identifier_class import (
    DiagnosticReadDataByIdentifierClass,
)
from .diagnostic_read_data_by_periodic_id import DiagnosticReadDataByPeriodicId
from .diagnostic_read_data_by_periodic_id_class import (
    DiagnosticReadDataByPeriodicIdClass,
)
from .diagnostic_read_dtc_information import DiagnosticReadDtcInformation
from .diagnostic_read_dtc_information_class import (
    DiagnosticReadDtcInformationClass,
)
from .diagnostic_read_memory_by_address import DiagnosticReadMemoryByAddress
from .diagnostic_read_memory_by_address_class import (
    DiagnosticReadMemoryByAddressClass,
)
from .diagnostic_read_scaling_data_by_identifier import (
    DiagnosticReadScalingDataByIdentifier,
)
from .diagnostic_read_scaling_data_by_identifier_class import (
    DiagnosticReadScalingDataByIdentifierClass,
)
from .diagnostic_request_control_of_on_board_device import (
    DiagnosticRequestControlOfOnBoardDevice,
)
from .diagnostic_request_control_of_on_board_device_class import (
    DiagnosticRequestControlOfOnBoardDeviceClass,
)
from .diagnostic_request_current_powertrain_data import (
    DiagnosticRequestCurrentPowertrainData,
)
from .diagnostic_request_current_powertrain_data_class import (
    DiagnosticRequestCurrentPowertrainDataClass,
)
from .diagnostic_request_download import DiagnosticRequestDownload
from .diagnostic_request_download_class import DiagnosticRequestDownloadClass
from .diagnostic_request_emission_related_dtc import (
    DiagnosticRequestEmissionRelatedDtc,
)
from .diagnostic_request_emission_related_dtc_class import (
    DiagnosticRequestEmissionRelatedDtcClass,
)
from .diagnostic_request_emission_related_dtc_permanent_status import (
    DiagnosticRequestEmissionRelatedDtcPermanentStatus,
)
from .diagnostic_request_emission_related_dtc_permanent_status_class import (
    DiagnosticRequestEmissionRelatedDtcPermanentStatusClass,
)
from .diagnostic_request_file_transfer import DiagnosticRequestFileTransfer
from .diagnostic_request_file_transfer_class import (
    DiagnosticRequestFileTransferClass,
)
from .diagnostic_request_on_board_monitoring_test_results import (
    DiagnosticRequestOnBoardMonitoringTestResults,
)
from .diagnostic_request_on_board_monitoring_test_results_class import (
    DiagnosticRequestOnBoardMonitoringTestResultsClass,
)
from .diagnostic_request_powertrain_freeze_frame_data import (
    DiagnosticRequestPowertrainFreezeFrameData,
)
from .diagnostic_request_powertrain_freeze_frame_data_class import (
    DiagnosticRequestPowertrainFreezeFrameDataClass,
)
from .diagnostic_request_upload import DiagnosticRequestUpload
from .diagnostic_request_upload_class import DiagnosticRequestUploadClass
from .diagnostic_request_vehicle_info import DiagnosticRequestVehicleInfo
from .diagnostic_request_vehicle_info_class import (
    DiagnosticRequestVehicleInfoClass,
)
from .diagnostic_response_on_event import DiagnosticResponseOnEvent
from .diagnostic_response_on_event_class import DiagnosticResponseOnEventClass
from .diagnostic_routine import DiagnosticRoutine
from .diagnostic_routine_control import DiagnosticRoutineControl
from .diagnostic_routine_control_class import DiagnosticRoutineControlClass
from .diagnostic_routine_generic_interface import (
    DiagnosticRoutineGenericInterface,
)
from .diagnostic_routine_interface import DiagnosticRoutineInterface
from .diagnostic_security_access import DiagnosticSecurityAccess
from .diagnostic_security_access_class import DiagnosticSecurityAccessClass
from .diagnostic_security_event_reporting_mode_mapping import (
    DiagnosticSecurityEventReportingModeMapping,
)
from .diagnostic_security_level import DiagnosticSecurityLevel
from .diagnostic_security_level_interface import (
    DiagnosticSecurityLevelInterface,
)
from .diagnostic_security_level_port_mapping import (
    DiagnosticSecurityLevelPortMapping,
)
from .diagnostic_service_data_identifier_port_mapping import (
    DiagnosticServiceDataIdentifierPortMapping,
)
from .diagnostic_service_data_mapping import DiagnosticServiceDataMapping
from .diagnostic_service_generic_mapping import DiagnosticServiceGenericMapping
from .diagnostic_service_sw_mapping import DiagnosticServiceSwMapping
from .diagnostic_service_table import DiagnosticServiceTable
from .diagnostic_service_validation_interface import (
    DiagnosticServiceValidationInterface,
)
from .diagnostic_session import DiagnosticSession
from .diagnostic_session_control import DiagnosticSessionControl
from .diagnostic_session_control_class import DiagnosticSessionControlClass
from .diagnostic_software_cluster_props import DiagnosticSoftwareClusterProps
from .diagnostic_storage_condition import DiagnosticStorageCondition
from .diagnostic_storage_condition_group import DiagnosticStorageConditionGroup
from .diagnostic_storage_condition_port_mapping import (
    DiagnosticStorageConditionPortMapping,
)
from .diagnostic_test_result import DiagnosticTestResult
from .diagnostic_test_routine_identifier import DiagnosticTestRoutineIdentifier
from .diagnostic_transfer_exit import DiagnosticTransferExit
from .diagnostic_transfer_exit_class import DiagnosticTransferExitClass
from .diagnostic_trouble_code_group import DiagnosticTroubleCodeGroup
from .diagnostic_trouble_code_j_1939 import DiagnosticTroubleCodeJ1939
from .diagnostic_trouble_code_obd import DiagnosticTroubleCodeObd
from .diagnostic_trouble_code_props import DiagnosticTroubleCodeProps
from .diagnostic_trouble_code_uds import DiagnosticTroubleCodeUds
from .diagnostic_trouble_code_uds_to_clear_condition_group_mapping import (
    DiagnosticTroubleCodeUdsToClearConditionGroupMapping,
)
from .diagnostic_trouble_code_uds_to_trouble_code_obd_mapping import (
    DiagnosticTroubleCodeUdsToTroubleCodeObdMapping,
)
from .diagnostic_upload_interface import DiagnosticUploadInterface
from .diagnostic_write_data_by_identifier import (
    DiagnosticWriteDataByIdentifier,
)
from .diagnostic_write_data_by_identifier_class import (
    DiagnosticWriteDataByIdentifierClass,
)
from .diagnostic_write_memory_by_address import DiagnosticWriteMemoryByAddress
from .diagnostic_write_memory_by_address_class import (
    DiagnosticWriteMemoryByAddressClass,
)
from .dlt_log_channel_design import DltLogChannelDesign
from .dlt_log_channel_design_to_process_design_mapping import (
    DltLogChannelDesignToProcessDesignMapping,
)
from .dlt_log_channel_to_process_mapping import DltLogChannelToProcessMapping
from .dlt_message_collection_set import DltMessageCollectionSet
from .do_ip_tp_config import DoIpTpConfig
from .documentation import Documentation
from .e_2_e_profile_compatibility_props import E2EProfileCompatibilityProps
from .e_2_e_profile_configuration_set import E2EProfileConfigurationSet
from .ecu_abstraction_sw_component_type import EcuAbstractionSwComponentType
from .ecu_instance import EcuInstance
from .ecu_timing import EcuTiming
from .ecuc_definition_collection import EcucDefinitionCollection
from .ecuc_destination_uri_def_set import EcucDestinationUriDefSet
from .ecuc_module_configuration_values import EcucModuleConfigurationValues
from .ecuc_module_def import EcucModuleDef
from .ecuc_value_collection import EcucValueCollection
from .end_to_end_protection_set import EndToEndProtectionSet
from .enumeration_mapping_table import EnumerationMappingTable
from .eth_ip_props import EthIpProps
from .eth_tcp_ip_icmp_props import EthTcpIpIcmpProps
from .eth_tcp_ip_props import EthTcpIpProps
from .eth_tp_config import EthTpConfig
from .ethernet_cluster import EthernetCluster
from .ethernet_frame import EthernetFrame
from .ethernet_raw_data_stream_grant import EthernetRawDataStreamGrant
from .ethernet_raw_data_stream_mapping import EthernetRawDataStreamMapping
from .ethernet_wakeup_sleep_on_dataline_config_set import (
    EthernetWakeupSleepOnDatalineConfigSet,
)
from .evaluated_variant_set import EvaluatedVariantSet
from .executable import Executable
from .executable_timing import ExecutableTiming
from .flat_map import FlatMap
from .flexray_ar_tp_config import FlexrayArTpConfig
from .flexray_cluster import FlexrayCluster
from .flexray_frame import FlexrayFrame
from .flexray_tp_config import FlexrayTpConfig
from .fm_feature import FmFeature
from .fm_feature_map import FmFeatureMap
from .fm_feature_model import FmFeatureModel
from .fm_feature_selection_set import FmFeatureSelectionSet
from .function_group_set import FunctionGroupSet
from .gateway import Gateway
from .general_purpose_connection import GeneralPurposeConnection
from .general_purpose_i_pdu import GeneralPurposeIPdu
from .general_purpose_pdu import GeneralPurposePdu
from .generic_ethernet_frame import GenericEthernetFrame
from .global_time_domain import GlobalTimeDomain
from .hw_category import HwCategory
from .hw_element import HwElement
from .hw_type import HwType
from .i_pv_6_ext_header_filter_set import IPv6ExtHeaderFilterSet
from .i_signal import ISignal
from .i_signal_group import ISignalGroup
from .i_signal_i_pdu import ISignalIPdu
from .i_signal_i_pdu_group import ISignalIPduGroup
from .identifier import Identifier
from .ids_design import IdsDesign
from .idsm_instance import IdsmInstance
from .idsm_properties import IdsmProperties
from .ieee_1722_tp_ethernet_frame import Ieee1722TpEthernetFrame
from .implementation_data_type import ImplementationDataType
from .interface_mapping_set import InterfaceMappingSet
from .interpolation_routine_mapping_set import InterpolationRoutineMappingSet
from .ip_iam_remote_subject import IpIamRemoteSubject
from .ip_sec_config_props import IpSecConfigProps
from .ip_sec_iam_remote_subject import IpSecIamRemoteSubject
from .j_1939_cluster import J1939Cluster
from .j_1939_controller_application import J1939ControllerApplication
from .j_1939_dcm_i_pdu import J1939DcmIPdu
from .j_1939_tp_config import J1939TpConfig
from .keyword_set import KeywordSet
from .life_cycle_info_set import LifeCycleInfoSet
from .life_cycle_state_definition_group import LifeCycleStateDefinitionGroup
from .lin_cluster import LinCluster
from .lin_event_triggered_frame import LinEventTriggeredFrame
from .lin_sporadic_frame import LinSporadicFrame
from .lin_tp_config import LinTpConfig
from .lin_unconditional_frame import LinUnconditionalFrame
from .machine import Machine
from .machine_design import MachineDesign
from .machine_timing import MachineTiming
from .mc_function import McFunction
from .mc_group import McGroup
from .mode_declaration_group import ModeDeclarationGroup
from .mode_declaration_mapping_set import ModeDeclarationMappingSet
from .mode_switch_interface import ModeSwitchInterface
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .multiplexed_i_pdu import MultiplexedIPdu
from .n_pdu import NPdu
from .nm_config import NmConfig
from .nm_pdu import NmPdu
from .nv_block_sw_component_type import NvBlockSwComponentType
from .nv_data_interface import NvDataInterface
from .parameter_interface import ParameterInterface
from .parameter_sw_component_type import ParameterSwComponentType
from .pdur_i_pdu_group import PdurIPduGroup
from .persistency_deployment_element_to_crypto_key_slot_mapping import (
    PersistencyDeploymentElementToCryptoKeySlotMapping,
)
from .persistency_deployment_to_crypto_key_slot_mapping import (
    PersistencyDeploymentToCryptoKeySlotMapping,
)
from .persistency_deployment_to_dlt_log_channel_mapping import (
    PersistencyDeploymentToDltLogChannelMapping,
)
from .persistency_file_storage import PersistencyFileStorage
from .persistency_file_storage_interface import PersistencyFileStorageInterface
from .persistency_key_value_storage import PersistencyKeyValueStorage
from .persistency_key_value_storage_interface import (
    PersistencyKeyValueStorageInterface,
)
from .persistency_port_prototype_to_file_storage_mapping import (
    PersistencyPortPrototypeToFileStorageMapping,
)
from .persistency_port_prototype_to_key_value_storage_mapping import (
    PersistencyPortPrototypeToKeyValueStorageMapping,
)
from .phm_contribution_to_machine_mapping import (
    PhmContributionToMachineMapping,
)
from .phm_health_channel_interface import PhmHealthChannelInterface
from .phm_health_channel_recovery_notification_interface import (
    PhmHealthChannelRecoveryNotificationInterface,
)
from .phm_recovery_action_interface import PhmRecoveryActionInterface
from .phm_supervised_entity_interface import PhmSupervisedEntityInterface
from .phm_supervision_recovery_notification_interface import (
    PhmSupervisionRecoveryNotificationInterface,
)
from .physical_dimension import PhysicalDimension
from .physical_dimension_mapping_set import PhysicalDimensionMappingSet
from .platform_health_management_contribution import (
    PlatformHealthManagementContribution,
)
from .platform_module_ethernet_endpoint_configuration import (
    PlatformModuleEthernetEndpointConfiguration,
)
from .port_interface_mapping_set import PortInterfaceMappingSet
from .port_interface_to_data_type_mapping import PortInterfaceToDataTypeMapping
from .port_prototype_blueprint import PortPrototypeBlueprint
from .post_build_variant_criterion import PostBuildVariantCriterion
from .post_build_variant_criterion_value_set import (
    PostBuildVariantCriterionValueSet,
)
from .predefined_variant import PredefinedVariant
from .process import Process
from .process_design import ProcessDesign
from .process_design_to_machine_design_mapping_set import (
    ProcessDesignToMachineDesignMappingSet,
)
from .process_execution_error import ProcessExecutionError
from .process_to_machine_mapping_set import ProcessToMachineMappingSet
from .provided_service_instance_to_sw_cluster_design_p_port_prototype_mapping import (
    ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping,
)
from .provided_someip_service_instance import ProvidedSomeipServiceInstance
from .provided_user_defined_service_instance import (
    ProvidedUserDefinedServiceInstance,
)
from .rapid_prototyping_scenario import RapidPrototypingScenario
from .raw_data_stream_client_interface import RawDataStreamClientInterface
from .raw_data_stream_deployment import RawDataStreamDeployment
from .raw_data_stream_grant_design import RawDataStreamGrantDesign
from .raw_data_stream_server_interface import RawDataStreamServerInterface
from .recovery_notification_to_p_port_prototype_mapping import (
    RecoveryNotificationToPPortPrototypeMapping,
)
from .reference_base import ReferenceBase
from .required_service_instance_to_sw_cluster_design_r_port_prototype_mapping import (
    RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping,
)
from .required_someip_service_instance import RequiredSomeipServiceInstance
from .required_user_defined_service_instance import (
    RequiredUserDefinedServiceInstance,
)
from .rest_http_port_prototype_mapping import RestHttpPortPrototypeMapping
from .rest_service_interface import RestServiceInterface
from .sdg_def import SdgDef
from .secure_com_props_set import SecureComPropsSet
from .secure_communication_props_set import SecureCommunicationPropsSet
from .secured_i_pdu import SecuredIPdu
from .security_event_context_mapping_application import (
    SecurityEventContextMappingApplication,
)
from .security_event_context_mapping_bsw_module import (
    SecurityEventContextMappingBswModule,
)
from .security_event_context_mapping_comm_connector import (
    SecurityEventContextMappingCommConnector,
)
from .security_event_context_mapping_functional_cluster import (
    SecurityEventContextMappingFunctionalCluster,
)
from .security_event_definition import SecurityEventDefinition
from .security_event_filter_chain import SecurityEventFilterChain
from .security_event_mapping import SecurityEventMapping
from .security_event_report_interface import SecurityEventReportInterface
from .security_event_report_to_security_event_definition_mapping import (
    SecurityEventReportToSecurityEventDefinitionMapping,
)
from .sender_receiver_interface import SenderReceiverInterface
from .sensor_actuator_sw_component_type import SensorActuatorSwComponentType
from .serialization_technology import SerializationTechnology
from .service_instance_collection_set import ServiceInstanceCollectionSet
from .service_instance_to_port_prototype_mapping import (
    ServiceInstanceToPortPrototypeMapping,
)
from .service_instance_to_signal_mapping_set import (
    ServiceInstanceToSignalMappingSet,
)
from .service_interface import ServiceInterface
from .service_interface_mapping_set import ServiceInterfaceMappingSet
from .service_interface_pedigree import ServiceInterfacePedigree
from .service_proxy_sw_component_type import ServiceProxySwComponentType
from .service_sw_component_type import ServiceSwComponentType
from .service_timing import ServiceTiming
from .short_name_fragment import ShortNameFragment
from .signal_service_translation_props_set import (
    SignalServiceTranslationPropsSet,
)
from .so_ad_routing_group import SoAdRoutingGroup
from .socket_connection_ipdu_identifier_set import (
    SocketConnectionIpduIdentifierSet,
)
from .software_cluster import SoftwareCluster
from .software_cluster_design import SoftwareClusterDesign
from .software_package import SoftwarePackage
from .someip_data_prototype_transformation_props import (
    SomeipDataPrototypeTransformationProps,
)
from .someip_sd_client_event_group_timing_config import (
    SomeipSdClientEventGroupTimingConfig,
)
from .someip_sd_client_service_instance_config import (
    SomeipSdClientServiceInstanceConfig,
)
from .someip_sd_server_event_group_timing_config import (
    SomeipSdServerEventGroupTimingConfig,
)
from .someip_sd_server_service_instance_config import (
    SomeipSdServerServiceInstanceConfig,
)
from .someip_service_instance_to_machine_mapping import (
    SomeipServiceInstanceToMachineMapping,
)
from .someip_service_interface_deployment import (
    SomeipServiceInterfaceDeployment,
)
from .someip_tp_config import SomeipTpConfig
from .startup_config_set import StartupConfigSet
from .std_cpp_implementation_data_type import StdCppImplementationDataType
from .string import String
from .sw_addr_method import SwAddrMethod
from .sw_axis_type import SwAxisType
from .sw_base_type import SwBaseType
from .sw_record_layout import SwRecordLayout
from .sw_systemconst import SwSystemconst
from .sw_systemconstant_value_set import SwSystemconstantValueSet
from .swc_bsw_mapping import SwcBswMapping
from .swc_implementation import SwcImplementation
from .swc_timing import SwcTiming
from .synchronized_time_base_consumer_interface import (
    SynchronizedTimeBaseConsumerInterface,
)
from .synchronized_time_base_provider_interface import (
    SynchronizedTimeBaseProviderInterface,
)
from .system import System
from .system_signal import SystemSignal
from .system_signal_group import SystemSignalGroup
from .system_timing import SystemTiming
from .tcp_option_filter_set import TcpOptionFilterSet
from .td_cp_software_cluster_mapping_set import TdCpSoftwareClusterMappingSet
from .time_base_provider_to_persistency_mapping import (
    TimeBaseProviderToPersistencyMapping,
)
from .time_sync_port_prototype_to_time_base_mapping import (
    TimeSyncPortPrototypeToTimeBaseMapping,
)
from .tls_iam_remote_subject import TlsIamRemoteSubject
from .tlv_data_id_definition_set import TlvDataIdDefinitionSet
from .transformation_props_set import TransformationPropsSet
from .transformation_props_to_service_interface_element_mapping_set import (
    TransformationPropsToServiceInterfaceElementMappingSet,
)
from .trigger_interface import TriggerInterface
from .ttcan_cluster import TtcanCluster
from .unit import Unit
from .unit_group import UnitGroup
from .user_defined_cluster import UserDefinedCluster
from .user_defined_ethernet_frame import UserDefinedEthernetFrame
from .user_defined_i_pdu import UserDefinedIPdu
from .user_defined_pdu import UserDefinedPdu
from .user_defined_service_instance_to_machine_mapping import (
    UserDefinedServiceInstanceToMachineMapping,
)
from .user_defined_service_interface_deployment import (
    UserDefinedServiceInterfaceDeployment,
)
from .vehicle_package import VehiclePackage
from .vfb_timing import VfbTiming
from .view_map_set import ViewMapSet
from .xcp_pdu import XcpPdu

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ArPackage:
    """AUTOSAR package, allowing to create top level packages to structure the
    contained ARElements.

    ARPackages are open sets. This means that in a file based
    description system multiple files can be used to partially describe
    the contents of a package. This is an extended version of MSR's SW-
    SYSTEM.

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
    :ivar reference_bases: This denotes the reference bases for the
        package. This is the basis for all relative references within
        the package. The base needs to be selected according to the base
        attribute within the references.
    :ivar elements: Elements that are part of this package The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar ar_packages: This represents a sub package within an
        ARPackage, thus allowing for an unlimited package hierarchy. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
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
        name = "AR-PACKAGE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["ArPackage.ShortNameFragments"] = field(
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
    annotations: Optional["ArPackage.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blueprint_policys: Optional["ArPackage.BlueprintPolicys"] = field(
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
    reference_bases: Optional["ArPackage.ReferenceBases"] = field(
        default=None,
        metadata={
            "name": "REFERENCE-BASES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    elements: Optional["ArPackage.Elements"] = field(
        default=None,
        metadata={
            "name": "ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ar_packages: Optional["ArPackage.ArPackages"] = field(
        default=None,
        metadata={
            "name": "AR-PACKAGES",
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
    class BlueprintPolicys:
        blueprint_policy_list: List[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_not_modifiable: List[BlueprintPolicyNotModifiable] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        blueprint_policy_single: List[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ReferenceBases:
        reference_base: List[ReferenceBase] = field(
            default_factory=list,
            metadata={
                "name": "REFERENCE-BASE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Elements:
        acl_object_set: List[AclObjectSet] = field(
            default_factory=list,
            metadata={
                "name": "ACL-OBJECT-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        acl_operation: List[AclOperation] = field(
            default_factory=list,
            metadata={
                "name": "ACL-OPERATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        acl_permission: List[AclPermission] = field(
            default_factory=list,
            metadata={
                "name": "ACL-PERMISSION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        acl_role: List[AclRole] = field(
            default_factory=list,
            metadata={
                "name": "ACL-ROLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        adaptive_application_sw_component_type: List[
            AdaptiveApplicationSwComponentType
        ] = field(
            default_factory=list,
            metadata={
                "name": "ADAPTIVE-APPLICATION-SW-COMPONENT-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        alias_name_set: List[AliasNameSet] = field(
            default_factory=list,
            metadata={
                "name": "ALIAS-NAME-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        allocator: List[Allocator] = field(
            default_factory=list,
            metadata={
                "name": "ALLOCATOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ap_application_error: List[ApApplicationError] = field(
            default_factory=list,
            metadata={
                "name": "AP-APPLICATION-ERROR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ap_application_error_domain: List[ApApplicationErrorDomain] = field(
            default_factory=list,
            metadata={
                "name": "AP-APPLICATION-ERROR-DOMAIN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ap_application_error_set: List[ApApplicationErrorSet] = field(
            default_factory=list,
            metadata={
                "name": "AP-APPLICATION-ERROR-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_array_data_type: List[ApplicationArrayDataType] = field(
            default_factory=list,
            metadata={
                "name": "APPLICATION-ARRAY-DATA-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_assoc_map_data_type: List[ApplicationAssocMapDataType] = (
            field(
                default_factory=list,
                metadata={
                    "name": "APPLICATION-ASSOC-MAP-DATA-TYPE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        application_deferred_data_type: List[ApplicationDeferredDataType] = (
            field(
                default_factory=list,
                metadata={
                    "name": "APPLICATION-DEFERRED-DATA-TYPE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        application_partition: List[ApplicationPartition] = field(
            default_factory=list,
            metadata={
                "name": "APPLICATION-PARTITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_primitive_data_type: List[ApplicationPrimitiveDataType] = (
            field(
                default_factory=list,
                metadata={
                    "name": "APPLICATION-PRIMITIVE-DATA-TYPE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        application_record_data_type: List[ApplicationRecordDataType] = field(
            default_factory=list,
            metadata={
                "name": "APPLICATION-RECORD-DATA-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_sw_component_type: List[ApplicationSwComponentType] = (
            field(
                default_factory=list,
                metadata={
                    "name": "APPLICATION-SW-COMPONENT-TYPE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        blueprint_mapping_set: List[BlueprintMappingSet] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_composition_timing: List[BswCompositionTiming] = field(
            default_factory=list,
            metadata={
                "name": "BSW-COMPOSITION-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_entry_relationship_set: List[BswEntryRelationshipSet] = field(
            default_factory=list,
            metadata={
                "name": "BSW-ENTRY-RELATIONSHIP-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_implementation: List[BswImplementation] = field(
            default_factory=list,
            metadata={
                "name": "BSW-IMPLEMENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_module_description: List[BswModuleDescription] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-DESCRIPTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_module_entry: List[BswModuleEntry] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-ENTRY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_module_timing: List[BswModuleTiming] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        build_action_manifest: List[BuildActionManifest] = field(
            default_factory=list,
            metadata={
                "name": "BUILD-ACTION-MANIFEST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bus_mirror_channel_mapping_can: List[BusMirrorChannelMappingCan] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BUS-MIRROR-CHANNEL-MAPPING-CAN",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        bus_mirror_channel_mapping_flexray: List[
            BusMirrorChannelMappingFlexray
        ] = field(
            default_factory=list,
            metadata={
                "name": "BUS-MIRROR-CHANNEL-MAPPING-FLEXRAY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bus_mirror_channel_mapping_ip: List[BusMirrorChannelMappingIp] = field(
            default_factory=list,
            metadata={
                "name": "BUS-MIRROR-CHANNEL-MAPPING-IP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bus_mirror_channel_mapping_user_defined: List[
            BusMirrorChannelMappingUserDefined
        ] = field(
            default_factory=list,
            metadata={
                "name": "BUS-MIRROR-CHANNEL-MAPPING-USER-DEFINED",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        calibration_parameter_value_set: List[CalibrationParameterValueSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "CALIBRATION-PARAMETER-VALUE-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        can_cluster: List[CanCluster] = field(
            default_factory=list,
            metadata={
                "name": "CAN-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        can_frame: List[CanFrame] = field(
            default_factory=list,
            metadata={
                "name": "CAN-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        can_tp_config: List[CanTpConfig] = field(
            default_factory=list,
            metadata={
                "name": "CAN-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        client_id_definition_set: List[ClientIdDefinitionSet] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-ID-DEFINITION-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        client_server_interface: List[ClientServerInterface] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        client_server_interface_to_bsw_module_entry_blueprint_mapping: List[
            ClientServerInterfaceToBswModuleEntryBlueprintMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-INTERFACE-TO-BSW-MODULE-ENTRY-BLUEPRINT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        collection: List[Collection] = field(
            default_factory=list,
            metadata={
                "name": "COLLECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_certificate_to_crypto_certificate_mapping: List[
            ComCertificateToCryptoCertificateMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "COM-CERTIFICATE-TO-CRYPTO-CERTIFICATE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_event_grant: List[ComEventGrant] = field(
            default_factory=list,
            metadata={
                "name": "COM-EVENT-GRANT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_event_grant_design: List[ComEventGrantDesign] = field(
            default_factory=list,
            metadata={
                "name": "COM-EVENT-GRANT-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_field_grant: List[ComFieldGrant] = field(
            default_factory=list,
            metadata={
                "name": "COM-FIELD-GRANT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_field_grant_design: List[ComFieldGrantDesign] = field(
            default_factory=list,
            metadata={
                "name": "COM-FIELD-GRANT-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_find_service_grant: List[ComFindServiceGrant] = field(
            default_factory=list,
            metadata={
                "name": "COM-FIND-SERVICE-GRANT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_find_service_grant_design: List[ComFindServiceGrantDesign] = field(
            default_factory=list,
            metadata={
                "name": "COM-FIND-SERVICE-GRANT-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_key_to_crypto_key_slot_mapping: List[
            ComKeyToCryptoKeySlotMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "COM-KEY-TO-CRYPTO-KEY-SLOT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_method_grant: List[ComMethodGrant] = field(
            default_factory=list,
            metadata={
                "name": "COM-METHOD-GRANT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_method_grant_design: List[ComMethodGrantDesign] = field(
            default_factory=list,
            metadata={
                "name": "COM-METHOD-GRANT-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_offer_service_grant: List[ComOfferServiceGrant] = field(
            default_factory=list,
            metadata={
                "name": "COM-OFFER-SERVICE-GRANT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        com_offer_service_grant_design: List[ComOfferServiceGrantDesign] = (
            field(
                default_factory=list,
                metadata={
                    "name": "COM-OFFER-SERVICE-GRANT-DESIGN",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        com_sec_oc_to_crypto_key_slot_mapping: List[
            ComSecOcToCryptoKeySlotMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "COM-SEC-OC-TO-CRYPTO-KEY-SLOT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        complex_device_driver_sw_component_type: List[
            ComplexDeviceDriverSwComponentType
        ] = field(
            default_factory=list,
            metadata={
                "name": "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composite_interface: List[CompositeInterface] = field(
            default_factory=list,
            metadata={
                "name": "COMPOSITE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composition_p_port_to_executable_p_port_mapping: List[
            CompositionPPortToExecutablePPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "COMPOSITION-P-PORT-TO-EXECUTABLE-P-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composition_r_port_to_executable_r_port_mapping: List[
            CompositionRPortToExecutableRPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "COMPOSITION-R-PORT-TO-EXECUTABLE-R-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composition_sw_component_type: List[CompositionSwComponentType] = (
            field(
                default_factory=list,
                metadata={
                    "name": "COMPOSITION-SW-COMPONENT-TYPE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        compu_method: List[CompuMethod] = field(
            default_factory=list,
            metadata={
                "name": "COMPU-METHOD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        consistency_needs_blueprint_set: List[ConsistencyNeedsBlueprintSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "CONSISTENCY-NEEDS-BLUEPRINT-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        constant_specification: List[ConstantSpecification] = field(
            default_factory=list,
            metadata={
                "name": "CONSTANT-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        constant_specification_mapping_set: List[
            ConstantSpecificationMappingSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSTANT-SPECIFICATION-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        consumed_provided_service_instance_group: List[
            ConsumedProvidedServiceInstanceGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        container_i_pdu: List[ContainerIPdu] = field(
            default_factory=list,
            metadata={
                "name": "CONTAINER-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        coupling_element: List[CouplingElement] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        cp_software_cluster: List[CpSoftwareCluster] = field(
            default_factory=list,
            metadata={
                "name": "CP-SOFTWARE-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        cp_software_cluster_binary_manifest_descriptor: List[
            CpSoftwareClusterBinaryManifestDescriptor
        ] = field(
            default_factory=list,
            metadata={
                "name": "CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        cp_software_cluster_mapping_set: List[CpSoftwareClusterMappingSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "CP-SOFTWARE-CLUSTER-MAPPING-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        cp_software_cluster_resource_pool: List[
            CpSoftwareClusterResourcePool
        ] = field(
            default_factory=list,
            metadata={
                "name": "CP-SOFTWARE-CLUSTER-RESOURCE-POOL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_certificate_interface: List[CryptoCertificateInterface] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-CERTIFICATE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_certificate_to_port_prototype_mapping: List[
            CryptoCertificateToPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-CERTIFICATE-TO-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_key_slot_interface: List[CryptoKeySlotInterface] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-KEY-SLOT-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_key_slot_to_port_prototype_mapping: List[
            CryptoKeySlotToPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-KEY-SLOT-TO-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_need_to_port_prototype_mapping: List[
            CryptoNeedToPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-NEED-TO-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_provider_interface: List[CryptoProviderInterface] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-PROVIDER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_provider_to_port_prototype_mapping: List[
            CryptoProviderToPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-PROVIDER-TO-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_service_certificate: List[CryptoServiceCertificate] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-SERVICE-CERTIFICATE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_service_key: List[CryptoServiceKey] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-SERVICE-KEY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_service_primitive: List[CryptoServicePrimitive] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-SERVICE-PRIMITIVE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_service_queue: List[CryptoServiceQueue] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-SERVICE-QUEUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_trust_master_interface: List[CryptoTrustMasterInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "CRYPTO-TRUST-MASTER-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        custom_cpp_implementation_data_type: List[
            CustomCppImplementationDataType
        ] = field(
            default_factory=list,
            metadata={
                "name": "CUSTOM-CPP-IMPLEMENTATION-DATA-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_constr: List[DataConstr] = field(
            default_factory=list,
            metadata={
                "name": "DATA-CONSTR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_exchange_point: List[DataExchangePoint] = field(
            default_factory=list,
            metadata={
                "name": "DATA-EXCHANGE-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_transformation_set: List[DataTransformationSet] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TRANSFORMATION-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_type_mapping_set: List[DataTypeMappingSet] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TYPE-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dcm_i_pdu: List[DcmIPdu] = field(
            default_factory=list,
            metadata={
                "name": "DCM-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dds_provided_service_instance: List[DdsProvidedServiceInstance] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DDS-PROVIDED-SERVICE-INSTANCE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        dds_required_service_instance: List[DdsRequiredServiceInstance] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DDS-REQUIRED-SERVICE-INSTANCE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        dds_service_instance_to_machine_mapping: List[
            DdsServiceInstanceToMachineMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DDS-SERVICE-INSTANCE-TO-MACHINE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dds_service_interface_deployment: List[
            DdsServiceInterfaceDeployment
        ] = field(
            default_factory=list,
            metadata={
                "name": "DDS-SERVICE-INTERFACE-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        deterministic_client: List[DeterministicClient] = field(
            default_factory=list,
            metadata={
                "name": "DETERMINISTIC-CLIENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_access_permission: List[DiagnosticAccessPermission] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ACCESS-PERMISSION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_aging: List[DiagnosticAging] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-AGING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_condition: List[DiagnosticClearCondition] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_condition_group: List[
            DiagnosticClearConditionGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-CONDITION-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_condition_port_mapping: List[
            DiagnosticClearConditionPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-CONDITION-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_diagnostic_information: List[
            DiagnosticClearDiagnosticInformation
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_diagnostic_information_class: List[
            DiagnosticClearDiagnosticInformationClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_reset_emission_related_info: List[
            DiagnosticClearResetEmissionRelatedInfo
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_clear_reset_emission_related_info_class: List[
            DiagnosticClearResetEmissionRelatedInfoClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_com_control: List[DiagnosticComControl] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-COM-CONTROL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_com_control_class: List[DiagnosticComControlClass] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-COM-CONTROL-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_condition_interface: List[DiagnosticConditionInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-CONDITION-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_connection: List[DiagnosticConnection] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CONNECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_contribution_set: List[DiagnosticContributionSet] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CONTRIBUTION-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_control_dtc_setting: List[DiagnosticControlDtcSetting] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-CONTROL-DTC-SETTING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_control_dtc_setting_class: List[
            DiagnosticControlDtcSettingClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_custom_service_class: List[DiagnosticCustomServiceClass] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-CUSTOM-SERVICE-CLASS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_custom_service_instance: List[
            DiagnosticCustomServiceInstance
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_data_element_interface: List[
            DiagnosticDataElementInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-ELEMENT-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_data_identifier: List[DiagnosticDataIdentifier] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_data_identifier_generic_interface: List[
            DiagnosticDataIdentifierGenericInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-IDENTIFIER-GENERIC-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_data_identifier_interface: List[
            DiagnosticDataIdentifierInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-IDENTIFIER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_data_identifier_set: List[DiagnosticDataIdentifierSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-DATA-IDENTIFIER-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_data_transfer: List[DiagnosticDataTransfer] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-TRANSFER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_data_transfer_class: List[DiagnosticDataTransferClass] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-DATA-TRANSFER-CLASS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_dem_provided_data_mapping: List[
            DiagnosticDemProvidedDataMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DEM-PROVIDED-DATA-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_do_ip_activation_line_interface: List[
            DiagnosticDoIpActivationLineInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DO-IP-ACTIVATION-LINE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_do_ip_group_identification_interface: List[
            DiagnosticDoIpGroupIdentificationInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DO-IP-GROUP-IDENTIFICATION-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_do_ip_power_mode_interface: List[
            DiagnosticDoIpPowerModeInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DO-IP-POWER-MODE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_do_ip_trigger_vehicle_announcement_interface: List[
            DiagnosticDoIpTriggerVehicleAnnouncementInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DO-IP-TRIGGER-VEHICLE-ANNOUNCEMENT-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_download_interface: List[DiagnosticDownloadInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-DOWNLOAD-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_dtc_information_interface: List[
            DiagnosticDtcInformationInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DTC-INFORMATION-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_dynamic_data_identifier: List[
            DiagnosticDynamicDataIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_dynamically_define_data_identifier: List[
            DiagnosticDynamicallyDefineDataIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_dynamically_define_data_identifier_class: List[
            DiagnosticDynamicallyDefineDataIdentifierClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_ecu_instance_props: List[DiagnosticEcuInstanceProps] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-ECU-INSTANCE-PROPS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_ecu_reset: List[DiagnosticEcuReset] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ECU-RESET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_ecu_reset_class: List[DiagnosticEcuResetClass] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ECU-RESET-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_ecu_reset_interface: List[DiagnosticEcuResetInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-ECU-RESET-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_enable_condition: List[DiagnosticEnableCondition] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ENABLE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_enable_condition_group: List[
            DiagnosticEnableConditionGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ENABLE-CONDITION-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_enable_condition_port_mapping: List[
            DiagnosticEnableConditionPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_environmental_condition: List[
            DiagnosticEnvironmentalCondition
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ENVIRONMENTAL-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event: List[DiagnosticEvent] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_interface: List[DiagnosticEventInterface] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_port_mapping: List[DiagnosticEventPortMapping] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-EVENT-PORT-MAPPING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_event_to_debounce_algorithm_mapping: List[
            DiagnosticEventToDebounceAlgorithmMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_to_enable_condition_group_mapping: List[
            DiagnosticEventToEnableConditionGroupMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_to_operation_cycle_mapping: List[
            DiagnosticEventToOperationCycleMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_to_security_event_mapping: List[
            DiagnosticEventToSecurityEventMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-TO-SECURITY-EVENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_to_storage_condition_group_mapping: List[
            DiagnosticEventToStorageConditionGroupMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_to_trouble_code_j_1939_mapping: List[
            DiagnosticEventToTroubleCodeJ1939Mapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-J-1939-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_event_to_trouble_code_uds_mapping: List[
            DiagnosticEventToTroubleCodeUdsMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_extended_data_record: List[DiagnosticExtendedDataRecord] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-EXTENDED-DATA-RECORD",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_fim_alias_event: List[DiagnosticFimAliasEvent] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FIM-ALIAS-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_fim_alias_event_group: List[
            DiagnosticFimAliasEventGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_fim_alias_event_group_mapping: List[
            DiagnosticFimAliasEventGroupMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_fim_alias_event_mapping: List[
            DiagnosticFimAliasEventMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FIM-ALIAS-EVENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_fim_event_group: List[DiagnosticFimEventGroup] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FIM-EVENT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_fim_function_mapping: List[DiagnosticFimFunctionMapping] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-FIM-FUNCTION-MAPPING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_freeze_frame: List[DiagnosticFreezeFrame] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FREEZE-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_function_identifier: List[DiagnosticFunctionIdentifier] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-FUNCTION-IDENTIFIER",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_function_identifier_inhibit: List[
            DiagnosticFunctionIdentifierInhibit
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FUNCTION-IDENTIFIER-INHIBIT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_generic_uds_interface: List[
            DiagnosticGenericUdsInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-GENERIC-UDS-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_indicator: List[DiagnosticIndicator] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-INDICATOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_indicator_interface: List[DiagnosticIndicatorInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-INDICATOR-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_indicator_port_mapping: List[
            DiagnosticIndicatorPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-INDICATOR-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_info_type: List[DiagnosticInfoType] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-INFO-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_inhibit_source_event_mapping: List[
            DiagnosticInhibitSourceEventMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-INHIBIT-SOURCE-EVENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_io_control: List[DiagnosticIoControl] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-IO-CONTROL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_io_control_class: List[DiagnosticIoControlClass] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-IO-CONTROL-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_iumpr: List[DiagnosticIumpr] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-IUMPR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_iumpr_denominator_group: List[
            DiagnosticIumprDenominatorGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_iumpr_group: List[DiagnosticIumprGroup] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-IUMPR-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_j_1939_expanded_freeze_frame: List[
            DiagnosticJ1939ExpandedFreezeFrame
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_j_1939_freeze_frame: List[DiagnosticJ1939FreezeFrame] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-J-1939-FREEZE-FRAME",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_j_1939_node: List[DiagnosticJ1939Node] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-J-1939-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_j_1939_spn: List[DiagnosticJ1939Spn] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-J-1939-SPN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_j_1939_spn_mapping: List[DiagnosticJ1939SpnMapping] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-J-1939-SPN-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_j_1939_sw_mapping: List[DiagnosticJ1939SwMapping] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-J-1939-SW-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_master_to_slave_event_mapping: List[
            DiagnosticMasterToSlaveEventMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_master_to_slave_event_mapping_set: List[
            DiagnosticMasterToSlaveEventMappingSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_measurement_identifier: List[
            DiagnosticMeasurementIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MEASUREMENT-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_memory_destination_mirror: List[
            DiagnosticMemoryDestinationMirror
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MEMORY-DESTINATION-MIRROR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_memory_destination_port_mapping: List[
            DiagnosticMemoryDestinationPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MEMORY-DESTINATION-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_memory_destination_primary: List[
            DiagnosticMemoryDestinationPrimary
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_memory_destination_user_defined: List[
            DiagnosticMemoryDestinationUserDefined
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_memory_identifier: List[DiagnosticMemoryIdentifier] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MEMORY-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_monitor_interface: List[DiagnosticMonitorInterface] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-MONITOR-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_operation_cycle: List[DiagnosticOperationCycle] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-OPERATION-CYCLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_operation_cycle_interface: List[
            DiagnosticOperationCycleInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-OPERATION-CYCLE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_operation_cycle_port_mapping: List[
            DiagnosticOperationCyclePortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_parameter_identifier: List[
            DiagnosticParameterIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-PARAMETER-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_powertrain_freeze_frame: List[
            DiagnosticPowertrainFreezeFrame
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_protocol: List[DiagnosticProtocol] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-PROTOCOL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_provided_data_mapping: List[
            DiagnosticProvidedDataMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-PROVIDED-DATA-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_data_by_identifier: List[
            DiagnosticReadDataByIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_data_by_identifier_class: List[
            DiagnosticReadDataByIdentifierClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_data_by_periodic_id: List[
            DiagnosticReadDataByPeriodicId
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_data_by_periodic_id_class: List[
            DiagnosticReadDataByPeriodicIdClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_dtc_information: List[DiagnosticReadDtcInformation] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-READ-DTC-INFORMATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_read_dtc_information_class: List[
            DiagnosticReadDtcInformationClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-DTC-INFORMATION-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_memory_by_address: List[
            DiagnosticReadMemoryByAddress
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_memory_by_address_class: List[
            DiagnosticReadMemoryByAddressClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_scaling_data_by_identifier: List[
            DiagnosticReadScalingDataByIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_read_scaling_data_by_identifier_class: List[
            DiagnosticReadScalingDataByIdentifierClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_control_of_on_board_device: List[
            DiagnosticRequestControlOfOnBoardDevice
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_control_of_on_board_device_class: List[
            DiagnosticRequestControlOfOnBoardDeviceClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_current_powertrain_data: List[
            DiagnosticRequestCurrentPowertrainData
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_current_powertrain_data_class: List[
            DiagnosticRequestCurrentPowertrainDataClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_download: List[DiagnosticRequestDownload] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-DOWNLOAD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_download_class: List[
            DiagnosticRequestDownloadClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_emission_related_dtc: List[
            DiagnosticRequestEmissionRelatedDtc
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_emission_related_dtc_class: List[
            DiagnosticRequestEmissionRelatedDtcClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_emission_related_dtc_permanent_status: List[
            DiagnosticRequestEmissionRelatedDtcPermanentStatus
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_emission_related_dtc_permanent_status_class: List[
            DiagnosticRequestEmissionRelatedDtcPermanentStatusClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_file_transfer: List[
            DiagnosticRequestFileTransfer
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-FILE-TRANSFER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_file_transfer_class: List[
            DiagnosticRequestFileTransferClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_on_board_monitoring_test_results: List[
            DiagnosticRequestOnBoardMonitoringTestResults
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_on_board_monitoring_test_results_class: List[
            DiagnosticRequestOnBoardMonitoringTestResultsClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_powertrain_freeze_frame_data: List[
            DiagnosticRequestPowertrainFreezeFrameData
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_powertrain_freeze_frame_data_class: List[
            DiagnosticRequestPowertrainFreezeFrameDataClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_upload: List[DiagnosticRequestUpload] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-UPLOAD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_request_upload_class: List[DiagnosticRequestUploadClass] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-REQUEST-UPLOAD-CLASS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_request_vehicle_info: List[DiagnosticRequestVehicleInfo] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-REQUEST-VEHICLE-INFO",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_request_vehicle_info_class: List[
            DiagnosticRequestVehicleInfoClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_response_on_event: List[DiagnosticResponseOnEvent] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-RESPONSE-ON-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_response_on_event_class: List[
            DiagnosticResponseOnEventClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_routine: List[DiagnosticRoutine] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ROUTINE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_routine_control: List[DiagnosticRoutineControl] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ROUTINE-CONTROL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_routine_control_class: List[
            DiagnosticRoutineControlClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ROUTINE-CONTROL-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_routine_generic_interface: List[
            DiagnosticRoutineGenericInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ROUTINE-GENERIC-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_routine_interface: List[DiagnosticRoutineInterface] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ROUTINE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_security_access: List[DiagnosticSecurityAccess] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SECURITY-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_security_access_class: List[
            DiagnosticSecurityAccessClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SECURITY-ACCESS-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_security_event_reporting_mode_mapping: List[
            DiagnosticSecurityEventReportingModeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SECURITY-EVENT-REPORTING-MODE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_security_level: List[DiagnosticSecurityLevel] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SECURITY-LEVEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_security_level_interface: List[
            DiagnosticSecurityLevelInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SECURITY-LEVEL-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_security_level_port_mapping: List[
            DiagnosticSecurityLevelPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SECURITY-LEVEL-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_service_data_identifier_port_mapping: List[
            DiagnosticServiceDataIdentifierPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SERVICE-DATA-IDENTIFIER-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_service_data_mapping: List[DiagnosticServiceDataMapping] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-SERVICE-DATA-MAPPING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_service_generic_mapping: List[
            DiagnosticServiceGenericMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SERVICE-GENERIC-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_service_sw_mapping: List[DiagnosticServiceSwMapping] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-SERVICE-SW-MAPPING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_service_table: List[DiagnosticServiceTable] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SERVICE-TABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_service_validation_interface: List[
            DiagnosticServiceValidationInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SERVICE-VALIDATION-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_session: List[DiagnosticSession] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SESSION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_session_control: List[DiagnosticSessionControl] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SESSION-CONTROL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_session_control_class: List[
            DiagnosticSessionControlClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SESSION-CONTROL-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_software_cluster_props: List[
            DiagnosticSoftwareClusterProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SOFTWARE-CLUSTER-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_storage_condition: List[DiagnosticStorageCondition] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-STORAGE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_storage_condition_group: List[
            DiagnosticStorageConditionGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-STORAGE-CONDITION-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_storage_condition_port_mapping: List[
            DiagnosticStorageConditionPortMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_test_result: List[DiagnosticTestResult] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-TEST-RESULT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_test_routine_identifier: List[
            DiagnosticTestRoutineIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_transfer_exit: List[DiagnosticTransferExit] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-TRANSFER-EXIT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_transfer_exit_class: List[DiagnosticTransferExitClass] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-TRANSFER-EXIT-CLASS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_trouble_code_group: List[DiagnosticTroubleCodeGroup] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-TROUBLE-CODE-GROUP",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_trouble_code_j_1939: List[DiagnosticTroubleCodeJ1939] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-TROUBLE-CODE-J-1939",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_trouble_code_obd: List[DiagnosticTroubleCodeObd] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-TROUBLE-CODE-OBD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_trouble_code_props: List[DiagnosticTroubleCodeProps] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-TROUBLE-CODE-PROPS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_trouble_code_uds: List[DiagnosticTroubleCodeUds] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-TROUBLE-CODE-UDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_trouble_code_uds_to_clear_condition_group_mapping: List[
            DiagnosticTroubleCodeUdsToClearConditionGroupMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-TROUBLE-CODE-UDS-TO-CLEAR-CONDITION-GROUP-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_trouble_code_uds_to_trouble_code_obd_mapping: List[
            DiagnosticTroubleCodeUdsToTroubleCodeObdMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-TROUBLE-CODE-UDS-TO-TROUBLE-CODE-OBD-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_upload_interface: List[DiagnosticUploadInterface] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-UPLOAD-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_write_data_by_identifier: List[
            DiagnosticWriteDataByIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_write_data_by_identifier_class: List[
            DiagnosticWriteDataByIdentifierClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_write_memory_by_address: List[
            DiagnosticWriteMemoryByAddress
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_write_memory_by_address_class: List[
            DiagnosticWriteMemoryByAddressClass
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dlt_log_channel_design: List[DltLogChannelDesign] = field(
            default_factory=list,
            metadata={
                "name": "DLT-LOG-CHANNEL-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dlt_log_channel_design_to_process_design_mapping: List[
            DltLogChannelDesignToProcessDesignMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DLT-LOG-CHANNEL-DESIGN-TO-PROCESS-DESIGN-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dlt_log_channel_to_process_mapping: List[
            DltLogChannelToProcessMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "DLT-LOG-CHANNEL-TO-PROCESS-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        dlt_message_collection_set: List[DltMessageCollectionSet] = field(
            default_factory=list,
            metadata={
                "name": "DLT-MESSAGE-COLLECTION-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_tp_config: List[DoIpTpConfig] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        documentation: List[Documentation] = field(
            default_factory=list,
            metadata={
                "name": "DOCUMENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        e_2_e_profile_compatibility_props: List[
            E2EProfileCompatibilityProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "E-2-E-PROFILE-COMPATIBILITY-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        e_2_e_profile_configuration_set: List[E2EProfileConfigurationSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "E-2-E-PROFILE-CONFIGURATION-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        ecu_abstraction_sw_component_type: List[
            EcuAbstractionSwComponentType
        ] = field(
            default_factory=list,
            metadata={
                "name": "ECU-ABSTRACTION-SW-COMPONENT-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecu_instance: List[EcuInstance] = field(
            default_factory=list,
            metadata={
                "name": "ECU-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecu_timing: List[EcuTiming] = field(
            default_factory=list,
            metadata={
                "name": "ECU-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_definition_collection: List[EcucDefinitionCollection] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-DEFINITION-COLLECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_destination_uri_def_set: List[EcucDestinationUriDefSet] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-DESTINATION-URI-DEF-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_module_configuration_values: List[
            EcucModuleConfigurationValues
        ] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-MODULE-CONFIGURATION-VALUES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_module_def: List[EcucModuleDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-MODULE-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_value_collection: List[EcucValueCollection] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-VALUE-COLLECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        end_to_end_protection_set: List[EndToEndProtectionSet] = field(
            default_factory=list,
            metadata={
                "name": "END-TO-END-PROTECTION-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        enumeration_mapping_table: List[EnumerationMappingTable] = field(
            default_factory=list,
            metadata={
                "name": "ENUMERATION-MAPPING-TABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eth_ip_props: List[EthIpProps] = field(
            default_factory=list,
            metadata={
                "name": "ETH-IP-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eth_tcp_ip_icmp_props: List[EthTcpIpIcmpProps] = field(
            default_factory=list,
            metadata={
                "name": "ETH-TCP-IP-ICMP-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eth_tcp_ip_props: List[EthTcpIpProps] = field(
            default_factory=list,
            metadata={
                "name": "ETH-TCP-IP-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eth_tp_config: List[EthTpConfig] = field(
            default_factory=list,
            metadata={
                "name": "ETH-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_cluster: List[EthernetCluster] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_frame: List[EthernetFrame] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_raw_data_stream_grant: List[EthernetRawDataStreamGrant] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ETHERNET-RAW-DATA-STREAM-GRANT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        ethernet_raw_data_stream_mapping: List[
            EthernetRawDataStreamMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-RAW-DATA-STREAM-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_wakeup_sleep_on_dataline_config_set: List[
            EthernetWakeupSleepOnDatalineConfigSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        evaluated_variant_set: List[EvaluatedVariantSet] = field(
            default_factory=list,
            metadata={
                "name": "EVALUATED-VARIANT-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        executable: List[Executable] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        executable_timing: List[ExecutableTiming] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTABLE-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flat_map: List[FlatMap] = field(
            default_factory=list,
            metadata={
                "name": "FLAT-MAP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_ar_tp_config: List[FlexrayArTpConfig] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-AR-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_cluster: List[FlexrayCluster] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_frame: List[FlexrayFrame] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_tp_config: List[FlexrayTpConfig] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        fm_feature: List[FmFeature] = field(
            default_factory=list,
            metadata={
                "name": "FM-FEATURE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        fm_feature_map: List[FmFeatureMap] = field(
            default_factory=list,
            metadata={
                "name": "FM-FEATURE-MAP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        fm_feature_model: List[FmFeatureModel] = field(
            default_factory=list,
            metadata={
                "name": "FM-FEATURE-MODEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        fm_feature_selection_set: List[FmFeatureSelectionSet] = field(
            default_factory=list,
            metadata={
                "name": "FM-FEATURE-SELECTION-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        function_group_set: List[FunctionGroupSet] = field(
            default_factory=list,
            metadata={
                "name": "FUNCTION-GROUP-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        gateway: List[Gateway] = field(
            default_factory=list,
            metadata={
                "name": "GATEWAY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        general_purpose_connection: List[GeneralPurposeConnection] = field(
            default_factory=list,
            metadata={
                "name": "GENERAL-PURPOSE-CONNECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        general_purpose_i_pdu: List[GeneralPurposeIPdu] = field(
            default_factory=list,
            metadata={
                "name": "GENERAL-PURPOSE-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        general_purpose_pdu: List[GeneralPurposePdu] = field(
            default_factory=list,
            metadata={
                "name": "GENERAL-PURPOSE-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        generic_ethernet_frame: List[GenericEthernetFrame] = field(
            default_factory=list,
            metadata={
                "name": "GENERIC-ETHERNET-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        global_time_domain: List[GlobalTimeDomain] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-TIME-DOMAIN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        hw_category: List[HwCategory] = field(
            default_factory=list,
            metadata={
                "name": "HW-CATEGORY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        hw_element: List[HwElement] = field(
            default_factory=list,
            metadata={
                "name": "HW-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        hw_type: List[HwType] = field(
            default_factory=list,
            metadata={
                "name": "HW-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        i_pv_6_ext_header_filter_set: List[IPv6ExtHeaderFilterSet] = field(
            default_factory=list,
            metadata={
                "name": "I-PV-6-EXT-HEADER-FILTER-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        i_signal: List[ISignal] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        i_signal_group: List[ISignalGroup] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        i_signal_i_pdu: List[ISignalIPdu] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        i_signal_i_pdu_group: List[ISignalIPduGroup] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-I-PDU-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ids_design: List[IdsDesign] = field(
            default_factory=list,
            metadata={
                "name": "IDS-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        idsm_instance: List[IdsmInstance] = field(
            default_factory=list,
            metadata={
                "name": "IDSM-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        idsm_properties: List[IdsmProperties] = field(
            default_factory=list,
            metadata={
                "name": "IDSM-PROPERTIES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ieee_1722_tp_ethernet_frame: List[Ieee1722TpEthernetFrame] = field(
            default_factory=list,
            metadata={
                "name": "IEEE-1722-TP-ETHERNET-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        implementation_data_type: List[ImplementationDataType] = field(
            default_factory=list,
            metadata={
                "name": "IMPLEMENTATION-DATA-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        interface_mapping_set: List[InterfaceMappingSet] = field(
            default_factory=list,
            metadata={
                "name": "INTERFACE-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        interpolation_routine_mapping_set: List[
            InterpolationRoutineMappingSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "INTERPOLATION-ROUTINE-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ip_iam_remote_subject: List[IpIamRemoteSubject] = field(
            default_factory=list,
            metadata={
                "name": "IP-IAM-REMOTE-SUBJECT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ip_sec_config_props: List[IpSecConfigProps] = field(
            default_factory=list,
            metadata={
                "name": "IP-SEC-CONFIG-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ip_sec_iam_remote_subject: List[IpSecIamRemoteSubject] = field(
            default_factory=list,
            metadata={
                "name": "IP-SEC-IAM-REMOTE-SUBJECT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_cluster: List[J1939Cluster] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_controller_application: List[J1939ControllerApplication] = (
            field(
                default_factory=list,
                metadata={
                    "name": "J-1939-CONTROLLER-APPLICATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        j_1939_dcm_i_pdu: List[J1939DcmIPdu] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-DCM-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_tp_config: List[J1939TpConfig] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        keyword_set: List[KeywordSet] = field(
            default_factory=list,
            metadata={
                "name": "KEYWORD-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        life_cycle_info_set: List[LifeCycleInfoSet] = field(
            default_factory=list,
            metadata={
                "name": "LIFE-CYCLE-INFO-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        life_cycle_state_definition_group: List[
            LifeCycleStateDefinitionGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "LIFE-CYCLE-STATE-DEFINITION-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_cluster: List[LinCluster] = field(
            default_factory=list,
            metadata={
                "name": "LIN-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_event_triggered_frame: List[LinEventTriggeredFrame] = field(
            default_factory=list,
            metadata={
                "name": "LIN-EVENT-TRIGGERED-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_sporadic_frame: List[LinSporadicFrame] = field(
            default_factory=list,
            metadata={
                "name": "LIN-SPORADIC-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_tp_config: List[LinTpConfig] = field(
            default_factory=list,
            metadata={
                "name": "LIN-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_unconditional_frame: List[LinUnconditionalFrame] = field(
            default_factory=list,
            metadata={
                "name": "LIN-UNCONDITIONAL-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        machine: List[Machine] = field(
            default_factory=list,
            metadata={
                "name": "MACHINE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        machine_design: List[MachineDesign] = field(
            default_factory=list,
            metadata={
                "name": "MACHINE-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        machine_timing: List[MachineTiming] = field(
            default_factory=list,
            metadata={
                "name": "MACHINE-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mc_function: List[McFunction] = field(
            default_factory=list,
            metadata={
                "name": "MC-FUNCTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mc_group: List[McGroup] = field(
            default_factory=list,
            metadata={
                "name": "MC-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mode_declaration_group: List[ModeDeclarationGroup] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mode_declaration_mapping_set: List[ModeDeclarationMappingSet] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mode_switch_interface: List[ModeSwitchInterface] = field(
            default_factory=list,
            metadata={
                "name": "MODE-SWITCH-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        multiplexed_i_pdu: List[MultiplexedIPdu] = field(
            default_factory=list,
            metadata={
                "name": "MULTIPLEXED-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        n_pdu: List[NPdu] = field(
            default_factory=list,
            metadata={
                "name": "N-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nm_config: List[NmConfig] = field(
            default_factory=list,
            metadata={
                "name": "NM-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nm_pdu: List[NmPdu] = field(
            default_factory=list,
            metadata={
                "name": "NM-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nv_block_sw_component_type: List[NvBlockSwComponentType] = field(
            default_factory=list,
            metadata={
                "name": "NV-BLOCK-SW-COMPONENT-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nv_data_interface: List[NvDataInterface] = field(
            default_factory=list,
            metadata={
                "name": "NV-DATA-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        parameter_interface: List[ParameterInterface] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        parameter_sw_component_type: List[ParameterSwComponentType] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-SW-COMPONENT-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        pdur_i_pdu_group: List[PdurIPduGroup] = field(
            default_factory=list,
            metadata={
                "name": "PDUR-I-PDU-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_deployment_element_to_crypto_key_slot_mapping: List[
            PersistencyDeploymentElementToCryptoKeySlotMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-DEPLOYMENT-ELEMENT-TO-CRYPTO-KEY-SLOT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_deployment_to_crypto_key_slot_mapping: List[
            PersistencyDeploymentToCryptoKeySlotMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-DEPLOYMENT-TO-CRYPTO-KEY-SLOT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_deployment_to_dlt_log_channel_mapping: List[
            PersistencyDeploymentToDltLogChannelMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-DEPLOYMENT-TO-DLT-LOG-CHANNEL-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_file_storage: List[PersistencyFileStorage] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-FILE-STORAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_file_storage_interface: List[
            PersistencyFileStorageInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-FILE-STORAGE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_key_value_storage: List[PersistencyKeyValueStorage] = (
            field(
                default_factory=list,
                metadata={
                    "name": "PERSISTENCY-KEY-VALUE-STORAGE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        persistency_key_value_storage_interface: List[
            PersistencyKeyValueStorageInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-KEY-VALUE-STORAGE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_port_prototype_to_file_storage_mapping: List[
            PersistencyPortPrototypeToFileStorageMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-PORT-PROTOTYPE-TO-FILE-STORAGE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_port_prototype_to_key_value_storage_mapping: List[
            PersistencyPortPrototypeToKeyValueStorageMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-PORT-PROTOTYPE-TO-KEY-VALUE-STORAGE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        phm_contribution_to_machine_mapping: List[
            PhmContributionToMachineMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PHM-CONTRIBUTION-TO-MACHINE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        phm_health_channel_interface: List[PhmHealthChannelInterface] = field(
            default_factory=list,
            metadata={
                "name": "PHM-HEALTH-CHANNEL-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        phm_health_channel_recovery_notification_interface: List[
            PhmHealthChannelRecoveryNotificationInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "PHM-HEALTH-CHANNEL-RECOVERY-NOTIFICATION-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        phm_recovery_action_interface: List[PhmRecoveryActionInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "PHM-RECOVERY-ACTION-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        phm_supervised_entity_interface: List[PhmSupervisedEntityInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "PHM-SUPERVISED-ENTITY-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        phm_supervision_recovery_notification_interface: List[
            PhmSupervisionRecoveryNotificationInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "PHM-SUPERVISION-RECOVERY-NOTIFICATION-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        physical_dimension: List[PhysicalDimension] = field(
            default_factory=list,
            metadata={
                "name": "PHYSICAL-DIMENSION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        physical_dimension_mapping_set: List[PhysicalDimensionMappingSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "PHYSICAL-DIMENSION-MAPPING-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        platform_health_management_contribution: List[
            PlatformHealthManagementContribution
        ] = field(
            default_factory=list,
            metadata={
                "name": "PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        platform_module_ethernet_endpoint_configuration: List[
            PlatformModuleEthernetEndpointConfiguration
        ] = field(
            default_factory=list,
            metadata={
                "name": "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        port_interface_mapping_set: List[PortInterfaceMappingSet] = field(
            default_factory=list,
            metadata={
                "name": "PORT-INTERFACE-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        port_interface_to_data_type_mapping: List[
            PortInterfaceToDataTypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PORT-INTERFACE-TO-DATA-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        port_prototype_blueprint: List[PortPrototypeBlueprint] = field(
            default_factory=list,
            metadata={
                "name": "PORT-PROTOTYPE-BLUEPRINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        post_build_variant_criterion: List[PostBuildVariantCriterion] = field(
            default_factory=list,
            metadata={
                "name": "POST-BUILD-VARIANT-CRITERION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        post_build_variant_criterion_value_set: List[
            PostBuildVariantCriterionValueSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "POST-BUILD-VARIANT-CRITERION-VALUE-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        predefined_variant: List[PredefinedVariant] = field(
            default_factory=list,
            metadata={
                "name": "PREDEFINED-VARIANT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        process: List[Process] = field(
            default_factory=list,
            metadata={
                "name": "PROCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        process_design: List[ProcessDesign] = field(
            default_factory=list,
            metadata={
                "name": "PROCESS-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        process_design_to_machine_design_mapping_set: List[
            ProcessDesignToMachineDesignMappingSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "PROCESS-DESIGN-TO-MACHINE-DESIGN-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        process_execution_error: List[ProcessExecutionError] = field(
            default_factory=list,
            metadata={
                "name": "PROCESS-EXECUTION-ERROR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        process_to_machine_mapping_set: List[ProcessToMachineMappingSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "PROCESS-TO-MACHINE-MAPPING-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        provided_service_instance_to_sw_cluster_design_p_port_prototype_mapping: List[
            ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PROVIDED-SERVICE-INSTANCE-TO-SW-CLUSTER-DESIGN-P-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        provided_someip_service_instance: List[
            ProvidedSomeipServiceInstance
        ] = field(
            default_factory=list,
            metadata={
                "name": "PROVIDED-SOMEIP-SERVICE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        provided_user_defined_service_instance: List[
            ProvidedUserDefinedServiceInstance
        ] = field(
            default_factory=list,
            metadata={
                "name": "PROVIDED-USER-DEFINED-SERVICE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rapid_prototyping_scenario: List[RapidPrototypingScenario] = field(
            default_factory=list,
            metadata={
                "name": "RAPID-PROTOTYPING-SCENARIO",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        raw_data_stream_client_interface: List[
            RawDataStreamClientInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "RAW-DATA-STREAM-CLIENT-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        raw_data_stream_deployment: List[RawDataStreamDeployment] = field(
            default_factory=list,
            metadata={
                "name": "RAW-DATA-STREAM-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        raw_data_stream_grant_design: List[RawDataStreamGrantDesign] = field(
            default_factory=list,
            metadata={
                "name": "RAW-DATA-STREAM-GRANT-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        raw_data_stream_server_interface: List[
            RawDataStreamServerInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "RAW-DATA-STREAM-SERVER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        recovery_notification_to_p_port_prototype_mapping: List[
            RecoveryNotificationToPPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "RECOVERY-NOTIFICATION-TO-P-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        required_service_instance_to_sw_cluster_design_r_port_prototype_mapping: List[
            RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "REQUIRED-SERVICE-INSTANCE-TO-SW-CLUSTER-DESIGN-R-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        required_someip_service_instance: List[
            RequiredSomeipServiceInstance
        ] = field(
            default_factory=list,
            metadata={
                "name": "REQUIRED-SOMEIP-SERVICE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        required_user_defined_service_instance: List[
            RequiredUserDefinedServiceInstance
        ] = field(
            default_factory=list,
            metadata={
                "name": "REQUIRED-USER-DEFINED-SERVICE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rest_http_port_prototype_mapping: List[
            RestHttpPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "REST-HTTP-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rest_service_interface: List[RestServiceInterface] = field(
            default_factory=list,
            metadata={
                "name": "REST-SERVICE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sdg_def: List[SdgDef] = field(
            default_factory=list,
            metadata={
                "name": "SDG-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        secure_com_props_set: List[SecureComPropsSet] = field(
            default_factory=list,
            metadata={
                "name": "SECURE-COM-PROPS-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        secure_communication_props_set: List[SecureCommunicationPropsSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "SECURE-COMMUNICATION-PROPS-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        secured_i_pdu: List[SecuredIPdu] = field(
            default_factory=list,
            metadata={
                "name": "SECURED-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_context_mapping_application: List[
            SecurityEventContextMappingApplication
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-CONTEXT-MAPPING-APPLICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_context_mapping_bsw_module: List[
            SecurityEventContextMappingBswModule
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-CONTEXT-MAPPING-BSW-MODULE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_context_mapping_comm_connector: List[
            SecurityEventContextMappingCommConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-CONTEXT-MAPPING-COMM-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_context_mapping_functional_cluster: List[
            SecurityEventContextMappingFunctionalCluster
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-CONTEXT-MAPPING-FUNCTIONAL-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_definition: List[SecurityEventDefinition] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-DEFINITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_filter_chain: List[SecurityEventFilterChain] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-FILTER-CHAIN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_mapping: List[SecurityEventMapping] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        security_event_report_interface: List[SecurityEventReportInterface] = (
            field(
                default_factory=list,
                metadata={
                    "name": "SECURITY-EVENT-REPORT-INTERFACE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        security_event_report_to_security_event_definition_mapping: List[
            SecurityEventReportToSecurityEventDefinitionMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-REPORT-TO-SECURITY-EVENT-DEFINITION-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sender_receiver_interface: List[SenderReceiverInterface] = field(
            default_factory=list,
            metadata={
                "name": "SENDER-RECEIVER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sensor_actuator_sw_component_type: List[
            SensorActuatorSwComponentType
        ] = field(
            default_factory=list,
            metadata={
                "name": "SENSOR-ACTUATOR-SW-COMPONENT-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        serialization_technology: List[SerializationTechnology] = field(
            default_factory=list,
            metadata={
                "name": "SERIALIZATION-TECHNOLOGY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        service_instance_collection_set: List[ServiceInstanceCollectionSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "SERVICE-INSTANCE-COLLECTION-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        service_instance_to_port_prototype_mapping: List[
            ServiceInstanceToPortPrototypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INSTANCE-TO-PORT-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        service_instance_to_signal_mapping_set: List[
            ServiceInstanceToSignalMappingSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INSTANCE-TO-SIGNAL-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        service_interface: List[ServiceInterface] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        service_interface_mapping_set: List[ServiceInterfaceMappingSet] = (
            field(
                default_factory=list,
                metadata={
                    "name": "SERVICE-INTERFACE-MAPPING-SET",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        service_interface_pedigree: List[ServiceInterfacePedigree] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INTERFACE-PEDIGREE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        service_proxy_sw_component_type: List[ServiceProxySwComponentType] = (
            field(
                default_factory=list,
                metadata={
                    "name": "SERVICE-PROXY-SW-COMPONENT-TYPE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        service_sw_component_type: List[ServiceSwComponentType] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-SW-COMPONENT-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        service_timing: List[ServiceTiming] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        signal_service_translation_props_set: List[
            SignalServiceTranslationPropsSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "SIGNAL-SERVICE-TRANSLATION-PROPS-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        so_ad_routing_group: List[SoAdRoutingGroup] = field(
            default_factory=list,
            metadata={
                "name": "SO-AD-ROUTING-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        socket_connection_ipdu_identifier_set: List[
            SocketConnectionIpduIdentifierSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-CONNECTION-IPDU-IDENTIFIER-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        software_cluster: List[SoftwareCluster] = field(
            default_factory=list,
            metadata={
                "name": "SOFTWARE-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        software_cluster_design: List[SoftwareClusterDesign] = field(
            default_factory=list,
            metadata={
                "name": "SOFTWARE-CLUSTER-DESIGN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        software_package: List[SoftwarePackage] = field(
            default_factory=list,
            metadata={
                "name": "SOFTWARE-PACKAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_data_prototype_transformation_props: List[
            SomeipDataPrototypeTransformationProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-DATA-PROTOTYPE-TRANSFORMATION-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_sd_client_event_group_timing_config: List[
            SomeipSdClientEventGroupTimingConfig
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_sd_client_service_instance_config: List[
            SomeipSdClientServiceInstanceConfig
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_sd_server_event_group_timing_config: List[
            SomeipSdServerEventGroupTimingConfig
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_sd_server_service_instance_config: List[
            SomeipSdServerServiceInstanceConfig
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_service_instance_to_machine_mapping: List[
            SomeipServiceInstanceToMachineMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SERVICE-INSTANCE-TO-MACHINE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_service_interface_deployment: List[
            SomeipServiceInterfaceDeployment
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SERVICE-INTERFACE-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_tp_config: List[SomeipTpConfig] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-TP-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        startup_config_set: List[StartupConfigSet] = field(
            default_factory=list,
            metadata={
                "name": "STARTUP-CONFIG-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        std_cpp_implementation_data_type: List[
            StdCppImplementationDataType
        ] = field(
            default_factory=list,
            metadata={
                "name": "STD-CPP-IMPLEMENTATION-DATA-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sw_addr_method: List[SwAddrMethod] = field(
            default_factory=list,
            metadata={
                "name": "SW-ADDR-METHOD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sw_axis_type: List[SwAxisType] = field(
            default_factory=list,
            metadata={
                "name": "SW-AXIS-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sw_base_type: List[SwBaseType] = field(
            default_factory=list,
            metadata={
                "name": "SW-BASE-TYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sw_record_layout: List[SwRecordLayout] = field(
            default_factory=list,
            metadata={
                "name": "SW-RECORD-LAYOUT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sw_systemconst: List[SwSystemconst] = field(
            default_factory=list,
            metadata={
                "name": "SW-SYSTEMCONST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sw_systemconstant_value_set: List[SwSystemconstantValueSet] = field(
            default_factory=list,
            metadata={
                "name": "SW-SYSTEMCONSTANT-VALUE-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        swc_bsw_mapping: List[SwcBswMapping] = field(
            default_factory=list,
            metadata={
                "name": "SWC-BSW-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        swc_implementation: List[SwcImplementation] = field(
            default_factory=list,
            metadata={
                "name": "SWC-IMPLEMENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        swc_timing: List[SwcTiming] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        synchronized_time_base_consumer_interface: List[
            SynchronizedTimeBaseConsumerInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZED-TIME-BASE-CONSUMER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        synchronized_time_base_provider_interface: List[
            SynchronizedTimeBaseProviderInterface
        ] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZED-TIME-BASE-PROVIDER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        system: List[System] = field(
            default_factory=list,
            metadata={
                "name": "SYSTEM",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        system_signal: List[SystemSignal] = field(
            default_factory=list,
            metadata={
                "name": "SYSTEM-SIGNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        system_signal_group: List[SystemSignalGroup] = field(
            default_factory=list,
            metadata={
                "name": "SYSTEM-SIGNAL-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        system_timing: List[SystemTiming] = field(
            default_factory=list,
            metadata={
                "name": "SYSTEM-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        tcp_option_filter_set: List[TcpOptionFilterSet] = field(
            default_factory=list,
            metadata={
                "name": "TCP-OPTION-FILTER-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_cp_software_cluster_mapping_set: List[
            TdCpSoftwareClusterMappingSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "TD-CP-SOFTWARE-CLUSTER-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        time_base_provider_to_persistency_mapping: List[
            TimeBaseProviderToPersistencyMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "TIME-BASE-PROVIDER-TO-PERSISTENCY-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        time_sync_port_prototype_to_time_base_mapping: List[
            TimeSyncPortPrototypeToTimeBaseMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "TIME-SYNC-PORT-PROTOTYPE-TO-TIME-BASE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        tls_iam_remote_subject: List[TlsIamRemoteSubject] = field(
            default_factory=list,
            metadata={
                "name": "TLS-IAM-REMOTE-SUBJECT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        tlv_data_id_definition_set: List[TlvDataIdDefinitionSet] = field(
            default_factory=list,
            metadata={
                "name": "TLV-DATA-ID-DEFINITION-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        transformation_props_set: List[TransformationPropsSet] = field(
            default_factory=list,
            metadata={
                "name": "TRANSFORMATION-PROPS-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        transformation_props_to_service_interface_element_mapping_set: List[
            TransformationPropsToServiceInterfaceElementMappingSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "TRANSFORMATION-PROPS-TO-SERVICE-INTERFACE-ELEMENT-MAPPING-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        trigger_interface: List[TriggerInterface] = field(
            default_factory=list,
            metadata={
                "name": "TRIGGER-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ttcan_cluster: List[TtcanCluster] = field(
            default_factory=list,
            metadata={
                "name": "TTCAN-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        unit: List[Unit] = field(
            default_factory=list,
            metadata={
                "name": "UNIT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        unit_group: List[UnitGroup] = field(
            default_factory=list,
            metadata={
                "name": "UNIT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_cluster: List[UserDefinedCluster] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_ethernet_frame: List[UserDefinedEthernetFrame] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-ETHERNET-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_i_pdu: List[UserDefinedIPdu] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_pdu: List[UserDefinedPdu] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_service_instance_to_machine_mapping: List[
            UserDefinedServiceInstanceToMachineMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-SERVICE-INSTANCE-TO-MACHINE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_service_interface_deployment: List[
            UserDefinedServiceInterfaceDeployment
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-SERVICE-INTERFACE-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        vehicle_package: List[VehiclePackage] = field(
            default_factory=list,
            metadata={
                "name": "VEHICLE-PACKAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        vfb_timing: List[VfbTiming] = field(
            default_factory=list,
            metadata={
                "name": "VFB-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        view_map_set: List[ViewMapSet] = field(
            default_factory=list,
            metadata={
                "name": "VIEW-MAP-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        xcp_pdu: List[XcpPdu] = field(
            default_factory=list,
            metadata={
                "name": "XCP-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ArPackages:
        ar_package: List["ArPackage"] = field(
            default_factory=list,
            metadata={
                "name": "AR-PACKAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
