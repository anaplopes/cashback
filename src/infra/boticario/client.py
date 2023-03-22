import requests
from typing import Type
from src.settings import settings
from collections import namedtuple
from requests import Request, Response
from src.infra.boticario.exceptions import BoticarioException, BoticarioRequestException


class BoticarioClient:
    def __init__(self) -> None:
        self._url = settings.GB_API_URL
        self._header = {"Content-type": "application/json"}
        self._default_return = namedtuple(
            "BoticarioClient", "status_code request response"
        )

    def __send_http_request(self, req_prepared: Type[Request]) -> Type[Response]:
        session = requests.Session()
        return session.send(req_prepared)

    def get_cashback(self, cpf: str) -> any:
        request = Request(
            method="GET",
            url=f"{self._url}?cpf={cpf}",
            headers=self._header,
        )
        response = self.__send_http_request(req_prepared=request.prepare())

        if 400 <= response.status_code < 500:
            raise BoticarioRequestException(
                error=response.reason,
                message=response.text,
                status_code=response.status_code,
            )

        elif response.status_code >= 500:
            raise BoticarioException(
                message=response.text, status_code=response.status_code
            )

        else:
            return self._default_return(
                status_code=response.status_code,
                request=request,
                response=response.text,
            )
