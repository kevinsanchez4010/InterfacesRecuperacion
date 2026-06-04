# Sistema de Login - ElectroVolt

## Descripción General
Se ha creado un sistema completo de autenticación con las siguientes características:

### Componentes Implementados

#### 1. **Vistas (Views)**
- `login_view()` - Página de login
- `logout_view()` - Cerrar sesión
- `dashboard_view()` - Panel privado protegido por autenticación

#### 2. **Templates**
- `login.html` - Formulario de login con mensajes de error/éxito
- `templates/private/dashboard.html` - Panel privado del usuario
- `static/private/index.html` - Página privada de bienvenida

#### 3. **URLs Disponibles**
```
/login/          - Página de login
/logout/         - Cerrar sesión
/dashboard/      - Panel privado (protegido)
```

---

## Cómo Usar

### Acceder al Login
1. Navega a: `http://localhost:8000/login/`
2. Ingresa credenciales de usuario

### Crear Usuario de Prueba

Desde la terminal en tu proyecto:

```bash
python manage.py createsuperuser
```

O crear usuario desde Django admin:

```bash
python manage.py shell
```

Dentro del shell:
```python
from django.contrib.auth.models import User
User.objects.create_user(
    username='testuser',
    email='test@electrovolt.com',
    password='Test123456',
    first_name='Juan',
    last_name='Pérez'
)
```

### Flujo de Autenticación

```
┌─────────────┐
│   Inicio    │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ ¿Usuario logueado?│
└──────┬───────────┘
       │
  No   │   Sí
       │       └─────────────────┐
       │                         │
       ▼                         ▼
┌─────────────┐        ┌─────────────┐
│ Login Page  │        │  Dashboard  │
└──────┬──────┘        └─────────────┘
       │
       ├─ Credenciales OK → Dashboard
       │
       └─ Credenciales Fallo → Mostrar Error
```

---

## Características de Seguridad

### ✅ Implementadas

1. **Decorador `@login_required`**
   - Protege vistas privadas
   - Redirige a login si no está autenticado

2. **Tokens CSRF**
   - `{% csrf_token %}` en formularios
   - Previene ataques Cross-Site Request Forgery

3. **Mensajes de Django**
   - Feedback al usuario (éxito/error)
   - Mensajes flash automáticos

4. **Hashing de Contraseñas**
   - Django hash automático
   - Nunca se almacenan contraseñas en texto plano

5. **Meta tags de Seguridad**
   - `noindex, nofollow` en áreas privadas
   - Previene indexación en buscadores

---

## Estructura de Archivos

```
inicio/
├── views.py                          (Vistas de login/dashboard)
├── urls.py                           (Rutas de autenticación)
├── templates/
│   ├── login.html                    (Formulario de login)
│   └── private/
│       └── dashboard.html            (Panel privado)
└── static/
    └── private/
        └── index.html                (Página privada estática)
```

---

## Personalización

### Cambiar URL de Login por Defecto

En `settings.py`:
```python
LOGIN_URL = 'login'           # URL nombrada
LOGIN_REDIRECT_URL = 'dashboard'  # Redirigir después de login
LOGOUT_REDIRECT_URL = 'index'     # Redirigir después de logout
```

### Agregar Nuevas Vistas Privadas

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def mi_vista_privada(request):
    return render(request, 'private/my-page.html')
```

### Verificar Autenticación en Templates

```html
{% if user.is_authenticated %}
    <p>Hola, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Cerrar sesión</a>
{% else %}
    <a href="{% url 'login' %}">Iniciar sesión</a>
{% endif %}
```

---

## Próximas Mejoras (Opcional)

- [ ] Sistema de registro de usuarios
- [ ] Recuperación de contraseña
- [ ] Autenticación OAuth (Google, GitHub)
- [ ] Factor doble (2FA)
- [ ] Panel de administración
- [ ] Registro de actividad
- [ ] Notificaciones en tiempo real

---

## Testing

### Probar flujo de login

```python
# test_login.py
from django.test import Client
from django.contrib.auth.models import User

def test_login():
    client = Client()
    user = User.objects.create_user('test', 'test@example.com', 'pass123')
    
    # Test login exitoso
    response = client.post('/login/', {'username': 'test', 'password': 'pass123'})
    assert response.status_code == 302  # Redirect to dashboard
    
    # Test login fallido
    response = client.post('/login/', {'username': 'test', 'password': 'wrongpass'})
    assert response.status_code == 200  # Stay on login page
```

---

## Preguntas Frecuentes

**P: ¿Cómo agrego más campos al perfil de usuario?**
R: Crea un modelo `Profile` que tenga una relación OneToOne con User.

**P: ¿Cómo manejo roles y permisos?**
R: Usa `@permission_required` o `groups` de Django.

**P: ¿Cómo protejo rutas de API?**
R: Usa `login_required` o tokens de autenticación (DRF).

---

**Creado:** 2024-06-04
**Versión:** 1.0
**Estado:** ✅ Producción
