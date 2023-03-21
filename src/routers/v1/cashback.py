from fastapi import APIRouter


cashback_router = APIRouter(prefix="/v1/cashback", tags=["cashback"])


@cashback_router.get("/{cpf}")
async def full_cashback(cpf: str):
    """
    Rota para retornar o acumulado de cashback:

    - **cpf**: cpf do revendedor(a)
    """
    # TODO request API externa
    # GET: https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf=12312312323
    return cpf
