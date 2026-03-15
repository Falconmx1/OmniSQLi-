# 🔥 OmniSQLi - La navaja suiza definitiva para SQL Injection

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Falconmx1/OmniSQLi-/pulls)

## 🚀 ¿Qué es OmniSQLi?

OmniSQLi es una suite integral de pruebas de penetración especializada en SQL Injection que **supera las capacidades de SQLmap** mediante la integración de múltiples herramientas de élite y potenciándolas con Inteligencia Artificial.

### ⚡ Características que rompen la madre:

- **🤖 Sistema Multi-Agente con IA**: 5 agentes especializados (Reconocimiento, Generación de Payloads, Explotación, Reportes, Coordinación) usando LangChain
- **🎯 VEXSQLI.py**: Generación de payloads ofuscados con NLP para evadir WAFs como Cloudflare, Akamai, F5
- **⚡ Ghauri**: Inyección optimizada en peticiones complejas (JSON/XML) y autenticación avanzada
- **🧠 Hakuin**: Extracción de datos en Blind SQLi usando modelos de lenguaje (hasta 10x más rápido)
- **🍃 NoSQLMap**: Explotación de bases NoSQL (MongoDB, Cassandra, Redis, CouchDB)
- **🖥️ jSQL Injection**: Interfaz gráfica para visualización de datos y gestión multi-objetivo
- **💀 SQLninja**: Post-explotación especializada en MSSQL (cmd shell, xp_cmdshell, pivoting)
- **🔍 Detección inteligente de WAFs**: Identifica y adapta estrategias para más de 50 WAFs
- **📊 Reportes automáticos**: Genera informes detallados en HTML, PDF y Markdown

## 🏗️ Arquitectura
OmniSQLi-/
├── agents/ # Agentes de IA (LangChain)
│ ├── recon/ # Reconocimiento inteligente
│ ├── payload_gen/ # Generación de payloads con NLP
│ ├── exploit/ # Ejecución de exploits
│ ├── report/ # Generación de reportes
│ └── coordinator/ # Orquestador de agentes
├── modules/ # Módulos integrados
│ ├── vexsqli/ # NLP payload obfuscation
│ ├── ghauri/ # Ghauri core
│ ├── hakuin/ # Blind SQLi optimization
│ ├── multiagent/ # Multi-agent system
│ ├── nosqlmap/ # NoSQL exploitation
│ ├── jsql/ # GUI interface
│ └── sqlninja/ # MSSQL post-exploitation
├── core/ # Motor principal
│ ├── detection/ # Detección de vulnerabilidades
│ ├── injection/ # Motor de inyección
│ ├── extraction/ # Extracción de datos
│ └── bypass/ # Técnicas de bypass
├── utils/ # Utilidades
│ ├── waf_detection/ # Detecta y clasifica WAFs
│ ├── db_handlers/ # Manejadores específicos por DB
│ ├── network/ # Peticiones HTTP/HTTPS
│ └── encoding/ # Codificaciones y ofuscación
├── payloads/ # Base de datos de payloads
├── reports/ # Reportes generados
├── tests/ # Pruebas unitarias
└── docs/ # Documentación


## 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Falconmx1/OmniSQLi-.git
cd OmniSQLi-

# Instalar dependencias
pip install -r requirements.txt

# Instalar módulos adicionales (opcional)
python setup.py install

# Modo automático (todo incluido)
python omnisqli.py -u "http://target.com/page.php?id=1"

# Con agentes de IA específicos
python omnisqli.py -u "http://target.com/page.php?id=1" --agents recon,payload_gen,exploit

# Extracción optimizada para Blind SQLi
python omnisqli.py -u "http://target.com/page.php?id=1" --blind --optimize hakuin

# Bypass de WAF con NLP
python omnisqli.py -u "http://target.com/page.php?id=1" --waf-bypass --nlp

# Interfaz gráfica
python omnisqli.py --gui

# Reporte detallado
python omnisqli.py -u "http://target.com/page.php?id=1" --report html

# Escaneo masivo con múltiples agentes
python omnisqli.py --list targets.txt --threads 10 --ai-coordination

# Post-explotación en MSSQL
python omnisqli.py -u "http://target.com/page.php?id=1" --dbms mssql --post-exploit --get-shell

# NoSQL injection
python omnisqli.py -u "http://target.com/api/users" --nosql --db mongodb
