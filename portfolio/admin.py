from django.contrib import admin
from .models import About, Domain, Experience, ExperienceType, Project, Publication, PublicationType


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['about_me', 'home_img']
    list_display_links = ['about_me']

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['title_kor', 'title_eng', 'desc_kor', 'desc_eng', 'icon']
    list_display_links = ['title_kor']

@admin.register(ExperienceType)
class ExperienceTypeAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['ex_type', 'title_kor', 'start', 'end', 'title_eng', 'location_kor', 'location_eng',
                    'desc_kor', 'desc_eng']
    list_display_links = ['title_kor']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title_kor', 'title_eng', 'title_img', 'date_start', 'date_end', 'desc_kor', 'desc_eng', 'proj_url']
    list_display_links = ['title_kor']

@admin.register(PublicationType)
class PublicationTypeAdmin(admin.ModelAdmin):
    list_display = ['p_type']

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['p_type', 'citation_kor', 'p_date', 'citation_eng', 'desc_kor', 'desc_eng', 'p_url']
    list_display_links = ['citation_kor']