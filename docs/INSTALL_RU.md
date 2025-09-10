## Установка и Использование

---

### Без установки

```sh
# Клонирование репозитории
git clone https://github.com/stpatriarch/onekey.git && cd onekey

# пользование: Этот метод позволяет запускать без установки, напрямую как скрипт.
python3 src/onekey/core/core.py 

```

### Установка

```sh
# Клонирование репозитории
git clone https://github.com/stpatriarch/onekey.git && cd onekey

# Создание виртуальной окружения и активация
python3 -m venv venv && source venv/bin/activate

# Установка
pip install .
```

### Использование

```sh
# Первый метод: Оно будет требовать сначала ключ потом хост по очереди։
# Генерированный пароль будет копрованно в буфер обмена.
onekey

# Второй метод: Можно сразу вставить ключ и хост сразу.
# Генерированный пароль будет копрованно в буфер обмена.
onekey -k your_key_here -h your_host_here
```
