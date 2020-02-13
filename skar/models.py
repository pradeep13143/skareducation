# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField
GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'))
ID_CHOICES = (('Aadhar','Aadhar'),('Driving Licence','Driving Licence'),('Voter ID','Voter ID'),('Pancard','Pancard'),('Passport','Passport'))

# Create your models here.
class Base(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default = True)

	class Meta:
		abstract = True

class HomeBanner(Base):
	title = models.CharField("Title of Banner", max_length=200)
	image = ThumbnailerImageField(upload_to ="static/uploads/%Y/%m/%d")
	content = RichTextField()
	tagline = models.CharField("Tagline of Banner", max_length=500, blank=True)

	def __str__(self):
		return self.title

class WhatWeOffer(Base):
	title = models.CharField("Title of Banner", max_length=200)
	content = RichTextField()
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class WhyChooseUs(Base):
	name = models.CharField("Name", max_length=200)
	content = RichTextField()

	def __str__(self):
		return self.name

class WhyChooseUsTopics(Base):
	name = models.CharField("Name", max_length=200)
	content = RichTextField()

	def __str__(self):
		return self.name


class Testimonials(Base):
	name = models.CharField("Name", max_length=200)
	address = models.CharField("Name", max_length=200, blank=True, null=True)
	image = ThumbnailerImageField(upload_to ="static/uploads/%Y/%m/%d", blank=True, null=True)
	content = RichTextField()

	def __str__(self):
		return self.name

class State(Base):
	name = models.CharField("State Name", max_length=200)

	def __str__(self):
		return self.name

class District(Base):
	state = models.ForeignKey(State)
	name = models.CharField("District Name", max_length=200)

	def __str__(self):
		return self.name

class City(Base):
	district = models.ForeignKey(District)
	name = models.CharField("City Name", max_length=200)

	def __str__(self):
		return self.name

class Grade(Base):
	name = models.CharField("Syllabus Name", max_length=200)

	def __str__(self):
		return self.name

class Board(Base):
	name = models.CharField("Syllabus Name", max_length=200)

	def __str__(self):
		return self.name

class Subject(Base):
	name = models.CharField("Subject name", max_length=200)

	def __str__(self):
		return self.name


class Student(Base):
	parent_name = models.CharField("Parent Name", max_length=200)
	email = models.EmailField("Email", blank=True)
	phone = models.CharField("Phone numbers", max_length=500)
	student_name = models.CharField("Student Name", max_length=200)
	gender = models.CharField("Gender", choices = GENDER_CHOICES, max_length=200)
	address = models.TextField()
	pincode = models.CharField(max_length=200, blank=True, null=True)
	board = models.ForeignKey(Board, blank=True, null=True)
	grade = models.ForeignKey(Grade, blank=True, null=True)
	subjects = models.ManyToManyField(Subject, blank=True)
	details = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.student_name

class Teacher(Base):
	name = models.CharField("Name", max_length=200)
	email = models.EmailField("Email", blank=True)
	phone = models.CharField("Phone numbers", max_length=500)
	gender = models.CharField("Gender", choices = GENDER_CHOICES, max_length=200)
	address = models.TextField()
	city = models.ForeignKey(City, blank=True, null=True)
	photo = ThumbnailerImageField()
	id_proof_type = models.CharField("Type of ID proof", choices = ID_CHOICES, max_length=200)
	id_proof = models.FileField(upload_to="proofs")
	details = models.TextField(blank=True, null=True)
	subjects = models.ManyToManyField(Subject, blank=True)

	def __str__(self):
		return self.name

class TeacherCategory(Base):
	name = models.CharField("Name", max_length=200)
	slug = models.SlugField("SEO friendly url, use only aplhabets and hyphen", max_length=60)
	order = models.IntegerField()

	def __str__(self):
		return self.name

class TeacherContent(Base):
	category = models.ForeignKey(TeacherCategory)
	name = models.CharField("Name", max_length=200)
	description = RichTextField("Description")

	def __str__(self):
		return self.name

class StudentCategory(Base):
	name = models.CharField("Name", max_length=200)
	slug = models.SlugField("SEO friendly url, use only aplhabets and hyphen", max_length=60)
	order = models.IntegerField()

	def __str__(self):
		return self.name

class StudentContent(Base):
	category = models.ForeignKey(StudentCategory)
	name = models.CharField("Name", max_length=200)
	description = RichTextField("Description")

	def __str__(self):
		return self.name

class Vacancy(Base):
	name = models.CharField("Job Name", max_length=200)
	description = RichTextField()
	location = models.CharField("Location", max_length=200)

	def __str__(self):
		return self.name

class AboutUs(Base):
	name = models.CharField("Headline", max_length=200)
	description = RichTextField()

	def __str__(self):
		return self.name

class Admission(Base):
	student = models.ForeignKey(Student)
	teacher = models.ForeignKey(Teacher)
	start_date = models.DateTimeField(blank=True, null=True)
	end_date = models.DateTimeField(blank=True, null=True)
	admission_fee = models.IntegerField(blank=True, null=True)
	tuitor_fee = models.IntegerField(blank=True, null=True)
	more_detail = models.TextField(blank=True)
	subject = models.ManyToManyField(Subject, blank=True)


class ContactUs(Base):
	name = models.CharField("Name", max_length=200)
	email = models.CharField("Email", max_length=200)
	subject = models.CharField("Subject", max_length=200, blank=True)
	message = models.TextField("Message", blank=True)

	def __str__(self):
		return self.name
