import re
import sys
entrada = input('CPF [746.824.890-70]:')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print("você enviou dados sequencias")
    sys.exit()
cpfUltimoDigito_1 = cpf[-2]

cpf_para_calculo = cpf[:9]

resultado_digito_1 = 0
contador_regressivo_1 = 10
for digito in cpf_para_calculo:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

if digito_1 == int(cpfUltimoDigito_1):
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    cpfParaCalc_2 = cpf[:10]
    for digito_2 in cpfParaCalc_2:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_novo_gerado = f'{cpf_para_calculo}{digito_1}{digito_2}'
if cpf == cpf_novo_gerado:
    print(f'{entrada} é válido')
else:
    print(f'{entrada} é inválido')
