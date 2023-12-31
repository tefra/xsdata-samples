from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.cell_versioned_child_structure import FarePricesRelStructure
from netex.models.cell_versioned_child_structure import PriceGroup
from netex.models.cell_versioned_child_structure import PriceGroupsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.fare_frame import FareFrame
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.interchanging import Interchanging
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network import Network
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.price_group_ref import PriceGroupRef
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.tariff import Tariff
from netex.models.tariff_zone import TariffZone
from netex.models.tariff_zone_ref import TariffZoneRef
from netex.models.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.time_interval import TimeInterval
from netex.models.time_interval_price import TimeIntervalPrice
from netex.models.time_interval_ref import TimeIntervalRef
from netex.models.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.models.time_structure_factor import TimeStructureFactor
from netex.models.time_structure_factor_ref import TimeStructureFactorRef
from netex.models.time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from netex.models.time_unit import TimeUnit
from netex.models.time_unit_ref import TimeUnitRef
from netex.models.time_units_rel_structure import TimeUnitsRelStructure
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_concession import TypeOfConcession
from netex.models.type_of_fare_product import TypeOfFareProduct
from netex.models.type_of_fare_product_ref import TypeOfFareProductRef
from netex.models.type_of_tariff import TypeOfTariff
from netex.models.type_of_tariff_ref import TypeOfTariffRef
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from netex.models.value_set import ValueSet
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002',
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        validity_condition=[
                            AvailabilityCondition(
                                id='hde:range',
                                version='any',
                                from_date=XmlDateTime(2011, 1, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        FareFrameRef(
                            value='REQUEST',
                            ref='myfares:any'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of simple point to point fares'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='myfares:DTA@Time_Interval',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        choice=[
                            ValidBetween(
                                from_date=XmlDateTime(2011, 1, 1, 0, 0, 0, 0, 0),
                                to_date=XmlDateTime(2011, 7, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                ],
                version='1.0',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybuses.eu/stuff',
                            description='My buses'
                        ),
                        Codespace(
                            id='myfares',
                            xmlns='myfares',
                            xmlns_url='http://www.myfares,com/fares',
                            description='Fare data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='myfares'
                    ),
                    default_currency='EUR'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:DTA@Time_Interval@network',
                            version='1.0',
                            name=MultilingualString(
                                value='Fares  for Winter timetable for Network'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Common_Resources'
                                    ),
                                ]
                            ),
                            network=Network(
                                id='mybus:DTA',
                                version='any',
                                transport_organisation_ref=OperatorRef(
                                    version='any',
                                    ref='mybus:DTA'
                                ),
                                tariff_zones=TariffZoneRefsRelStructure(
                                    tariff_zone_ref=[
                                        TariffZoneRef(
                                            version='any',
                                            ref='myfares:1'
                                        ),
                                    ]
                                )
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    TariffZone(
                                        id='myfares:1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Zone 1'
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@Time_Interval@products',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ServiceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Time_Interval@network'
                                    ),
                                ]
                            ),
                            time_units=TimeUnitsRelStructure(
                                time_unit_ref_or_time_unit=[
                                    TimeUnit(
                                        id='myfares:1hour',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Time unit of 1 hour'
                                        )
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='myfares:Time_interval',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Zonal Fare'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        type_of_tariff_ref=TypeOfTariffRef(
                                            version='ntx:v1.0',
                                            ref='ntx:zonal'
                                        ),
                                        time_unit_ref=TimeUnitRef(
                                            version='1.0',
                                            ref='myfares:1hour'
                                        ),
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='myfares:1hour',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='One Hour'
                                                    ),
                                                    duration=XmlDuration("PT1H"),
                                                    time_structure_factors=TimeStructureFactorsRelStructure(
                                                        parking_charge_band_ref_or_time_structure_factor_ref_or_time_structure_factor=[
                                                            TimeStructureFactor(
                                                                id='myfares:tsf_1h',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value="One hour's  use"
                                                                ),
                                                                factor='1',
                                                                time_unit_ref=TimeUnitRef(
                                                                    version='1.0',
                                                                    ref='myfares:1hour'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                TimeInterval(
                                                    id='myfares:2hour',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Two Hours'
                                                    ),
                                                    duration=XmlDuration("PT2H"),
                                                    time_structure_factors=TimeStructureFactorsRelStructure(
                                                        parking_charge_band_ref_or_time_structure_factor_ref_or_time_structure_factor=[
                                                            TimeStructureFactor(
                                                                id='myfares:tsf_2h',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value="Two hour's  use"
                                                                ),
                                                                factor='2',
                                                                time_unit_ref=TimeUnitRef(
                                                                    version='1.0',
                                                                    ref='myfares:1hour'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                TimeInterval(
                                                    id='myfares:1day',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='All Day Use on day of purchase'
                                                    ),
                                                    start_time=XmlTime(6, 0, 0, 0),
                                                    end_time=XmlTime(2, 0, 0, 0),
                                                    day_offset=1,
                                                    time_structure_factors=TimeStructureFactorsRelStructure(
                                                        parking_charge_band_ref_or_time_structure_factor_ref_or_time_structure_factor=[
                                                            TimeStructureFactor(
                                                                id='myfares:tsf_day',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='All day use on day of purchase'
                                                                ),
                                                                factor='24',
                                                                time_unit_ref=TimeUnitRef(
                                                                    version='1.0',
                                                                    ref='myfares:1hour'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='myfares:Time_interval@access',
                                                    version='1.0',
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Time_interval@access',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.XOR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            tariff_zone_ref=[
                                                                TariffZoneRef(
                                                                    version='any',
                                                                    ref='myfares:1'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Time_interval@access_when',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Allowed periods for  use of a  zone'
                                                    ),
                                                    time_interval_ref_or_time_intervals_or_time_structure_factors=TimeStructureFactorsRelStructure(
                                                        parking_charge_band_ref_or_time_structure_factor_ref_or_time_structure_factor=[
                                                            TimeStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:tsf_1h'
                                                            ),
                                                            TimeStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:tsf_2h'
                                                            ),
                                                            TimeStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:tsf_day'
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Time_interval@access_when',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access_when',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.XOR
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Time_interval@conditions_of_travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Conditions of travel'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Time_interval@conditions_of_travel',
                                                        version='1.0',
                                                        name=MultilingualString(
                                                            value='Conditions of travel'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_use',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                FrequencyOfUse(
                                                                    id='myfares:Time_interval@conditions_of_travel@frequency',
                                                                    version='1.0',
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.UNLIMITED
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:Time_interval@conditions_of_travel@interchanging',
                                                                    version='1.0',
                                                                    can_interchange=True,
                                                                    can_break_journey=True
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        ),
                                        price_groups=PriceGroupsRelStructure(
                                            price_group_ref_or_price_group=[
                                                PriceGroupRef(
                                                    version='1.0',
                                                    ref='myfares:DTA@Time_interval'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                fare_product=[
                                    PreassignedFareProduct(
                                        id='myfares:Period_pass',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='1 zone use for specified period'
                                        ),
                                        type_of_fare_product_ref_or_types_of_fare_product=TypeOfFareProductRef(
                                            version='ntx:v1.0',
                                            ref='ntx:period_pass'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='myfares:Period_pass@travel',
                                                    version='1.0',
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Time_interval@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Time_interval@access_when'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Time_interval@conditions_of_travel'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='myfares:Period_pass@travel',
                                                    version='1.0',
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1.0',
                                                        ref='myfares:Period_pass@travel'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            sales_offer_packages=SalesOfferPackagesInFrameRelStructure(
                                sales_offer_package=[
                                    SalesOfferPackage(
                                        id='myfares:PeriodPass-SOP@p-ticket',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Printed et Period Pass'
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='myfares:PeriodPass-SOP@p-ticket@atStop',
                                                    version='10',
                                                    name=MultilingualString(
                                                        value='Onboard'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Pay for ticket onboard'
                                                    ),
                                                    order=1,
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.AT_STOP,
                                                    ticketing_service_facility_list=[
                                                        TicketingServiceFacilityEnumeration.PURCHASE,
                                                    ],
                                                    payment_methods=[
                                                        PaymentMethodEnumeration.CASH_AND_CARD,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        ref='ntx:collect_on_board',
                                                        version_ref='ntx:v1.0'
                                                    )
                                                ),
                                                DistributionAssignment(
                                                    id='myfares:PeriodPass-SOP@p-ticket@onBoard',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Onboard'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Pay for ticket onboard'
                                                    ),
                                                    order=2,
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.ON_BOARD,
                                                    ticketing_service_facility_list=[
                                                        TicketingServiceFacilityEnumeration.PURCHASE,
                                                    ],
                                                    payment_methods=[
                                                        PaymentMethodEnumeration.CASH_AND_CARD,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        ref='ntx:collect_on_board',
                                                        version_ref='ntx:v1.0'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:PeriodPass-SOP@p-ticket',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:printed_ticket'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Period_pass'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='myfares:PeriodPass-SOP@m-ticket',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Mobile ticket - Period Pass'
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='myfares:PeriodPass-SOP@m-ticket@online',
                                                    version='10',
                                                    name=MultilingualString(
                                                        value='Online'
                                                    ),
                                                    order=1,
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.MOBILE_DEVICE,
                                                    payment_methods=[
                                                        PaymentMethodEnumeration.CARDS_ONLY,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        ref='ntx:mobile_app',
                                                        version_ref='ntx:v1.0'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:PeriodPass-SOP@m-ticket',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:mobile_app'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Period_pass'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@Time_Interval@prices',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@Time_Interval@products'
                                    ),
                                ]
                            ),
                            price_groups=FarePricesInFrameRelStructure(
                                price_group=[
                                    PriceGroup(
                                        id='myfares:DTA@Time_interval',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Prices for Time Interval zonal  Products'
                                        ),
                                        members=FarePricesRelStructure(
                                            fare_price_ref_or_cell_ref_or_fare_price=[
                                                TimeIntervalPrice(
                                                    id='myfares:1hour',
                                                    version='1.0',
                                                    amount=Decimal('1.50'),
                                                    time_interval_ref=TimeIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:1hour'
                                                    )
                                                ),
                                                TimeIntervalPrice(
                                                    id='myfares:2hour',
                                                    version='1.0',
                                                    amount=Decimal('2.00'),
                                                    time_interval_ref=TimeIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:2hour'
                                                    )
                                                ),
                                                TimeIntervalPrice(
                                                    id='myfares:1day',
                                                    version='1.0',
                                                    amount=Decimal('5.00'),
                                                    time_interval_ref=TimeIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:1day'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='mybus:DTA@Common_Resources',
                            version='1.0',
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='ntx',
                                        xmlns='ntx',
                                        xmlns_url='http://netex.org.uk/',
                                        description='Netex built in value'
                                    ),
                                ]
                            ),
                            types_of_value=TypesOfValueInFrameRelStructure(
                                choice=[
                                    ValueSet(
                                        id='ntx:Types_of_Tariff',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Types of Tariff'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfTariff(
                                                    id='ntx:Distance_kilometers',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Kilometer Distance Kilometers'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:flat',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Flat'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:point_to_point',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Point to point'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:zone_to_zone',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Zone to Zone'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:zonal',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Zonal'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:unit_distance',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Unit distance (count of stops, sections, zones)'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:section',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Section'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:banded',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Yime banded'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:stored_value',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Stored value'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:discount',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Discount value'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:multitrip',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Multitrip carnet'
                                                    )
                                                ),
                                                TypeOfTariff(
                                                    id='ntx:identity_card',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='SIdentity'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfTariff'
                                    ),
                                    ValueSet(
                                        id='ntx:Types_of_FareProduct',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Types of Fare Product'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfFareProduct(
                                                    id='ntx:trip',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Trip product'
                                                    )
                                                ),
                                                TypeOfFareProduct(
                                                    id='ntx:multi_trip',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Multitrip / carnet  product'
                                                    )
                                                ),
                                                TypeOfFareProduct(
                                                    id='ntx:period_pass',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Peroid pass product'
                                                    )
                                                ),
                                                TypeOfFareProduct(
                                                    id='ntx:day_pass',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Day pass product'
                                                    )
                                                ),
                                                TypeOfFareProduct(
                                                    id='ntx:discount_card',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Discount  product'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfFareProduct'
                                    ),
                                    ValueSet(
                                        id='myfares:Types_of_Concession',
                                        version='any',
                                        name=MultilingualString(
                                            value='Types of concession'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfConcession(
                                                    id='myfares:adult',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Adult'
                                                    )
                                                ),
                                                TypeOfConcession(
                                                    id='myfares:child',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Student'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfConcession'
                                    ),
                                    ValueSet(
                                        id='myfares:Types_of_TravelDocument',
                                        version='any',
                                        name=MultilingualString(
                                            value='Types of concession'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfTravelDocument(
                                                    id='myfares:printed_ticket',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Paper ticket'
                                                    )
                                                ),
                                                TypeOfTravelDocument(
                                                    id='myfares:mobile_app',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Mobile app'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfTravelDocument'
                                    ),
                                    ValueSet(
                                        id='ntx:Types_of_AccessRightAssignment',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Types of Access Right Assignment'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:eligible',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Eligible for a product or discount'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:can_access',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Grants access rights to use or travel on'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:condition_of_use',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Defines a condition or restriction on use'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfAccessRightAssignment'
                                    ),
                                ]
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='mybus:DTA',
                                        version='any',
                                        name=MultilingualString(
                                            value='Demo Transit Authority'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
