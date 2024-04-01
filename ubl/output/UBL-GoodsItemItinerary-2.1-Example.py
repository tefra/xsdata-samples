from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import CommodityClassification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import ContainedInTransportEquipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import GoodsItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import Location
from ubl.models.common.ubl_common_aggregate_components_2_1 import Package
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import Period
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedArrivalTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedDepartureTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReferencedConsignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReferencedTransportEquipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import RoadTransport
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import ShipmentStage
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportEquipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportEquipmentSeal
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportHandlingUnit
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportMeans
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportServiceProviderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportationSegment
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportationService
from ubl.models.common.ubl_common_basic_components_2_1 import CargoTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import Condition
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import EndDate
from ubl.models.common.ubl_common_basic_components_2_1 import EndTime
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import IssueTime
from ubl.models.common.ubl_common_basic_components_2_1 import LicensePlateId
from ubl.models.common.ubl_common_basic_components_2_1 import LocationTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import PackagingTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import SequenceNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import StartDate
from ubl.models.common.ubl_common_basic_components_2_1 import StartTime
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TraceId
from ubl.models.common.ubl_common_basic_components_2_1 import TransportEquipmentTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportExecutionPlanReferenceId
from ubl.models.common.ubl_common_basic_components_2_1 import TransportMeansTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportModeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportServiceCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportationServiceDescription
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import VersionId
from ubl.models.maindoc.ubl_goods_item_itinerary_2_1 import GoodsItemItinerary
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = GoodsItemItinerary(
    ublversion_id=UblversionId(
        value='2.1'
    ),
    id=Id(
        value='1'
    ),
    issue_date=IssueDate(
        value=XmlDate(2011, 9, 13)
    ),
    issue_time=IssueTime(
        value=XmlTime(10, 5, 20, 0, 60)
    ),
    version_id=VersionId(
        value='1'
    ),
    transport_execution_plan_reference_id=TransportExecutionPlanReferenceId(
        value='TEP_1'
    ),
    sender_party=SenderParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value='4058673827641',
                    scheme_name='GLN',
                    scheme_agency_name='GS1'
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value='NECOSS'
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value='SomeName'
            ),
            telephone=Telephone(
                value='+49450557000'
            ),
            electronic_mail=ElectronicMail(
                value='SomeName@necoss.de'
            )
        )
    ),
    receiver_party=ReceiverParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value='4058673827000',
                    scheme_name='GLN',
                    scheme_agency_name='GS1'
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value='Consignor'
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value='SomeName'
            ),
            telephone=Telephone(
                value='+8687878763'
            ),
            electronic_mail=ElectronicMail(
                value='SomeName@consignor.cn'
            )
        )
    ),
    referenced_transport_equipment=[
        ReferencedTransportEquipment(
            id=Id(
                value='1'
            ),
            transport_equipment_seal=[
                TransportEquipmentSeal(
                    id=Id(
                        value='1_1'
                    ),
                    condition=Condition(
                        value='IN_RIGHT_CONDITION'
                    )
                ),
            ],
            package=[
                Package(
                    quantity=Quantity(
                        value=Decimal('10')
                    ),
                    packaging_type_code=PackagingTypeCode(
                        value='PX'
                    ),
                    goods_item=[
                        GoodsItem(
                            item=[
                                Item(
                                    commodity_classification=[
                                        CommodityClassification(
                                            cargo_type_code=CargoTypeCode(
                                                value='12'
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
        ReferencedTransportEquipment(
            id=Id(
                value='2'
            ),
            transport_equipment_seal=[
                TransportEquipmentSeal(
                    id=Id(
                        value='2_1'
                    ),
                    condition=Condition(
                        value='IN_RIGHT_CONDITION'
                    )
                ),
            ],
            package=[
                Package(
                    quantity=Quantity(
                        value=Decimal('10')
                    ),
                    packaging_type_code=PackagingTypeCode(
                        value='PX'
                    ),
                    goods_item=[
                        GoodsItem(
                            item=[
                                Item(
                                    commodity_classification=[
                                        CommodityClassification(
                                            cargo_type_code=CargoTypeCode(
                                                value='12'
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
    ],
    transportation_segment=[
        TransportationSegment(
            sequence_numeric=SequenceNumeric(
                value=Decimal('1')
            ),
            transport_execution_plan_reference_id=TransportExecutionPlanReferenceId(
                value='TEP_2'
            ),
            transportation_service=TransportationService(
                transport_service_code=TransportServiceCode(
                    value='3'
                ),
                transportation_service_description=[
                    TransportationServiceDescription(
                        value='Rail transport service from Hamburg to Bremen'
                    ),
                ]
            ),
            transport_service_provider_party=TransportServiceProviderParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value='4058673827100',
                            scheme_name='GLN',
                            scheme_agency_name='GS1'
                        )
                    ),
                ],
                party_name=[
                    PartyName(
                        name=Name(
                            value='NTT'
                        )
                    ),
                ],
                contact=Contact(
                    name=Name(
                        value='SomeName'
                    ),
                    telephone=Telephone(
                        value='+49450557777'
                    ),
                    electronic_mail=ElectronicMail(
                        value='SomeName@ntt.de'
                    )
                )
            ),
            referenced_consignment=ReferencedConsignment(
                id=Id(
                    value='NTT_1'
                ),
                transport_handling_unit=[
                    TransportHandlingUnit(
                        id=Id(
                            value='NTT_THU_1'
                        ),
                        transport_equipment=[
                            TransportEquipment(
                                id=Id(
                                    value='NTT_THU_1'
                                ),
                                contained_in_transport_equipment=[
                                    ContainedInTransportEquipment(
                                        id=Id(
                                            value='NTT_TE_1'
                                        ),
                                        transport_equipment_type_code=TransportEquipmentTypeCode(
                                            value='RR'
                                        ),
                                        trace_id=TraceId(
                                            value='12345678914564'
                                        )
                                    ),
                                ],
                                package=[
                                    Package(
                                        id=Id(
                                            value='CON_1'
                                        ),
                                        quantity=Quantity(
                                            value=Decimal('10')
                                        )
                                    ),
                                ]
                            ),
                        ]
                    ),
                    TransportHandlingUnit(
                        id=Id(
                            value='NTT_THU_2'
                        ),
                        transport_equipment=[
                            TransportEquipment(
                                id=Id(
                                    value='CON_2'
                                ),
                                contained_in_transport_equipment=[
                                    ContainedInTransportEquipment(
                                        id=Id(
                                            value='NTT_TE_2'
                                        ),
                                        transport_equipment_type_code=TransportEquipmentTypeCode(
                                            value='RR'
                                        ),
                                        trace_id=TraceId(
                                            value='12345678914565'
                                        )
                                    ),
                                ],
                                package=[
                                    Package(
                                        id=Id(
                                            value='CON_2'
                                        ),
                                        quantity=Quantity(
                                            value=Decimal('10')
                                        )
                                    ),
                                ]
                            ),
                        ]
                    ),
                ]
            ),
            shipment_stage=[
                ShipmentStage(
                    id=Id(
                        value='1'
                    ),
                    transport_mode_code=TransportModeCode(
                        value='2'
                    ),
                    transport_means_type_code=TransportMeansTypeCode(
                        value='230'
                    ),
                    planned_departure_transport_event=PlannedDepartureTransportEvent(
                        location=Location(
                            address=Address(
                                id=Id(
                                    value='DEHAM',
                                    scheme_name='UN/LOCODE',
                                    scheme_agency_name='UN'
                                ),
                                street_name=StreetName(
                                    value='Neuer Wandrahm 4'
                                ),
                                city_name=CityName(
                                    value='Hamburg'
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value='DE'
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=StartDate(
                                    value=XmlDate(2011, 10, 3)
                                ),
                                start_time=StartTime(
                                    value=XmlTime(9, 30, 10, 0, 60)
                                ),
                                end_date=EndDate(
                                    value=XmlDate(2011, 10, 3)
                                ),
                                end_time=EndTime(
                                    value=XmlTime(12, 30, 10, 0, 60)
                                )
                            ),
                        ]
                    ),
                    planned_arrival_transport_event=PlannedArrivalTransportEvent(
                        location=Location(
                            location_type_code=LocationTypeCode(
                                value='13'
                            ),
                            address=Address(
                                id=Id(
                                    value='4568763527610',
                                    scheme_name='GLN',
                                    scheme_agency_name='GS1'
                                ),
                                street_name=StreetName(
                                    value='Ludwig-Erhard-Str. 15'
                                ),
                                city_name=CityName(
                                    value='Bremen'
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value='DE'
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=StartDate(
                                    value=XmlDate(2011, 10, 3)
                                ),
                                start_time=StartTime(
                                    value=XmlTime(18, 30, 10, 0, 60)
                                ),
                                end_date=EndDate(
                                    value=XmlDate(2011, 10, 3)
                                ),
                                end_time=EndTime(
                                    value=XmlTime(21, 30, 10, 0, 60)
                                )
                            ),
                        ]
                    )
                ),
            ]
        ),
        TransportationSegment(
            sequence_numeric=SequenceNumeric(
                value=Decimal('2')
            ),
            transport_execution_plan_reference_id=TransportExecutionPlanReferenceId(
                value='TEP_1'
            ),
            transportation_service=TransportationService(
                transport_service_code=TransportServiceCode(
                    value='3'
                ),
                transportation_service_description=[
                    TransportationServiceDescription(
                        value='Rail transport service from Bremen to Nurnberg'
                    ),
                ]
            ),
            transport_service_provider_party=TransportServiceProviderParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value='4058673827641',
                            scheme_name='GLN',
                            scheme_agency_name='GS1'
                        )
                    ),
                ],
                party_name=[
                    PartyName(
                        name=Name(
                            value='NECOSS'
                        )
                    ),
                ],
                contact=Contact(
                    name=Name(
                        value='SomeName'
                    ),
                    telephone=Telephone(
                        value='+49450557000'
                    ),
                    electronic_mail=ElectronicMail(
                        value='SomeName@necoss.de'
                    )
                )
            ),
            referenced_consignment=ReferencedConsignment(
                id=Id(
                    value='CON_1'
                ),
                transport_handling_unit=[
                    TransportHandlingUnit(
                        id=Id(
                            value='CON_THU_1'
                        ),
                        transport_equipment=[
                            TransportEquipment(
                                id=Id(
                                    value='CON_1'
                                ),
                                contained_in_transport_equipment=[
                                    ContainedInTransportEquipment(
                                        id=Id(
                                            value='NEC_TE_1'
                                        ),
                                        transport_equipment_type_code=TransportEquipmentTypeCode(
                                            value='RR'
                                        ),
                                        trace_id=TraceId(
                                            value='12345678914542'
                                        )
                                    ),
                                ],
                                package=[
                                    Package(
                                        id=Id(
                                            value='CON_1'
                                        ),
                                        quantity=Quantity(
                                            value=Decimal('10')
                                        )
                                    ),
                                ]
                            ),
                        ]
                    ),
                    TransportHandlingUnit(
                        id=Id(
                            value='CON_THU_2'
                        ),
                        transport_equipment=[
                            TransportEquipment(
                                id=Id(
                                    value='CON_2'
                                ),
                                contained_in_transport_equipment=[
                                    ContainedInTransportEquipment(
                                        id=Id(
                                            value='NEC_TE_2'
                                        ),
                                        transport_equipment_type_code=TransportEquipmentTypeCode(
                                            value='RR'
                                        ),
                                        trace_id=TraceId(
                                            value='12345678914543'
                                        )
                                    ),
                                ],
                                package=[
                                    Package(
                                        id=Id(
                                            value='CON_2'
                                        ),
                                        quantity=Quantity(
                                            value=Decimal('10')
                                        )
                                    ),
                                ]
                            ),
                        ]
                    ),
                ]
            ),
            shipment_stage=[
                ShipmentStage(
                    id=Id(
                        value='2'
                    ),
                    planned_departure_transport_event=PlannedDepartureTransportEvent(
                        location=Location(
                            location_type_code=LocationTypeCode(
                                value='13'
                            ),
                            address=Address(
                                id=Id(
                                    value='4568763527610',
                                    scheme_name='GLN',
                                    scheme_agency_name='GS1'
                                ),
                                street_name=StreetName(
                                    value='Ludwig-Erhard-Str. 15'
                                ),
                                city_name=CityName(
                                    value='Bremen'
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value='DE'
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=StartDate(
                                    value=XmlDate(2011, 10, 4)
                                ),
                                start_time=StartTime(
                                    value=XmlTime(9, 30, 10, 0, 60)
                                ),
                                end_date=EndDate(
                                    value=XmlDate(2011, 10, 4)
                                ),
                                end_time=EndTime(
                                    value=XmlTime(9, 30, 10, 0, 60)
                                )
                            ),
                        ]
                    ),
                    planned_arrival_transport_event=PlannedArrivalTransportEvent(
                        location=Location(
                            location_type_code=LocationTypeCode(
                                value='13'
                            ),
                            address=Address(
                                street_name=StreetName(
                                    value='Sandstr. 38-40'
                                ),
                                city_name=CityName(
                                    value='Nurnberg'
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value='DE'
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=StartDate(
                                    value=XmlDate(2011, 10, 4)
                                ),
                                start_time=StartTime(
                                    value=XmlTime(15, 30, 10, 0, 60)
                                ),
                                end_date=EndDate(
                                    value=XmlDate(2011, 10, 4)
                                ),
                                end_time=EndTime(
                                    value=XmlTime(18, 30, 10, 0, 60)
                                )
                            ),
                        ]
                    )
                ),
            ]
        ),
        TransportationSegment(
            sequence_numeric=SequenceNumeric(
                value=Decimal('3')
            ),
            transport_execution_plan_reference_id=TransportExecutionPlanReferenceId(
                value='TEP_3'
            ),
            transportation_service=TransportationService(
                transport_service_code=TransportServiceCode(
                    value='3'
                ),
                transportation_service_description=[
                    TransportationServiceDescription(
                        value='Road transport service from Hamburg to Bremen'
                    ),
                ]
            ),
            transport_service_provider_party=TransportServiceProviderParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value='4058673827112',
                            scheme_name='GLN',
                            scheme_agency_name='GS1'
                        )
                    ),
                ],
                party_name=[
                    PartyName(
                        name=Name(
                            value='EXT-HAL'
                        )
                    ),
                ],
                contact=Contact(
                    name=Name(
                        value='SomeName'
                    ),
                    telephone=Telephone(
                        value='+49450557234'
                    ),
                    electronic_mail=ElectronicMail(
                        value='SomeName@ext-hal.de'
                    )
                )
            ),
            referenced_consignment=ReferencedConsignment(
                id=Id(
                    value='EXT_1'
                ),
                transport_handling_unit=[
                    TransportHandlingUnit(
                        id=Id(
                            value='EXT_THU_1'
                        ),
                        transport_equipment=[
                            TransportEquipment(
                                id=Id(
                                    value='CON_1'
                                ),
                                contained_in_transport_equipment=[
                                    ContainedInTransportEquipment(
                                        id=Id(
                                            value='EXT_TE_1'
                                        ),
                                        transport_equipment_type_code=TransportEquipmentTypeCode(
                                            value='TE'
                                        ),
                                        trace_id=TraceId(
                                            value='12345678914111'
                                        )
                                    ),
                                ],
                                package=[
                                    Package(
                                        id=Id(
                                            value='CON_1'
                                        ),
                                        quantity=Quantity(
                                            value=Decimal('10')
                                        )
                                    ),
                                ]
                            ),
                        ],
                        transport_means=[
                            TransportMeans(
                                road_transport=RoadTransport(
                                    license_plate_id=LicensePlateId(
                                        value='WFN667'
                                    )
                                )
                            ),
                        ]
                    ),
                    TransportHandlingUnit(
                        id=Id(
                            value='EXT_THU_2'
                        ),
                        transport_equipment=[
                            TransportEquipment(
                                id=Id(
                                    value='CON_2'
                                ),
                                contained_in_transport_equipment=[
                                    ContainedInTransportEquipment(
                                        id=Id(
                                            value='EXT_TE_2'
                                        ),
                                        transport_equipment_type_code=TransportEquipmentTypeCode(
                                            value='TE'
                                        ),
                                        trace_id=TraceId(
                                            value='12345678914112'
                                        )
                                    ),
                                ],
                                package=[
                                    Package(
                                        id=Id(
                                            value='CON_2'
                                        ),
                                        quantity=Quantity(
                                            value=Decimal('10')
                                        )
                                    ),
                                ]
                            ),
                        ],
                        transport_means=[
                            TransportMeans(
                                road_transport=RoadTransport(
                                    license_plate_id=LicensePlateId(
                                        value='WFN667'
                                    )
                                )
                            ),
                        ]
                    ),
                ]
            ),
            shipment_stage=[
                ShipmentStage(
                    id=Id(
                        value='3'
                    ),
                    planned_departure_transport_event=PlannedDepartureTransportEvent(
                        location=Location(
                            location_type_code=LocationTypeCode(
                                value='13'
                            ),
                            address=Address(
                                street_name=StreetName(
                                    value='Sandstr. 38-40'
                                ),
                                city_name=CityName(
                                    value='Nurnberg'
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value='DE'
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=StartDate(
                                    value=XmlDate(2011, 10, 6)
                                ),
                                start_time=StartTime(
                                    value=XmlTime(9, 30, 10, 0, 60)
                                ),
                                end_date=EndDate(
                                    value=XmlDate(2011, 10, 6)
                                ),
                                end_time=EndTime(
                                    value=XmlTime(12, 30, 10, 0, 60)
                                )
                            ),
                        ]
                    ),
                    planned_arrival_transport_event=PlannedArrivalTransportEvent(
                        location=Location(
                            address=Address(
                                street_name=StreetName(
                                    value='Grosse strasse 34'
                                ),
                                city_name=CityName(
                                    value='Nurnberg'
                                ),
                                country=Country(
                                    identification_code=IdentificationCode(
                                        value='DE'
                                    )
                                )
                            )
                        ),
                        period=[
                            Period(
                                start_date=StartDate(
                                    value=XmlDate(2011, 10, 6)
                                ),
                                start_time=StartTime(
                                    value=XmlTime(12, 30, 10, 0, 60)
                                ),
                                end_date=EndDate(
                                    value=XmlDate(2011, 10, 6)
                                ),
                                end_time=EndTime(
                                    value=XmlTime(15, 30, 10, 0, 60)
                                )
                            ),
                        ]
                    )
                ),
            ]
        ),
    ]
)
