from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import signup_form,login_form
from quiz.models import quizze
from quiz_qus.models import *
from random import shuffle
from leaderboard.models import leaderboard as lb
from django.utils.timezone import datetime
from userprofile.models import profile

from userprofile.models import profile


from django.contrib.auth import authenticate,login,get_user_model,logout

######
from fuzzywuzzy import fuzz
import json
import os

kt=0
cm=0
gm=0
fr=0
g=0

frf=1
ktf=0
cmf=0
gmf=0
strans=""
ansl=[]


keyword=[]
com =["and","that","the","for","it","it's","was","his","who","work","used","way","also","by","can","which","as","known","then","if","between","through","another","","or","my","in","from","a","any","on","combination","to","into","is","of","It","A","each","both"]

#####


User=get_user_model()


def index(request):
	if request.POST:
		print(request.POST)
	return render(request,'index/index.html',{})


def login_view(request):
	form_class=login_form(request.POST or None)
	content={
		"form": form_class
	}
	if not request.user.is_authenticated:
		if form_class.is_valid():
			username=form_class.cleaned_data.get("email")
			password=form_class.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect("/instruction")
			else:
			    print("Error")
		return render(request,'login/login.html',content)
	else:
		obj=lb.objects.filter(user=request.user)
		if obj.exists():
			return redirect('/result')
		else:
			return redirect('/instruction')



def logout_view(request):
	if request.user is not None:
		logout(request)
	return redirect('/')


def signup(request):
	form_class=signup_form(request.POST or None)
	context={
		"form":form_class
	}
	if form_class.is_valid():
		name=form_class.cleaned_data.get("name")
		email=form_class.cleaned_data.get("email")
		college=form_class.cleaned_data.get("college")
		year=form_class.cleaned_data.get("year")
		branch=form_class.cleaned_data.get("branch")
		password=form_class.cleaned_data.get("password")
		contact=form_class.cleaned_data.get("contact")
		new_user= User.objects.create_user(email,email,password)
		user_profile=profile(
				user=new_user,
				name=name,
				college=college,
				year=year,
				branch=branch,
				contact=contact,
			)
		user_profile.save()
		if new_user is not None:
			return redirect("/login")
	return render(request,'signup/signup.html',context)



def instruction(request):
	if request.user.profile_set.all().first().start_time==0:
		return render(request,'index/instruction.html',{})
	else:
		if request.user.is_authenticated:
			logout(request)
		return render(request,'test/rule_broken.html',{})



def leaderboard(request):
	object_1=lb.objects.all().order_by('-points')
	context={
		"object":object_1
	}
	return render(request,'test/leaderboard.html',context)










def dashboard(request):
	quiz_object=quizze.objects.filter(title='Recruitment Drive').first()
	queryset=list(quiz_object.ques.all())
	shuffle(queryset)
	time=quiz_object.time
	context={
		"question1":queryset[0],
		"question2":queryset[1],
		"question3":queryset[2],
		"question4":queryset[3],
		"question5":queryset[4],
		"question6":queryset[5],
		"question7":queryset[6],
		"question8":queryset[7],
		"question9":queryset[8],
		"question10":queryset[9],
		"question11":queryset[10],
		"question12":queryset[11],
		"question13":queryset[12],
		"question14":queryset[13],
		"question15":queryset[14],
		"question16":queryset[15],
		"question17":queryset[16],
		"question18":queryset[17],
		"question19":queryset[18],
		"question20":queryset[19],
		"question21":queryset[20],
		"question22":queryset[21],
		"question23":queryset[22],
		"question24":queryset[23],
		"question25":queryset[24],
		"question26":queryset[25],
		"question27":queryset[26],
		"question28":queryset[27],
		"question29":queryset[28],
		"question30":queryset[29],
		"time":time
	}

	if request.POST:
		count=0
		attempted_qus=0
		for jk in range(30):		
			if request.POST.get(str(queryset[jk].qus_id))==str(queryset[jk].correct_option):
				count=count+1		
			if request.POST.get(str(queryset[jk].qus_id))==None:
				attempted_qus=attempted_qus+1
		attempted_qus=30 - attempted_qus
		correct_qus=count
		wrong_qus=attempted_qus-count
		points=(count*4)
		object_1=lb.objects.filter(user=request.user)
		if points<=40:
			message="Congrats You have Done well !!"
		elif points>40 and points<=60:
			message="Congrats You have Done Pretty well !!"
		elif points>60 and points<=80:
			message="Congrats You have Done your Best !!"
		else:
			message="Congrats You Rocked !!"
		if not object_1.exists():
			lb1=lb(
					user=request.user,
					correct_qus=correct_qus,
					wrong_qus=wrong_qus,
					points=points,
					message=message,
					attempted_qus=attempted_qus
				)
			lb1.save()
			return redirect('/result')
		else:
			return redirect('/')
	if request.user.is_authenticated:
		if request.user.profile_set.all().first().start_time==0:
			obj=profile.objects.get(user=request.user)
			obj.start_time=1
			obj.save()
		else:
			if request.user.is_authenticated:
				logout(request)
			return render(request,'test/rule_broken.html',{})
	return render(request,'test/dashboard.html',context)



def result(request):
	if request.user.is_authenticated:
		obj=lb.objects.filter(user=request.user)
		if obj.exists():
			context_2={
				"cqus":obj.first().correct_qus,
				"wqus":obj.first().wrong_qus,
				"points":obj.first().points,
				"message":obj.first().message
			}
		
		logout(request)
	else:
		context_2={}
	return render(request,'test/result.html',context_2)

def subjective(request):
	queryset=list(subQuestion.objects.all())
	shuffle(queryset)
	time=15
	context={
		"question1":queryset[0],
		"question2":queryset[1],
		"question3":queryset[2],
		"question4":queryset[3],
		"question5":queryset[4],
		"question6":queryset[5],
		# "question7":queryset[6],
		# "question8":queryset[7],
		# "question9":queryset[8],
		# "question10":queryset[9],
		# "question11":queryset[10],
		# "question12":queryset[11],
		# "question13":queryset[12],
		# "question14":queryset[13],
		# "question15":queryset[14],
		# "question16":queryset[15],
		# "question17":queryset[16],
		# "question18":queryset[17],
		# "question19":queryset[18],
		# "question20":queryset[19],
		# "question21":queryset[20],
		# "question22":queryset[21],
		# "question23":queryset[22],
		# "question24":queryset[23],
		# "question25":queryset[24],
		# "question26":queryset[25],
		# "question27":queryset[26],
		# "question28":queryset[27],
		# "question29":queryset[28],
		# "question30":queryset[29],
		"time":time
	}

	if request.POST:
		count=0
		attempted_qus=0
		ques_list = []
		q1 = request.POST.get('ques1')
		q2 = request.POST.get('ques2')
		q3 = request.POST.get('ques3')
		q4 = request.POST.get('ques4')
		q5 = request.POST.get('ques5')
		q6 = request.POST.get('ques6')
		print(">>>", q1,q2,q3,q4,q5,q6)
		ques_list.append(q1)
		ques_list.append(q2)
		ques_list.append(q3)
		ques_list.append(q4)
		ques_list.append(q5)
		ques_list.append(q6)
		module_dir = os.path.dirname(__file__)
		file_path = os.path.join(module_dir, 'words_alpha.txt')
		data_file = open(file_path , 'r')
		data = data_file.read()
		valid_words = set(data.split())
		data_file.close()
		total = 0
		for i in range(len(ques_list)):
			keyword.clear()
			text = ques_list[i]
			
			ansl = queryset[i].correct_option
			for a in ansl:
				ass= a.split()
				for sas in ass:
					sas=sas.lower()
					for check in ansl:
						if a==check:
							continue
						else:
							assc= check.split()
						for x in assc:
							x=x.lower()
							if x==sas and x not in com and x not in keyword:
								keyword.append(x)


			ans=0
			g=0
			text=text.strip()
			english_words = valid_words
			if text==" " or text=="":
				gm=0
			else:
				text= text.split()
				#print(text)
				for t in text:
					t= t.lower()
					if t[-1]=="." : 
						t= t[:-1]
					if t in english_words:
						#print(t)
						g=g+1
					# if g==10:
						# break
			if g>7:
				for ev in ansl:
					ans = ans + fuzz.token_set_ratio(ev,text)
					ans = ans + fuzz.ratio(ev,text)
				
				
			global kt
			global cm
			repeat=[]
			for t in text:
				#if t=="NLP":
				#	lm=lm+1
				t=t.lower()
				if t in keyword and t not in repeat:
					value= keyword.index(t)
					if value>=2:
						kt=kt+0.05
					elif value==0:
						kt=kt+0.1
					elif value==1:
						kt=kt+0.08
					repeat.append(t)
			check=[]
			c=0
			#print(repeat)
			#print(keyword)
			for i in range(0,len(repeat)-1):
				if keyword.index(repeat[i])<keyword.index(repeat[i+1]) and repeat[i] not in check:
					check.append(repeat[i])
			c-len(check)
			if kt > 1:
				kt=1
			if len(check)==0:
				cm=0
			else:
				cm=len(check)/len(repeat)
			
			gm=g/len(text)
			fr= ans/(len(ansl))
			global frf,ktf,cmf,gmf
			
			r = fr/(frf*100) + ktf*kt +cmf*cm +gmf*gm
			#print(r)
			
			if r>0.95:
				r=10
			elif r>0.9:
				r=9.5
			elif r>0.85:
				r=9
			elif r>0.8:
				r=8.5
			elif r>0.75:
				r=8
			elif r>0.7:
				r=7.5
			elif r>0.65:
				r=7
			elif r>0.6:
				r=6.5
			elif r>0.55:
				r=6
			elif r>0.5:
				r=5.5
			elif r>0.45:
				r=5
			elif r>0.4:
				r=4.5
			elif r>0.35:
				r=4
			elif r>0.3:
				r=3.5
			elif r>0.25:
				r=3
			elif r>0.2:
				r=2.5
			elif r>0.15:
				r=2
			elif r>0.1:
				r=1.5
			elif r>0.05:
				r=1
			else:
				r=0		
			
			print("Your marks is ", r)
			total = total+r
		return render(request,'test/subResult.html',{'points':total})
		# for jk in range(30):		
		# 	if request.POST.get(str(queryset[jk].qus_id))==str(queryset[jk].correct_option):
		# 		count=count+1		
		# 	if request.POST.get(str(queryset[jk].qus_id))==None:
		# 		attempted_qus=attempted_qus+1
		# attempted_qus=30 - attempted_qus
		# correct_qus=count
		# wrong_qus=attempted_qus-count
		# points=(count*4)
		# object_1=lb.objects.filter(user=request.user)
		# if points<=40:
		# 	message="Congrats You have Done well !!"
		# elif points>40 and points<=60:
		# 	message="Congrats You have Done Pretty well !!"
		# elif points>60 and points<=80:
		# 	message="Congrats You have Done your Best !!"
		# else:
		# 	message="Congrats You Rocked !!"
		# if not object_1.exists():
		# 	lb1=lb(
		# 			user=request.user,
		# 			correct_qus=correct_qus,
		# 			wrong_qus=wrong_qus,
		# 			points=points,
		# 			message=message,
		# 			attempted_qus=attempted_qus
		# 		)
		# 	lb1.save()
		# 	return redirect('/result')
		# else:
		# 	return redirect('/')

	# if request.user.is_authenticated:
	# 	if request.user.profile_set.all().first().start_time==0:
	# 		obj=profile.objects.get(user=request.user)
	# 		obj.start_time=1
	# 		obj.save()
	# 	else:
	# 		if request.user.is_authenticated:
	# 			logout(request)
	# 		return render(request,'test/rule_broken.html',{})

	return render(request,'test/subjective.html',context)

