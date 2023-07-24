from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import EventLineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import EventTactic
from ubl.models.common.ubl_common_aggregate_components_2_1 import EventTacticEnumeration
from ubl.models.common.ubl_common_aggregate_components_2_1 import ParticipatingLocationsLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import Period
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import PromotionalEvent
from ubl.models.common.ubl_common_aggregate_components_2_1 import PromotionalEventLineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import PromotionalSpecification
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import RetailPlannedImpact
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import StandardItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import SupplyItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import DisplayTacticTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import ForecastPurposeCode
from ubl.models.common.ubl_common_basic_components_2_1 import ForecastTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineNumberNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import PromotionalEventTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import RetailEventName
from ubl.models.common.ubl_common_basic_components_2_1 import RetailEventStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import SpecificationId
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_retail_event_2_1 import RetailEvent
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = RetailEvent(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    customization_id=CustomizationId(
        value="UBL-TR"
    ),
    profile_id=ProfileId(
        value="bpid:urn:oasis:names:draft:bpss:ubl-2-1-cpfr-retail-event"
    ),
    id=Id(
        value="RE758494"
    ),
    copy_indicator=False,
    uuid=Uuid(
        value="349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4"
    ),
    issue_date=XmlDate(2009, 12, 1),
    issue_time=XmlTime(12, 0, 1, 0),
    note=[
        Note(
            value="sample"
        ),
    ],
    retail_event_name=RetailEventName(
        value="ACME NEW BRANCH OPENNING"
    ),
    retail_event_status_code=RetailEventStatusCode(
        value="PLANNED"
    ),
    description=[
        Description(
            value="ACME NEW BRANCH will be opened in Brusells on May 12, 2010"
        ),
    ],
    period=Period(
        start_date=XmlDate(2010, 5, 12),
        end_date=XmlDate(2010, 6, 12)
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
    promotional_event=PromotionalEvent(
        promotional_event_type_code=PromotionalEventTypeCode(
            value="STORE_OPENING"
        ),
        submission_date=XmlDate(2009, 12, 1),
        latest_proposal_acceptance_date=XmlDate(2010, 1, 6),
        promotional_specification=[
            PromotionalSpecification(
                specification_id=SpecificationId(
                    value="ACME_STROP_0023823"
                ),
                promotional_event_line_item=[
                    PromotionalEventLineItem(
                        amount=Amount(
                            value=Decimal("100.0"),
                            currency_id="GBP"
                        ),
                        event_line_item=EventLineItem(
                            line_number_numeric=LineNumberNumeric(
                                value=Decimal("1")
                            ),
                            participating_locations_location=ParticipatingLocationsLocation(
                                id=Id(
                                    value="ACME_BR_BE_0023"
                                )
                            ),
                            retail_planned_impact=[
                                RetailPlannedImpact(
                                    amount=Amount(
                                        value=Decimal("0.0"),
                                        currency_id="GBP"
                                    ),
                                    forecast_purpose_code=ForecastPurposeCode(
                                        value="SALES_FORECAST"
                                    ),
                                    forecast_type_code=ForecastTypeCode(
                                        value="PROMOTIONAL"
                                    ),
                                    period=Period(
                                        start_date=XmlDate(2010, 5, 12),
                                        end_date=XmlDate(2010, 6, 12)
                                    )
                                ),
                            ],
                            supply_item=SupplyItem(
                                description=[
                                    Description(
                                        value="Acme knitwear scarf"
                                    ),
                                ],
                                name=Name(
                                    value="scarf"
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
                ],
                event_tactic=[
                    EventTactic(
                        event_tactic_enumeration=EventTacticEnumeration(
                            display_tactic_type_code=DisplayTacticTypeCode(
                                value="DISPLAY_GENERAL"
                            )
                        ),
                        period=Period(
                            start_date=XmlDate(2010, 4, 1),
                            end_date=XmlDate(2010, 6, 12)
                        )
                    ),
                ]
            ),
        ]
    )
)
