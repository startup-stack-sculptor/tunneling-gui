from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError

class StaticIpForm(FlaskForm):
    ip_address = StringField('IP Address', validators=[InputRequired(), IPAddress()])
    subnet_mask= StringField('Subnet Mask', validators=[InputRequired()])
    gateway = StringField('Gateway', validators=[InputRequired()])

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    password_again = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])

class TunnelForm(FlaskForm):
    tunnel_type = RadioField('Tunnel Type', choices=[('normal','Normal'),('bridge','Bridge')], default='normal')
    server_port_type = RadioField('', choices=[('tcp','TCP'),('udp','UDP')], default='tcp')
    client_port_type = RadioField('', choices=[('tcp','TCP'),('udp','UDP')], default='tcp')
    server_subnet_1 = StringField('', validators=[InputRequired()])
    server_subnet_2 = StringField('', validators=[InputRequired()])
    client_subnet_1 = StringField('', validators=[InputRequired()])
    client_subnet_2 = StringField('', validators=[InputRequired()])
    mdns = BooleanField('Enable MDNS (Avahi Daemon)')
    pimd = BooleanField('Enable PIMD (Multicast Routing)')