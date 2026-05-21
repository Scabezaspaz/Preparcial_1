import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from registro_notas import RegistroNotas

@pytest.fixture
def registro():
    return RegistroNotas()

# ── R1: REGISTRAR NOTA ─────────────────────────────
def test_registrar_nota_valida(registro):
    registro.registrar_nota("Matematicas", 3.5, "2026-1")
    assert len(registro.notas) == 1

def test_registrar_nota_limite_inferior(registro):
    registro.registrar_nota("Matematicas", 0.0, "2026-1")
    assert len(registro.notas) == 1

def test_registrar_nota_limite_superior(registro):
    registro.registrar_nota("Matematicas", 5.0, "2026-1")
    assert len(registro.notas) == 1

def test_registrar_nota_invalida_negativa(registro):
    with pytest.raises(ValueError):
        registro.registrar_nota("Matematicas", -1.0, "2026-1")

def test_registrar_nota_invalida_mayor_cinco(registro):
    with pytest.raises(ValueError):
        registro.registrar_nota("Matematicas", 6.0, "2026-1")

# ── R2: APROBAR O REPROBAR ─────────────────────────
def test_aprueba_con_nota_exacta(registro):
    registro.registrar_nota("Matematicas", 3.0, "2026-1")
    assert registro.aprobar("Matematicas", "2026-1") == True

def test_reprueba_con_nota_limite(registro):
    registro.registrar_nota("Matematicas", 2.9, "2026-1")
    assert registro.aprobar("Matematicas", "2026-1") == False

def test_aprueba_con_nota_alta(registro):
    registro.registrar_nota("Matematicas", 5.0, "2026-1")
    assert registro.aprobar("Matematicas", "2026-1") == True

# ── R3: CALCULAR PROMEDIO ──────────────────────────
def test_promedio_sin_notas(registro):
    assert registro.calcular_promedio() == 0.0

def test_promedio_una_nota(registro):
    registro.registrar_nota("Matematicas", 4.0, "2026-1")
    assert registro.calcular_promedio() == 4.0

def test_promedio_varias_notas(registro):
    registro.registrar_nota("Matematicas", 3.0, "2026-1")
    registro.registrar_nota("Fisica", 5.0, "2026-1")
    assert registro.calcular_promedio() == 4.0

# ── R4: NO DUPLICAR NOTAS ─────────────────────────
def test_duplicar_nota_misma_materia_mismo_semestre(registro):
    registro.registrar_nota("Matematicas", 3.5, "2026-1")
    with pytest.raises(ValueError):
        registro.registrar_nota("Matematicas", 4.0, "2026-1")

def test_misma_materia_semestre_diferente(registro):
    registro.registrar_nota("Matematicas", 3.5, "2026-1")
    registro.registrar_nota("Matematicas", 4.0, "2026-2")
    assert len(registro.notas) == 2

def test_materias_diferentes_mismo_semestre(registro):
    registro.registrar_nota("Matematicas", 3.5, "2026-1")
    registro.registrar_nota("Fisica", 4.0, "2026-1")
    assert len(registro.notas) == 2