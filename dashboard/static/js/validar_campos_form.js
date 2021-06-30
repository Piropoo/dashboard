form = document.querySelector('form')
botao = form.querySelector('button')

botao.addEventListener('click', (event) => {

    erro_login = form.querySelector('[data-erro-login]')
    erro_senha = form.querySelector('[data-erro-senha]')

    login_digitado = form.querySelector('[data-form-login]').value.trim()
    password_digitado = form.querySelector('[data-form-senha]').value

    erro_login.textContent = ''
    erro_senha.textContent = ''

    if (login_digitado.length == 0){
        
        erro_login.textContent = 'O login não pode estar em branco.'

        event.preventDefault()

    }else{

        eh_email = false
        numero_de_arrobas = 0
        tem_ponto = false
        tem_espaco = false

        login_digitado.split('').forEach((letra) => {
            if (letra == '@'){
                eh_email = true
                numero_de_arrobas += 1
            }
            if (letra == '.'){
                tem_ponto = true
            }
            if (letra == ' '){
                tem_espaco = true
            }
        })
        if (tem_espaco){

            erro_login.textContent = 'O usuário não pode conter espaços.' 

        }else{
            if (eh_email && !(tem_ponto) || login_digitado.split('')[0] == '@' || 
            login_digitado.split('')[0] == '.' || login_digitado.split('')[-1] == '@'
            || login_digitado.split('')[-1] == '.' || numero_de_arrobas > 1){

                erro_login.textContent = 'Insira um email válido.'

                event.preventDefault()

            }
            if(!(eh_email)){

                if (login_digitado.length < 6){

                    erro_login.textContent = 'Insira um usuário válido.'

                    event.preventDefault()

                }

            }
        }

    }

    if (password_digitado.length == 0){

        erro_senha.textContent = 'A senha não pode estar em branco.'

        event.preventDefault()

    }


})