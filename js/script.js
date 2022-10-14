function submitForm(){
    var obj = {
        nome: document.getElementById('nome').value, 
        email: document.getElementById('email').value, 
        idade: document.getElementById('idade').value
    }

    console.log(obj)
}

function adicionar(){
    var texto = document.getElementById('texto');
    var para = document.createElement('p');
    para.innerHTML = texto.value;
    var corpo = document.getElementById('corpo');
    corpo.appendChild(para)
    texto.value = "";
}

function remover(){
    var pai = document.getElementById('div1');
    var filho = document.getElementById('elemnto1');
    pai.removeChild(filho);
}

function mudarCor(){
    if(document.getElementById('body').style.backgroundColor == 'blue')
        document.getElementById('body').style.backgroundColor = 'green';
    else
        document.getElementById('body').style.backgroundColor = 'blue';
}