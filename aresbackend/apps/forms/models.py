from django.db import models

# Create your models here.

class BudgetForm(models.Model):

    WHATSAPP = 0
    EMAIL = 1

    RETURN_WAYS = (
        (WHATSAPP, "WhatsApp"),
        (EMAIL, "E-mail"),
    )

    INSTALLATIONS = 0
    STRUCTURED_CABLING = 1
    HOME_AUTOMATION = 2
    SPDA = 3
    GROUP_MEASUREMENT = 4

    SERVICES = (
        (INSTALLATIONS, "Instalações Elétricas Residenciais e Prediais"),
        (STRUCTURED_CABLING, "Infraestrutura de Cabeamento Estruturado"),
        (HOME_AUTOMATION, "Automação Residencial"),
        (SPDA, "SPDA"),
        (GROUP_MEASUREMENT, "Medição Agrupada"),
    )

    first_name = models.CharField("Primeiro nome", max_length=50)
    last_name = models.CharField("Sobrenome", max_length=100)
    last_name = models.CharField("Sobrenome", max_length=100)
    cpf = models.CharField("CPF", max_length=11)
    phone = models.CharField("Celular", max_length=11)
    email = models.EmailField()
    description = models.CharField("Descrição", max_length=500)
    service = models.IntegerField("Serviço", choices=SERVICES)
    return_way = models.IntegerField("Forma de retorno", choices=RETURN_WAYS)

    class Meta:
      verbose_name = "Formulário de orçamento"
      verbose_name_plural = "Formulários de orçamentos"