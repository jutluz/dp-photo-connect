$(function() { 

    $(document).on("click", "#bt-enviar", function() {
  
        email = $("#email").val();
        senha = $("#password").val();
        console.log(email, senha);

        var dados = JSON.stringify({email: email, senha: senha });

        $.ajax({
            url: 'http://localhost:5000/login',
            type: 'POST',
            dataType: 'json', 
            contentType: 'application/json', 
            data: dados, 
            success: loginOK, 
            error: erroAoLogar
        });
        function loginOK (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Login OK!!!");
                window.location.assign("feed.html");
            } else {
                alert("ERRO no login: "+retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoLogar (retorno) {
            console.log("Erro")
            alert("Erro ao logar: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

});