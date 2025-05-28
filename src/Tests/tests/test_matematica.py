from src.Tests.app.matematica import Matematica
# from ...app.matematica import Matematica

def test_somar():
    assert Matematica.somar(1, 2) == 3