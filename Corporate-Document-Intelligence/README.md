# Corporate Document Intelligence System — Ejemplo 2 (Sección 4.0.2)

Este repositorio contiene el código correspondiente al **Ejemplo 2** del Trabajo de Fin de Grado *Exploración de sistemas multi-agente en IA generativa*:  
**Asistente de documentación interna (ingesta multiformato, RAG y citación verificable)**.

El sistema permite la ingestión de documentos en múltiples formatos (PDF, TXT, DOCX, etc.), la construcción de un índice semántico para recuperación aumentada de información (RAG) y la generación de respuestas con **citación verificable**.

Este ejemplo acompaña la **Sección 4.0.2** de la memoria y la figura que describe el flujo del asistente de documentación.

---

## 📂 Estructura del repositorio

- `src/corporate_document_intelligence_system/`
  - `main.py` → punto de entrada del sistema  
  - `crew.py` → definición de la crew y orquestación  
  - `config/agents.yaml` → configuración de agentes (roles, objetivos)  
  - `config/tasks.yaml` → configuración de tareas asignadas  
  - `tools/` → herramientas personalizadas usadas por los agentes  
- `knowledge/` → ejemplos de documentos auxiliares  
- `pyproject.toml` → metadatos del proyecto  
- `requirements.txt` → dependencias mínimas (para instalación con `pip`)  
- `.env.example` → plantilla de credenciales y claves API  
- `.gitignore` → exclusiones recomendadas (para no subir `.env`, `.venv`, cachés, etc.)

---

## ⚙️ Instalación y uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/matiasgarciar/Latest-AI-Development.git
   cd Latest-AI-Development/Corporate-Document-Intelligence
   ```

2. **(Opcional) Crear un entorno virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   ```
   Después edita el archivo `.env` y añade tus claves:
   ```ini
   OPENAI_API_KEY=sk-...
   SERPER_API_KEY=...
   ```

5. **Ejecutar el sistema:**
   ```bash
   python src/corporate_document_intelligence_system/main.py      --doc_path "data/manual_interno.pdf"      --query "Resumen de políticas de seguridad"
   ```

---

## 🔗 Relación con la memoria

Este ejemplo implementa el flujo descrito en la **Sección 4.0.2**, con:  
- **Ingesta multiformato** (PDF, TXT, DOCX, etc.).  
- **Construcción de un índice semántico** para recuperación aumentada (RAG).  
- **Citación verificable** en las respuestas generadas.  

---

✍️ Autor: **Matías García**  
📖 Trabajo Fin de Grado – *Exploración de sistemas multi-agente en IA generativa*
