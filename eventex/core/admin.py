from django.contrib import admin
from django.utils.html import format_html
from eventex.core.models import Speaker, Contact, Talk, Course


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj: Speaker):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj: Speaker):
        return format_html(f'<img width="32px" src="{obj.photo}"/>')

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

    def email(self, obj: Speaker):
        return obj.contact_set.emails().first()

    email.short_description = 'e-mail'

    def phone(self, obj: Speaker):
        return obj.contact_set.phones().first()

    phone.short_description = 'telefone'

admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
admin.site.register(Course)
