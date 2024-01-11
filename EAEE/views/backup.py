from django.shortcuts import HttpResponse
from EAEE.models import PacienteModel, TipoDeVinculoComPacienteModels, RegistroFinanceiroModel
from django.http import JsonResponse
import json
from datetime import datetime


def armazenar(request, ):
    body = {"paciente": [{"id": 1, "paciente_nome": "Francisco", "paciente_foto": "", "paciente_dt_nascimento": "2024-01-11", "paciente_identidade": "", "paciente_exame": "", "paciente_exame_2": "", "paciente_exame_3": "", "paciente_dt_inscricao": "2024-01-11T12:29:25Z"}], "responsavel": [{"id": 1, "paciente_filiacao_nome": "Francisco Jos\u00e9 de Oliveira Du\u00f3", "paciente_filiacao_tipo_vinculo": "Pai", "paciente_filiacao_email": "francisco.duo2000@gmail.com", "paciente_filiacao_dt_nascimento": '', "paciente_filiacao_contato_telefone_pessoal": "61985829628",
                                                                                                                                                                                                                                                                                                   "paciente_filiacao_contato_telefone_empresa": '', "paciente_filiacao_cpf": '', "paciente_filiacao_nacionalidade": '', "paciente_filiacao_profissao": '', "paciente_filiacao_estado_civil": "DF", "paceinte_filiacao_endereco": "Quadra QR 401 Conjunto 9", "paceinte_filiacao_cep": "Quadra QR 401 Conjunto 9", "paceinte_filiacao_comprovante_residencia": ""}], "financeiro": [{"id": 1, "registro_financeiro_funcionario_id": 1, "registro_financeiro_valor": "200", "registro_financeiro_destino": "sistema", "registro_financeiro_tipo_id": 1, "registro_financeiro_dt": "2024-01-11T12:29:53Z", "data_filtro": "2024-01-11"}]}
    dados_json = body

    # Extrair dados do dicionário
    pacientes = dados_json.get('paciente', [])
    responsaveis = dados_json.get('responsavel', [])
    financeiros = dados_json.get('financeiro', [])

    # Armazenar dados no modelo Paciente
    for paciente_data in pacientes:
        PacienteModel.objects.create(
            paciente_nome=paciente_data.get('paciente_nome', ''),
            paciente_foto=paciente_data.get('paciente_foto', ''),
            paciente_dt_nascimento=datetime.strptime(
                paciente_data.get('paciente_dt_nascimento'), '%Y-%m-%d'),
            # Adicione outros campos conforme necessário
        )

    # Armazenar dados no modelo Responsavel
    for responsavel_data in responsaveis:

        TipoDeVinculoComPacienteModels.objects.create(
            paciente_filiacao_nome=responsavel_data.get(
                'paciente_filiacao_nome', ''),
            paciente_filiacao_tipo_vinculo=responsavel_data.get(
                'paciente_filiacao_tipo_vinculo', ''),
            # Adicione outros campos conforme necessário
        )

    # Armazenar dados no modelo Financeiro
    for financeiro_data in financeiros:
        RegistroFinanceiroModel.objects.create(
            registro_financeiro_funcionario_id=financeiro_data.get(
                'registro_financeiro_funcionario_id', None),
            registro_financeiro_valor=financeiro_data.get(
                'registro_financeiro_valor', ''),
            registro_financeiro_destino=financeiro_data.get(
                'registro_financeiro_destino', ''),
            registro_financeiro_tipo_id=financeiro_data.get(
                'registro_financeiro_tipo_id', ''),
            registro_financeiro_dt=datetime.strptime(financeiro_data.get(
                'registro_financeiro_dt'), '%Y-%m-%dT%H:%M:%SZ'),
            data_filtro=datetime.strptime(
                financeiro_data.get('data_filtro'), '%Y-%m-%d'),
            # Adicione outros campos conforme necessário
        )

    return HttpResponse("Dados armazenados com sucesso!")


def pacientes_e_responsaveis(request, ):
    paciente = list(PacienteModel.objects.values())
    responsavel = list(TipoDeVinculoComPacienteModels.objects.values())
    financeiro = list(RegistroFinanceiroModel.objects.values())

    return JsonResponse({'paciente': paciente, 'responsavel': responsavel, 'financeiro': financeiro})
