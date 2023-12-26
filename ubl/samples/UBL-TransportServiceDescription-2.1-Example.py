from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Location
from ubl.models.common.ubl_common_aggregate_components_2_1 import MeasurementDimension
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import Period
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedArrivalTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import PlannedDepartureTransportEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import ServiceChargePaymentTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import ShipmentStage
from ubl.models.common.ubl_common_aggregate_components_2_1 import SupportedTransportEquipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportServiceDescriptionRequestDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportServiceProviderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportationService
from ubl.models.common.ubl_common_aggregate_components_2_1 import ValidityPeriod
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import AttributeId
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import LocationTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Measure
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TransportEquipmentTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportServiceCode
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_transport_service_description_2_1 import TransportServiceDescription
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = TransportServiceDescription(
    ublversion_id=UblversionId(
        value='2.1'
    ),
    id=Id(
        value='TSD_RESP_1'
    ),
    issue_date=XmlDate(2011, 9, 12),
    issue_time=XmlTime(11, 1, 10, 0, 60),
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
    transport_service_description_request_document_reference=TransportServiceDescriptionRequestDocumentReference(
        id=Id(
            value='TSD_REQ_1'
        )
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
    service_charge_payment_terms=ServiceChargePaymentTerms(
        amount=Amount(
            value=Decimal('2500'),
            currency_id='EUR'
        ),
        payment_due_date=XmlDate(2011, 11, 6)
    ),
    validity_period=ValidityPeriod(
        start_date=XmlDate(2011, 9, 12),
        end_date=XmlDate(2011, 9, 30),
        end_time=XmlTime(16, 0, 0, 0, 60)
    ),
    transportation_service=[
        TransportationService(
            transport_service_code=TransportServiceCode(
                value='3'
            ),
            supported_transport_equipment=[
                SupportedTransportEquipment(
                    id=Id(
                        value='1'
                    ),
                    transport_equipment_type_code=TransportEquipmentTypeCode(
                        value='CN'
                    ),
                    measurement_dimension=[
                        MeasurementDimension(
                            attribute_id=AttributeId(
                                value='Length'
                            ),
                            measure=Measure(
                                value=Decimal('6.1'),
                                unit_code='MTR'
                            )
                        ),
                        MeasurementDimension(
                            attribute_id=AttributeId(
                                value='Height'
                            ),
                            measure=Measure(
                                value=Decimal('2.6'),
                                unit_code='MTR'
                            )
                        ),
                        MeasurementDimension(
                            attribute_id=AttributeId(
                                value='Width'
                            ),
                            measure=Measure(
                                value=Decimal('2.44'),
                                unit_code='MTR'
                            )
                        ),
                    ]
                ),
                SupportedTransportEquipment(
                    id=Id(
                        value='1'
                    ),
                    transport_equipment_type_code=TransportEquipmentTypeCode(
                        value='CN'
                    ),
                    measurement_dimension=[
                        MeasurementDimension(
                            attribute_id=AttributeId(
                                value='Length'
                            ),
                            measure=Measure(
                                value=Decimal('6.1'),
                                unit_code='MTR'
                            )
                        ),
                        MeasurementDimension(
                            attribute_id=AttributeId(
                                value='Height'
                            ),
                            measure=Measure(
                                value=Decimal('2.6'),
                                unit_code='MTR'
                            )
                        ),
                        MeasurementDimension(
                            attribute_id=AttributeId(
                                value='Width'
                            ),
                            measure=Measure(
                                value=Decimal('2.44'),
                                unit_code='MTR'
                            )
                        ),
                    ]
                ),
            ],
            shipment_stage=[
                ShipmentStage(
                    id=Id(
                        value='1'
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
                                start_date=XmlDate(2011, 10, 3),
                                start_time=XmlTime(9, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 3),
                                end_time=XmlTime(12, 30, 10, 0, 60)
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
                                start_date=XmlDate(2011, 10, 3),
                                start_time=XmlTime(18, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 3),
                                end_time=XmlTime(21, 30, 10, 0, 60)
                            ),
                        ]
                    )
                ),
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
                                start_date=XmlDate(2011, 10, 4),
                                start_time=XmlTime(9, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 4),
                                end_time=XmlTime(9, 30, 10, 0, 60)
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
                                start_date=XmlDate(2011, 10, 4),
                                start_time=XmlTime(15, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 4),
                                end_time=XmlTime(18, 30, 10, 0, 60)
                            ),
                        ]
                    )
                ),
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
                                start_date=XmlDate(2011, 10, 6),
                                start_time=XmlTime(9, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 6),
                                end_time=XmlTime(12, 30, 10, 0, 60)
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
                                start_date=XmlDate(2011, 10, 6),
                                start_time=XmlTime(12, 30, 10, 0, 60),
                                end_date=XmlDate(2011, 10, 6),
                                end_time=XmlTime(15, 30, 10, 0, 60)
                            ),
                        ]
                    )
                ),
            ]
        ),
    ]
)
