from django.core.management.base import BaseCommand
from trader.models import Menu


class Command(BaseCommand):
    help = 'Creates menu items'

    '''This command will work if your db is new or id in menu table starts from 1, else there will be a conflict'''

    def handle(self, *args, **kwargs):

        if Menu.objects.all():
            return 'Please create new database for creating test menu items'

        Menu.objects.bulk_create(
            [
                Menu(name='Menu1 level1', is_main=True, parent=None),
                Menu(name='Menu2 level1', is_main=True, parent=None),
                Menu(name='Menu3 level1', is_main=True, parent=None),
                Menu(name='Menu4 level1', is_main=True, parent=None),
            ]
        )

        Menu.objects.bulk_create(
            [
                Menu(name='Menu1 level2', is_main=False, parent_id=1),
                Menu(name='Menu2 level2', is_main=False, parent_id=1),
                Menu(name='Menu3 level2', is_main=False, parent_id=1),
                Menu(name='Menu1 level2', is_main=False, parent_id=2),
            ]
        )

        Menu.objects.bulk_create(
            [
                Menu(name='Menu1 level3', is_main=False, parent_id=5),
                Menu(name='Menu1 level3', is_main=False, parent_id=6),
                Menu(name='Menu2 level3', is_main=False, parent_id=6),
                Menu(name='Menu1 level3', is_main=False, parent_id=8),
            ]
        )

        print(f'Successfully created the menu items for test')
