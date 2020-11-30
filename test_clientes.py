"""
Los recuerdos de ella test
"""

from clientes.principal import *
import json

class TestTiendecita:

    def test_listarTodos(self):
        expected_output = {
                    'id': 1,
                    'nombre': "James Adrian",
                    'apellido': "Cerati",
                    'direccion': "Cra 109 Bogota",
                    'telefono': "3124589635"
                  }
        clientes = Clientes()
        assert json.loads(clientes.get_all()) == expected_output