"""
Los recuerdos de ella test
"""

from clientes.principal import *
import json

class TestTiendecita:

    def test_listarTodos(self):
        expected_output = [{'id': 1, 'nombre': "James Adrian", 'apellido': "Cerati", 'direccion': "Cra 109 Bogota", 'telefono': "3124589635"}]
        clientes = Clientes()
        a, b = json.dumps(clientes.get_byId(1), sort_keys=True), json.dumps(expected_output, sort_keys=True)
        assert a == b