c = get_config()

# Устанавливаем IP-адрес и порт для JupyterHub
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Устанавливаем IP-адрес для подключения хаба
c.JupyterHub.hub_connect_ip = '127.0.0.1'

# Настройка подключения к базе данных PostgreSQL
c.JupyterHub.db_url = 'postgresql://postgres:postgres@db_service:5432/postgres'

# Используем Dummy Authenticator для тестирования
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# Настройка спаунера
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'
