from django import forms
from .models import Divulgacao, Setor, HorarioSetor, Refeicao

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        kwargs.setdefault("required", False)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class DivulgacaoForm(forms.ModelForm):
    imagem_da_divulgacao = MultipleFileField()
    
    class Meta:
        model = Divulgacao
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['autor'].required=False
        self.fields['autor'].widget = forms.HiddenInput()
        
class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class HorarioSetorForm(forms.ModelForm):
    class Meta:
        model = HorarioSetor
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['horario_inicio'].widget.attrs.update({'class': 'form-control mask-time'})
        self.fields['horario_fim'].widget.attrs.update({'class': 'form-control mask-time'})

class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['horario_inicio'].widget.attrs.update({'class': 'form-control mask-time'})
        self.fields['horario_fim'].widget.attrs.update({'class': 'form-control mask-time'})
        self.fields['data'].widget.attrs.update({'class': 'form-control mask-date', 'placeholder': 'DD/MM/AA'})