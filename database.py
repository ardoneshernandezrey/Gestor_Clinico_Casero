import json
from models import Paciente  # Importamos tu modelo validado

class BaseDeDatos:
    def __init__(self, archivo: str = "pacientes.json"):
        self.archivo = archivo

    # 📖 1. CARGAR PACIENTES
    def cargar_pacientes(self) -> list[dict]:
        try:
            # El Context Manager 'with' garantiza el cierre del archivo
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []  # Devuelve una lista vacía si el archivo no existe aún

    # 💾 2. GUARDAR PACIENTES
    def guardar_pacientes(self, lista_pacientes: list[dict]) -> None:
        with open(self.archivo, "w", encoding="utf-8") as f:
            # indent=4 hace que el archivo JSON sea legible para humanos
            json.dump(lista_pacientes, f, indent=4, ensure_ascii=False)

    # ➕ 3. AÑADIR UN PACIENTE NUEVO Y ASIGNAR ID
    def añadir_paciente(self, paciente: Paciente) -> Paciente:
        todos = self.cargar_pacientes()
        
        # 🩺 Algoritmo de ID Autoincremental:
        # Si hay pacientes, el nuevo ID será el mayor + 1. Si no, empieza en 1.
        if todos:
            nuevo_id = max(p["id"] for p in todos) + 1
        else:
            nuevo_id = 1
            
        paciente.id = nuevo_id  # Asignamos el ID al objeto Pydantic
        
        # Convertimos el modelo Pydantic a diccionario plano para el JSON
        todos.append(paciente.model_dump())
        
        self.guardar_pacientes(todos)
        return paciente