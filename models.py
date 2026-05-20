from pydantic import BaseModel, field_validator

class Paciente(BaseModel):
    id: int | None = None   # ID Opcional (se genera al guardar)
    nombre: str
    edad: int 
    condicion: str          # Ej. "Gripe", "Chequeo", "Hipertension"

    @field_validator('edad')
    @classmethod
    def validar_edad(cls, v: int) -> int:
        if v < 0:
            raise ValueError('La edad no puede ser un numero negativo')
        return v
    
    @field_validator('nombre')
    @classmethod
    def capitalizar_nombre(cls, v: str) -> str:
        # .title() transforma "ardon hernández" en "Ardon Hernández"
        # .strip() elimina espacios en blanco innecesarios al inicio o final
        nombre_limpio = v.strip().title()
        if not nombre_limpio:
            raise ValueError('El nombre no puede estar vacío')
        return nombre_limpio    
