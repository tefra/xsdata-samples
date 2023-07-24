from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import ForecastLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import ForecastPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SalesItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import StandardItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import ForecastPurposeCode
from ubl.models.common.ubl_common_basic_components_2_1 import ForecastTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_forecast_2_1 import Forecast
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Forecast(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    profile_id=ProfileId(
        value="bpid:urn:oasis:names:draft:bpss:ubl-2-1-cpfr-forecast-draft"
    ),
    id=Id(
        value="OF758494"
    ),
    copy_indicator=False,
    uuid=Uuid(
        value="349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4"
    ),
    issue_date=XmlDate(2010, 1, 1),
    issue_time=XmlTime(12, 0, 1, 0),
    note=[
        Note(
            value="sample"
        ),
    ],
    based_on_consensus_indicator=True,
    forecast_purpose_code=ForecastPurposeCode(
        value="ORDER_FORECAST"
    ),
    forecast_period=ForecastPeriod(
        start_date=XmlDate(2010, 2, 1),
        end_date=XmlDate(2010, 5, 26)
    ),
    sender_party=SenderParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="6903148000007"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="Consortial"
                )
            ),
        ],
        postal_address=PostalAddress(
            street_name=StreetName(
                value="Busy Street"
            ),
            building_name=BuildingName(
                value="Thereabouts"
            ),
            building_number=BuildingNumber(
                value="56A"
            ),
            city_name=CityName(
                value="Farthing"
            ),
            postal_zone=PostalZone(
                value="AA99 1BB"
            ),
            country_subentity=CountrySubentity(
                value="Heremouthshire"
            ),
            address_line=[
                AddressLine(
                    line=Line(
                        value="The Roundabout"
                    )
                ),
            ],
            country=Country(
                identification_code=IdentificationCode(
                    value="GB"
                )
            )
        ),
        party_tax_scheme=[
            PartyTaxScheme(
                registration_name=RegistrationName(
                    value="Farthing Purchasing Consortium"
                ),
                company_id=CompanyId(
                    value="175 269 2355"
                ),
                exemption_reason=[
                    ExemptionReason(
                        value="N/A"
                    ),
                ],
                tax_scheme=TaxScheme(
                    id=Id(
                        value="VAT"
                    ),
                    tax_type_code=TaxTypeCode(
                        value="VAT"
                    )
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="Mrs Bouquet"
            ),
            telephone=Telephone(
                value="0158 1233714"
            ),
            telefax=Telefax(
                value="0158 1233856"
            ),
            electronic_mail=ElectronicMail(
                value="bouquet@fpconsortial.co.uk"
            )
        )
    ),
    receiver_party=ReceiverParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="2203148000007"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="IYT Corporation"
                )
            ),
        ],
        postal_address=PostalAddress(
            street_name=StreetName(
                value="Avon Way"
            ),
            building_name=BuildingName(
                value="Thereabouts"
            ),
            building_number=BuildingNumber(
                value="56A"
            ),
            city_name=CityName(
                value="Bridgtow"
            ),
            postal_zone=PostalZone(
                value="ZZ99 1ZZ"
            ),
            country_subentity=CountrySubentity(
                value="Avon"
            ),
            address_line=[
                AddressLine(
                    line=Line(
                        value="3rd Floor, Room 5"
                    )
                ),
            ],
            country=Country(
                identification_code=IdentificationCode(
                    value="GB"
                )
            )
        ),
        party_tax_scheme=[
            PartyTaxScheme(
                registration_name=RegistrationName(
                    value="Bridgtow District Council"
                ),
                company_id=CompanyId(
                    value="12356478"
                ),
                exemption_reason=[
                    ExemptionReason(
                        value="Local Authority"
                    ),
                ],
                tax_scheme=TaxScheme(
                    id=Id(
                        value="UK VAT"
                    ),
                    tax_type_code=TaxTypeCode(
                        value="VAT"
                    )
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="Mr Fred Churchill"
            ),
            telephone=Telephone(
                value="0127 2653214"
            ),
            telefax=Telefax(
                value="0127 2653215"
            ),
            electronic_mail=ElectronicMail(
                value="fred@iytcorporation.gov.uk"
            )
        )
    ),
    buyer_customer_party=BuyerCustomerParty(
        party=Party(
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value="0012345000359"
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
                        value="0012345000058"
                    )
                ),
            ]
        )
    ),
    forecast_line=[
        ForecastLine(
            id=Id(
                value="forecastLineID"
            ),
            forecast_type_code=ForecastTypeCode(
                value="TOTAL"
            ),
            forecast_period=ForecastPeriod(
                start_date=XmlDate(2010, 2, 1),
                end_date=XmlDate(2010, 5, 26)
            ),
            sales_item=SalesItem(
                quantity=Quantity(
                    value=Decimal("20"),
                    unit_code="KGM"
                ),
                item=Item(
                    description=[
                        Description(
                            value="Acme beeswax"
                        ),
                    ],
                    name=Name(
                        value="beeswax"
                    ),
                    buyers_item_identification=BuyersItemIdentification(
                        id=Id(
                            value="6578489"
                        )
                    ),
                    sellers_item_identification=SellersItemIdentification(
                        id=Id(
                            value="17589683"
                        )
                    ),
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value="00123450000584"
                        )
                    )
                )
            )
        ),
    ]
)
