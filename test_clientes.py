"""
Los recuerdos de ella test
"""

from clientes.principal import *


class TestTiendecita:

    def test_listarTodos(self):
        clientes = Clientes()
        assert 4 == clientes.get_all()