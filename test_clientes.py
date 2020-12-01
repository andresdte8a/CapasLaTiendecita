"""
Los recuerdos de ella test
"""
import requests
from clientes.principal import *

class TestTiendecita:

    def test_listarTodos(self):
        resp = requests.get("http://localhost:8080/clientes/get_all")
        assert resp.status_code == 200