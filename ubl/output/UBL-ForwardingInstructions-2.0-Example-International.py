from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import ConsigneeParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Consignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import ConsignorParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinalDeliveryParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinalDestinationCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import FreightAllowanceCharge
from ubl.models.common.ubl_common_aggregate_components_2_1 import FreightForwarderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import GoodsItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import NotifyParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginalDepartureCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Shipment
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReason
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReasonCode
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseAmount
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import ChargeIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentityCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomsStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomsTariffQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import DeclaredCustomsValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import DeclaredStatisticsValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import FreeOnBoardValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import GrossVolumeMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import GrossWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import HazardousRiskIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import InsuranceValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import IssueTime
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import MultiplierFactorNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import NetNetWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import NetVolumeMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import NetWeightMeasure
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Postbox
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RequiredCustomsId
from ubl.models.common.ubl_common_basic_components_2_1 import SequenceNumberId
from ubl.models.common.ubl_common_basic_components_2_1 import SequenceNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import SpecialInstructions
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TariffCode
from ubl.models.common.ubl_common_basic_components_2_1 import TariffDescription
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TotalGoodsItemQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTransportHandlingUnitQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.common.ubl_common_basic_components_2_1 import ValueAmount
from ubl.models.maindoc.ubl_forwarding_instructions_2_1 import ForwardingInstructions
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = ForwardingInstructions(
    ublversion_id=UblversionId(
        value='2.0'
    ),
    customization_id=CustomizationId(
        value='urn:oasis:names:specification:ubl:xpath:ForwardingInstructions-2.0:samples-2.0-draft'
    ),
    profile_id=ProfileId(
        value='bpid:urn:oasis:names:draft:bpss:ubl-2-sample-international-scenario'
    ),
    id=Id(
        value='KHN23-44044'
    ),
    uuid=Uuid(
        value='6E09886B-DC6E-439F-82D1-7C83746352B1'
    ),
    issue_date=IssueDate(
        value=XmlDate(2005, 6, 24)
    ),
    issue_time=IssueTime(
        value=XmlTime(14, 20, 0, 0, 0)
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
                    value='CONS-0001'
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
                    value=Decimal('100')
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
                        )
                    ),
                ]
            ),
        ]
    )
)
