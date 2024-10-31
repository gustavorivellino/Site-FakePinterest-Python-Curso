from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, FileField
from wtforms.validators import Email, Length, DataRequired, EqualTo
from fakepinterest.models import User



class FormLogin(FlaskForm):
    email = StringField('E-mail de Usuário', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha de Usário', validators=[DataRequired(), Length(6,20)])
    botao_submit_login = SubmitField('Fazer Login')

    def validate_email(self, email):
        usuario = User.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário inexistente, crie uma conta !')
        
    def validate_senha(self, senha):
        usuario = User.query.filter_by(senha=senha.data).first()
        if not usuario:
            raise ValidationError('Senha Incorreta, tente novamente !')


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail de Usuário', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha de Usuário', validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField('Confirme sua Senha', validators=[DataRequired(), Length(6,20),EqualTo('senha')])
    botão_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = User.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado, faça login para continuar !')
        
        
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_submit_foto = SubmitField('Enviar Foto')