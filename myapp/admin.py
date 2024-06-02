from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register(Request_Type)
admin.site.register(Department)
admin.site.register(Category)
# admin.site.register(Authorizer_Name)
# admin.site.register(Executor_Name)
admin.site.register(System_Details)

@admin.register(Authorizer_Name)
class Authorizer_Name_admin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Executor_Name)
class Executor_Name_admin(admin.ModelAdmin):
    list_display=['id','name']


@admin.register(RFC_Register)
class RFC_FormAdmin(admin.ModelAdmin):
    list_display =['Rfc_Number','created_date','Reference_RFC_No','Department','Request_Type','Environment','Planned_Date','Category','Reason_for_change',
                   'Description_of_change','System_Details','To_be_executed_by','Change_Requested_by','Change_authorizer',
                   'Change_level','Change_impact_assessment','Risk_Rating','Attachments','Change_rollback_procedures','Activity_Notes','status',
                   'Activity_Date']
    
