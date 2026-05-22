import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from pytest_bdd import given, when, then, parsers, scenarios
from registro_notas import RegistroNotas

scenarios('../notas.feature')

@given("un estudiante sin notas registradas")
def registro():
    return RegistroNotas()

@when(parsers.parse("registra la nota {nota:f} en \"{materia}\" para el semestre \"{semestre}\""))
def registrar_nota(registro, nota, materia, semestre):
    registro.registrar_nota(materia, nota, semestre)

@then(parsers.parse("el resultado de aprobar \"{materia}\" en \"{semestre}\" es verdadero"))
def verificar_aprueba(registro, materia, semestre):
    assert registro.aprobar(materia, semestre) == True

@then(parsers.parse("el resultado de aprobar \"{materia}\" en \"{semestre}\" es falso"))
def verificar_reprueba(registro, materia, semestre):
    assert registro.aprobar(materia, semestre) == False

@then(parsers.parse("el promedio es {promedio:f}"))
def verificar_promedio(registro, promedio):
    assert registro.calcular_promedio() == promedio

@then(parsers.parse("registrar la nota {nota:f} en \"{materia}\" para \"{semestre}\" lanza un error"))
def verificar_error_duplicado(registro, nota, materia, semestre):
    with pytest.raises(ValueError):
        registro.registrar_nota(materia, nota, semestre)