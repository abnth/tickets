from ac.models import *
from django import forms
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
last_ticket=100
#last_ticket=int(Ticket.objects.all().aggregate(Max('ticket_id'))['ticket_id__max'])
#ticket_id_new=last_ticket+1
#print ticket_id_new
class SubmitTicketForm(forms.ModelForm):
		tab_id=forms.CharField(max_length=8,help_text="Enter your tablet  id:")
                topic_id=forms.ChoiceField(choices=[(x['category'], str(x['category'])) for x in Category.objects.values('category')],help_text="Select the category of your problem:")
    		message=forms.CharField(max_length=500,help_text="message :",widget=forms.widgets.Textarea(attrs={'cols': 35, 'rows': 5}))
                created_date_time=forms.DateTimeField(
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now)
                overdue_date_time=forms.DateTimeField(
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now)
                closed_date_time=forms.DateTimeField(
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now)
                status=forms.IntegerField(
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=0)
                reopened_date_time=forms.DateTimeField(
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now)
                topic_priority=forms.IntegerField(
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=2)
                duration_for_reply=forms.IntegerField(
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=24)
		
    		class Meta:
			model=Ticket
			fields=('tab_id','user_id','topic_id','message')   		           
                                
                def clean_topic_id(self):
                                category = Category.objects.get(category=self.cleaned_data['topic_id'])
                                return category
		def __init__(self,*args,**kwargs):
		    user_details = kwargs.pop("user_details")     # client is the parameter passed from views.py
		    super(SubmitTicketForm, self).__init__(*args,**kwargs)
		    self.fields['user_id'] = forms.EmailField(help_text="Enter your email  id:",
widget=forms.TextInput(attrs={'readonly':'readonly','value':user_details}))
		def clean(self):
        		cleaned_data = self.cleaned_data
        		entered_tab_id = int(cleaned_data.get('tab_id'))        		
			tablets=Tablet_info.objects.all()
			found=0
			for tablet in tablets:
				starttab=tablet.start_tab_id
				endtab=tablet.end_tab_id
				print starttab
				if starttab<=entered_tab_id<=endtab:
					found=1;
			if found==0:
				raise forms.ValidationError("You have entered an invalid tablet id")
			else:
        			return cleaned_data
