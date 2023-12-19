from typing import Union, List

from pydantic import BaseModel


class PaymentDetail(BaseModel):
    amount: Union[str, None] = None
    payment_term: Union[str, None] = None


class ContractSubject(BaseModel):
    estate_type: Union[str, None] = None
    permitted_use: Union[str, None] = None
    cadastral_number: Union[str, None] = None
    area: Union[str, None] = None
    address: Union[str, None] = None
    objects_on_land: List[str] = []
    estate_encumbrance: Union[str, None] = None
    object_transferred_before_contract: Union[str, None] = None


class LegalDocument(BaseModel):
    document_date: Union[str, None] = None
    sellers: Union[List, None] = None
    payment: PaymentDetail
    customer: Union[str, None] = None
    contract_subject: ContractSubject
