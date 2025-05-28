# test numero_par
from src.Tests.app.numero_par import numero_par

def test_numero_par_verdadeiro():
    assert numero_par(4) == True
def test_numero_par_falso():
    assert numero_par(7) == False