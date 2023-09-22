const customExpress = require('./config/customExpress');
const conexao = require('./config/conexao');
const tabelas = require('./model/tabelas');

conexao.connect(erro => {
    if(erro){
        console.log(erro);
    }else {
        console.log('Consexão realizada com sucesso!');
        tabelas.init(conexao);
    }
});

const app = customExpress();

app.listen(3000, () => console.log('Servidor rodando na porta 3000'))
app.get('/', (req, res) => res.send('Servidor rodando, tudo ok'));