import uvicorn
import xmltodict
from fastapi import FastAPI, Request

from app.models.schemas import LegalDocument
from app.utils import content_type_validator, process_data

app = FastAPI()


@app.post("/process-json/")
def process_json(tree: LegalDocument, request: Request):
    content_type_validator(request, 'application/json')
    return process_data(tree.model_dump(exclude_none=True))


@app.post("/process-xml/")
async def process_xml(request: Request):
    content_type_validator(request, 'application/xml')
    body = await request.body()
    xml_data = body.decode('utf-8')
    data = xmltodict.parse(xml_data)
    return process_data(data.get('root', {}))


# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
