# Abstract Entity Manager – Backend

Este es un backend abstracto construido con **FastAPI** y **Pydantic**, que permite definir entidades y operar sobre sus datos sin depender de una base de datos fija. Soporta validaciones dinámicas, autenticación JWT, y un patrón Repository extensible.

---

## 🚀 Funcionalidades

- Definición dinámica de entidades (`/define`)
- CRUD de datos para cualquier entidad
- Validación automática con Pydantic
- Autenticación JWT con roles (`admin`, `user`)
- Implementación por defecto en memoria
- Interfaz desacoplada del motor de base de datos

---

## 🛠️ Stack

- Python 3.11+
- FastAPI
- Pydantic
- PyJWT o python-jose
- Uvicorn
- SQLAlchemy (opcional para base real)

---

## 📦 Instalación

```bash
git clone https://github.com/tu-usuario/abstract-entity-manager
cd abstract-entity-manager
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints de autenticación
POST /register: username, password, role (admin/user)

POST /login: devuelve access_token

Acción	Método	Ruta	Autorización
Crear entidad	POST	/define	admin
Editar entidad	PUT	/define/{entity}	admin
Borrar entidad	DELETE	/define/{entity}	admin
Crear dato	POST	/{entity}	user/admin
Listar datos	GET	/{entity}	user/admin


TODO futuro
Validación avanzada con relaciones
Interfaz React
Exportación CSV/Excel
Webhooks / triggers

