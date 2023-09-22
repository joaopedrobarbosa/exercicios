const db = require("../config/conexao");

class Atendimento {
    adicionar(atendimento) {
        const sql = `INSERT INTO atendimentos(nome, servico, pet, status, observacoes) VALUES('${atendimento.nome}', '${atendimento.servico}', '${atendimento.pet}', '${atendimento.status}', '${atendimento.observacoes}')`;
        
        atendimento.status = "marcado";
        observacoes = "";

        db.run(sql);
    }
}

module.exports = new Atendimento();