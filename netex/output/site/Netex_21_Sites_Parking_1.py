from decimal import Decimal
from netex.models.access import Access
from netex.models.access_end_structure import AccessEndStructure
from netex.models.access_mode_enumeration import AccessModeEnumeration
from netex.models.accesses_rel_structure import AccessesRelStructure
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.accessibility_tool_enumeration import AccessibilityToolEnumeration
from netex.models.accessibility_tool_list import AccessibilityToolList
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.availability_condition_ref import AvailabilityConditionRef
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.country_ref import CountryRef
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType1
from netex.models.entity_in_version_structure import DayTypesRelStructure
from netex.models.entity_in_version_structure import TimebandVersionedChildStructure
from netex.models.entity_in_version_structure import TimebandsRelStructure
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.entrance_enumeration import EntranceEnumeration
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.iana_country_tld_enumeration import IanaCountryTldEnumeration
from netex.models.limitation_status_enumeration import LimitationStatusEnumeration
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.parking import Parking
from netex.models.parking_capacities_rel_structure import ParkingCapacitiesRelStructure
from netex.models.parking_capacity import ParkingCapacity
from netex.models.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from netex.models.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.models.parking_entrances_for_vehicles_rel_structure import ParkingEntrancesForVehiclesRelStructure
from netex.models.parking_layout_enumeration import ParkingLayoutEnumeration
from netex.models.parking_payment_process_enumeration import ParkingPaymentProcessEnumeration
from netex.models.parking_properties import ParkingProperties
from netex.models.parking_properties_ref import ParkingPropertiesRef
from netex.models.parking_properties_rel_structure import ParkingPropertiesRelStructure
from netex.models.parking_ref_structure import ParkingRefStructure
from netex.models.parking_reservation_enumeration import ParkingReservationEnumeration
from netex.models.parking_stay_enumeration import ParkingStayEnumeration
from netex.models.parking_type_enumeration import ParkingTypeEnumeration
from netex.models.parking_user_enumeration import ParkingUserEnumeration
from netex.models.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.models.parkings_in_frame_rel_structure import ParkingsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.payment_by_mobile_structure import PaymentByMobileStructure
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.place_ref_structure import PlaceRefStructure
from netex.models.postal_address import PostalAddress
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.public_use_enumeration import PublicUseEnumeration
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_entrances_rel_structure import SiteEntrancesRelStructure
from netex.models.site_facility_set import SiteFacilitySet
from netex.models.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.models.site_frame import SiteFrame
from netex.models.site_type_enumeration import SiteTypeEnumeration
from netex.models.transfer_duration_structure import TransferDurationStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.zone_ref_structure import ZoneRefStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        )
    ),
    publication_refresh_interval=XmlDuration("PT5M0S"),
    data_objects=DataObjectsRelStructure(
        choice=[
            SiteFrame(
                id='pkg:SF01',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        choice=[
                            AvailabilityCondition(
                                id='pkg:PP01_Opening_Hours',
                                version='any',
                                day_types=DayTypesRelStructure(
                                    day_type_ref_or_day_type=[
                                        DayType1(
                                            id='pkg:EveryDay',
                                            version='any',
                                            name=MultilingualString(
                                                value='Every day'
                                            ),
                                            properties=PropertiesOfDayRelStructure(
                                                property_of_day=[
                                                    PropertyOfDay(
                                                        days_of_week=[
                                                            DayOfWeekEnumeration.EVERYDAY,
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                        DayTypeRef(
                                            ref=''
                                        ),
                                    ]
                                ),
                                timebands=TimebandsRelStructure(
                                    timeband_ref_or_timeband=[
                                        TimebandVersionedChildStructure(
                                            id='pkg:PP01_Opening_Hours@range',
                                            version='any',
                                            start_time_or_start_event=XmlTime(6, 30, 0, 0),
                                            choice=[
                                                XmlTime(12, 0, 0, 0),
                                            ]
                                        ),
                                    ]
                                )
                            ),
                            AvailabilityCondition(
                                id='pkg:PP01_Exit_Hours',
                                version='any',
                                day_types=DayTypesRelStructure(
                                    day_type_ref_or_day_type=[
                                        DayType1(
                                            id='pkg:24HrsEveryDay',
                                            version='any',
                                            name=MultilingualString(
                                                value='Every day'
                                            ),
                                            properties=PropertiesOfDayRelStructure(
                                                property_of_day=[
                                                    PropertyOfDay(
                                                        days_of_week=[
                                                            DayOfWeekEnumeration.EVERYDAY,
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                        DayTypeRef(
                                            ref=''
                                        ),
                                    ]
                                )
                            ),
                        ]
                    ),
                ],
                version='any',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='pkg_data',
                            xmlns='pkg',
                            xmlns_url='http://www.pkgdata.co.uk/data',
                            description='Other interchange DATA SOURCE '
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='pkg_data'
                    )
                ),
                parkings=ParkingsInFrameRelStructure(
                    parking=[
                        Parking(
                            id='pkg:PP01',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityConditionRef(
                                            version='any',
                                            ref='pkg:PP01_Opening_Hours'
                                        ),
                                    ]
                                ),
                            ],
                            data_source_ref_attribute='parkopedia',
                            version='any',
                            name=MultilingualString(
                                value='Barcester  CIty centre  Car Park'
                            ),
                            short_name=MultilingualString(
                                value='CIty Car Park'
                            ),
                            description=[
                                MultilingualString(
                                    value='Mult storey next to Sainsbury . Three storeys 220 public and 30 disabled places '
                                ),
                            ],
                            centroid=SimplePointVersionStructure(
                                id='xyz',
                                location=LocationStructure2(
                                    longitude=Decimal('-180'),
                                    latitude=Decimal('-90'),
                                    id='xyz12',
                                    srs_name='WGS84'
                                )
                            ),
                            url='http://www.barpark.co.uk',
                            image='http://ww.mycarpark.com/prettypicture.jpg',
                            postal_address=PostalAddress(
                                id='pkg:PP01@address',
                                version='any',
                                country_ref=CountryRef(
                                    value='String',
                                    ref=IanaCountryTldEnumeration.UK
                                ),
                                house_number='27',
                                street=MultilingualString(
                                    value='High Street'
                                ),
                                town=MultilingualString(
                                    value='Barcester'
                                ),
                                post_code='BXC 24P'
                            ),
                            landmark=MultilingualString(
                                value="Sainsbury's"
                            ),
                            public_use=PublicUseEnumeration.ALL,
                            covered=CoveredEnumeration.INDOORS,
                            all_areas_wheelchair_accessible=False,
                            facilities=SiteFacilitySetsRelStructure(
                                site_facility_set_ref_or_site_facility_set=[
                                    SiteFacilitySet(
                                        id='pkg:PP01',
                                        version='any',
                                        accessibility_tool_list=AccessibilityToolList(
                                            value=[
                                                AccessibilityToolEnumeration.PUSHCHAIR,
                                                AccessibilityToolEnumeration.WHEELCHAIR,
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            site_type=SiteTypeEnumeration.RETAIL,
                            at_centre=True,
                            entrances=SiteEntrancesRelStructure(
                                entrance_ref_or_parking_entrance_ref_or_entrance=[
                                    ParkingEntranceForVehicles(
                                        id='pkg:PP01@EV11@Entrance',
                                        validity_conditions_or_valid_between=[
                                            ValidityConditionsRelStructure(
                                                choice=[
                                                    AvailabilityConditionRef(
                                                        version='any',
                                                        ref='pkg:PP01_Opening_Hours'
                                                    ),
                                                ]
                                            ),
                                        ],
                                        version='any',
                                        name=MultilingualString(
                                            value='Main Vehicle Entrance from street'
                                        ),
                                        parent_zone_ref=ZoneRefStructure(
                                            version='any',
                                            ref='pkg:PP01'
                                        ),
                                        label=MultilingualString(
                                            value='IN'
                                        ),
                                        entrance_type=EntranceEnumeration.GATE,
                                        is_external=True,
                                        is_entry=True,
                                        is_exit=False,
                                        width=Decimal('14.0'),
                                        height=Decimal('12.0')
                                    ),
                                    ParkingEntranceForVehicles(
                                        id='pkg:PP01@EV12@Exit',
                                        validity_conditions_or_valid_between=[
                                            ValidityConditionsRelStructure(
                                                choice=[
                                                    AvailabilityConditionRef(
                                                        version='any',
                                                        ref='pkg:PP01_Exit_Hours'
                                                    ),
                                                ]
                                            ),
                                        ],
                                        version='any',
                                        name=MultilingualString(
                                            value='Main Vehicle Exit to street'
                                        ),
                                        parent_zone_ref=ZoneRefStructure(
                                            version='any',
                                            ref='pkg:PP01'
                                        ),
                                        label=MultilingualString(
                                            value='Exit'
                                        ),
                                        entrance_type=EntranceEnumeration.GATE,
                                        is_external=True,
                                        is_entry=False,
                                        is_exit=True,
                                        width=Decimal('14.0'),
                                        height=Decimal('12.0')
                                    ),
                                ]
                            ),
                            accesses=AccessesRelStructure(
                                access_ref_or_access=[
                                    Access(
                                        id='pkg:PP01@A1',
                                        version='any',
                                        description=MultilingualString(
                                            value='Walk to Station'
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M"),
                                            mobility_restricted_traveller_duration=XmlDuration("PT20M")
                                        ),
                                        both_ways=True,
                                        from_value=AccessEndStructure(
                                            transport_mode=AllModesEnumeration.RAIL,
                                            place_ref=PlaceRefStructure(
                                                ref='napt:9100:00476',
                                                version_ref='EXTERNAL'
                                            )
                                        ),
                                        to=AccessEndStructure(
                                            transport_mode=AllModesEnumeration.SELF_DRIVE,
                                            place_ref=ParkingRefStructure(
                                                version='any',
                                                ref='pkg:PP01'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            parking_type=ParkingTypeEnumeration.SHOPPING_CENTRE_PARKING,
                            parking_layout=ParkingLayoutEnumeration.MULTISTOREY,
                            number_of_parking_levels=3,
                            principal_capacity=250,
                            total_capacity=250,
                            overnight_parking_permitted=True,
                            recharging_available=False,
                            real_time_occupancy_available=True,
                            parking_payment_process=[
                                ParkingPaymentProcessEnumeration.PAY_AT_BAY,
                            ],
                            payment_methods=[
                                PaymentMethodEnumeration.CREDIT_CARD,
                                PaymentMethodEnumeration.CASH,
                                PaymentMethodEnumeration.DEBIT_CARD,
                                PaymentMethodEnumeration.CREDIT_CARD,
                                PaymentMethodEnumeration.MOBILE_PHONE,
                            ],
                            default_currency='GBP',
                            currencies_accepted=[
                                'GBP',
                            ],
                            parking_reservation=ParkingReservationEnumeration.NO_RESERVATIONS,
                            booking_url='http://www.bookmyparking.com',
                            parking_properties=ParkingPropertiesRelStructure(
                                parking_properties=[
                                    ParkingProperties(
                                        id='pkg:PP01',
                                        version='any',
                                        parking_user_types=[
                                            ParkingUserEnumeration.ALL_USERS,
                                        ],
                                        parking_stay_list=[
                                            ParkingStayEnumeration.ALL,
                                        ],
                                        maximum_stay=XmlDuration("PT48H"),
                                        spaces=ParkingCapacitiesRelStructure(
                                            parking_capacity_ref_or_parking_capacity=[
                                                ParkingCapacity(
                                                    id='pkg:PP01@C01_disabled',
                                                    version='any',
                                                    parking_properties_ref=ParkingPropertiesRef(
                                                        version='any',
                                                        ref='pkg:PP01'
                                                    ),
                                                    parking_user_type=ParkingUserEnumeration.REGISTERED_DISABLED,
                                                    parking_vehicle_type=ParkingVehicleEnumeration.PASSENGER_CAR,
                                                    parking_stay_type=ParkingStayEnumeration.UNLIMITED,
                                                    number_of_spaces=30
                                                ),
                                                ParkingCapacity(
                                                    id='pkg:PP01@C02_other',
                                                    version='any',
                                                    parking_properties_ref=ParkingPropertiesRef(
                                                        version='any',
                                                        ref='pkg:PP01'
                                                    ),
                                                    parking_user_type=ParkingUserEnumeration.ALL_USERS,
                                                    parking_vehicle_type=ParkingVehicleEnumeration.PASSENGER_CAR,
                                                    parking_stay_type=ParkingStayEnumeration.UNLIMITED,
                                                    number_of_spaces=220
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_entrances=ParkingEntrancesForVehiclesRelStructure(
                                parking_entrance_for_vehicles_ref_or_parking_entrance_for_vehicles=[
                                    ParkingEntranceForVehiclesRef(
                                        version='any',
                                        ref='pkg:PP01@EV11@Entrance'
                                    ),
                                    ParkingEntranceForVehiclesRef(
                                        version='any',
                                        ref='pkg:PP01@EV12@Exit'
                                    ),
                                ]
                            )
                        ),
                        Parking(
                            id='pkg:PS22',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='pkg:Parking_Charge_Hours',
                                            version='any',
                                            name=MultilingualString(
                                                value='Charged Parking times'
                                            ),
                                            description=MultilingualString(
                                                value='Modnay to friday not PublicHolidays'
                                            ),
                                            day_types=DayTypesRelStructure(
                                                day_type_ref_or_day_type=[
                                                    DayType1(
                                                        id='pkg:WorkingDay',
                                                        version='any',
                                                        name=MultilingualString(
                                                            value='Working day'
                                                        ),
                                                        properties=PropertiesOfDayRelStructure(
                                                            property_of_day=[
                                                                PropertyOfDay(
                                                                    description=MultilingualString(

                                                                    ),
                                                                    days_of_week=[
                                                                        DayOfWeekEnumeration.MONDAY,
                                                                        DayOfWeekEnumeration.TUESDAY,
                                                                        DayOfWeekEnumeration.WEDNESDAY,
                                                                        DayOfWeekEnumeration.THURSDAY,
                                                                        DayOfWeekEnumeration.FRIDAY,
                                                                    ],
                                                                    holiday_types=[
                                                                        HolidayTypeEnumeration.NOT_HOLIDAY,
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            ),
                                            timebands=TimebandsRelStructure(
                                                timeband_ref_or_timeband=[
                                                    TimebandVersionedChildStructure(
                                                        id='pkg:Parking_Charge_Hours@range',
                                                        version='any',
                                                        start_time_or_start_event=XmlTime(8, 30, 0, 0),
                                                        choice=[
                                                            XmlTime(5, 30, 0, 0),
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                            data_source_ref_attribute='parkopedia',
                            version='any',
                            name=MultilingualString(
                                value='Barcester  High street Parking '
                            ),
                            short_name=MultilingualString(
                                value='CIty Car Park'
                            ),
                            description=[
                                MultilingualString(
                                    value='On street parking metered 8.30 to 6 pm Mondat to Friday  '
                                ),
                            ],
                            url='http://www.barpccyparkingregs.co.uk',
                            accessibility_assessment=AccessibilityAssessment(
                                id='pkg:PS22',
                                version='any',
                                mobility_impaired_access=LimitationStatusEnumeration.TRUE
                            ),
                            access_modes=[
                                AccessModeEnumeration.FOOT,
                            ],
                            public_use=PublicUseEnumeration.ALL,
                            covered=CoveredEnumeration.OUTDOORS,
                            all_areas_wheelchair_accessible=True,
                            accesses=AccessesRelStructure(
                                access_ref_or_access=[
                                    Access(
                                        id='pkg:PS22@A01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Walk to Station'
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M"),
                                            mobility_restricted_traveller_duration=XmlDuration("PT20M")
                                        ),
                                        both_ways=True,
                                        from_value=AccessEndStructure(
                                            transport_mode=AllModesEnumeration.RAIL,
                                            place_ref=PlaceRefStructure(
                                                ref='napt:9100:00476',
                                                version_ref='EXTERNAL'
                                            )
                                        ),
                                        to=AccessEndStructure(
                                            transport_mode=AllModesEnumeration.SELF_DRIVE,
                                            place_ref=ParkingRefStructure(
                                                version='any',
                                                ref='pkg:PS22'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            parking_type=ParkingTypeEnumeration.PARKING_ZONE,
                            parking_layout=ParkingLayoutEnumeration.ROADSIDE,
                            principal_capacity=45,
                            total_capacity=50,
                            overnight_parking_permitted=True,
                            prohibited_for_hazardous_materials=False,
                            recharging_available=False,
                            parking_payment_process=[
                                ParkingPaymentProcessEnumeration.PAY_BY_MOBILE_DEVICE,
                                ParkingPaymentProcessEnumeration.PAY_AND_DISPLAY,
                            ],
                            payment_methods=[
                                PaymentMethodEnumeration.CREDIT_CARD,
                                PaymentMethodEnumeration.CASH,
                                PaymentMethodEnumeration.DEBIT_CARD,
                                PaymentMethodEnumeration.CREDIT_CARD,
                                PaymentMethodEnumeration.MOBILE_PHONE,
                            ],
                            default_currency='GBP',
                            currencies_accepted=[
                                'GBP',
                            ],
                            cards_accepted=[
                                'diners',
                                'mastercard',
                                'visa',
                                'eftpos',
                            ],
                            parking_reservation=ParkingReservationEnumeration.NO_RESERVATIONS,
                            booking_url='http://www.bookmyparking.com',
                            payment_by_mobile=PaymentByMobileStructure(
                                phone_number_to_pay='7242',
                                support_phone_number='0202417656',
                                payment_url='http://www.bookmyparking.com'
                            ),
                            free_parking_out_of_hours=True,
                            parking_properties=ParkingPropertiesRelStructure(
                                parking_properties=[
                                    ParkingProperties(
                                        id='pkg:PS22',
                                        version='any',
                                        parking_user_types=[
                                            ParkingUserEnumeration.ALL,
                                        ],
                                        parking_stay_list=[
                                            ParkingStayEnumeration.UNLIMITED,
                                        ],
                                        spaces=ParkingCapacitiesRelStructure(
                                            parking_capacity_ref_or_parking_capacity=[
                                                ParkingCapacity(
                                                    id='pkg:PS22@01_disabled',
                                                    version='any',
                                                    parking_properties_ref=ParkingPropertiesRef(
                                                        version='any',
                                                        ref='pkg:PS22'
                                                    ),
                                                    parking_user_type=ParkingUserEnumeration.REGISTERED_DISABLED,
                                                    parking_vehicle_type=ParkingVehicleEnumeration.PASSENGER_CAR,
                                                    parking_stay_type=ParkingStayEnumeration.UNLIMITED,
                                                    number_of_spaces=5
                                                ),
                                                ParkingCapacity(
                                                    id='pkg:PS22@other',
                                                    version='any',
                                                    parking_properties_ref=ParkingPropertiesRef(
                                                        version='any',
                                                        ref='pkg:PS22'
                                                    ),
                                                    parking_user_type=ParkingUserEnumeration.ALL_USERS,
                                                    parking_vehicle_type=ParkingVehicleEnumeration.PASSENGER_CAR,
                                                    parking_stay_type=ParkingStayEnumeration.UNLIMITED,
                                                    number_of_spaces=45
                                                ),
                                            ]
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
