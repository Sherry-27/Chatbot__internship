from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title='NexusChat Practice API',
    description='Learning FastAPI before building the real RAG API.',
    version='0.1.0',
)

class EchoRequest(BaseModel):
    message: str
    repeat: Optional[int] = 1

class EchoResponse(BaseModel):
    original: str
    echoed: str
    times: int

class MathRequest(BaseModel):
    a: float
    b: float
    operation: str

class MathResponse(BaseModel):
    result: float
    expression: str

@app.get('/health')
def health_check():
    return {'status': 'ok', 'service': 'NexusChat Practice API'}

@app.post('/echo', response_model=EchoResponse)
def echo(request: EchoRequest):
    if request.repeat < 1 or request.repeat > 10:
        raise HTTPException(status_code=400, detail='repeat must be between 1 and 10')
    echoed = ' '.join([request.message] * request.repeat)
    return EchoResponse(original=request.message, echoed=echoed, times=request.repeat)

@app.post('/calculate', response_model=MathResponse)
def calculate(request: MathRequest):
    op = request.operation.lower()
    if op == 'add':
        result = request.a + request.b
        expr = f'{request.a} + {request.b} = {result}'
    elif op == 'subtract':
        result = request.a - request.b
        expr = f'{request.a} - {request.b} = {result}'
    elif op == 'multiply':
        result = request.a * request.b
        expr = f'{request.a} * {request.b} = {result}'
    elif op == 'divide':
        if request.b == 0:
            raise HTTPException(status_code=400, detail='Cannot divide by zero')
        result = request.a / request.b
        expr = f'{request.a} / {request.b} = {result}'
    else:
        raise HTTPException(status_code=400, detail=f'Unknown operation: {op}.')
    return MathResponse(result=result, expression=expr)

if __name__ == '__main__':
    uvicorn.run('practice_api:app', host='0.0.0.0', port=8000, reload=True)