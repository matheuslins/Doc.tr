from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
from django.core.mail import send_mail
from core.utils import generate_hash_key
from django.conf import settings
from core.mail import send_mail_template


User = get_user_model()

class PasswordResetForm(forms.Form):

	email = forms.EmailField(label = 'Email')

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email = email).exists():
			return email
		raise forms.ValidationError(
			'Nenhum usuario encontrado com este e-mail'
		)
	def save(self):
		user = User.objects.get(email = self.cleaned_data['email'])
		key = generate_hash_key(user.email)
		reset = PasswordReset(key = key, user = user)
		reset.save()
		template_name = 'password_reset_mail.html'
		subject = 'Recuperar senha do Doc Tr.'
		contexto = {
			'reset': reset,
		}
		send_mail_template(subject, template_name,contexto,[user.email])


class RegisterForm(forms.ModelForm):

	password1 = forms.CharField(label = 'Senha', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirmação de Senha', widget = forms.PasswordInput)

	MIN_LENGTH = 8

	def clean_password1(self):
		password1 = self.cleaned_data.get('password1')

		# At least MIN_LENGTH long
		if len(password1) < self.MIN_LENGTH:
			raise forms.ValidationError("A senha deve ter %d caracteres no mínimo." % self.MIN_LENGTH)

		# At least one letter and one non-letter
		first_isalpha = password1[0].isalpha()
		if all(c.isalpha() == first_isalpha for c in password1):
			raise forms.ValidationError("A senha deve conter pelo menos uma letra e pelo menos um dígito ou "\
										"um caractere de pontuação.")

		# ... any other validation you want ...

		return password1

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('A confirmmação de senha está incorreta')
		return password2

	def save(self, commit = True):
		user = super(RegisterForm,self).save(commit = False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError('Já existe usuário com este E-mail, tente novamente')
		return email

class RegisterForm_Doctor(RegisterForm):

	class Meta:
		model = Doctor
		fields = ['name', 'email','phone', 'username','crm']

class RegisterForm_Patient(RegisterForm):

	class Meta:
		model = Patient
		fields = ['name', 'email','phone', 'username','blood_type','clinical_condition','medicine','allergy','weight','height','address','sex','birth_data']   
		#fields = '__all__'

class EditAccountForm_Doctor(forms.ModelForm):

	class Meta:
		model = Doctor
		fields = ['name', 'email','phone', 'username','crm', 'username', 'birth_data', 'sex']


class EditAccountForm_Patient(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ['name', 'email','phone', 'username','blood_type','allergy','weight','height','address','sex','birth_data']   





