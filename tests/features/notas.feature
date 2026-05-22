Feature: Registro de notas academicas
  Como estudiante de la Universidad Regional del Sur
  Quiero registrar mis notas por materia y semestre
  Para hacer seguimiento de mi rendimiento academico

  Background:
    Given un estudiante sin notas registradas

  @smoke
  Scenario: Estudiante aprueba con nota exacta de aprobacion
    When registra la nota 3.0 en "Matematicas" para el semestre "2026-1"
    Then el resultado de aprobar "Matematicas" en "2026-1" es verdadero

  @smoke
  Scenario: Estudiante reprueba con nota inferior al limite
    When registra la nota 2.9 en "Fisica" para el semestre "2026-1"
    Then el resultado de aprobar "Fisica" en "2026-1" es falso

  @critical
  Scenario: Estudiante aprueba con nota alta
    When registra la nota 5.0 en "Quimica" para el semestre "2026-1"
    Then el resultado de aprobar "Quimica" en "2026-1" es verdadero

  @critical
  Scenario: Calcular promedio sin notas registradas
    Then el promedio es 0.0

  @regression
  Scenario: Calcular promedio con varias notas
    When registra la nota 3.0 en "Matematicas" para el semestre "2026-1"
    And registra la nota 5.0 en "Fisica" para el semestre "2026-1"
    Then el promedio es 4.0

  @critical
  Scenario: Error al duplicar nota en misma materia y semestre
    When registra la nota 3.5 en "Matematicas" para el semestre "2026-1"
    Then registrar la nota 4.0 en "Matematicas" para "2026-1" lanza un error

  @regression
  Scenario Outline: Verificar aprobacion con diferentes notas
    When registra la nota <nota> en "<materia>" para el semestre "2026-1"
    Then el resultado de aprobar "<materia>" en "2026-1" es <resultado>

    Examples:
      | nota | materia     | resultado |
      | 5.0  | Matematicas | verdadero |
      | 3.0  | Fisica      | verdadero |
      | 2.9  | Quimica     | falso     |
      | 0.0  | Historia    | falso     |