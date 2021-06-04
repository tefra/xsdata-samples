from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime
from netex.models.availability_condition_ref import AvailabilityConditionRef
from netex.models.branding_ref import BrandingRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.entity_structure import EntityStructure
from netex.models.extensions_2 import Extensions2
from netex.models.fare_day_type_ref import FareDayTypeRef
from netex.models.key_list import KeyList
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.private_code import PrivateCode
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.relative_operator_enumeration import RelativeOperatorEnumeration
from netex.models.service_calendar_ref import ServiceCalendarRef
from netex.models.serviced_organisation_ref import ServicedOrganisationRef
from netex.models.status_enumeration import StatusEnumeration
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.models.timeband_ref import TimebandRef
from netex.models.validity_condition_ref import ValidityConditionRef
from netex.models.validity_condition_ref_structure import ValidityConditionRefStructure
from netex.models.validity_rule_parameter_ref import ValidityRuleParameterRef
from netex.models.validity_trigger_ref import ValidityTriggerRef
from netex.models.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeTextsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "alternativeTexts_RelStructure"

    alternative_text: List["AlternativeText"] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class DayTypesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dayTypes_RelStructure"

    fare_day_type_ref: List[FareDayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_ref: List[DayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_day_type: List["FareDayType"] = field(
        default_factory=list,
        metadata={
            "name": "FareDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_day_type: List["OrganisationDayType"] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type: List["DayType2"] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_day_type: List["DayType1"] = field(
        default_factory=list,
        metadata={
            "name": "DayType_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class OperatingDaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingDays_RelStructure"

    operating_day_ref: List[OperatingDayRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_day: List["OperatingDay"] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ValidityConditionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityConditions_RelStructure"

    availability_condition_ref: List[AvailabilityConditionRef] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_rule_parameter_ref: List[ValidityRuleParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_trigger_ref: List[ValidityTriggerRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTriggerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_condition_ref: List[ValidityConditionRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_between: List["ValidBetween"] = field(
        default_factory=list,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    simple_availability_condition: List["SimpleAvailabilityCondition"] = field(
        default_factory=list,
        metadata={
            "name": "SimpleAvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_during: List["ValidDuring"] = field(
        default_factory=list,
        metadata={
            "name": "ValidDuring",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    availability_condition: List["AvailabilityCondition"] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_rule_parameter: List["ValidityRuleParameter"] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_trigger: List["ValidityTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_condition: List["ValidityCondition2"] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_validity_condition: List["ValidityCondition1"] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class EntityInVersionStructure(EntityStructure):
    validity_conditions: Optional[ValidityConditionsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_between: List["ValidBetween"] = field(
        default_factory=list,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_texts: Optional[AlternativeTextsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_source_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    status_attribute: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "name": "status",
            "type": "Attribute",
        }
    )
    derived_from_version_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromVersionRef",
            "type": "Attribute",
        }
    )
    compatible_with_version_frame_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "compatibleWithVersionFrameVersionRef",
            "type": "Attribute",
        }
    )
    derived_from_object_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromObjectRef",
            "type": "Attribute",
        }
    )


@dataclass
class DataManagedObjectStructure(EntityInVersionStructure):
    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_set_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        }
    )


@dataclass
class VersionedChildStructure(EntityInVersionStructure):
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class AlternativeTextVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AlternativeText_VersionedChildStructure"

    data_managed_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DataManagedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
        }
    )
    use_for_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "useForLanguage",
            "type": "Attribute",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DayTypeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DayType_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    properties: Optional[PropertiesOfDayRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timebands: Optional["TimebandsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class DayType1(DataManagedObjectStructure):
    class Meta:
        name = "DayType_"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDayVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OperatingDay_VersionStructure"

    calendar_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CalendarDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TimebandVersionedChildStructure(DataManagedObjectStructure):
    class Meta:
        name = "Timeband_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ValidityConditionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ValidityCondition_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    conditioned_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ConditionedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    with_condition_ref: Optional[ValidityConditionRefStructure] = field(
        default=None,
        metadata={
            "name": "WithConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ValidityCondition1(DataManagedObjectStructure):
    class Meta:
        name = "ValidityCondition_"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeText(AlternativeTextVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class DayType2(DayTypeVersionStructure):
    class Meta:
        name = "DayType"
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: Optional["ValidityConditionsRelStructure"] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
        }
    )
    valid_between: List["ValidBetween"] = field(
        default_factory=list,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
        }
    )
    alternative_texts: Optional[AlternativeTextsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
        }
    )


@dataclass
class FareDayTypeVersionedStructure(DayTypeVersionStructure):
    class Meta:
        name = "FareDayType_VersionedStructure"


@dataclass
class OperatingDay(OperatingDayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: Optional["ValidityConditionsRelStructure"] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
        }
    )
    valid_between: List["ValidBetween"] = field(
        default_factory=list,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
        }
    )
    alternative_texts: Optional[AlternativeTextsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
        }
    )


@dataclass
class OrganisationDayTypeVersionStructure(DayTypeVersionStructure):
    class Meta:
        name = "OrganisationDayType_VersionStructure"

    is_service_day: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsServiceDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    serviced_organisation_ref: Optional[ServicedOrganisationRef] = field(
        default=None,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ValidBetweenVersionStructure(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidBetween_VersionStructure"

    from_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FromDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ValidityCondition2(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidityCondition"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class ValidityRuleParameterVersionStructure(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidityRuleParameter_VersionStructure"

    rule_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "RuleObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttributeName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    comparison_operator: Optional[RelativeOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    attribute_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "AttributeValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    method: Optional[object] = field(
        default=None,
        metadata={
            "name": "Method",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_valid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isValid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ValidityTriggerVersionStructure(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidityTrigger_VersionStructure"

    trigger_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TriggerObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class TimebandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timebands_RelStructure"

    timeband_ref: List[TimebandRef] = field(
        default_factory=list,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timeband: List[TimebandVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class AvailabilityConditionVersionStructure(ValidBetweenVersionStructure):
    class Meta:
        name = "AvailabilityCondition_VersionStructure"

    is_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_day_bits: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timebands: Optional["TimebandsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_days: Optional[OperatingDaysRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class FareDayType(FareDayTypeVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: Optional["ValidityConditionsRelStructure"] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
        }
    )
    valid_between: List["ValidBetween"] = field(
        default_factory=list,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
        }
    )
    alternative_texts: Optional[AlternativeTextsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
        }
    )


@dataclass
class OrganisationDayType(OrganisationDayTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: Optional["ValidityConditionsRelStructure"] = field(
        default=None,
        metadata={
            "name": "validityConditions",
            "type": "Element",
        }
    )
    valid_between: List["ValidBetween"] = field(
        default_factory=list,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
        }
    )
    alternative_texts: Optional[AlternativeTextsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
        }
    )


@dataclass
class ValidBetween(ValidBetweenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class ValidDuringVersionStructure(ValidBetweenVersionStructure):
    class Meta:
        name = "ValidDuring_VersionStructure"

    fare_day_type_ref: List[FareDayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    day_type_ref: Optional[DayTypeRef] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    days_of_week: List[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    days: Optional[str] = field(
        default=None,
        metadata={
            "name": "Days",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 7,
            "max_length": 7,
            "pattern": r"([Y | N])*",
        }
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class ValidityRuleParameter(ValidityRuleParameterVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class ValidityTrigger(ValidityTriggerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class AvailabilityCondition(AvailabilityConditionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class SimpleAvailabilityCondition(ValidDuringVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class ValidDuring(ValidDuringVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    fare_day_type_ref: List[FareDayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    day_type_ref: Optional[DayTypeRef] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
        }
    )
    days_of_week: List[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "tokens": True,
        }
    )
    days: Optional[str] = field(
        default=None,
        metadata={
            "name": "Days",
            "type": "Element",
            "min_length": 7,
            "max_length": 7,
            "pattern": r"([Y | N])*",
        }
    )
    timebands: Optional["TimebandsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
