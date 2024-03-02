from django.db.models import Count
from django.utils import timezone

def distribute_user_to_groups(product, user):
    if product.start_date < timezone.now():
        groups = Group.objects.filter(product=product)
        users_count = User.objects.filter(groups_related__product=product).count()
        remaining_users = users_count % groups.count()

        for group in groups:
            group_users_count = group.users.count()
            if group_users_count < group.max_users and remaining_users > 0:
                group.users.add(user)
                remaining_users -= 1
            elif group_users_count < group.min_users:
                group.users.add(user)


# При доступе к продукту вызываем функцию для распределения пользователя по группам
def access_product(product, user):
    if product.has_access(user):
        distribute_user_to_groups(product, user)