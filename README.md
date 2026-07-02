# CRUD de Empleados y Cargos en Django (VBF y VBC)

Proyecto de la **Guía 3**: desarrollo de un CRUD en Django implementado de **dos formas** para
compararlas: con **Vistas Basadas en Funciones (VBF)** y con **Vistas Basadas en Clases (VBC)**.

El dominio del proyecto es la gestión de **Empleados** y **Cargos** de una empresa.

- **App desplegada:** https://djangocrud-yxul.onrender.com
- **Repositorio:** https://github.com/dmero10/django-crud-empleados

---

## 1. ¿Qué hace el proyecto?

Permite administrar dos entidades relacionadas:

- **Cargo (`Position`)**: el puesto de trabajo (ej. Gerente, Cajero, Vendedor).
- **Empleado (`Employee`)**: la persona, que tiene asignado **un** cargo.

Sobre ambas entidades se pueden hacer las 4 operaciones de un CRUD:
**C**rear, **L**eer (listar y ver detalle), **A**ctualizar y **B**orrar.

El acceso requiere iniciar sesión (registro / login de usuarios).

---

## 2. Estructura del proyecto

```
django-crud/
├── djangocrud/          # Configuración del proyecto (settings, urls principales)
├── tasks/               # App base tomada del video (login/registro y navbar compartido)
├── empleados_fbv/       # 1ª ETAPA: CRUD con Vistas Basadas en Funciones (VBF)
├── empleados_cbv/       # 2ª ETAPA: CRUD con Vistas Basadas en Clases (VBC)
├── requirements.txt     # Dependencias del proyecto
├── build.sh             # Script de construcción para el despliegue en Render
├── render.yaml          # Configuración del servicio en Render
└── manage.py            # Utilidad de administración de Django
```

**Decisión de diseño:** los modelos y formularios se definen **una sola vez** en `empleados_fbv`.
La app `empleados_cbv` los **reutiliza** (los importa), de modo que ambas versiones comparten los
mismos modelos y la misma base de datos. Así se ve claramente que **lo único que cambia entre las
dos etapas son las vistas** (funciones vs clases), que es el objetivo de la guía.

---

## 3. Modelos (`empleados_fbv/models.py`)

### Cargo (`Position`)
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | `CharField(100)` | Nombre del cargo |
| `description` | `CharField(200)`, opcional | Descripción del cargo |

### Empleado (`Employee`)
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `first_name` | `CharField(100)` | Nombres |
| `last_name` | `CharField(100)` | Apellidos |
| `email` | `EmailField` | Correo |
| `salary` | `DecimalField(10,2)` | Sueldo |
| `hire_date` | `DateField` | Fecha de ingreso |
| `position` | `ForeignKey(Position)` | Cargo asignado |

**Relación:** un `Cargo` puede tener **muchos** empleados, y cada `Empleado` pertenece a **un solo**
cargo. Esto se logra con el `ForeignKey` de `Employee` hacia `Position`.

Ambos modelos implementan el método `__str__()` para mostrar información legible (por ejemplo, en el
panel de administración y en las listas).

---

## 4. Formularios (`empleados_fbv/forms.py`)

Se usan `ModelForm` (formularios generados automáticamente a partir de los modelos):

- `PositionForm`: campos `name` y `description`.
- `EmployeeForm`: campos del empleado. El campo **`position` se muestra como lista desplegable**
  (`Select`) con los cargos registrados, y `hire_date` usa un selector de fecha (calendario).

Ambos formularios aplican clases de **Bootstrap** a sus campos para mejorar la apariencia.

---

## 5. Primera etapa — Vistas Basadas en Funciones (VBF)

Ubicación: `empleados_fbv/views.py`

Cada operación es una **función** de Python que recibe el `request` y controla manualmente si la
petición es `GET` (mostrar el formulario) o `POST` (guardar los datos):

| Función | Operación |
|---------|-----------|
| `position_list` / `employee_list` | Listar |
| `position_create` / `employee_create` | Crear |
| `position_update` / `employee_update` | Editar |
| `position_delete` / `employee_delete` | Borrar |
| `employee_detail` | Ver detalle de un empleado |

Todas las vistas usan el decorador `@login_required` para exigir sesión iniciada.

Las rutas están en `empleados_fbv/urls.py` (prefijo `/empleados/`).

---

## 6. Segunda etapa — Vistas Basadas en Clases (VBC)

Ubicación: `empleados_cbv/views.py`

El **mismo CRUD** pero usando las **vistas genéricas** de Django. En lugar de escribir el manejo de
`GET`/`POST`, se hereda de una clase que ya trae esa lógica y solo se configuran unos atributos
(`model`, `form_class`, `template_name`, `success_url`):

| Clase | Vista genérica | Operación |
|-------|----------------|-----------|
| `PositionListView` / `EmployeeListView` | `ListView` | Listar |
| `EmployeeDetailView` | `DetailView` | Ver detalle |
| `PositionCreateView` / `EmployeeCreateView` | `CreateView` | Crear |
| `PositionUpdateView` / `EmployeeUpdateView` | `UpdateView` | Editar |
| `PositionDeleteView` / `EmployeeDeleteView` | `DeleteView` | Borrar |

Las rutas están en `empleados_cbv/urls.py` (prefijo `/empleados_cbv/`) y usan `.as_view()` para
convertir cada clase en una vista.

---

## 7. Comparación VBF vs VBC

| Aspecto | VBF (Funciones) | VBC (Clases) |
|---------|-----------------|--------------|
| Qué es | Una función `def` | Una clase que hereda de una vista genérica |
| Manejo de GET/POST | Manual (`if request.method == ...`) | Automático (lo hace Django) |
| Cantidad de código | Más largo | Más corto |
| En las URLs | `views.mi_funcion` | `views.MiClase.as_view()` |
| Login | `@login_required` | `LoginRequiredMixin` |
| Ideal para | Lógica muy personalizada | CRUDs estándar |

**Conclusión:** ambas versiones producen el mismo resultado. VBF da más control y es más explícito;
VBC requiere menos código porque reutiliza la lógica que Django ya trae hecha.

---

## 8. Plantillas HTML

Cada app tiene sus plantillas en una subcarpeta con el nombre de la app
(`templates/empleados_fbv/` y `templates/empleados_cbv/`) para evitar conflictos de nombres.
Todas heredan de `base.html` (Bootstrap + barra de navegación común).

Por cada entidad hay: lista, formulario (crear/editar), confirmación de borrado y, en el caso de
empleados, una vista de detalle.

---

## 9. Cómo ejecutar el proyecto en local

```bash
# 1. Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate          # En Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones (crea las tablas en la base de datos)
python manage.py migrate

# 4. Ejecutar el servidor de desarrollo
python manage.py runserver
```

Luego abrir en el navegador: `http://127.0.0.1:8000/`

### Rutas principales

| Página | URL |
|--------|-----|
| Inicio | `/` |
| Registro | `/signup/` |
| Iniciar sesión | `/signin/` |
| Cargos (VBF) | `/empleados/positions/` |
| Empleados (VBF) | `/empleados/employees/` |
| Cargos (VBC) | `/empleados_cbv/positions/` |
| Empleados (VBC) | `/empleados_cbv/employees/` |

> Para crear empleados primero deben existir cargos, porque el empleado debe elegir uno.

---

## 10. Despliegue

El proyecto está desplegado en **Render**. La configuración de producción está preparada en
`settings.py` (lee variables de entorno), junto con `build.sh` (instala dependencias, recolecta
archivos estáticos y aplica migraciones) y `render.yaml` (define el servicio web).
Los archivos estáticos se sirven con **WhiteNoise**.

---

## Tecnologías utilizadas

- **Python** / **Django**
- **Bootstrap 5** (interfaz)
- **SQLite** (base de datos)
- **Gunicorn** + **WhiteNoise** (producción)
- **Render** (hosting) · **GitHub** (repositorio)
