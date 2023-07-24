from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import CatalogueDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contract
from ubl.models.common.ubl_common_aggregate_components_2_1 import ContractDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import DestinationCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestForQuotationLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import SpecialTerms
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_request_for_quotation_2_1 import RequestForQuotation
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = RequestForQuotation(
    ublversion_id=UblversionId(
        value="2.0"
    ),
    customization_id=CustomizationId(
        value="urn:oasis:names:specification:ubl:xpath:RequestForQuotation-2.0:sbs-1.0-draft"
    ),
    profile_id=ProfileId(
        value="bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-request-for-quotation-draft"
    ),
    id=Id(
        value="G867B"
    ),
    copy_indicator=False,
    uuid=Uuid(
        value="8D076867-AE6D-439F-8281-5AAFC7F4E3B1"
    ),
    issue_date=XmlDate(2005, 6, 19),
    issue_time=XmlTime(11, 32, 26, 0, 0),
    note=[
        Note(
            value="sample"
        ),
    ],
    catalogue_document_reference=CatalogueDocumentReference(
        id=Id(
            value="2005-9A"
        ),
        issue_date=XmlDate(2005, 11, 3)
    ),
    originator_customer_party=OriginatorCustomerParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="The Terminus"
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
                    value="S Massiah"
                ),
                telephone=Telephone(
                    value="0127 98876545"
                ),
                telefax=Telefax(
                    value="0127 98876546"
                ),
                electronic_mail=ElectronicMail(
                    value="smassiah@the-email.co.uk"
                )
            )
        )
    ),
    seller_supplier_party=SellerSupplierParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value="CO001"
        ),
        party=Party(
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
        )
    ),
    delivery=[
        Delivery(
            delivery_address=DeliveryAddress(
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
            requested_delivery_period=RequestedDeliveryPeriod(
                start_date=XmlDate(2005, 6, 29),
                start_time=XmlTime(9, 30, 47, 0, 0),
                end_date=XmlDate(2005, 6, 29),
                end_time=XmlTime(9, 30, 47, 0, 0)
            )
        ),
    ],
    delivery_terms=[
        DeliveryTerms(
            special_terms=[
                SpecialTerms(
                    value="1% deduction for late delivery as per contract"
                ),
            ]
        ),
    ],
    destination_country=DestinationCountry(
        identification_code=IdentificationCode(
            value="GB"
        ),
        name=Name(
            value="Great Britain"
        )
    ),
    contract=[
        Contract(
            contract_document_reference=[
                ContractDocumentReference(
                    id=Id(
                        value="GHJ76849"
                    ),
                    issue_date=XmlDate(2002, 8, 13)
                ),
            ]
        ),
    ],
    request_for_quotation_line=[
        RequestForQuotationLine(
            id=Id(
                value="1"
            ),
            note=[
                Note(
                    value="sample"
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value="1"
                ),
                quantity=Quantity(
                    value=Decimal("100"),
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
                    )
                )
            )
        ),
    ]
)
