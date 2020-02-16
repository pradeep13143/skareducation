# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from .models import *

# Create your views here.
def home(request):
	whatweoffers = WhatWeOffer.objects.filter(active=True).order_by('order')
	banners = HomeBanner.objects.filter(active=True)
	why_choose_us_topics = WhyChooseUsTopics.objects.filter(active=True)
	why_choose_us = WhyChooseUs.objects.filter(active=True).latest('id')
	testimonials = Testimonials.objects.filter(active=True)
	return render(request, 'home.html', locals())


def about_us(request):
	aboutus = AboutUs.objects.filter(active=True)
	return render(request, 'about-us.html', locals())


def blog(request):
	return render(request, 'blog.html', locals())


def faq(request):
	return render(request, 'faq.html', locals())


def team(request):
	return render(request, 'team.html', locals())

def contact_us(request):
	success_message = ''
	if request.method == 'POST':
		contactus = ContactUs()
		contactus.name = request.POST.get('name', '')
		contactus.email = request.POST.get('email', '')
		contactus.subject = request.POST.get('subject', '')
		contactus.message = request.POST.get('message', '')
		contactus.save()
		success_message = "Thanks for contacting us, we will contact you shortly."
	return render(request, 'contact-us.html', locals())

def careers(request):
	careers = Vacancy.objects.filter(active=True)
	return render(request, 'careers.html', locals())

def tutor_content(request, slug):
	category = TeacherCategory.objects.filter(slug=slug).latest('id')
	content = TeacherContent.objects.filter(category=category)
	return render(request, 'tutor-content.html', locals())

def student_content(request, slug):
	category = StudentCategory.objects.filter(slug=slug).latest('id')
	content = StudentContent.objects.filter(category=category)
	return render(request, 'student-content.html', locals())


@csrf_exempt
def register_student(request):
	success_message = ''
	added = False
	if request.method == 'POST':
		student = Student()
		student.parent_name = request.POST.get('parent_name', '')
		student.email = request.POST.get('email', '')
		student.student_name = request.POST.get('student_name', '')
		student.phone = request.POST.get('phone', '')
		student.gender = request.POST.get('gender', '')
		student.address = request.POST.get('address', '')
		student.pincode = request.POST.get('pincode', '')
		student.details = request.POST.get('other_details', '')
		student.save()
		added = True
		success_message = "Thanks for Registering with us, we will contact you shortly."
	return render(request, 'register-student.html', locals())


def register_tutor(request):
	success_message = ''
	added = False
	if request.method == 'POST':
		teacher = Teacher()
		teacher.name = request.POST.get('name', '')
		teacher.email = request.POST.get('email', '')
		teacher.id_proof_type = request.POST.get('student_name', '')
		teacher.phone = request.POST.get('phone', '')
		teacher.gender = request.POST.get('gender', '')
		teacher.address = request.POST.get('address', '')
		teacher.pincode = request.POST.get('pincode', '')
		teacher.details = request.POST.get('other_details', '')
		teacher.id_proof = request.FILES['id_proof']
		teacher.photo = request.FILES['photograph']
		teacher.save()
		added = True
		success_message = "Thanks for Registering with us, we will contact you shortly."
	return render(request, 'register-tutor.html', locals())


def manage_admin(request):
	error_message = ''
	user = request.user
	if request.method == "POST":
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/manage-home/') 
		else:
			error_message = "Invalid user, please check your credentials"
	return render(request, 'manage.html', locals())

def manage_home(request):
	return render(request, 'manage-home.html', locals())