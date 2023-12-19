from fastapi import Request, HTTPException

from app.services.extraction.normalizer import normalize_date, normalize_duration


def content_type_validator(request: Request, content: str):
    if request.headers.get('content-type') != content:
        raise HTTPException(status_code=400, detail='Invalid content type')


def process_data(data: dict):
    if 'document_date' in data:
        data['document_date'] = normalize_date(data['document_date'])
    elif 'payment' in data and 'payment_term' in data['payment']:
        data['payment']['payment_term'] = normalize_duration(data['payment']['payment_term'])
    return data
