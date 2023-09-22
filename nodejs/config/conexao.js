const mysql = require('mysql');

const conexao = mysql.createConnection({
    host: 'localhost',
    port: 3306,
    user: 'usuario',
    password: '123456',
    database: 'banco_dados'
});

module.exports = conexao;