# Showroom Natura OjitOs

Pequeña web app construida con FastAPI para la gestión de productos, clientes y ventas.


## Requisitos

- Python 3.10+
- [Visual Studio Code](https://code.visualstudio.com/) en Windows

Instala las dependencias dentro de un entorno virtual:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

Ejecuta la API en modo desarrollo desde la terminal integrada de VS Code:

```powershell
python -m uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000/`.

Los archivos estáticos (CSS, imágenes, JS) se cargan desde el directorio `static/`. Asegúrate de mantenerlo presente para evitar errores al iniciar la aplicación.
