from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from taggit.managers import TaggableManager
from shared.utils import *

class UserProfile(models.Model):
	tab_id=models.IntegerField(primary_key=True)
	#username=models.CharField(max_length=20)
	#email=models.EmailField(max_length=30)
        user = OneToOneField(User)
	location=models.CharField(max_length=10)
	nickname=models.CharField(max_length=10)# May not needed
	#password = models.CharField(max_length=15)
	avatar= models.ImageField(upload_to='static/images/profile_image', blank=True)
	online_status=models.BooleanField(default=False)# Good!
	user_type=models.IntegerField(max_length=1,default=0)
	skills=models.CharField(max_length=100, blank=True)#to mantain user profile
	posts = IntegerField(default=0)
	reply_count=models.IntegerField(default=0)
	role=models.IntegerField()#to differentiate b/w user and admin

	def __unicode__(self):
		return self.username

	def increment_posts(self):
        	self.posts += 1
         	self.save()

	def increment_replies(self):
        	self.reply_count += 1
        	self.save()


class Category(models.Model):
	category=models.CharField(max_length=20)
	tags = TaggableManager()

	def __unicode__(self):
		return self.category

class Post(models.Model):
        title = CharField(max_length=60)
	body=models.TextField()
	created_date=models.DateTimeField(auto_now_add=True)
	#fk
	user=models.ForeignKey('UserProfile')
	#fk
	category=models.ForeignKey('Category')
	count=models.IntegerField(default=0)
	admin_id=models.IntegerField()#question will need admin's approval

	class Meta:
		ordering = ["created_date"]

	def __unicode__(self):
		return self.title
	def increment_count(self):
        	self.count += 1
        	self.save()
	def short(self):
        	created = self.created_date.strftime("%b %d, %I:%M %p")
        	return u"%s - %s\n%s" % (self.user, self.title, created_date)
	def profile_data(self):
        	p = self.created_date.profile
        	return p.posts, p.avatar


class Reply(models.Model):
	#fk
	title=models.ForeignKey('Post')
	body=models.TextField()
        #creator = ForeignKey(User, blank=True, null=True)
	user=models.ForeignKey(User)
	post_date=models.DateTimeField(auto_now_add=True)
	file_upload=models.FileField(upload_to='forum/file')
	ratings=models.IntegerField(max_length=5,default=0)# there should be a limit within which the rating should be done
	admin_approved=models.BooleanField(default=False)
	count=models.IntegerField(default=0)

	class Meta:
        	ordering = ["post_date"]
 
	def __unicode__(self):
		return self.title
	def increment_count(self):
        	self.count += 1
        	self.save()
	def short(self):
        	created = self.post_date.strftime("%b %d, %I:%M %p")
        	return u"%s - %s\n%s" % (self.user, self.title, post_date)
	def profile_data(self):
        	p = self.post_date.profile
        	return p.posts, p.avatar




class Comment(models.Model):
	#fk
	answer=models.ForeignKey(Reply)
	text=models.TextField()
	created_date=models.DateTimeField(auto_now_add=True)
	count=models.IntegerField(default=0)
	user=models.ForeignKey(User)

	class Meta:
        	ordering = ["-created_date"]

	def __unicode__(self):
		return self.count



class Ticket(models.Model):
	user_id=models.ForeignKey(User)
	topic_id=models.ForeignKey(Category)
	message=models.TextField()
	ticket_id=models.IntegerField()
	file_uploads=models.FileField(upload_to='tickets/file')
	created_date_time=models.DateTimeField(auto_now_add=True)
	overdue_date_time=models.DateTimeField(auto_now_add=True)
	closed_date_time=models.DateTimeField(auto_now_add=True)
	status=models.IntegerField()
	reopened_date_time=models.DateTimeField(auto_now_add=True)
	topic_priority=models.IntegerField()
	duration_for_reply=models.IntegerField()

	def __unicode__(self):
		return self.user_id


class Tablet_info(models.Model):
	rcID=models.IntegerField()
	rcName=models.CharField(max_length=100)
	start_tab_id=models.IntegerField()
	end_tab_id=models.IntegerField()
	count=models.IntegerField()
	city=models.CharField(max_length=20)

	def __unicode__(self):
		return self.start_tab_id,self.end_tab_id


