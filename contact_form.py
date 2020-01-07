from flask import Flask, render_template, flash, request
import json2html
from flask import jsonify
from flask_sslify import SSLify

from json2html import *
import json2table
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
DEBUG = True
app = Flask(__name__)
sslify = SSLify(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

@app.route("/submitFormDetails", methods=['GET', 'POST'])
def getFormDetails():
    json_data = request.get_json()
    print(json_data)
    print(type(json_data))
    send_email(json_data)
    resp = jsonify(success=True)
    return resp
    #return render_template('index.html')

@app.route("/sendemail", methods=['GET', 'POST'])
def send_email(data):
    # Python code to illustrate Sending mail with attachments
    # from your Gmail account

    # libraries to be imported
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import json

    fromaddr = 'analtix12@gmail.com'
    toaddr = "analtix12@gmail.com"
    toaddr = "hemachandra.s17@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Loan Eligibility"

    # string to store the body of the mail
    #data = {'firstname': 'Prasanna', 'lastname': 'Balakrishnan', 'email_id': 'balan.prasanna22%40gmail.com', 'mob_no': '07760464722', 'pan_card': '242324', 'selectedBusinessType': 'a) Self employment', 'annual_income': '12 - 30 Lacs'}

    print("Print Json DAta")
    print(data)
    print(type(data))
    print("Inside Send email 12345")
    body = "content to store the json file"
    #data_processed = json_data
    data_processed = json.dumps(data)
    print(type(data_processed))
    print(data_processed)

    formatted_table = json2html.convert(json=data)
    print(formatted_table)
    #body = json_data.to_html()
    #print("Goig to print body "+formatted_table)

    # attach the body with the msg instance
    part2 = MIMEText(formatted_table, 'html')
    msg.attach(part2)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("analtix12@gmail.com", "Halo123@06")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))
