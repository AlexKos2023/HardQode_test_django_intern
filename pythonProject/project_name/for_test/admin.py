from django.contrib import admin
from django.apps import apps

#Получение списка моделей, определенных в приложении 'for_test'
app_models = apps.get_app_config('for_test').get_models()

#Для каждой модели в списке app_models выполняется регистрация
#в административной панели Django с помощью метода register()
for model in app_models:
    admin.site.register(model)
