# Registro de Notas Académicas

## Tecnología elegida
- **Lenguaje:** Python 3.13
- **Tests unitarios:** pytest
- **BDD:** pytest-bdd con Gherkin
- **CI/CD:** GitHub Actions

Se eligió Python porque permite implementar TDD y BDD de forma simple,
con herramientas maduras como pytest y pytest-bdd.

---

## 1.1 Particiones de equivalencia — Requerimiento 1

| Partición | Rango | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida baja | 0.0 – 2.9 | 1.5 | Nota registrada (reprueba) |
| Válida media | 3.0 – 4.0 | 3.5 | Nota registrada (aprueba) |
| Válida alta | 4.1 – 5.0 | 4.8 | Nota registrada (aprueba) |
| Inválida negativa | < 0.0 | -1.0 | Error: nota fuera de rango |
| Inválida alta | > 5.0 | 6.0 | Error: nota fuera de rango |

---

## 1.2 Análisis de valores límite — Requerimiento 1

| Valor | ¿Dentro del rango? | Resultado esperado |
|---|---|---|
| -0.1 | ❌ Fuera | Error: nota fuera de rango |
| 0.0 | ✅ Dentro | Nota registrada |
| 0.1 | ✅ Dentro | Nota registrada |
| 4.9 | ✅ Dentro | Nota registrada |
| 5.0 | ✅ Dentro | Nota registrada |
| 5.1 | ❌ Fuera | Error: nota fuera de rango |

---

## 1.3 Preguntas al Product Owner — Requerimiento 4

**Pregunta 1:** ¿Qué se considera "mismo semestre"? ¿Es un código como "2026-1" 
o es el año calendario?

**Justificación:** Si el semestre se identifica solo por año, dos períodos del 
mismo año serían el mismo semestre, lo que cambiaría completamente cuándo 
lanzar el error de duplicado.

**Pregunta 2:** Si un estudiante registra una nota incorrecta, ¿puede 
corregirla o el sistema debe bloquear cualquier modificación?

**Justificación:** Si se permite corrección, necesitamos diseñar casos de prueba 
para actualización. Si no se permite, el caso de "intentar registrar de nuevo" 
siempre debe lanzar error sin excepción.

---

## 2. Tabla de casos de prueba

| ID | Requerimiento | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP01 | R1 | Registrar nota válida baja | Estudiante sin notas | Materia: Matemáticas, Nota: 1.5 | Llamar registrar_nota() | Nota registrada exitosamente | Positivo |
| CP02 | R1 | Registrar nota válida alta | Estudiante sin notas | Materia: Física, Nota: 4.8 | Llamar registrar_nota() | Nota registrada exitosamente | Positivo |
| CP03 | R1 | Registrar nota inválida negativa | Estudiante sin notas | Materia: Química, Nota: -1.0 | Llamar registrar_nota() | ValueError: nota fuera de rango | Negativo |
| CP04 | R1 | Registrar nota inválida mayor a 5 | Estudiante sin notas | Materia: Historia, Nota: 6.0 | Llamar registrar_nota() | ValueError: nota fuera de rango | Negativo |
| CP05 | R1 | Registrar nota en límite inferior | Estudiante sin notas | Materia: Arte, Nota: 0.0 | Llamar registrar_nota() | Nota registrada exitosamente | Borde |
| CP06 | R1 | Registrar nota en límite superior | Estudiante sin notas | Materia: Arte, Nota: 5.0 | Llamar registrar_nota() | Nota registrada exitosamente | Borde |
| CP07 | R2 | Estudiante aprueba con nota exacta | Nota registrada | Nota: 3.0 | Llamar aprobar() | Retorna True | Borde |
| CP08 | R2 | Estudiante reprueba con nota límite | Nota registrada | Nota: 2.9 | Llamar aprobar() | Retorna False | Borde |
| CP09 | R2 | Estudiante aprueba con nota alta | Nota registrada | Nota: 5.0 | Llamar aprobar() | Retorna True | Positivo |
| CP10 | R3 | Promedio sin notas | Estudiante sin notas | Ninguno | Llamar calcular_promedio() | Retorna 0.0 | Negativo |
| CP11 | R3 | Promedio con una nota | Una nota registrada | Nota: 4.0 | Llamar calcular_promedio() | Retorna 4.0 | Positivo |
| CP12 | R3 | Promedio con varias notas | Dos notas registradas | Notas: 3.0 y 5.0 | Llamar calcular_promedio() | Retorna 4.0 | Positivo |
| CP13 | R4 | Duplicar nota misma materia mismo semestre | Nota ya registrada | Materia: Matemáticas, Semestre: 2026-1 | Llamar registrar_nota() dos veces | ValueError: nota duplicada | Negativo |
| CP14 | R4 | Misma materia semestre diferente | Nota ya registrada | Materia: Matemáticas, Semestre: 2026-2 | Llamar registrar_nota() | Nota registrada exitosamente | Positivo |
| CP15 | R4 | Materias diferentes mismo semestre | Nota ya registrada | Materias distintas, Semestre: 2026-1 | Llamar registrar_nota() dos veces | Ambas registradas exitosamente | Positivo |

---

## Reporte de cobertura
*(se completará después de ejecutar los tests)*

---

## Reflexión final
*(se completará al final de la actividad)*