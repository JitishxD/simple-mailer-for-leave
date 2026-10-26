"""Mail format. Change the wording here only."""

from config import SUBJECT_TEMPLATE

BODY_TEMPLATE = """Respected sir,
Please ignore any previous mail

Name : {name}
Register Number: {register_number}
Mobile Number of Student: {student_mobile}

Place of visit - {place}
Date and time of departure - {departure_date}, {departure_time}
Date and time of Arrival - {arrival_date}, {arrival_time}
Father’s Name :  {father_name}
Mobile Number of parent : {parent_mobile}
Address : {address}

Reason: {reason}

Thanks & Regards
{name}
"""


def build_subject(data: dict) -> str:
    return SUBJECT_TEMPLATE.format(**data)


def build_body(data: dict) -> str:
    return BODY_TEMPLATE.format(**data)
