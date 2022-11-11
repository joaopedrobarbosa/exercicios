module.exports = app => {
    app.get('/usuarios', (req, res) => res.send('Rota de usuarios'));
}