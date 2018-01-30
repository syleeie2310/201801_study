from django.views.generic import TemplateView
from .models import About, Domain, Experience, ExperienceType, Project, Publication, PublicationType

def get_ex(ex_type):
    rows = Experience.objects.filter(ex_type__title=ex_type)\
        .extra({'s': "DATE_FORMAT(start, '%%b. %%Y')", 'e': "DATE_FORMAT(end, '%%b. %%Y')"})\
        .values('s', 'e', 'title_kor', 'title_eng', 'location_kor', 'location_eng', 'desc_kor', 'desc_eng')\
        .order_by('-s')
    for entry in rows:
        if entry['e'] is None:
            entry['range_ko'] = "%s - 현재" % entry['s']
            entry['range_en'] = "%s - CURRENT" % entry['s']
        else:
            entry['range_ko'] = "%s - %s" % (entry['s'], entry['e'])
            entry['range_en'] = "%s - %s" % (entry['s'], entry['e'])
    return rows

class Index(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        # desc. text of myself
        context['about'] = About.objects.first()

        # domian
        context['domains'] = Domain.objects.all()

        # work experience
        context['works'] = get_ex("work")

        # educations
        context['edus'] = get_ex("멋진놈")


        return context
