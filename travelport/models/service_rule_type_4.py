from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.formatted_text_text_type_4 import FormattedTextTextType4
from travelport.models.modification_type_4 import ModificationType4
from travelport.models.optional_service_applicability_type_4 import (
    OptionalServiceApplicabilityType4,
)
from travelport.models.optional_service_application_limit_type_4 import (
    OptionalServiceApplicationLimitType4,
)
from travelport.models.service_data_4 import ServiceData4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class ServiceRuleType4:
    """
    Contains the rules for applying service rules.

    Parameters
    ----------
    application_rules
        The rules to apply the rule to the itinerary
    application_level
        Lists the levels where the option is applied in the itinerary. Some
        options are applied for the entire itinerary, some for entire
        segments, etc.
    modify_rules
        Groups the modification rules for the Option
    secondary_type_rules
        Lists the supported Secondary Codes for the optional / additional
        service.
    remarks
        Adds text remarks / rules for the optional / additional service
    key
        Unique ID to identify an optional service rule
    """

    class Meta:
        name = "ServiceRuleType"

    application_rules: None | ServiceRuleType4.ApplicationRules = field(
        default=None,
        metadata={
            "name": "ApplicationRules",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    application_level: None | ServiceRuleType4.ApplicationLevel = field(
        default=None,
        metadata={
            "name": "ApplicationLevel",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    modify_rules: None | ServiceRuleType4.ModifyRules = field(
        default=None,
        metadata={
            "name": "ModifyRules",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    secondary_type_rules: None | ServiceRuleType4.SecondaryTypeRules = field(
        default=None,
        metadata={
            "name": "SecondaryTypeRules",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    remarks: list[FormattedTextTextType4] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 99,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class ApplicationRules:
        """
        Parameters
        ----------
        required_for_all_travelers
            Indicates if the option needs to be applied to all travelers in
            the itinerary if selected
        required_for_all_segments
            Indicates if the option needs to be applied to all segments in
            the itinerary if selected
        required_for_all_segments_in_od
            Indicates if the option needs to be applied to all segments in a
            origin / destination (connection flights) if selected for one
            segment in the OD
        unselected_option_required
            If an UnselectedOption is present in the option, then the
            Unselected option  needs to be selected even if the option is
            not selected when this flag is set to true
        secondary_option_code_required
            If set to true, the secondary option code is required for this
            option
        """

        required_for_all_travelers: None | bool = field(
            default=None,
            metadata={
                "name": "RequiredForAllTravelers",
                "type": "Attribute",
            },
        )
        required_for_all_segments: None | bool = field(
            default=None,
            metadata={
                "name": "RequiredForAllSegments",
                "type": "Attribute",
            },
        )
        required_for_all_segments_in_od: None | bool = field(
            default=None,
            metadata={
                "name": "RequiredForAllSegmentsInOD",
                "type": "Attribute",
            },
        )
        unselected_option_required: None | bool = field(
            default=None,
            metadata={
                "name": "UnselectedOptionRequired",
                "type": "Attribute",
            },
        )
        secondary_option_code_required: None | bool = field(
            default=None,
            metadata={
                "name": "SecondaryOptionCodeRequired",
                "type": "Attribute",
            },
        )

    @dataclass
    class ApplicationLevel:
        """
        Parameters
        ----------
        application_limits
            Adds the limits on the number of options that can be selected
            for a particular type
        service_data
        applicable_levels
            Indicates the level in the itinerary when the option is applied.
        provider_defined_applicable_levels
            Indicates the actual provider defined ApplicableLevels which is
            mapped to Other
        """

        application_limits: (
            None | ServiceRuleType4.ApplicationLevel.ApplicationLimits
        ) = field(
            default=None,
            metadata={
                "name": "ApplicationLimits",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v37_0",
            },
        )
        service_data: list[ServiceData4] = field(
            default_factory=list,
            metadata={
                "name": "ServiceData",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v37_0",
                "max_occurs": 999,
            },
        )
        applicable_levels: list[OptionalServiceApplicabilityType4] = field(
            default_factory=list,
            metadata={
                "name": "ApplicableLevels",
                "type": "Attribute",
                "tokens": True,
            },
        )
        provider_defined_applicable_levels: None | str = field(
            default=None,
            metadata={
                "name": "ProviderDefinedApplicableLevels",
                "type": "Attribute",
            },
        )

        @dataclass
        class ApplicationLimits:
            """
            Parameters
            ----------
            application_limit
                The application limits for a particular level
            """

            application_limit: list[OptionalServiceApplicationLimitType4] = (
                field(
                    default_factory=list,
                    metadata={
                        "name": "ApplicationLimit",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v37_0",
                        "min_occurs": 1,
                        "max_occurs": 10,
                    },
                )
            )

    @dataclass
    class ModifyRules:
        """
        Parameters
        ----------
        modify_rule
            Indicates modification rules for the particular modification
            type.
        supported_modifications
            Lists the supported modifications for the itinerary.
        provider_defined_modification_type
            Indicates the actual provider defined modification type which is
            mapped to Other
        """

        modify_rule: list[ServiceRuleType4.ModifyRules.ModifyRule] = field(
            default_factory=list,
            metadata={
                "name": "ModifyRule",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v37_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
        supported_modifications: list[ModificationType4] = field(
            default_factory=list,
            metadata={
                "name": "SupportedModifications",
                "type": "Attribute",
                "tokens": True,
            },
        )
        provider_defined_modification_type: None | str = field(
            default=None,
            metadata={
                "name": "ProviderDefinedModificationType",
                "type": "Attribute",
            },
        )

        @dataclass
        class ModifyRule:
            """
            Parameters
            ----------
            modification
                The modificaiton for which this rule group applies.
            automatically_applied_on_add
                Indicates if the option will be automatically added to new
                segments / passengers in the itinerary.
            can_delete
                Indicates if the option can be deleted from the itinerary
                without segment or passenger modifications
            can_add
                Indicates if the option can be added to the itinerary
                without segment or passenger modification
            refundable
                Indicates if the price of the option is refundable.
            provider_defined_modification_type
                Indicates the actual provider defined modification type
                which is mapped to Other
            """

            modification: None | ModificationType4 = field(
                default=None,
                metadata={
                    "name": "Modification",
                    "type": "Attribute",
                    "required": True,
                },
            )
            automatically_applied_on_add: bool = field(
                default=False,
                metadata={
                    "name": "AutomaticallyAppliedOnAdd",
                    "type": "Attribute",
                },
            )
            can_delete: None | bool = field(
                default=None,
                metadata={
                    "name": "CanDelete",
                    "type": "Attribute",
                },
            )
            can_add: None | bool = field(
                default=None,
                metadata={
                    "name": "CanAdd",
                    "type": "Attribute",
                },
            )
            refundable: None | bool = field(
                default=None,
                metadata={
                    "name": "Refundable",
                    "type": "Attribute",
                },
            )
            provider_defined_modification_type: None | str = field(
                default=None,
                metadata={
                    "name": "ProviderDefinedModificationType",
                    "type": "Attribute",
                },
            )

    @dataclass
    class SecondaryTypeRules:
        """
        Parameters
        ----------
        secondary_type_rule
            Lists a single secondary code for the optional / additional
            service.
        """

        secondary_type_rule: list[
            ServiceRuleType4.SecondaryTypeRules.SecondaryTypeRule
        ] = field(
            default_factory=list,
            metadata={
                "name": "SecondaryTypeRule",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v37_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

        @dataclass
        class SecondaryTypeRule:
            """
            Parameters
            ----------
            application_limit
            secondary_type
                The unique type to associate a secondary type in an optional
                service
            """

            application_limit: list[OptionalServiceApplicationLimitType4] = (
                field(
                    default_factory=list,
                    metadata={
                        "name": "ApplicationLimit",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v37_0",
                        "max_occurs": 10,
                    },
                )
            )
            secondary_type: None | str = field(
                default=None,
                metadata={
                    "name": "SecondaryType",
                    "type": "Attribute",
                    "required": True,
                },
            )
