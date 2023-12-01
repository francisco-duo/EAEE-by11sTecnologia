from django.db import models


class PacienteRegistroModel(models.Model):
    """
        paciente_registro_paciente: ForeignKey Paciente
        paciente_registro_queixa: TextField
        paciente_registro_historico: ForeignKey Exame
        paciente_registro_procedimento_avaliativo: TextField
        paciente_registro_observacao_clinica: TextField
        paciente_registro_resultado: TextField
        paciente_registro_conclusao: TextField
    """
    