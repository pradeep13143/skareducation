from django import template

register = template.Library()
from skar.models import TeacherCategory, StudentCategory

@register.simple_tag()
def get_student_category():
	return StudentCategory.objects.filter(active=True).order_by('order')

@register.simple_tag()
def get_teacher_category():
	return  TeacherCategory.objects.filter(active=True).order_by('order')
