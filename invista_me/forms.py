from django.forms import ModelForm
from .models import Investimento


# Para fazer uma model form 
class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'