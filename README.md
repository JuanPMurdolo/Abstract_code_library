# 🧩 Abstract Entity Manager – Backend

This is an abstract backend built with **FastAPI** and **Pydantic**, designed to define entities and operate on their data without relying on a fixed database. It supports dynamic validation, JWT authentication, and an extensible Repository pattern.

---

## 🚀 Features

- 🔧 Dynamic entity definition (`/define`)
- 📋 CRUD operations for any entity
- ✅ Automatic validation with Pydantic
- 🔐 JWT authentication with roles (`admin`, `user`)
- 🧠 In-memory implementation by default
- 🧱 Database-agnostic architecture

---

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- PyJWT or python-jose
- Uvicorn
- SQLAlchemy *(optional for real databases)*

---

## 📦 Installation

```bash
git clone https://github.com/JuanPMurdolo/Abstract_code_library
cd Abstract_code_library/app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
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

