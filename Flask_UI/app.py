from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

class MyForm(FlaskForm):
    defaul_value = "@TestAutobot rias"
    snapshot_path = "tests/qa/cpap/rias/storage/tests/snapshots/RIAS_CreateSnapshotsTests.py"
    testselects = SelectField('Select test to run', choices=[('tests/qa/cpap/rias/storage/tests/snapshots/RIAS_ConcurrentSnapshotTest.py', 'tests/qa/cpap/rias/storage/tests/snapshots/RIAS_ConcurrentSnapshotTest.py'),
                                                   ('tests/qa/cpap/rias/storage/tests/snapshots/RIAS_CreateLargeSnapshotTest.py', 'tests/qa/cpap/rias/storage/tests/snapshots/RIAS_CreateLargeSnapshotTest.py'),
                                                   ('tests/qa/cpap/suites/rias_snapshots.ini', 'tests/qa/cpap/suites/rias_snapshots.ini')])
    repo = "repo:integration-testing"
    tabfield = StringField('@TestAutobot', validators=[InputRequired()])
    authuser = StringField('auth-user', validators=[InputRequired()])
    textarea = TextAreaField('Textarea')
    radios = RadioField('testtype', default='test-config-path:',
                        choices=[('test-config-path:', 'test-config-path'), ('test-path:', 'test-path')])
    saveartifacts = RadioField('saveartifacts', default='Yes',
                        choices=[('Yes', 'Yes'), ('No', 'No')])
    selects = SelectField('Select mzone', choices=[('us-south-genesis-dal-dev45-etcd.iaasdev.cloud.ibm.com', 'dev45'), ('us-south-stage01.iaasdev.cloud.ibm.com', 'staging'), ('us-south-genesis-dal-dev40-etcd.iaasdev.cloud.ibm.com', '7124')])

@app.route('/', methods=['GET', 'POST'])
def form():
    form = MyForm()

    if form.validate_on_submit():
        if form.saveartifacts.data == 'Yes':
            saveartifacts = "save-artifacts"
        else:
            saveartifacts = " "
        fianl_command = form.defaul_value+" "+form.selects.data+" "+form.repo+" "+form.radios.data+form.testselects.data+" auth-user:"+form.authuser.data+" report-es nodirectreport "+ saveartifacts
        print(fianl_command)
        return render_template('results.html', tabfield=form.tabfield.data, authuser=form.authuser.data, saveartifacts=saveartifacts, radios=form.radios.data, selects=form.selects.data, testselects=form.testselects.data,
                               defaul_value=form.defaul_value, test_path=form.snapshot_path, repos=form.repo)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)