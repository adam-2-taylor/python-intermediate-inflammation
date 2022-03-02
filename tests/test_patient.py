"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

###########################################
# Tests for doctor classes
# Doctor must have a name
def test_doctor_name():
    from inflammation.models import Doctor
    name = 'Hugh Montgomery'
    doc = Doctor('Hugh Montgomery')
    assert doc.name == name

# Doctor must have a list of patients
def test_doc_has_patients():
    from inflammation.models import Doctor, Patient
    pat = Patient('Alice')
    doc = Doctor('H Mont')
    doc.add_patient(pat)

    assert len(doc.patients) == 1

# Check doctor doesn't have duplicate patients
def test_doc_no_dup_pats():
    from inflammation.models import Doctor, Patient
    pat = Patient('Alice')
    doc = Doctor('H Mont')
    doc.add_patient(pat)
    doc.add_patient(pat)

    assert len(doc.patients) == 1