from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        generic_public_group, generic_public_group_created = Group.objects.get_or_create(name='一般民眾')

        entry_applicant_group, entry_applicant_group_created = Group.objects.get_or_create(name='進港申請者')

        county_data_maintainer_group, county_data_maintainer_group_created = Group.objects.get_or_create(name='縣市政府資料維護者')

        county_data_inquirer_group, county_data_inquirer_group_created = Group.objects.get_or_create(name='縣市政府資料查詢者')

        county_data_approver_group, county_data_approver_group_created = Group.objects.get_or_create(name='縣市政府資料批核者')

        fishery_agency_data_maintainer_group, fishery_agency_data_maintainer_group_created = Group.objects.get_or_create(name='漁業署資料維護者')

        fishery_agency_data_inquirer_group, fishery_agency_data_inquirer_group_created = Group.objects.get_or_create(name='漁業署資料查詢者')

        fishery_agency_data_approver_group,fishery_agency_data_approver_group_created = Group.objects.get_or_create(name='漁業署資料批核者')

        coast_guard_group, coast_guard_group_created = Group.objects.get_or_create(name='海巡署')