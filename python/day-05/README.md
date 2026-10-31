# Day 5 — OOP, Dataclasses, Composition, and Pydantic

**Duration:** 4 hours | **Project:** Typed Task Management Model

## Objectives
- Understand classes, objects, attributes, and methods.
- Use instance, class, and static methods.
- Apply encapsulation and composition.
- Create dataclasses with safe mutable defaults.
- Validate incoming data with Pydantic v2.
- Test valid and invalid model data.

## Study plan
1. Hour 1: Classes, objects, constructors, methods.
2. Hour 2: Encapsulation, composition, dataclasses.
3. Hour 3: Pydantic models and validation.
4. Hour 4: Build, test, and complete assignments.

## Run from repository root
```bash
python -m pip install -r python/day-05/requirements.txt
python python/day-05/code/demo.py
python -m pytest python/day-05/tests -q
```

## Files
- [Notes](notes.md)
- [Assignments](assignments.md)
- [Answers](answers.md)
- `code/models.py` — Pydantic and dataclass models
- `code/demo.py` — runnable example
- `tests/test_models.py` — unit tests

## Completion checklist
- [ ] Explain class vs object.
- [ ] Write instance methods.
- [ ] Explain composition.
- [ ] Use dataclass default_factory.
- [ ] Validate external data with Pydantic.
- [ ] Run tests successfully.
