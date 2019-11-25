from django.contrib import admin
from accounts.models import UserProfile, LeadPage, CultPage, ProfPage, EntrePage, GamePage, NatPage

# Register your models here

admin.site.site_header = "Admin Page"

class UserProfileAdmin(admin.ModelAdmin):
    change_form_template = 'admin/userprofile/admin_userprofile.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['id'] = object_id
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

class NatPageAdmin(admin.ModelAdmin):
    search_fields = ['Category']

class GamePageAdmin(admin.ModelAdmin):
    search_fields = ['Category']

class CultPageAdmin(admin.ModelAdmin):
    search_fields = ['Category']

class ProfPageAdmin(admin.ModelAdmin):
    search_fields = ['Category']

class EntrePageAdmin(admin.ModelAdmin):
    search_fields = ['Category']

class LeadPageAdmin(admin.ModelAdmin):
    search_fields = ['Category']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(LeadPage, LeadPageAdmin)
admin.site.register(CultPage, CultPageAdmin)
admin.site.register(ProfPage, ProfPageAdmin)
admin.site.register(EntrePage, EntrePageAdmin)
admin.site.register(GamePage, GamePageAdmin)
admin.site.register(NatPage, NatPageAdmin)
