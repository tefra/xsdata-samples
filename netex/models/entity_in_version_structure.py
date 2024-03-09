from dataclasses import dataclass, field
from typing import List, Optional, Type, Union, Any
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime
from .availability_condition_ref import AvailabilityConditionRef
from .branding_ref import BrandingRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .day_of_week_enumeration import DayOfWeekEnumeration
from .day_type_ref import DayTypeRef
from .entity_structure import EntityStructure
from .extensions_2 import Extensions2
from .fare_day_type_ref import FareDayTypeRef
from .key_list import KeyList
from .modification_enumeration import ModificationEnumeration
from .multilingual_string import MultilingualString
from .operating_day_ref import OperatingDayRef
from .private_code import PrivateCode
from .properties_of_day_rel_structure import PropertiesOfDayRelStructure
from .relative_operator_enumeration import RelativeOperatorEnumeration
from .service_calendar_ref import ServiceCalendarRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .status_enumeration import StatusEnumeration
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .time_of_day_enumeration import TimeOfDayEnumeration
from .timeband_ref import TimebandRef
from .validity_condition_ref import ValidityConditionRef
from .validity_condition_ref_structure import ValidityConditionRefStructure
from .validity_rule_parameter_ref import ValidityRuleParameterRef
from .validity_trigger_ref import ValidityTriggerRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntityInVersionStructure(EntityStructure):
    validity_conditions_or_valid_between: List[
        Union["ValidityConditionsRelStructure", "ValidBetween"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityConditions",
                    "type": Type["ValidityConditionsRelStructure"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": Type["ValidBetween"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    alternative_texts: Optional["AlternativeTextsRelStructure"] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_source_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        },
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status_attribute: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "name": "status",
            "type": "Attribute",
        },
    )
    derived_from_version_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromVersionRef",
            "type": "Attribute",
        },
    )
    compatible_with_version_frame_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "compatibleWithVersionFrameVersionRef",
            "type": "Attribute",
        },
    )
    derived_from_object_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromObjectRef",
            "type": "Attribute",
        },
    )


@dataclass
class DataManagedObjectStructure(EntityInVersionStructure):
    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    responsibility_set_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        },
    )


@dataclass
class VersionedChildStructure(EntityInVersionStructure):
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
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
        },
    )
    text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
        },
    )
    use_for_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "useForLanguage",
            "type": "Attribute",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


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
        },
    )
    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
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
        },
    )
    start_time_or_start_event: Optional[
        Union[XmlTime, TimeOfDayEnumeration]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartEvent",
                    "type": TimeOfDayEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice: List[
        Union[XmlTime, TimeOfDayEnumeration, int, XmlDuration]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndEvent",
                    "type": TimeOfDayEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Duration",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        },
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
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    conditioned_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ConditionedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    with_condition_ref: Optional[ValidityConditionRefStructure] = field(
        default=None,
        metadata={
            "name": "WithConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class AlternativeText(AlternativeTextVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class OperatingDay(OperatingDayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


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
        },
    )
    to_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class ValidityCondition1(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidityCondition"
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


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
        },
    )
    choice: List[
        Union[
            str,
            RelativeOperatorEnumeration,
            "ValidityRuleParameterVersionStructure.AttributeValue",
            "ValidityRuleParameterVersionStructure.Method",
            bool,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AttributeName",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComparisonOperator",
                    "type": RelativeOperatorEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AttributeValue",
                    "type": Type[
                        "ValidityRuleParameterVersionStructure.AttributeValue"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Method",
                    "type": Type[
                        "ValidityRuleParameterVersionStructure.Method"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "isValid",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass
    class AttributeValue:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )

    @dataclass
    class Method:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
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
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class TimebandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timebands_RelStructure"

    timeband_ref_or_timeband: List[
        Union[TimebandRef, TimebandVersionedChildStructure]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Timeband",
                    "type": TimebandVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
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
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    properties: Optional[PropertiesOfDayRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class ValidBetween(ValidBetweenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    key_list: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    conditioned_object_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    with_condition_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ValidDuringVersionStructure(ValidBetweenVersionStructure):
    class Meta:
        name = "ValidDuring_VersionStructure"

    choice: Optional[
        Union[FareDayTypeRef, DayTypeRef, DayOfWeekEnumeration, str]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DaysOfWeek",
                    "type": List[DayOfWeekEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "Days",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                    "min_length": 7,
                    "max_length": 7,
                    "pattern": r"([Y | N])*",
                },
            ),
        },
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class ValidityRuleParameter(ValidityRuleParameterVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ValidityTrigger(ValidityTriggerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class AlternativeTextsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "alternativeTexts_RelStructure"

    alternative_text: List[AlternativeText] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


@dataclass
class OperatingDaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingDays_RelStructure"

    operating_day_ref_or_operating_day: List[
        Union[OperatingDayRef, OperatingDay]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDay",
                    "type": OperatingDay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class DayType1(DayTypeVersionStructure):
    class Meta:
        name = "DayType"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareDayTypeVersionedStructure(DayTypeVersionStructure):
    class Meta:
        name = "FareDayType_VersionedStructure"


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
        },
    )
    serviced_organisation_ref: Optional[ServicedOrganisationRef] = field(
        default=None,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class SimpleAvailabilityCondition(ValidDuringVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class ValidDuring(ValidDuringVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    key_list: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class FareDayType(FareDayTypeVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationDayType(OrganisationDayTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class DayTypesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dayTypes_RelStructure"

    day_type_ref_or_day_type: List[
        Union[
            FareDayTypeRef,
            DayTypeRef,
            FareDayType,
            OrganisationDayType,
            DayType1,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDayType",
                    "type": FareDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": OrganisationDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": DayType1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
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
        },
    )
    day_types: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    valid_day_bits: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_days: Optional[OperatingDaysRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class AvailabilityCondition(AvailabilityConditionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ValidityConditionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityConditions_RelStructure"

    choice: List[
        Union[
            AvailabilityConditionRef,
            ValidityRuleParameterRef,
            ValidityTriggerRef,
            ValidityConditionRef,
            ValidBetween,
            SimpleAvailabilityCondition,
            ValidDuring,
            AvailabilityCondition,
            ValidityRuleParameter,
            ValidityTrigger,
            ValidityCondition1,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameterRef",
                    "type": ValidityRuleParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTriggerRef",
                    "type": ValidityTriggerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityConditionRef",
                    "type": ValidityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": ValidBetween,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleAvailabilityCondition",
                    "type": SimpleAvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameter",
                    "type": ValidityRuleParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTrigger",
                    "type": ValidityTrigger,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityCondition",
                    "type": ValidityCondition1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
