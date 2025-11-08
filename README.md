# 🤖 Chat con OpenAI usando Python Reflex

Aplicación web interactiva que implementa un chat con OpenAI utilizando Python y el framework [Reflex](https://reflex.dev/). Este proyecto demuestra cómo construir interfaces web modernas completamente en Python, sin necesidad de escribir JavaScript.

> **Nota:** Proyecto basado en el [tutorial de MoureDev](https://youtu.be/2u7JlBEavx0?si=blpgMew16INH4Jug) sobre Reflex.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## ✨ Características

- 💬 Chat interactivo con OpenAI GPT
- 🎨 Interfaz web moderna y responsive
- 🐍 100% Python (backend y frontend)
- 📝 Código completamente documentado
- ⚡ Compilación automática a JavaScript mediante Reflex
- 🔒 Variables de entorno para gestión segura de API keys

## 🛠 Tecnologías

- **[Python 3.12+](https://www.python.org/)** - Lenguaje de programación principal
- **[Reflex](https://reflex.dev/)** - Framework para crear aplicaciones web con Python
- **[OpenAI API](https://platform.openai.com/)** - Integración con modelos de lenguaje GPT
- **JavaScript** - Generado automáticamente por Reflex

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Una cuenta en [OpenAI](https://platform.openai.com/) con acceso a la API
- Git (para clonar el repositorio)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/alexisnlh/Python-Reflex.git
cd python-reflex
```

### 2. Crear entorno virtual (recomendado)

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no existe el archivo `requirements.txt`, instala las dependencias manualmente:

```bash
pip install reflex openai python-dotenv
```

## ⚙️ Configuración

### 1. Obtener API Key de OpenAI

1. Ve a [OpenAI Platform](https://platform.openai.com/)
2. Inicia sesión o crea una cuenta
3. Navega a **API Keys** en el menú
4. Crea una nueva clave secreta
5. **Importante:** Guarda esta clave, no podrás verla de nuevo

### 2. Configurar variables de entorno

Crea un archivo `.env` en el directorio `Python-Reflex/python-reflex`:

```bash
# Ruta: Python-Reflex/python-reflex/.env
API_KEY_REFLEX=tu-api-key-de-openai-aqui
```

**⚠️ IMPORTANTE:** Nunca subas el archivo `.env` a GitHub. Asegúrate de que esté en el `.gitignore`.

### 3. Verificar estructura de archivos

```
Python-Reflex/
├── .web/              # Archivos JS compilados (generado automáticamente)
├── assets/            # Archivos estáticos (imágenes, fuentes, etc.)
├── python-reflex/      # Lógica principal de la aplicación
│   ├── .env          # Variables de entorno
│   └── ...
├── README.md
└── requirements.txt
```

## 🎯 Uso

### Iniciar la aplicación

```bash
# Asegúrate de estar en el directorio raíz del proyecto
reflex run
```

La aplicación se iniciará en modo desarrollo y se abrirá automáticamente en tu navegador predeterminado (generalmente en `http://localhost:3000`).

### Modo producción

```bash
reflex run --env prod
```

### Comandos útiles de Reflex

```bash
# Inicializar Reflex (primera vez)
reflex init

# Limpiar archivos compilados
reflex clear

# Exportar la aplicación
reflex export
```

## 📁 Estructura del Proyecto

```
.
├── .web/                    # Archivos JavaScript compilados automáticamente
│   ├── public/             # Recursos públicos
│   └── utils/              # Utilidades de frontend
│
├── assets/                  # Archivos estáticos
│   ├── images/             # Imágenes
│   └── fonts/              # Fuentes personalizadas
│
├── python_reflex/           # Módulo principal de la aplicación
│   ├── .env               # Variables de entorno
│   ├── __init__.py        # Inicialización del módulo
│   ├── state.py          # Gestión del estado de la aplicación
│   ├── style.py         # Componentes reutilizables de UI
│   └── python_reflex.py        # Páginas de la aplicación
│
├── .gitignore             # Archivos ignorados por Git
├── README.md
├── requirements.txt       # Dependencias del proyecto
└── rxconfig.py           # Configuración de Reflex
```

### Descripción de componentes clave

- **`.web/`**: Directorio autogenerado por Reflex con el código JavaScript compilado. No debe modificarse manualmente.
- **`assets/`**: Almacena recursos estáticos como imágenes, iconos y fuentes.
- **`python_reflex/`**: Contiene toda la lógica de la aplicación en Python.
- **`.env`**: Archivo crítico para almacenar la API key de OpenAI de forma segura.

## 📝 Notas Adicionales

### Seguridad

- Nunca compartas tu API key de OpenAI públicamente
- El archivo `.env` debe estar en el `.gitignore`
- Revisa regularmente el uso de tu API key en el panel de OpenAI

### Costos

Ten en cuenta que el uso de la API de OpenAI tiene costos asociados. Revisa la [documentación de precios](https://openai.com/pricing) para más información.

### Troubleshooting

**Error: No module named 'reflex'**
```bash
pip install reflex
```

**Error: API key not found**
- Verifica que el archivo `.env` existe en `python_reflex/`
- Asegúrate de que la variable se llama exactamente `API_KEY_REFLEX`
- Reinicia la aplicación después de crear el archivo `.env`

**La aplicación no se abre en el navegador**
- Verifica que no haya otro proceso usando el puerto 3000
- Intenta acceder manualmente a `http://localhost:3000`

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Alexis NLH**

- GitHub: [@alexisnlh](https://github.com/alexisnlh)

## 🙏 Agradecimientos

- [MoureDev](https://github.com/mouredev) por el tutorial original
- [Reflex](https://reflex.dev/) por el excelente framework
- [OpenAI](https://openai.com/) por proporcionar la API

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub