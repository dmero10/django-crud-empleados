from django.forms import ModelForm, DateInput, Select
from .models import Position, Employee


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'description']

    # Aplica clases de Bootstrap a cada campo automáticamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'salary', 'hire_date', 'position']
        widgets = {
            'hire_date': DateInput(attrs={'type': 'date'}),
            'position': Select(attrs={'class': 'form-select'}),
        }

    # Aplica clases de Bootstrap a cada campo automáticamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # El desplegable (position) usa 'form-select'; el resto 'form-control'
            if name != 'position':
                field.widget.attrs['class'] = 'form-control'
