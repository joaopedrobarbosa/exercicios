module.exports = app => {
    app.get('/atendimentos', (req, res) => res.send('Rota de atendimento'));
    app.post('/atendimentos', (req, res) => res.send('Rota de POST'));
}