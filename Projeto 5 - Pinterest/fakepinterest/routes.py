from flask import render_template, url_for, redirect
from fakepinterest import app
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormCriarConta, FormLogin, FormFoto
from fakepinterest.models import User, Foto
from fakepinterest import app, database, bcrypt
import os 
from werkzeug.utils import secure_filename

@app.route('/', methods=['POST', 'GET'])
def home():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario=User.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('home.html', form=form_login)


@app.route('/criarconta', methods=['POST', 'GET'])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha_crypt = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8')
        usuario = User(email=form_criarconta.email.data, senha=senha_crypt, username=form_criarconta.username.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario , remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criar_conta.html', form=form_criarconta)


@app.route('/perfil/<id_usuario>', methods=['POST', 'GET'])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            print(nome_seguro)
            caminho_arquivo = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], nome_seguro)
            try:
                arquivo.save(caminho_arquivo)
            except Exception as e:
                print(f"Erro ao salvar o arquivo {e}")


            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()

        return render_template('perfil.html', usuario=current_user, form=form_foto)

    else:
        usuario = User.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)

@app.route('/logout')
def logout():
    logout_user(current_user)
    return redirect(url_for('home'))

@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao).all()
    return render_template('feed.html', fotos=fotos)