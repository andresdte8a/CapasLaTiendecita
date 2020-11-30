"""
Los recuerdos de ella test
"""

from clientes import *


class TestTiendecita:

    def test_listarTodos(self):
        clientes = clientes()
        assert 4 == clientes.get_all()