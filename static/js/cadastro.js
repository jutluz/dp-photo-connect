$(function() { 

    $(document).on("click", "#bt-enviar", function() {
  
        nome = $("#nome").val();
        email = $("#email").val();
        senha = $("#password").val();
        console.log(nome, email, senha);

        var dados = JSON.stringify({ nome: nome, email: email, senha: senha });

        $.ajax({
            url: 'http://localhost:5000/incluir_pessoa',
            type: 'POST',
            dataType: 'json', 
            contentType: 'application/json', 
            data: dados, 
            success: pessoaIncluida, 
            error: erroAoIncluir
        });
        function pessoaIncluida (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Cadastro realizado com sucesso!");
                $("#nome").val("");
                $("#email").val("");
                $("#password").val("");
                window.location.assign("login.html");
            } else {
                alert("Erro na inclusão: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            console.log("Não deixe nenhum campo em branco!")
            alert("Erro ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

});