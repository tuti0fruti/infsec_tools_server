# InfSecTools

Проект для сборки и продажи средств защиты информации на основе Django и базы данных MSSQL.

## Установка и настройка

### 1. Установка необходимых пакетов

Сначала необходимо установить Django и драйвер для работы с MSSQL:
    pip install django
    pip install django-mssql-backend
    pip install mssql-django

### 2. Создание проекта и приложения

Создаем проект Django:
    django-admin startproject infsec_tools

Затем создаем приложение внутри проекта:
    cd infsec_tools
    python manage.py startapp core

### 3. Настройка подключения к базе данных MSSQL

В файле `infsec_tools/settings.py` добавляем настройки базы данных:

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'InfSecTools2',
        'USER': 'sa',
        'PASSWORD': 'MSSQLSERVER',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}


### 4. Создание моделей

python manage.py inspectdb > core/models.py

### 5. Создание и выполнение миграций

Создаем и выполняем миграции для базы данных:
python manage.py makemigrations
python manage.py migrate

### 6. Сериализация данных

Создаем сериализаторы для моделей в файле `core/serializers.py`:

from rest_framework import serializers
from .models import Classifier, Complexsolution, Complexsolutionproducts, Customerrequest, Customerrequestitems, Employee, Product, Soldproduct

class ClassifierSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Classifier """
    class Meta:
        model = Classifier
        fields = '__all__'

class ComplexsolutionSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Complexsolution """
    class Meta:
        model = Complexsolution
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Product """
    class Meta:
        model = Product
        fields = '__all__'

class ComplexsolutionproductsSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Complexsolutionproducts """
    class Meta:
        model = Complexsolutionproducts
        fields = '__all__'

class CustomerrequestSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Customerrequest """
    class Meta:
        model = Customerrequest
        fields = '__all__'

class CustomerrequestitemsSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Customerrequestitems """
    class Meta:
        model = Customerrequestitems
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Employee """
    class Meta:
        model = Employee
        fields = '__all__'

class SoldproductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Soldproduct """
    class Meta:
        model = Soldproduct
        fields = '__all__'

### 7. Создание представлений

Создаем представления для моделей в файле `core/views.py`:

from rest_framework import viewsets
from .models import Classifier, Complexsolution, Complexsolutionproducts, Customerrequest, Customerrequestitems, Employee, Product, Soldproduct
from .serializers import ClassifierSerializer, ComplexsolutionSerializer, ComplexsolutionproductsSerializer, CustomerrequestSerializer, CustomerrequestitemsSerializer, EmployeeSerializer, ProductSerializer, SoldproductSerializer

class ClassifierViewSet(viewsets.ModelViewSet):
    """ Представление для модели Classifier """
    queryset = Classifier.objects.all()
    serializer_class = ClassifierSerializer

class ComplexsolutionViewSet(viewsets.ModelViewSet):
    """ Представление для модели Complexsolution """
    queryset = Complexsolution.objects.all()
    serializer_class = ComplexsolutionSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ Представление для модели Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ComplexsolutionproductsViewSet(viewsets.ModelViewSet):
    """ Представление для модели Complexsolutionproducts """
    queryset = Complexsolutionproducts.objects.all()
    serializer_class = ComplexsolutionproductsSerializer

class CustomerrequestViewSet(viewsets.ModelViewSet):
    """ Представление для модели Customerrequest """
    queryset = Customerrequest.objects.all()
    serializer_class = CustomerrequestSerializer

class CustomerrequestitemsViewSet(viewsets.ModelViewSet):
    """ Представление для модели Customerrequestitems """
    queryset = Customerrequestitems.objects.all()
    serializer_class = CustomerrequestitemsSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """ Представление для модели Employee """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SoldproductViewSet(viewsets.ModelViewSet):
    """ Представление для модели Soldproduct """
    queryset = Soldproduct.objects.all()
    serializer_class = SoldproductSerializer

### 8. Настройка маршрутов

Добавляем маршруты в файл `core/urls.py`:

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ClassifierViewSet, ComplexsolutionViewSet, ComplexsolutionproductsViewSet, CustomerrequestViewSet, CustomerrequestitemsViewSet, EmployeeViewSet, ProductViewSet, SoldproductViewSet

router = DefaultRouter()
router.register(r'Classifiers', ClassifierViewSet)
router.register(r'complexsolutions', ComplexsolutionViewSet)
router.register(r'complexsolutionproducts', ComplexsolutionproductsViewSet)
router.register(r'customerrequests', CustomerrequestViewSet)
router.register(r'customerrequestitems', CustomerrequestitemsViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'soldproducts', SoldproductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

Добавляем маршруты в файл `infsec_tools/urls.py`:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

### 9. Создание файла .gitignore

Создаем файл `.gitignore` в корне проекта и добавляем туда файлы и директории, которые не должны отслеживаться системой контроля версий:

*.pyc
__pycache__/
db.sqlite3
*.log
.env
.DS_Store
.vscode/
.idea/
*.swp

### Запуск сервера

Теперь можно запустить сервер и протестировать API:
    python manage.py runserver

Зайди на `http://127.0.0.1:8000/api/` для просмотра доступных маршрутов.

## Описание структуры проекта

- **infsec_tools/settings.py**: Основные настройки проекта Django, включая настройки базы данных, установленные приложения, статические файлы и т.д.
- **infsec_tools/urls.py**: Основные маршруты проекта. Здесь подключаются маршруты из приложений.
- **infsec_tools/wsgi.py**: Точка входа для WSGI-совместимых веб-серверов для обслуживания проекта.
- **infsec_tools/asgi.py**: Точка входа для ASGI-совместимых веб-серверов.
- **manage.py**: Скрипт командной строки для управления проектом Django (миграции, запуск сервера и т.д.).
- **core/models.py**: Здесь определяются модели данных приложения.
- **core/views.py**: Здесь создаются представления, которые обрабатывают HTTP-запросы и возвращают HTTP-ответы.
- **core/serializers.py**: Здесь создаются сериализаторы, которые преобразуют данные в JSON и обратно.

## Заключение

Проект готов к работе и подключен к базе данных MSSQL. Модели, сериализация, миграции и представления настроены и готовы к использованию.

## Теория

    #### `models.Model`
    Каждый класс в модели наследует `models.Model`. Это основной класс Django, который определяет модель как объект базы данных.

    #### `AutoField`
    `AutoField` - это поле для автоматического увеличения, которое обычно используется для идентификаторов.

        **Атрибуты:**
        - `primary_key`: Указывает, что это поле является первичным ключом для модели. 

    #### `CharField`
    `CharField` используется для хранения строковых данных с ограниченной длиной.

        **Атрибуты:**
        - `max_length`: Максимальная длина строки.
        - `db_collation`: Опционально указывает на способ сортировки и сопоставления строк в базе данных.

    #### `TextField`
    `TextField` используется для хранения больших текстовых данных.

        **Атрибуты:**
        - `db_collation`: Опционально указывает на способ сортировки и сопоставления строк в базе данных.
        - `blank`: Указывает, может ли поле быть пустым в форме.
        - `null`: Указывает, может ли поле содержать `NULL` в базе данных.

    #### `ForeignKey`
    `ForeignKey` используется для создания связи "многие к одному" с другой моделью.

        **Атрибуты:**
        - `to`: Указывает модель, к которой делается ссылка.
        - `on_delete`: Указывает, что должно происходить при удалении объекта, на который указывает ссылка. Опции включают `CASCADE`, `PROTECT`, `SET_NULL`, и другие.

    #### `DecimalField`
    `DecimalField` используется для хранения чисел с фиксированной точностью, что полезно для денежных значений.

        **Атрибуты:**
        - `max_digits`: Максимальное количество цифр, которые могут храниться.
        - `decimal_places`: Количество цифр после запятой.

    #### `DateField`
    `DateField` используется для хранения дат.

        **Атрибуты:**
        - `auto_now`: Указывает, что поле должно автоматически сохранять текущее время при каждом сохранении объекта.
        - `auto_now_add`: Указывает, что поле должно сохранять текущее время при создании объекта.

    #### `IntegerField`
    `IntegerField` используется для хранения целых чисел.

    #### `BinaryField`
    `BinaryField` используется для хранения бинарных данных.

    #### `class Meta`
    Внутренний класс `Meta` используется для задания различных параметров модели.

        **Атрибуты:**
        - `managed`: Указывает, должна ли Django управлять созданием, изменением и удалением таблицы. Если `False`, Django не будет создавать и изменять таблицу.
        - `db_table`: Указывает имя таблицы в базе данных.
        - `unique_together`: Задает уникальные комбинации полей.

    ## on_delete
    Атрибут `on_delete` в Django используется для определения поведения при удалении объекта, на который указывает внешний ключ (`ForeignKey`) или одиночная связь (`OneToOneField`). Этот атрибут определяет, как база данных должна реагировать при удалении родительского объекта, на который ссылаются другие объекты через внешний ключ.

    ### Возможные значения `on_delete`:

    1. **CASCADE**:
    - При удалении родительского объекта, все связанные с ним дочерние объекты также удаляются.
    - Пример использования:
        ```python
        class MyModel(models.Model):
            parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
        ```

    2. **PROTECT**:
    - Предотвращает удаление родительского объекта, если на него есть ссылки (внешние ключи).
    - Пример использования:
        ```python
        class MyModel(models.Model):
            parent = models.ForeignKey(ParentModel, on_delete=models.PROTECT)
        ```

    3. **SET_NULL**:
    - Устанавливает значение поля в `NULL` (пустое значение) при удалении родительского объекта.
    - Предполагает, что поле внешнего ключа допускает `NULL`.
    - Пример использования:
        ```python
        class MyModel(models.Model):
            parent = models.ForeignKey(ParentModel, on_delete=models.SET_NULL, null=True)
        ```

    4. **SET_DEFAULT**:
    - Устанавливает значение поля в значение по умолчанию при удалении родительского объекта.
    - Допускает задание значения по умолчанию для поля внешнего ключа.
    - Пример использования:
        ```python
        class MyModel(models.Model):
            parent = models.ForeignKey(ParentModel, on_delete=models.SET_DEFAULT, default=default_value)
        ```

    5. **DO_NOTHING**:
    - Ничего не делать при удалении родительского объекта. Оставляет внешний ключ без изменений.
    - Может привести к ошибкам целостности данных в базе данных, если не управлять вручную.
    - Пример использования:
        ```python
        class MyModel(models.Model):
            parent = models.ForeignKey(ParentModel, on_delete=models.DO_NOTHING)
        ```

    6. **RESTRICT**:
    - Аналогично `PROTECT`. Ограничивает удаление родительского объекта, если есть на него ссылки.
    - Работает как защита от удаления, но не поддерживается всеми базами данных.
    - Пример использования:
        ```python
        class MyModel(models.Model):
            parent = models.ForeignKey(ParentModel, on_delete=models.RESTRICT)
        ```

    ### Выбор значения `on_delete`:
    - **CASCADE** часто используется, когда объекты связаны и должны удаляться вместе с родительским объектом.
    - **PROTECT** или **RESTRICT** полезны для предотвращения удаления родительского объекта, если есть ссылки на него.
    - **SET_NULL** и **SET_DEFAULT** полезны, когда нужно задать определенное значение вместо удаленного объекта.
    - **DO_NOTHING** используется редко, так как может привести к нарушениям целостности данных.