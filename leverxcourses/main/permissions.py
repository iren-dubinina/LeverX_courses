from django.contrib.auth.models import Permission, Group

# Group.objects.create(name='student')
# Group.objects.create(name='lecturer')

group = Group.objects.filter(name='lecturer')[0]
permissions = Permission.objects.filter(codename__icontains='lecture')
group.permissions.add(*permissions)
permissions = Permission.objects.filter(codename__icontains='task')
group.permissions.add(*permissions)
permissions = Permission.objects.filter(codename__icontains='course')
group.permissions.add(*permissions)
