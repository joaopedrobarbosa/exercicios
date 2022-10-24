horas_extra = '';
while horas_extra != 0:
    nome = input('Qual é o nome do funcionario? ');
    salario = float(input('Qual é o salário do funcionario? '));
    horas_trabalhadas = float(input('Quantas horas o funcionario trabalhou? '));
    salario_hora = salario/40;

    horas_extra = 0;
    if horas_trabalhadas > 40.0:
        horas_extra = horas_trabalhadas - 40;

    salario = salario + ((salario_hora*1.5) * horas_extra)

    print(f"{nome} deve receber R$ {salario}")