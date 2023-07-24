from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import CarrierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import CommodityClassification
from ubl.models.common.ubl_common_aggregate_components_2_1 import ConsigneeParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Consignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import ConsignorParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import ConsolidatedShipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import ContractDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinalDestinationCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import FromLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import GoodsItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import Location
from ubl.models.common.ubl_common_aggregate_components_2_1 import MainCarriageShipmentStage
from ubl.models.common.ubl_common_aggregate_components_2_1 import MainTransportationService
from ubl.models.common.ubl_common_aggregate_components_2_1 import MaritimeTransport
from ubl.models.common.ubl_common_aggregate_components_2_1 import MeasurementDimension
from ubl.models.common.ubl_common_aggregate_components_2_1 import NotificationRequirement
from ubl.models.common.ubl_common_aggregate_components_2_1 import NotifyParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginalDepartureCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import Package
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import Period
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedArrivalTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedDeliveryTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedDepartureTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedPickupTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import PreCarriageShipmentStage
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import ServiceEndTimePeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import ToLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportContract
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportEquipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportExecutionTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportHandlingUnit
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportMeans
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportServiceDescriptionDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportServiceProviderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportUserParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportUserResponseRequiredPeriod
from ubl.models.common.ubl_common_basic_components_2_1 import AttributeId
from ubl.models.common.ubl_common_basic_components_2_1 import CargoTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentDescription
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentType
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import EndpointId
from ubl.models.common.ubl_common_basic_components_2_1 import FullnessIndicationCode
from ubl.models.common.ubl_common_basic_components_2_1 import GrossVolumeMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import GrossWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import JourneyId
from ubl.models.common.ubl_common_basic_components_2_1 import LoadingLengthMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import LocationTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Measure
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import NetWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import NotificationTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import PackagingTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import PostEventNotificationDurationMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationNationality
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationNationalityId
from ubl.models.common.ubl_common_basic_components_2_1 import ShippingMarks
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TotalGoodsItemQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import TotalPackageQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTransportHandlingUnitQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import TransportEquipmentTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportHandlingUnitTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportMeansTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportModeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportServiceCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportationServiceDescription
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import VersionId
from ubl.models.common.ubl_common_basic_components_2_1 import VesselId
from ubl.models.common.ubl_common_basic_components_2_1 import VesselName
from ubl.models.maindoc.ubl_transport_execution_plan_2_1 import TransportExecutionPlan
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = TransportExecutionPlan(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    id=Id(
        value="TEP_1"
    ),
    version_id=VersionId(
        value="1"
    ),
    issue_date=XmlDate(2011, 9, 13),
    issue_time=XmlTime(10, 0, 30, 0, 60),
    document_status_code=DocumentStatusCode(
        value="Confirmed"
    ),
    sender_party=SenderParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="4058673827641",
                    scheme_name="GLN",
                    scheme_agency_name="GS1"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="NECOSS"
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="SomeName"
            ),
            telephone=Telephone(
                value="+49450557000"
            ),
            electronic_mail=ElectronicMail(
                value="SomeName@necoss.de"
            )
        )
    ),
    receiver_party=ReceiverParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="4058673827000",
                    scheme_name="GLN",
                    scheme_agency_name="GS1"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="Consignor"
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="SomeName"
            ),
            telephone=Telephone(
                value="+8687878763"
            ),
            electronic_mail=ElectronicMail(
                value="SomeName@consignor.cn"
            )
        )
    ),
    transport_user_party=TransportUserParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="4058673827000",
                    scheme_name="GLN",
                    scheme_agency_name="GS1"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="Consignor"
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="SomeName"
            ),
            telephone=Telephone(
                value="+8687878763"
            ),
            electronic_mail=ElectronicMail(
                value="SomeName@consignor.cn"
            )
        )
    ),
    transport_service_provider_party=TransportServiceProviderParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="4058673827641",
                    scheme_name="GLN",
                    scheme_agency_name="GS1"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="NECOSS"
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="SomeName"
            ),
            telephone=Telephone(
                value="+49450557000"
            ),
            electronic_mail=ElectronicMail(
                value="SomeName@necoss.de"
            )
        )
    ),
    transport_service_description_document_reference=TransportServiceDescriptionDocumentReference(
        id=Id(
            value="2"
        )
    ),
    transport_contract=TransportContract(
        note=[
            Note(
                value="Framework Agreement"
            ),
        ],
        contract_document_reference=[
            ContractDocumentReference(
                id=Id(
                    value="TC101"
                ),
                issue_date=XmlDate(2010, 1, 1),
                document_type_code=DocumentTypeCode(
                    value="315"
                ),
                document_type=DocumentType(
                    value="Contract"
                ),
                document_description=[
                    DocumentDescription(
                        value="Framework Agreement between Consignor and NECOSS"
                    ),
                ]
            ),
        ]
    ),
    transport_user_response_required_period=[
        TransportUserResponseRequiredPeriod(
            end_date=XmlDate(2011, 9, 13),
            end_time=XmlTime(12, 0, 10, 0, 60)
        ),
    ],
    main_transportation_service=MainTransportationService(
        transport_service_code=TransportServiceCode(
            value="3"
        ),
        transportation_service_description=[
            TransportationServiceDescription(
                value="Transport from Hamburg to Nurnberg"
            ),
        ]
    ),
    service_end_time_period=ServiceEndTimePeriod(
        end_date=XmlDate(2011, 10, 6),
        end_time=XmlTime(16, 0, 10, 0, 60)
    ),
    from_location=FromLocation(
        location_type_code=LocationTypeCode(
            value="13"
        ),
        address=Address(
            id=Id(
                value="DEHAM",
                scheme_name="UN/LOCODE",
                scheme_agency_name="UN"
            ),
            street_name=StreetName(
                value="Neuer Wandrahm 4"
            ),
            city_name=CityName(
                value="Hamburg"
            ),
            postal_zone=PostalZone(
                value="29400"
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value="DE"
                )
            )
        )
    ),
    to_location=ToLocation(
        location_type_code=LocationTypeCode(
            value="7"
        ),
        address=Address(
            street_name=StreetName(
                value="Grosse strasse 34"
            ),
            city_name=CityName(
                value="Nurnberg"
            ),
            postal_zone=PostalZone(
                value="28400"
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value="DE"
                )
            )
        )
    ),
    transport_execution_terms=TransportExecutionTerms(
        delivery_terms=[
            DeliveryTerms(
                id=Id(
                    value="EXW",
                    scheme_agency_name="INCOTERMS"
                ),
                delivery_location=DeliveryLocation(
                    address=Address(
                        city_name=CityName(
                            value="Hamburg"
                        )
                    )
                )
            ),
        ],
        notification_requirement=[
            NotificationRequirement(
                notification_type_code=NotificationTypeCode(
                    value="TIME_SCHEDULE_DEVIATIONS"
                ),
                notify_party=[
                    NotifyParty(
                        endpoint_id=EndpointId(
                            value="www.consignee.de/statusnotifications/"
                        ),
                        party_name=[
                            PartyName(
                                name=Name(
                                    value="Consignee"
                                )
                            ),
                        ],
                        contact=Contact(
                            electronic_mail=ElectronicMail(
                                value="someName@consignee.de"
                            )
                        )
                    ),
                    NotifyParty(
                        endpoint_id=EndpointId(
                            value="www.consignor.cn/statusnotifications/"
                        ),
                        party_name=[
                            PartyName(
                                name=Name(
                                    value="Consignor"
                                )
                            ),
                        ],
                        contact=Contact(
                            electronic_mail=ElectronicMail(
                                value="someName@consignor.cn"
                            )
                        )
                    ),
                ]
            ),
            NotificationRequirement(
                notification_type_code=NotificationTypeCode(
                    value="ITEM_CONDITION_DEVIATIONS"
                ),
                post_event_notification_duration_measure=PostEventNotificationDurationMeasure(
                    value=Decimal("10"),
                    unit_code="MIN"
                ),
                notify_party=[
                    NotifyParty(
                        endpoint_id=EndpointId(
                            value="www.consignee.com/statusnotifications/"
                        ),
                        party_name=[
                            PartyName(
                                name=Name(
                                    value="Consignee"
                                )
                            ),
                        ],
                        contact=Contact(
                            electronic_mail=ElectronicMail(
                                value="someName@consignee.de"
                            )
                        )
                    ),
                    NotifyParty(
                        endpoint_id=EndpointId(
                            value="www.consignor.cn/statusnotifications/"
                        ),
                        party_name=[
                            PartyName(
                                name=Name(
                                    value="Consignor"
                                )
                            ),
                        ],
                        contact=Contact(
                            electronic_mail=ElectronicMail(
                                value="someName@consignor.cn"
                            )
                        )
                    ),
                ]
            ),
        ]
    ),
    consignment=[
        Consignment(
            id=Id(
                value="CON_1"
            ),
            gross_weight_measure=GrossWeightMeasure(
                value=Decimal("50000"),
                unit_code="KGM"
            ),
            net_weight_measure=NetWeightMeasure(
                value=Decimal("3000"),
                unit_code="KGM"
            ),
            gross_volume_measure=GrossVolumeMeasure(
                value=Decimal("78"),
                unit_code="MTQ"
            ),
            loading_length_measure=LoadingLengthMeasure(
                value=Decimal("12"),
                unit_code="MTR"
            ),
            hazardous_risk_indicator=False,
            total_transport_handling_unit_quantity=TotalTransportHandlingUnitQuantity(
                value=Decimal("2")
            ),
            consolidated_shipment=[
                ConsolidatedShipment(
                    id=Id(
                        value="GSIN_1"
                    )
                ),
                ConsolidatedShipment(
                    id=Id(
                        value="GSIN_2"
                    )
                ),
            ],
            planned_pickup_transport_event=PlannedPickupTransportEvent(
                location=Location(
                    address=Address(
                        id=Id(
                            value="DEHAM",
                            scheme_name="UN/LOCODE",
                            scheme_agency_name="UN"
                        ),
                        street_name=StreetName(
                            value="Neuer Wandrahm 4"
                        ),
                        city_name=CityName(
                            value="Hamburg"
                        ),
                        postal_zone=PostalZone(
                            value="29400"
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value="DE"
                            )
                        )
                    )
                ),
                period=[
                    Period(
                        start_date=XmlDate(2011, 10, 3),
                        start_time=XmlTime(9, 30, 10, 0, 60),
                        end_date=XmlDate(2011, 10, 3),
                        end_time=XmlTime(12, 30, 10, 0, 60)
                    ),
                ]
            ),
            planned_delivery_transport_event=PlannedDeliveryTransportEvent(
                location=Location(
                    address=Address(
                        street_name=StreetName(
                            value="Grosse strasse 34"
                        ),
                        city_name=CityName(
                            value="Nurnberg"
                        ),
                        postal_zone=PostalZone(
                            value="28400"
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value="DE"
                            )
                        )
                    )
                ),
                period=[
                    Period(
                        start_date=XmlDate(2011, 10, 6),
                        start_time=XmlTime(12, 30, 10, 0, 60),
                        end_date=XmlDate(2011, 10, 6),
                        end_time=XmlTime(15, 30, 10, 0, 60)
                    ),
                ]
            ),
            consignee_party=ConsigneeParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value="4058673827123",
                            scheme_name="GLN",
                            scheme_agency_name="GS1"
                        )
                    ),
                ],
                party_name=[
                    PartyName(
                        name=Name(
                            value="Consignee"
                        )
                    ),
                ],
                contact=Contact(
                    name=Name(
                        value="SomeName"
                    ),
                    telephone=Telephone(
                        value="+4987878763"
                    ),
                    electronic_mail=ElectronicMail(
                        value="SomeName@consignee.de"
                    )
                )
            ),
            consignor_party=ConsignorParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value="4058673827000",
                            scheme_name="GLN",
                            scheme_agency_name="GS1"
                        )
                    ),
                ],
                party_name=[
                    PartyName(
                        name=Name(
                            value="Consignor"
                        )
                    ),
                ],
                postal_address=PostalAddress(
                    id=Id(
                        value="4058673827000",
                        scheme_name="GLN",
                        scheme_agency_name="GS1"
                    )
                ),
                contact=Contact(
                    name=Name(
                        value="SomeName"
                    ),
                    telephone=Telephone(
                        value="+8676576456"
                    ),
                    electronic_mail=ElectronicMail(
                        value="SomeName@consignor.cn"
                    )
                )
            ),
            original_departure_country=OriginalDepartureCountry(
                identification_code=IdentificationCode(
                    value="CN"
                )
            ),
            final_destination_country=FinalDestinationCountry(
                identification_code=IdentificationCode(
                    value="DE"
                )
            ),
            main_carriage_shipment_stage=[
                MainCarriageShipmentStage(
                    planned_departure_transport_event=PlannedDepartureTransportEvent(
                        location=Location(
                            address=Address(
                                id=Id(
                                    value="DEHAM",
                                    scheme_name="UN/LOCODE",
                                    scheme_agency_name="UN"
                                ),
                                street_name=StreetName(
                                    value="Neuer Wandrahm 4"
                                ),
                                city_name=CityName(
                                    value="Hamburg"
                                ),
                                postal_zone=PostalZone(
                                    value="29400"
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value="DE"
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=XmlDate(2011, 10, 3),
                                start_time=XmlTime(9, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 3),
                                end_time=XmlTime(12, 30, 10, 0, 60)
                            ),
                        ]
                    ),
                    planned_arrival_transport_event=PlannedArrivalTransportEvent(
                        location=Location(
                            address=Address(
                                street_name=StreetName(
                                    value="Grosse strasse 34"
                                ),
                                city_name=CityName(
                                    value="Nurnberg"
                                ),
                                postal_zone=PostalZone(
                                    value="28400"
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value="DE"
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=XmlDate(2011, 10, 6),
                                start_time=XmlTime(12, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 6),
                                end_time=XmlTime(15, 30, 10, 0, 60)
                            ),
                        ]
                    )
                ),
            ],
            pre_carriage_shipment_stage=[
                PreCarriageShipmentStage(
                    transport_mode_code=TransportModeCode(
                        value="1"
                    ),
                    transport_means_type_code=TransportMeansTypeCode(
                        value="83"
                    ),
                    carrier_party=[
                        CarrierParty(
                            party_name=[
                                PartyName(
                                    name=Name(
                                        value="MAERSK"
                                    )
                                ),
                            ],
                            contact=Contact(
                                name=Name(
                                    value="SomeName"
                                ),
                                telephone=Telephone(
                                    value="+4598786765"
                                ),
                                electronic_mail=ElectronicMail(
                                    value="SomeName@maersk.dk"
                                )
                            )
                        ),
                    ],
                    transport_means=TransportMeans(
                        journey_id=JourneyId(
                            value="M22"
                        ),
                        registration_nationality_id=RegistrationNationalityId(
                            value="DK"
                        ),
                        registration_nationality=[
                            RegistrationNationality(
                                value="Denmark"
                            ),
                        ],
                        transport_means_type_code=TransportMeansTypeCode(
                            value="83"
                        ),
                        maritime_transport=MaritimeTransport(
                            vessel_id=VesselId(
                                value="SomeIMONr"
                            ),
                            vessel_name=VesselName(
                                value="SomeVesselName"
                            )
                        )
                    ),
                    planned_departure_transport_event=PlannedDepartureTransportEvent(
                        location=Location(
                            id=Id(
                                value="CNSHA",
                                scheme_name="UN/LOCODE",
                                scheme_agency_name="UN"
                            )
                        ),
                        period=[
                            Period(
                                start_date=XmlDate(2011, 9, 20),
                                start_time=XmlTime(9, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 9, 20),
                                end_time=XmlTime(12, 30, 10, 0, 60)
                            ),
                        ]
                    ),
                    planned_arrival_transport_event=PlannedArrivalTransportEvent(
                        location=Location(
                            id=Id(
                                value="DEHAM",
                                scheme_name="UN/LOCODE",
                                scheme_agency_name="UN"
                            )
                        ),
                        period=[
                            Period(
                                start_date=XmlDate(2011, 10, 1),
                                start_time=XmlTime(9, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 1),
                                end_time=XmlTime(12, 30, 10, 0, 60)
                            ),
                        ]
                    )
                ),
            ],
            transport_handling_unit=[
                TransportHandlingUnit(
                    id=Id(
                        value="CON_THU_1"
                    ),
                    transport_handling_unit_type_code=TransportHandlingUnitTypeCode(
                        value="4"
                    ),
                    hazardous_risk_indicator=False,
                    total_goods_item_quantity=TotalGoodsItemQuantity(
                        value=Decimal("500")
                    ),
                    total_package_quantity=TotalPackageQuantity(
                        value=Decimal("10")
                    ),
                    shipping_marks=[
                        ShippingMarks(
                            value="General Cargo"
                        ),
                    ],
                    transport_equipment=[
                        TransportEquipment(
                            id=Id(
                                value="CON_TE_1"
                            ),
                            transport_equipment_type_code=TransportEquipmentTypeCode(
                                value="CN"
                            ),
                            fullness_indication_code=FullnessIndicationCode(
                                value="1"
                            ),
                            returnability_indicator=True,
                            refrigerated_indicator=False,
                            description=[
                                Description(
                                    value="SomeDescription"
                                ),
                            ],
                            gross_weight_measure=GrossWeightMeasure(
                                value=Decimal("25000"),
                                unit_code="KGM"
                            ),
                            gross_volume_measure=GrossVolumeMeasure(
                                value=Decimal("39"),
                                unit_code="MTQ"
                            ),
                            power_indicator=False,
                            measurement_dimension=[
                                MeasurementDimension(
                                    attribute_id=AttributeId(
                                        value="Length"
                                    ),
                                    measure=Measure(
                                        value=Decimal("6.1"),
                                        unit_code="MTR"
                                    )
                                ),
                                MeasurementDimension(
                                    attribute_id=AttributeId(
                                        value="Height"
                                    ),
                                    measure=Measure(
                                        value=Decimal("2.6"),
                                        unit_code="MTR"
                                    )
                                ),
                                MeasurementDimension(
                                    attribute_id=AttributeId(
                                        value="Width"
                                    ),
                                    measure=Measure(
                                        value=Decimal("2.44"),
                                        unit_code="MTR"
                                    )
                                ),
                            ],
                            package=[
                                Package(
                                    id=Id(
                                        value="CON_P_1"
                                    ),
                                    quantity=Quantity(
                                        value=Decimal("10")
                                    ),
                                    packaging_type_code=PackagingTypeCode(
                                        value="PL"
                                    ),
                                    goods_item=[
                                        GoodsItem(
                                            item=[
                                                Item(
                                                    commodity_classification=[
                                                        CommodityClassification(
                                                            cargo_type_code=CargoTypeCode(
                                                                value="12"
                                                            )
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
                TransportHandlingUnit(
                    id=Id(
                        value="CON_THU_2"
                    ),
                    transport_handling_unit_type_code=TransportHandlingUnitTypeCode(
                        value="4"
                    ),
                    hazardous_risk_indicator=False,
                    total_goods_item_quantity=TotalGoodsItemQuantity(
                        value=Decimal("500")
                    ),
                    total_package_quantity=TotalPackageQuantity(
                        value=Decimal("10")
                    ),
                    shipping_marks=[
                        ShippingMarks(
                            value="General Cargo"
                        ),
                    ],
                    transport_equipment=[
                        TransportEquipment(
                            id=Id(
                                value="CON_TE_2"
                            ),
                            transport_equipment_type_code=TransportEquipmentTypeCode(
                                value="CN"
                            ),
                            fullness_indication_code=FullnessIndicationCode(
                                value="1"
                            ),
                            returnability_indicator=True,
                            refrigerated_indicator=False,
                            description=[
                                Description(
                                    value="SomeDescription"
                                ),
                            ],
                            gross_weight_measure=GrossWeightMeasure(
                                value=Decimal("25000"),
                                unit_code="KGM"
                            ),
                            gross_volume_measure=GrossVolumeMeasure(
                                value=Decimal("39"),
                                unit_code="MTQ"
                            ),
                            power_indicator=False,
                            measurement_dimension=[
                                MeasurementDimension(
                                    attribute_id=AttributeId(
                                        value="Length"
                                    ),
                                    measure=Measure(
                                        value=Decimal("6.1"),
                                        unit_code="MTR"
                                    )
                                ),
                                MeasurementDimension(
                                    attribute_id=AttributeId(
                                        value="Height"
                                    ),
                                    measure=Measure(
                                        value=Decimal("2.6"),
                                        unit_code="MTR"
                                    )
                                ),
                                MeasurementDimension(
                                    attribute_id=AttributeId(
                                        value="Width"
                                    ),
                                    measure=Measure(
                                        value=Decimal("2.44"),
                                        unit_code="MTR"
                                    )
                                ),
                            ],
                            package=[
                                Package(
                                    id=Id(
                                        value="CON_P_2"
                                    ),
                                    quantity=Quantity(
                                        value=Decimal("10")
                                    ),
                                    packaging_type_code=PackagingTypeCode(
                                        value="PL"
                                    ),
                                    goods_item=[
                                        GoodsItem(
                                            item=[
                                                Item(
                                                    commodity_classification=[
                                                        CommodityClassification(
                                                            cargo_type_code=CargoTypeCode(
                                                                value="12"
                                                            )
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ]
)
