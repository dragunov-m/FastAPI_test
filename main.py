import uvicorn
import xmltodict
from fastapi import FastAPI, HTTPException, Request

from app.models.schemas import LegalDocument
from app.services.extraction.normalizer import normalize_date, normalize_duration

app = FastAPI()


def content_type_validator(request, content):
    if request.headers.get('content-type') != content:
        raise HTTPException(status_code=400, detail='Invalid content type')


@app.post("/process-json/")
def process_json(tree: LegalDocument, request: Request):
    content_type_validator(request, 'application/json')

    data = tree

    if data.document_date:
        data.document_date = normalize_date(data.document_date)
    else:
        data.payment.payment_term = normalize_duration(data.payment.payment_term)
    return data.model_dump(exclude_none=True)


@app.post("/process-xml/")
async def process_xml(request: Request):
    content_type_validator(request, 'application/xml')

    body = await request.body()
    xml_data = body.decode('utf-8')
    data = xmltodict.parse(xml_data)
    # data['root']['document_date'] = normalize_date(data['root']['document_date'])
    data['root']['payment']['payment_term'] = normalize_duration(data['root']['payment']['payment_term'])
    inner_data = data['root']

    return inner_data


# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
