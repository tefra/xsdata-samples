from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import ActualPackage
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import AirTransport
from ubl.models.common.ubl_common_aggregate_components_2_1 import Attachment
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import CarrierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import ConsigneeParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Consignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import ConsignorParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import ContractDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import Despatch
from ubl.models.common.ubl_common_aggregate_components_2_1 import DespatchAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DespatchParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import DocumentDistribution
from ubl.models.common.ubl_common_aggregate_components_2_1 import DocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import EstimatedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import ExchangeRate
from ubl.models.common.ubl_common_aggregate_components_2_1 import ExportCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import ExternalReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinalDeliveryParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinalDeliveryTransportationService
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinalDestinationCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import FirstArrivalPortLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import FreightAllowanceCharge
from ubl.models.common.ubl_common_aggregate_components_2_1 import FreightForwarderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import GoodsItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LastExitPortLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import LoadingPortLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import NotifyParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginalDepartureCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginalDespatchTransportationService
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PaymentTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import RoadTransport
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Shipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import ShipmentStage
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransitPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportContract
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportHandlingUnit
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportMeans
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransshipPortLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import UnloadingPortLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import ValidityPeriod
from ubl.models.common.ubl_common_basic_components_2_1 import ActualDespatchDate
from ubl.models.common.ubl_common_basic_components_2_1 import ActualDespatchTime
from ubl.models.common.ubl_common_basic_components_2_1 import AdValoremIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import AircraftId
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReason
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReasonCode
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseAmount
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CalculationRate
from ubl.models.common.ubl_common_basic_components_2_1 import CarrierAssignedId
from ubl.models.common.ubl_common_basic_components_2_1 import ChargeIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import ContractType
from ubl.models.common.ubl_common_basic_components_2_1 import CopyIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentityCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomsStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomsTariffQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import Date
from ubl.models.common.ubl_common_basic_components_2_1 import DeclaredCarriageValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import DeclaredCustomsValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import DeclaredStatisticsValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentHash
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentType
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import EmbeddedDocumentBinaryObject
from ubl.models.common.ubl_common_basic_components_2_1 import EndDate
from ubl.models.common.ubl_common_basic_components_2_1 import EndTime
from ubl.models.common.ubl_common_basic_components_2_1 import ExpiryDate
from ubl.models.common.ubl_common_basic_components_2_1 import ExpiryTime
from ubl.models.common.ubl_common_basic_components_2_1 import FreeOnBoardValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import GrossVolumeMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import GrossWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import HazardousRiskIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import InsuranceValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import IssueTime
from ubl.models.common.ubl_common_basic_components_2_1 import JourneyId
from ubl.models.common.ubl_common_basic_components_2_1 import LatestDeliveryDate
from ubl.models.common.ubl_common_basic_components_2_1 import LatestDeliveryTime
from ubl.models.common.ubl_common_basic_components_2_1 import LicensePlateId
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import MathematicOperatorCode
from ubl.models.common.ubl_common_basic_components_2_1 import MaximumCopiesNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import MultiplierFactorNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import NetNetWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import NetVolumeMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import NetWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import OnCarriageIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import PackagingTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import PaymentMeansId
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Postbox
from ubl.models.common.ubl_common_basic_components_2_1 import PreCarriageIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import PrintQualifier
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RequiredCustomsId
from ubl.models.common.ubl_common_basic_components_2_1 import SequenceNumberId
from ubl.models.common.ubl_common_basic_components_2_1 import SequenceNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import ShippingOrderId
from ubl.models.common.ubl_common_basic_components_2_1 import SourceCurrencyBaseRate
from ubl.models.common.ubl_common_basic_components_2_1 import SourceCurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import SpecialInstructions
from ubl.models.common.ubl_common_basic_components_2_1 import StartDate
from ubl.models.common.ubl_common_basic_components_2_1 import StartTime
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TargetCurrencyBaseRate
from ubl.models.common.ubl_common_basic_components_2_1 import TargetCurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import TariffCode
from ubl.models.common.ubl_common_basic_components_2_1 import TariffDescription
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TotalGoodsItemQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import TotalPackageQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTransportHandlingUnitQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import TrackingId
from ubl.models.common.ubl_common_basic_components_2_1 import TransportHandlingUnitTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportMeansTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportModeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportServiceCode
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uri
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.common.ubl_common_basic_components_2_1 import ValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Xpath
from ubl.models.maindoc.ubl_waybill_2_1 import Waybill
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Waybill(
    ublversion_id=UblversionId(
        value='2.0'
    ),
    customization_id=CustomizationId(
        value='urn:oasis:names:specification:ubl:xpath:Waybill-2.0:samples-2.0-draft'
    ),
    profile_id=ProfileId(
        value='bpid:urn:oasis:names:draft:bpss:ubl-2-sample-international-scenario'
    ),
    id=Id(
        value='KHN23-44044-1'
    ),
    carrier_assigned_id=CarrierAssignedId(
        value='123456789987654321'
    ),
    uuid=Uuid(
        value='74638995-D67E-002F-436-8G17366352B1'
    ),
    issue_date=IssueDate(
        value=XmlDate(2005, 6, 25)
    ),
    issue_time=IssueTime(
        value=XmlTime(9, 0, 0, 0, 0)
    ),
    name=Name(
        value='Air Waybill'
    ),
    shipping_order_id=ShippingOrderId(
        value='KHN23-44044'
    ),
    ad_valorem_indicator=AdValoremIndicator(
        value=False
    ),
    declared_carriage_value_amount=DeclaredCarriageValueAmount(
        value=Decimal('1500.00'),
        currency_id='USD'
    ),
    consignor_party=ConsignorParty(
        party_name=[
            PartyName(
                name=Name(
                    value='Consortial'
                )
            ),
        ],
        postal_address=PostalAddress(
            street_name=StreetName(
                value='Boston Road'
            ),
            building_name=BuildingName(
                value='Suite M-102'
            ),
            building_number=BuildingNumber(
                value='630'
            ),
            city_name=CityName(
                value='Billerica'
            ),
            postal_zone=PostalZone(
                value='01821'
            ),
            country_subentity=CountrySubentity(
                value='Massachusetts'
            ),
            country_subentity_code=CountrySubentityCode(
                value='MA'
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value='US'
                )
            )
        ),
        contact=Contact(
            name=Name(
                value='Mrs Bouquet'
            ),
            telephone=Telephone(
                value=' +1 158 1233714'
            ),
            telefax=Telefax(
                value='+ 1 158 1233856'
            ),
            electronic_mail=ElectronicMail(
                value='bouquet@fpconsortial.com'
            )
        )
    ),
    carrier_party=CarrierParty(
        party_name=[
            PartyName(
                name=Name(
                    value='United Airfreight'
                )
            ),
        ],
        contact=Contact(
            id=Id(
                value='Freight Bookings'
            ),
            telephone=Telephone(
                value='+1 3362 4788'
            ),
            electronic_mail=ElectronicMail(
                value='bookings@unitedfreight.com'
            )
        )
    ),
    freight_forwarder_party=FreightForwarderParty(
        party_name=[
            PartyName(
                name=Name(
                    value='One-Stop Forwarders'
                )
            ),
        ],
        postal_address=PostalAddress(
            postbox=Postbox(
                value='99043'
            ),
            city_name=CityName(
                value='Boston'
            ),
            postal_zone=PostalZone(
                value='02210'
            ),
            country_subentity_code=CountrySubentityCode(
                value='MA'
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value='US'
                )
            )
        ),
        contact=Contact(
            name=Name(
                value='Con Solidador'
            ),
            telephone=Telephone(
                value=' +1 343 1453654'
            ),
            telefax=Telefax(
                value='+1 343 1453655'
            ),
            electronic_mail=ElectronicMail(
                value='ctanner@onestopfreight.com'
            )
        )
    ),
    shipment=Shipment(
        id=Id(
            value='CONS-0001'
        ),
        gross_weight_measure=GrossWeightMeasure(
            value=Decimal('130'),
            unit_code='KGM'
        ),
        net_weight_measure=NetWeightMeasure(
            value=Decimal('110'),
            unit_code='KGM'
        ),
        net_net_weight_measure=NetNetWeightMeasure(
            value=Decimal('100'),
            unit_code='KGM'
        ),
        gross_volume_measure=GrossVolumeMeasure(
            value=Decimal('2'),
            unit_code='MTQ'
        ),
        net_volume_measure=NetVolumeMeasure(
            value=Decimal('2.235'),
            unit_code='MTQ'
        ),
        total_goods_item_quantity=TotalGoodsItemQuantity(
            value=Decimal('1')
        ),
        total_transport_handling_unit_quantity=TotalTransportHandlingUnitQuantity(
            value=Decimal('10')
        ),
        insurance_value_amount=InsuranceValueAmount(
            value=Decimal('1000.00'),
            currency_id='USD'
        ),
        declared_customs_value_amount=DeclaredCustomsValueAmount(
            value=Decimal('524.80'),
            currency_id='GBP'
        ),
        free_on_board_value_amount=FreeOnBoardValueAmount(
            value=Decimal('1200.00'),
            currency_id='USD'
        ),
        special_instructions=[
            SpecialInstructions(
                value="Beeswax becomes liquid at 50'C"
            ),
        ],
        consignment=[
            Consignment(
                id=Id(
                    value='2005US12345678998765432112345678',
                    scheme_name='Unique Consignment Reference',
                    scheme_agency_name='WCO'
                ),
                tariff_description=[
                    TariffDescription(
                        value='Beeswax, other insect waxes and spermacetti'
                    ),
                ],
                tariff_code=TariffCode(
                    value='15219000'
                ),
                hazardous_risk_indicator=HazardousRiskIndicator(
                    value=False
                ),
                consignee_party=ConsigneeParty(
                    party_name=[
                        PartyName(
                            name=Name(
                                value='IYT Corporation'
                            )
                        ),
                    ],
                    postal_address=PostalAddress(
                        street_name=StreetName(
                            value='Avon Way'
                        ),
                        building_name=BuildingName(
                            value='Thereabouts'
                        ),
                        building_number=BuildingNumber(
                            value='56A'
                        ),
                        city_name=CityName(
                            value='Bridgtow'
                        ),
                        postal_zone=PostalZone(
                            value='ZZ99 1ZZ'
                        ),
                        country_subentity=CountrySubentity(
                            value='Avon'
                        ),
                        address_line=[
                            AddressLine(
                                line=Line(
                                    value='3rd Floor, Room 5'
                                )
                            ),
                        ],
                        country=Country(
                            identification_code=IdentificationCode(
                                value='GB'
                            )
                        )
                    ),
                    contact=Contact(
                        name=Name(
                            value='Mr Fred Churchill'
                        ),
                        telephone=Telephone(
                            value='+44 127 2653214'
                        ),
                        telefax=Telefax(
                            value='+44 127 2653215'
                        ),
                        electronic_mail=ElectronicMail(
                            value='fred@iytcorporation.gov.uk'
                        )
                    )
                ),
                notify_party=NotifyParty(
                    party_name=[
                        PartyName(
                            name=Name(
                                value='IYT Corporation'
                            )
                        ),
                    ],
                    postal_address=PostalAddress(
                        street_name=StreetName(
                            value='Avon Way'
                        ),
                        building_name=BuildingName(
                            value='Thereabouts'
                        ),
                        building_number=BuildingNumber(
                            value='56A'
                        ),
                        city_name=CityName(
                            value='Bridgtow'
                        ),
                        postal_zone=PostalZone(
                            value='ZZ99 1ZZ'
                        ),
                        country_subentity=CountrySubentity(
                            value='Avon'
                        ),
                        address_line=[
                            AddressLine(
                                line=Line(
                                    value='3rd Floor, Room 5'
                                )
                            ),
                        ],
                        country=Country(
                            identification_code=IdentificationCode(
                                value='GB'
                            )
                        )
                    ),
                    contact=Contact(
                        name=Name(
                            value='Mr Fred Churchill'
                        ),
                        telephone=Telephone(
                            value='+44 127 2653214'
                        ),
                        telefax=Telefax(
                            value='+44 127 2653215'
                        ),
                        electronic_mail=ElectronicMail(
                            value='fred@iytcorporation.gov.uk'
                        )
                    )
                ),
                final_delivery_party=FinalDeliveryParty(
                    party_name=[
                        PartyName(
                            name=Name(
                                value='The Terminus'
                            )
                        ),
                    ],
                    postal_address=PostalAddress(
                        street_name=StreetName(
                            value='Avon Way'
                        ),
                        building_name=BuildingName(
                            value='Thereabouts'
                        ),
                        building_number=BuildingNumber(
                            value='56A'
                        ),
                        city_name=CityName(
                            value='Bridgtow'
                        ),
                        postal_zone=PostalZone(
                            value='ZZ99 1ZZ'
                        ),
                        country_subentity=CountrySubentity(
                            value='Avon'
                        ),
                        address_line=[
                            AddressLine(
                                line=Line(
                                    value='3rd Floor, Room 5'
                                )
                            ),
                        ],
                        country=Country(
                            identification_code=IdentificationCode(
                                value='GB'
                            )
                        )
                    ),
                    contact=Contact(
                        name=Name(
                            value='S Massiah'
                        ),
                        telephone=Telephone(
                            value='+ 44 127 98876545'
                        ),
                        telefax=Telefax(
                            value='+ 44 127 98876546'
                        ),
                        electronic_mail=ElectronicMail(
                            value='smassiah@the-email.co.uk'
                        )
                    )
                ),
                original_departure_country=OriginalDepartureCountry(
                    identification_code=IdentificationCode(
                        value='US'
                    )
                ),
                final_destination_country=FinalDestinationCountry(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                ),
                transport_contract=TransportContract(
                    id=Id(
                        value='CONS-001'
                    ),
                    issue_date=IssueDate(
                        value=XmlDate(2005, 6, 24)
                    ),
                    contract_type=ContractType(
                        value='Forwarding Instructions'
                    ),
                    validity_period=ValidityPeriod(
                        start_date=StartDate(
                            value=XmlDate(2005, 6, 25)
                        ),
                        start_time=StartTime(
                            value=XmlTime(1, 0, 0, 0, 0)
                        ),
                        end_date=EndDate(
                            value=XmlDate(2005, 6, 30)
                        ),
                        end_time=EndTime(
                            value=XmlTime(18, 0, 0, 0, 0)
                        )
                    ),
                    contract_document_reference=[
                        ContractDocumentReference(
                            id=Id(
                                value='normalizedString'
                            ),
                            copy_indicator=CopyIndicator(
                                value=False
                            ),
                            uuid=Uuid(
                                value='normalizedString'
                            ),
                            issue_date=IssueDate(
                                value=XmlDate(1967, 8, 13)
                            ),
                            document_type_code=DocumentTypeCode(
                                value='normalizedString'
                            ),
                            document_type=DocumentType(
                                value='String'
                            ),
                            xpath=[
                                Xpath(
                                    value='String'
                                ),
                                Xpath(
                                    value='String'
                                ),
                            ],
                            attachment=Attachment(
                                embedded_document_binary_object=EmbeddedDocumentBinaryObject(
                                    value=b'R0lGODlhcgGSALMAAAQCAEMmCZtuMFQxDS8b',
                                    mime_code='application/CSTAdata+xml'
                                ),
                                external_reference=ExternalReference(
                                    uri=Uri(
                                        value='normalizedString'
                                    ),
                                    document_hash=DocumentHash(
                                        value='String'
                                    ),
                                    expiry_date=ExpiryDate(
                                        value=XmlDate(1967, 8, 13)
                                    ),
                                    expiry_time=ExpiryTime(
                                        value=XmlTime(14, 20, 0, 0, 0)
                                    )
                                )
                            )
                        ),
                        ContractDocumentReference(
                            id=Id(
                                value='normalizedString'
                            ),
                            copy_indicator=CopyIndicator(
                                value=False
                            ),
                            uuid=Uuid(
                                value='normalizedString'
                            ),
                            issue_date=IssueDate(
                                value=XmlDate(1967, 8, 13)
                            ),
                            document_type_code=DocumentTypeCode(
                                value='normalizedString'
                            ),
                            document_type=DocumentType(
                                value='String'
                            ),
                            xpath=[
                                Xpath(
                                    value='String'
                                ),
                                Xpath(
                                    value='String'
                                ),
                            ],
                            attachment=Attachment(
                                embedded_document_binary_object=EmbeddedDocumentBinaryObject(
                                    value=b'R0lGODlhcgGSALMAAAQCAEMmCZtuMFQxDS8b',
                                    mime_code='application/CSTAdata+xml'
                                ),
                                external_reference=ExternalReference(
                                    uri=Uri(
                                        value='normalizedString'
                                    ),
                                    document_hash=DocumentHash(
                                        value='String'
                                    ),
                                    expiry_date=ExpiryDate(
                                        value=XmlDate(1967, 8, 13)
                                    ),
                                    expiry_time=ExpiryTime(
                                        value=XmlTime(14, 20, 0, 0, 0)
                                    )
                                )
                            )
                        ),
                    ]
                ),
                original_despatch_transportation_service=OriginalDespatchTransportationService(
                    transport_service_code=TransportServiceCode(
                        value='Door to Pier'
                    )
                ),
                final_delivery_transportation_service=FinalDeliveryTransportationService(
                    transport_service_code=TransportServiceCode(
                        value='Pier to Pier'
                    )
                ),
                delivery_terms=DeliveryTerms(
                    id=Id(
                        value='FOB Destination'
                    ),
                    delivery_location=DeliveryLocation(
                        id=Id(
                            value='GBBRS',
                            scheme_id='UN/LOCODE',
                            scheme_agency_id='6'
                        ),
                        description=[
                            Description(
                                value='Bristol'
                            ),
                        ]
                    )
                ),
                payment_terms=PaymentTerms(
                    payment_means_id=[
                        PaymentMeansId(
                            value='Bankers Cheque'
                        ),
                    ]
                ),
                freight_allowance_charge=[
                    FreightAllowanceCharge(
                        charge_indicator=ChargeIndicator(
                            value=True
                        ),
                        allowance_charge_reason=[
                            AllowanceChargeReason(
                                value='Freight charges'
                            ),
                        ],
                        sequence_numeric=SequenceNumeric(
                            value=Decimal('1')
                        ),
                        amount=Amount(
                            value=Decimal('254.00'),
                            currency_id='USD'
                        )
                    ),
                    FreightAllowanceCharge(
                        charge_indicator=ChargeIndicator(
                            value=False
                        ),
                        allowance_charge_reason_code=AllowanceChargeReasonCode(
                            value='79'
                        ),
                        allowance_charge_reason=[
                            AllowanceChargeReason(
                                value='Sundry discount'
                            ),
                        ],
                        multiplier_factor_numeric=MultiplierFactorNumeric(
                            value=Decimal('0.05')
                        ),
                        sequence_numeric=SequenceNumeric(
                            value=Decimal('2')
                        ),
                        amount=Amount(
                            value=Decimal('12.70'),
                            currency_id='USD'
                        ),
                        base_amount=BaseAmount(
                            value=Decimal('254.00'),
                            currency_id='USD'
                        )
                    ),
                ]
            ),
        ],
        goods_item=[
            GoodsItem(
                id=Id(
                    value='1'
                ),
                sequence_number_id=SequenceNumberId(
                    value='1'
                ),
                description=[
                    Description(
                        value='Acme beeswax'
                    ),
                ],
                hazardous_risk_indicator=HazardousRiskIndicator(
                    value=False
                ),
                declared_customs_value_amount=DeclaredCustomsValueAmount(
                    value=Decimal('524.80'),
                    currency_id='GBP'
                ),
                declared_statistics_value_amount=DeclaredStatisticsValueAmount(
                    value=Decimal('1000.00'),
                    currency_id='USD'
                ),
                free_on_board_value_amount=FreeOnBoardValueAmount(
                    value=Decimal('1241.30'),
                    currency_id='USD'
                ),
                insurance_value_amount=InsuranceValueAmount(
                    value=Decimal('1241.30'),
                    currency_id='USD'
                ),
                value_amount=ValueAmount(
                    value=Decimal('1000.00'),
                    currency_id='USD'
                ),
                gross_weight_measure=GrossWeightMeasure(
                    value=Decimal('130'),
                    unit_code='KGM'
                ),
                net_weight_measure=NetWeightMeasure(
                    value=Decimal('110'),
                    unit_code='KGM'
                ),
                net_net_weight_measure=NetNetWeightMeasure(
                    value=Decimal('100'),
                    unit_code='KGM'
                ),
                gross_volume_measure=GrossVolumeMeasure(
                    value=Decimal('2'),
                    unit_code='MTQ'
                ),
                net_volume_measure=NetVolumeMeasure(
                    value=Decimal('2.235'),
                    unit_code='MTQ'
                ),
                quantity=Quantity(
                    value=Decimal('10')
                ),
                required_customs_id=RequiredCustomsId(
                    value='ECN12344566'
                ),
                customs_status_code=CustomsStatusCode(
                    value='Cleared'
                ),
                customs_tariff_quantity=CustomsTariffQuantity(
                    value=Decimal('1000')
                ),
                item=[
                    Item(
                        description=[
                            Description(
                                value='Beeswax'
                            ),
                        ],
                        name=Name(
                            value='Acme Beeswax'
                        ),
                        buyers_item_identification=BuyersItemIdentification(
                            id=Id(
                                value='6578489'
                            )
                        ),
                        sellers_item_identification=SellersItemIdentification(
                            id=Id(
                                value='17589683'
                            )
                        ),
                        origin_country=OriginCountry(
                            identification_code=IdentificationCode(
                                value='MX'
                            ),
                            name=Name(
                                value='Mexico'
                            )
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
                transport_mode_code=TransportModeCode(
                    value='3',
                    list_id='UN/ECE rec 16',
                    list_agency_id='6'
                ),
                transport_means_type_code=TransportMeansTypeCode(
                    value='Truck'
                ),
                pre_carriage_indicator=PreCarriageIndicator(
                    value=True
                ),
                on_carriage_indicator=OnCarriageIndicator(
                    value=False
                ),
                transit_period=TransitPeriod(
                    start_date=StartDate(
                        value=XmlDate(2005, 6, 25)
                    ),
                    start_time=StartTime(
                        value=XmlTime(11, 35, 0, 0, 0)
                    ),
                    end_date=EndDate(
                        value=XmlDate(2005, 6, 25)
                    ),
                    end_time=EndTime(
                        value=XmlTime(16, 0, 0, 0, 0)
                    )
                ),
                carrier_party=[
                    CarrierParty(
                        party_name=[
                            PartyName(
                                name=Name(
                                    value='Keep On Trucking'
                                )
                            ),
                        ],
                        contact=Contact(
                            telephone=Telephone(
                                value='+1 36222 33847'
                            )
                        )
                    ),
                ],
                transport_means=TransportMeans(
                    road_transport=RoadTransport(
                        license_plate_id=LicensePlateId(
                            value='2652 WE'
                        )
                    )
                )
            ),
            ShipmentStage(
                id=Id(
                    value='2'
                ),
                transport_mode_code=TransportModeCode(
                    value='4',
                    list_id='UN/ECE rec 16',
                    list_agency_id='6'
                ),
                transport_means_type_code=TransportMeansTypeCode(
                    value='Plane'
                ),
                pre_carriage_indicator=PreCarriageIndicator(
                    value=False
                ),
                on_carriage_indicator=OnCarriageIndicator(
                    value=False
                ),
                transit_period=TransitPeriod(
                    start_date=StartDate(
                        value=XmlDate(2005, 6, 25)
                    ),
                    start_time=StartTime(
                        value=XmlTime(23, 20, 0, 0, 0)
                    )
                ),
                carrier_party=[
                    CarrierParty(
                        party_name=[
                            PartyName(
                                name=Name(
                                    value='United Airfreight'
                                )
                            ),
                        ],
                        contact=Contact(
                            id=Id(
                                value='Freight Bookings'
                            ),
                            telephone=Telephone(
                                value='+1 3362 4788'
                            ),
                            electronic_mail=ElectronicMail(
                                value='bookings@unitedfreight.com'
                            )
                        )
                    ),
                ],
                transport_means=TransportMeans(
                    journey_id=JourneyId(
                        value='UA 1234'
                    ),
                    air_transport=AirTransport(
                        aircraft_id=AircraftId(
                            value='A-127763-747'
                        )
                    )
                ),
                loading_port_location=LoadingPortLocation(
                    id=Id(
                        value='USBOS',
                        scheme_id='UN/LOCODE',
                        scheme_agency_id='6'
                    ),
                    description=[
                        Description(
                            value='Boston Airport'
                        ),
                    ]
                ),
                unloading_port_location=UnloadingPortLocation(
                    id=Id(
                        value='GBBRS',
                        scheme_id='UN/LOCODE',
                        scheme_agency_id='6'
                    ),
                    description=[
                        Description(
                            value='Bristol Airport'
                        ),
                    ]
                ),
                transship_port_location=TransshipPortLocation(
                    id=Id(
                        value='GBLHR',
                        scheme_id='UN/LOCODE',
                        scheme_agency_id='6'
                    ),
                    description=[
                        Description(
                            value='Heathrow Apt/London'
                        ),
                    ]
                )
            ),
        ],
        delivery=Delivery(
            quantity=Quantity(
                value=Decimal('1')
            ),
            latest_delivery_date=LatestDeliveryDate(
                value=XmlDate(2005, 6, 30)
            ),
            latest_delivery_time=LatestDeliveryTime(
                value=XmlTime(18, 0, 0, 0, 0)
            ),
            tracking_id=TrackingId(
                value='NKH7712289-03339-000128'
            ),
            delivery_address=DeliveryAddress(
                street_name=StreetName(
                    value='Avon Way'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Bridgtow'
                ),
                postal_zone=PostalZone(
                    value='ZZ99 1ZZ'
                ),
                country_subentity=CountrySubentity(
                    value='Avon'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='3rd Floor, Room 5'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            ),
            requested_delivery_period=RequestedDeliveryPeriod(
                start_date=StartDate(
                    value=XmlDate(2005, 6, 29)
                ),
                start_time=StartTime(
                    value=XmlTime(1, 0, 0, 0, 0)
                ),
                end_date=EndDate(
                    value=XmlDate(2005, 6, 30)
                ),
                end_time=EndTime(
                    value=XmlTime(18, 0, 0, 0, 0)
                )
            ),
            estimated_delivery_period=EstimatedDeliveryPeriod(
                start_date=StartDate(
                    value=XmlDate(2005, 6, 30)
                ),
                start_time=StartTime(
                    value=XmlTime(1, 0, 0, 0, 0)
                )
            ),
            delivery_party=DeliveryParty(
                party_name=[
                    PartyName(
                        name=Name(
                            value='The Terminus'
                        )
                    ),
                ],
                contact=Contact(
                    name=Name(
                        value='S Massiah'
                    ),
                    telephone=Telephone(
                        value='+ 44 127 98876545'
                    ),
                    telefax=Telefax(
                        value='+ 44 127 98876546'
                    ),
                    electronic_mail=ElectronicMail(
                        value='smassiah@the-email.co.uk'
                    )
                )
            ),
            despatch=Despatch(
                actual_despatch_date=ActualDespatchDate(
                    value=XmlDate(2005, 6, 25)
                ),
                actual_despatch_time=ActualDespatchTime(
                    value=XmlTime(11, 35, 0, 0, 0)
                ),
                despatch_address=DespatchAddress(
                    street_name=StreetName(
                        value='Boston Road'
                    ),
                    building_name=BuildingName(
                        value='Suite M-102'
                    ),
                    building_number=BuildingNumber(
                        value='630'
                    ),
                    city_name=CityName(
                        value='Billerica'
                    ),
                    postal_zone=PostalZone(
                        value='01821'
                    ),
                    country_subentity=CountrySubentity(
                        value='Massachusetts'
                    ),
                    country_subentity_code=CountrySubentityCode(
                        value='MA'
                    ),
                    country=Country(
                        identification_code=IdentificationCode(
                            value='US'
                        )
                    )
                ),
                despatch_party=DespatchParty(
                    party_name=[
                        PartyName(
                            name=Name(
                                value='Consortial'
                            )
                        ),
                    ]
                ),
                contact=Contact(
                    name=Name(
                        value='Mrs Bouquet'
                    ),
                    telephone=Telephone(
                        value=' +1 158 1233714'
                    ),
                    telefax=Telefax(
                        value='+ 1 158 1233856'
                    ),
                    electronic_mail=ElectronicMail(
                        value='bouquet@fpconsortial.com'
                    )
                )
            )
        ),
        transport_handling_unit=[
            TransportHandlingUnit(
                id=Id(
                    value='1'
                ),
                transport_handling_unit_type_code=TransportHandlingUnitTypeCode(
                    value='PA',
                    list_id='TRED 8053',
                    list_agency_name='United Nations Economic Commission for Europe'
                ),
                hazardous_risk_indicator=HazardousRiskIndicator(
                    value=False
                ),
                total_goods_item_quantity=TotalGoodsItemQuantity(
                    value=Decimal('10')
                ),
                total_package_quantity=TotalPackageQuantity(
                    value=Decimal('10')
                ),
                actual_package=[
                    ActualPackage(
                        quantity=Quantity(
                            value=Decimal('10')
                        ),
                        packaging_type_code=PackagingTypeCode(
                            value='TB',
                            list_id='UN/ECE rec 21',
                            list_agency_id='6'
                        )
                    ),
                ]
            ),
        ],
        origin_address=OriginAddress(
            street_name=StreetName(
                value='Boston Road'
            ),
            building_name=BuildingName(
                value='Suite M-102'
            ),
            building_number=BuildingNumber(
                value='630'
            ),
            city_name=CityName(
                value='Billerica'
            ),
            postal_zone=PostalZone(
                value='01821'
            ),
            country_subentity=CountrySubentity(
                value='Massachusetts'
            ),
            country_subentity_code=CountrySubentityCode(
                value='MA'
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value='US'
                )
            )
        ),
        first_arrival_port_location=FirstArrivalPortLocation(
            id=Id(
                value='GBBRS',
                scheme_id='UN/LOCODE',
                scheme_agency_id='6'
            ),
            description=[
                Description(
                    value='Bristol'
                ),
            ]
        ),
        last_exit_port_location=LastExitPortLocation(
            id=Id(
                value='USBOS',
                scheme_id='UN/LOCODE',
                scheme_agency_id='6'
            ),
            description=[
                Description(
                    value='Boston'
                ),
            ]
        ),
        export_country=ExportCountry(
            identification_code=IdentificationCode(
                value='US'
            )
        ),
        freight_allowance_charge=[
            FreightAllowanceCharge(
                charge_indicator=ChargeIndicator(
                    value=True
                ),
                allowance_charge_reason=[
                    AllowanceChargeReason(
                        value='Freight charges'
                    ),
                ],
                sequence_numeric=SequenceNumeric(
                    value=Decimal('1')
                ),
                amount=Amount(
                    value=Decimal('254.00'),
                    currency_id='USD'
                )
            ),
            FreightAllowanceCharge(
                charge_indicator=ChargeIndicator(
                    value=False
                ),
                allowance_charge_reason_code=AllowanceChargeReasonCode(
                    value='79'
                ),
                allowance_charge_reason=[
                    AllowanceChargeReason(
                        value='Sundry discount'
                    ),
                ],
                multiplier_factor_numeric=MultiplierFactorNumeric(
                    value=Decimal('0.05')
                ),
                sequence_numeric=SequenceNumeric(
                    value=Decimal('2')
                ),
                amount=Amount(
                    value=Decimal('12.70'),
                    currency_id='USD'
                ),
                base_amount=BaseAmount(
                    value=Decimal('254.00'),
                    currency_id='USD'
                )
            ),
        ]
    ),
    document_reference=[
        DocumentReference(
            id=Id(
                value='AEG012345'
            ),
            uuid=Uuid(
                value='6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1'
            ),
            issue_date=IssueDate(
                value=XmlDate(2005, 6, 20)
            ),
            document_type=DocumentType(
                value='Order'
            )
        ),
        DocumentReference(
            id=Id(
                value='KHN23-44044'
            ),
            uuid=Uuid(
                value='6E09886B-DC6E-439F-82D1-7C83746352B1'
            ),
            issue_date=IssueDate(
                value=XmlDate(2005, 6, 24)
            ),
            document_type=DocumentType(
                value='Forwarding Instructions'
            )
        ),
    ],
    exchange_rate=[
        ExchangeRate(
            source_currency_code=SourceCurrencyCode(
                value='USD'
            ),
            source_currency_base_rate=SourceCurrencyBaseRate(
                value=Decimal('1.00')
            ),
            target_currency_code=TargetCurrencyCode(
                value='GBP'
            ),
            target_currency_base_rate=TargetCurrencyBaseRate(
                value=Decimal('1.00')
            ),
            calculation_rate=CalculationRate(
                value=Decimal('1.8947')
            ),
            mathematic_operator_code=MathematicOperatorCode(
                value='Multiply'
            ),
            date=Date(
                value=XmlDate(1967, 8, 13)
            )
        ),
    ],
    document_distribution=[
        DocumentDistribution(
            print_qualifier=PrintQualifier(
                value='Copies allowed'
            ),
            maximum_copies_numeric=MaximumCopiesNumeric(
                value=Decimal('5')
            ),
            party=Party(
                party_name=[
                    PartyName(
                        name=Name(
                            value='Consortial'
                        )
                    ),
                ],
                postal_address=PostalAddress(
                    street_name=StreetName(
                        value='Boston Road'
                    ),
                    building_name=BuildingName(
                        value='Suite M-102'
                    ),
                    building_number=BuildingNumber(
                        value='630'
                    ),
                    city_name=CityName(
                        value='Billerica'
                    ),
                    postal_zone=PostalZone(
                        value='01821'
                    ),
                    country_subentity=CountrySubentity(
                        value='Massachusetts'
                    ),
                    country_subentity_code=CountrySubentityCode(
                        value='MA'
                    ),
                    country=Country(
                        identification_code=IdentificationCode(
                            value='US'
                        )
                    )
                ),
                contact=Contact(
                    name=Name(
                        value='Mrs Bouquet'
                    ),
                    telephone=Telephone(
                        value=' +1 158 1233714'
                    ),
                    telefax=Telefax(
                        value='+ 1 158 1233856'
                    ),
                    electronic_mail=ElectronicMail(
                        value='bouquet@fpconsortial.com'
                    )
                )
            )
        ),
        DocumentDistribution(
            print_qualifier=PrintQualifier(
                value='Copies allowed'
            ),
            maximum_copies_numeric=MaximumCopiesNumeric(
                value=Decimal('4')
            ),
            party=Party(
                party_name=[
                    PartyName(
                        name=Name(
                            value='IYT Corporation'
                        )
                    ),
                ],
                postal_address=PostalAddress(
                    street_name=StreetName(
                        value='Avon Way'
                    ),
                    building_name=BuildingName(
                        value='Thereabouts'
                    ),
                    building_number=BuildingNumber(
                        value='56A'
                    ),
                    city_name=CityName(
                        value='Bridgtow'
                    ),
                    postal_zone=PostalZone(
                        value='ZZ99 1ZZ'
                    ),
                    country_subentity=CountrySubentity(
                        value='Avon'
                    ),
                    address_line=[
                        AddressLine(
                            line=Line(
                                value='3rd Floor, Room 5'
                            )
                        ),
                    ],
                    country=Country(
                        identification_code=IdentificationCode(
                            value='GB'
                        )
                    )
                ),
                contact=Contact(
                    name=Name(
                        value='Mr Fred Churchill'
                    ),
                    telephone=Telephone(
                        value='+44 127 2653214'
                    ),
                    telefax=Telefax(
                        value='+44 127 2653215'
                    ),
                    electronic_mail=ElectronicMail(
                        value='fred@iytcorporation.gov.uk'
                    )
                )
            )
        ),
    ]
)
