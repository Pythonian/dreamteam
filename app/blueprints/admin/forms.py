from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

from app.models import Department, Role


class DepartmentForm(FlaskForm):
    """
    For for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = SelectField('Department', coerce=int)
    role = SelectField('Role', coerce=int)
    submit = SubmitField('Submit')

    def __init__(self, employee, *args, **kwargs):
        super(EmployeeAssignForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.department.choices = [(department.id, department.name)
                                   for department in Department.query.order_by(
                                       Department.name).all()]
        self.employee = employee
