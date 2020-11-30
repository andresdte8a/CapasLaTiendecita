"""
Los recuerdos de ella test
"""

from clientes.principal import *
import requests

class TestTiendecita:

    def test_listarTodos(self):
        resp = requests.get("http://localhost:8080/clientes/get_all")
        assert 200 == resp.status_code()