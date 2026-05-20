# 🏥 Gestor Clínico Casero - Registro de Avances

Este repositorio contiene el desarrollo del sistema de gestión e hibridación profesional para el control de fichas clínicas en formato plano (JSON).

## 📊 Estado Actual del Proyecto (Cierre de Sesión)
- **Fase 1 (Modelo de Datos):** Completada y validada en `models.py`. Incluye validación de edad (no negativa) y formateo automático de nombres (`.title()` y `.strip()`).
- **Fase 2 (Persistencia JSON):** Completada en `database.py`. Clase `BaseDeDatos` con métodos de carga, guardado y asignación de ID autoincremental mediante Context Managers.
- **Fase 3 (Controlador FastAPI):** Código base escrito en `main.py` listo para inicializar rutas GET y POST.

## 🛠️ Protocolo de Reapertura (Para Mañana)
Al abrir la terminal de la M1 en esta carpeta, el orden de comandos para retomar el trabajo será:

1. **Sincronizar cambios por si acaso:**
   ```bash
   git pull
