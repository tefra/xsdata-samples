from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import EffectivePeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import ExceptionCriteriaLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import ForecastExceptionCriterionLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import StandardItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import SupplyItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import ValidityPeriod
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CollaborationPriorityCode
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import ComparisonDataSourceCode
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import DataSourceCode
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExceptionStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import ForecastPurposeCode
from ubl.models.common.ubl_common_basic_components_2_1 import ForecastTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PerformanceMetricTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import SupplyChainActivityTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import ThresholdQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import ThresholdValueComparisonCode
from ubl.models.common.ubl_common_basic_components_2_1 import TimeDeltaDaysQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_exception_criteria_2_1 import ExceptionCriteria
from xsdata.models.datatype import XmlDate


obj = ExceptionCriteria(
    ublversion_id=UblversionId(
        value='2.1'
    ),
    customization_id=CustomizationId(
        value='urn:oasis:names:specification:ubl:xpath:ExceptionCriteria-2.1:1.0-draft'
    ),
    profile_id=ProfileId(
        value='bpid:urn:oasis:names:draft:bpss:ubl-2-cpfr-exception-criteria-draft'
    ),
    id=Id(
        value='EC758494'
    ),
    copy_indicator=False,
    uuid=Uuid(
        value='349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4'
    ),
    issue_date=XmlDate(2009, 12, 25),
    note=[
        Note(
            value='sample'
        ),
    ],
    validity_period=ValidityPeriod(
        start_date=XmlDate(2010, 3, 28),
        end_date=XmlDate(2010, 8, 29)
    ),
    sender_party=SenderParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value='6903148000007'
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value='Consortial'
                )
            ),
        ],
        postal_address=PostalAddress(
            street_name=StreetName(
                value='Busy Street'
            ),
            building_name=BuildingName(
                value='Thereabouts'
            ),
            building_number=BuildingNumber(
                value='56A'
            ),
            city_name=CityName(
                value='Farthing'
            ),
            postal_zone=PostalZone(
                value='AA99 1BB'
            ),
            country_subentity=CountrySubentity(
                value='Heremouthshire'
            ),
            address_line=[
                AddressLine(
                    line=Line(
                        value='The Roundabout'
                    )
                ),
            ],
            country=Country(
                identification_code=IdentificationCode(
                    value='GB'
                )
            )
        ),
        party_tax_scheme=[
            PartyTaxScheme(
                registration_name=RegistrationName(
                    value='Farthing Purchasing Consortium'
                ),
                company_id=CompanyId(
                    value='175 269 2355'
                ),
                exemption_reason=[
                    ExemptionReason(
                        value='N/A'
                    ),
                ],
                tax_scheme=TaxScheme(
                    id=Id(
                        value='VAT'
                    ),
                    tax_type_code=TaxTypeCode(
                        value='VAT'
                    )
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value='Mrs Bouquet'
            ),
            telephone=Telephone(
                value='0158 1233714'
            ),
            telefax=Telefax(
                value='0158 1233856'
            ),
            electronic_mail=ElectronicMail(
                value='bouquet@fpconsortial.co.uk'
            )
        )
    ),
    receiver_party=ReceiverParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value='2203148000007'
                )
            ),
        ],
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
        party_tax_scheme=[
            PartyTaxScheme(
                registration_name=RegistrationName(
                    value='Bridgtow District Council'
                ),
                company_id=CompanyId(
                    value='12356478'
                ),
                exemption_reason=[
                    ExemptionReason(
                        value='Local Authority'
                    ),
                ],
                tax_scheme=TaxScheme(
                    id=Id(
                        value='UK VAT'
                    ),
                    tax_type_code=TaxTypeCode(
                        value='VAT'
                    )
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value='Mr Fred Churchill'
            ),
            telephone=Telephone(
                value='0127 2653214'
            ),
            telefax=Telefax(
                value='0127 2653215'
            ),
            electronic_mail=ElectronicMail(
                value='fred@iytcorporation.gov.uk'
            )
        )
    ),
    buyer_customer_party=BuyerCustomerParty(
        party=Party(
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='2203148000007'
                    )
                ),
            ]
        )
    ),
    seller_supplier_party=SellerSupplierParty(
        party=Party(
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='6903148000007'
                    )
                ),
            ]
        )
    ),
    exception_criteria_line=[
        ExceptionCriteriaLine(
            id=Id(
                value='exceptionCriteriaLineID'
            ),
            threshold_value_comparison_code=ThresholdValueComparisonCode(
                value='EXCEEDS_EXCEPTION_VALUE'
            ),
            threshold_quantity=ThresholdQuantity(
                value=Decimal('120000'),
                unit_code='KGM'
            ),
            exception_status_code=ExceptionStatusCode(
                value='NEW'
            ),
            collaboration_priority_code=CollaborationPriorityCode(
                value='HIGH'
            ),
            supply_chain_activity_type_code=SupplyChainActivityTypeCode(
                value='SALES'
            ),
            effective_period=EffectivePeriod(
                start_date=XmlDate(2010, 3, 28),
                end_date=XmlDate(2010, 8, 29)
            ),
            supply_item=[
                SupplyItem(
                    description=[
                        Description(
                            value='Acme beeswax'
                        ),
                    ],
                    name=Name(
                        value='beeswax'
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
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value='00123450000584'
                        )
                    )
                ),
            ]
        ),
        ExceptionCriteriaLine(
            id=Id(
                value='exceptionCriteriaLineID'
            ),
            threshold_value_comparison_code=ThresholdValueComparisonCode(
                value='EXCEEDS_EXCEPTION_VALUE'
            ),
            threshold_quantity=ThresholdQuantity(
                value=Decimal('120000'),
                unit_code='KGM'
            ),
            exception_status_code=ExceptionStatusCode(
                value='NEW'
            ),
            collaboration_priority_code=CollaborationPriorityCode(
                value='HIGH'
            ),
            performance_metric_type_code=PerformanceMetricTypeCode(
                value='SUPPLY'
            ),
            effective_period=EffectivePeriod(
                start_date=XmlDate(2010, 3, 28),
                end_date=XmlDate(2010, 5, 29)
            ),
            supply_item=[
                SupplyItem(
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value='00123450000581'
                        )
                    )
                ),
            ]
        ),
        ExceptionCriteriaLine(
            id=Id(
                value='exceptionCriteriaLineID'
            ),
            threshold_value_comparison_code=ThresholdValueComparisonCode(
                value='EXCEEDS_EXCEPTION_VALUE'
            ),
            threshold_quantity=ThresholdQuantity(
                value=Decimal('120000'),
                unit_code='KGM'
            ),
            exception_status_code=ExceptionStatusCode(
                value='NEW'
            ),
            collaboration_priority_code=CollaborationPriorityCode(
                value='HIGH'
            ),
            effective_period=EffectivePeriod(
                start_date=XmlDate(2010, 4, 28),
                end_date=XmlDate(2010, 6, 29)
            ),
            supply_item=[
                SupplyItem(
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value='00123450000582'
                        )
                    )
                ),
            ],
            forecast_exception_criterion_line=ForecastExceptionCriterionLine(
                forecast_purpose_code=ForecastPurposeCode(
                    value='SALES_FORECAST'
                ),
                forecast_type_code=ForecastTypeCode(
                    value='BASE'
                ),
                comparison_data_source_code=ComparisonDataSourceCode(
                    value='SELLER'
                ),
                data_source_code=DataSourceCode(
                    value='BUYER'
                ),
                time_delta_days_quantity=TimeDeltaDaysQuantity(
                    value=Decimal('20')
                )
            )
        ),
        ExceptionCriteriaLine(
            id=Id(
                value='exceptionCriteriaLineID'
            ),
            threshold_value_comparison_code=ThresholdValueComparisonCode(
                value='EXCEEDS_EXCEPTION_VALUE'
            ),
            threshold_quantity=ThresholdQuantity(
                value=Decimal('120000'),
                unit_code='KGM'
            ),
            exception_status_code=ExceptionStatusCode(
                value='NEW'
            ),
            collaboration_priority_code=CollaborationPriorityCode(
                value='HIGH'
            ),
            effective_period=EffectivePeriod(
                start_date=XmlDate(2010, 4, 28),
                end_date=XmlDate(2010, 6, 29)
            ),
            supply_item=[
                SupplyItem(
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value='00123450000580'
                        )
                    )
                ),
            ],
            forecast_exception_criterion_line=ForecastExceptionCriterionLine(
                forecast_purpose_code=ForecastPurposeCode(
                    value='SALES_FORECAST'
                ),
                forecast_type_code=ForecastTypeCode(
                    value='BASE'
                ),
                data_source_code=DataSourceCode(
                    value='BUYER'
                ),
                time_delta_days_quantity=TimeDeltaDaysQuantity(
                    value=Decimal('20')
                )
            )
        ),
    ]
)
