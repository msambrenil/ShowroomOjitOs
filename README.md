# Showroom Natura OjitOs

Este proyecto es una implementación inicial de la web app solicitada.

## Tecnologías

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) con SQLite.
- **Frontend:** HTML, JavaScript y CSS utilizando Material Design.

## Estructura

- `backend/`: código del servidor FastAPI.
- `frontend/`: recursos estáticos.

Para ejecutar el servidor de desarrollo:

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Luego acceder a `frontend/index.html` para ver la interfaz básica.
