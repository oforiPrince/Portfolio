from django.contrib import admin

from .models import Project, Certificate, AcquiredSkill, SkillCategory,Testimonial

admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(AcquiredSkill)
admin.site.register(SkillCategory)
admin.site.register(Testimonial)