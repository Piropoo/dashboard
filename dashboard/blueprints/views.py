from flask import Blueprint, session, redirect, render_template, url_for, request, flash
from dashboard.ext.database import Usuario

bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    if 'usuario_logado' not in session:
        session['usuario_logado'] = False

    if not session['usuario_logado']:
        return redirect(url_for('views.login'))
    else:
        return redirect(url_for('views.dashboard'))


@bp.route('/login')
def login():
    if not session['usuario_logado']:
        return render_template('login.html', titulo_da_pagina='Dashboard - Login',
                               usuario_logado=session['usuario_logado'] or False,
                               stylesheets=['login.css'],
                               scripts=['validar_campos_form.js'])


def autenticar_login(login_digitado, password_digitado):

    users = Usuario.query.all()
    usuario = None

    usuario_existe = False
    if '@' in login_digitado:
        campo = 'email'
        for user in users:
            if login_digitado == user.email:
                usuario = user
                usuario_existe = True
    else:
        campo = 'username'
        for user in users:
            if login_digitado == user.username:
                usuario = user
                usuario_existe = True

    if usuario_existe:
        if password_digitado == usuario.password:
            senha_correta = True
        else:
            senha_correta = False
        if senha_correta:
            dados = {'nome': usuario.nome, 'logado': True}
            return dados
        else:
            dados = {'erro': 'A senha está incorreta.', 'logado': False}
            return dados

    else:
        if campo == 'email':
            dados = {'erro': 'Este email não está cadastrado.', 'logado': False}
            return dados
        elif campo == 'username':
            dados = {'erro': 'Este usuário não está cadastrado.', 'logado': False}
            return dados


@bp.route('/autenticar', methods=['POST'])
def autenticar():
    login_digitado = request.form['login'].strip().lower()
    password_digitado = request.form['senha']

    dados = autenticar_login(login_digitado, password_digitado)

    logado = dados['logado']

    if logado:
        session['usuario_logado'] = True
        session['nome'] = dados['nome']
    else:
        flash(dados['erro'])

    return redirect(url_for('views.index'))


@bp.route('/dashboard')
def dashboard():
    primeiro_nome = session['nome'].split()[0]
    return render_template('dashboard.html', nome=primeiro_nome, usuario_logado=session['usuario_logado'],
                           stylesheets=['dashboard.css'])


@bp.route('/logout')
def logout():
    session['usuario_logado'] = False
    return redirect(url_for('views.index'))


def init_app(app):
    app.register_blueprint(bp)
