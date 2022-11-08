const express = require('express');

const app = express();

app.listen(3000, () => console.log('Servidor rodando na porta 3000'))
app.get('/', (req, res) => res.send('Servidor rodando, tudo ok'));
app.get('/atendimentos', (req, res) => res.send('Rotas de atendimento'));