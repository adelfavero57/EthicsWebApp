from accounts.models import Application, User, Answers, Question

test = User(username="exemplar", password="=g8CUu-^")
test.save()

app = Application(id=1, title="Exemplar", user=test,
                  supervisor="test", status="COMPLETED")
app.save()


Answers.objects.bulk_create([
    # 601
    Answers(id=1, short_answer_text="""Many participants will be first year University of Sydney psychology students who volunteer to participate by registering on the SONA system. Students will receive partial course credit in exchange for their participation in the initial part of the study. SONA participants can consent to participating in two follow-up portions of the study, one month and six months after the initial study, though they can participate in the initial study without consenting to the follow-up portions. If they consent to participating in the follow-up portions of the study one month and six months after the initial study or if they request for overall feedback for the study, university emails will be collected as a means of contact.
We will also advertise our study on career and recruiting websites. These participants will see a description of the purpose and methodology of the study and they can choose to sign up to an appointment or will be provided with a web link where they will be provided with an information statement and opportunity to consent to participate if they choose to. Participants from the community can also consent to participating in two follow-up portions of the study, one month and six months after the initial study, though they can participate in the initial study without consenting to the follow-up portions.""", question_id=Question.objects.filter(question_num=601)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),
    Answers(id=2, short_answer_text="""Selection of participants will be on condition that they are 18 years old or over.
Contact details will be obtained through the UoS coordinator for contacting undergraduate and postgraduate students via email. Potential participants will then be able to provide their contact details by responding to the recruitment email.""", question_id=Question.objects.filter(question_num=601)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),
    Answers(id=3, short_answer_text="""This study relates to the evaluation of software to give students feedback on their progress, so the potential participants will include students and members of the teaching team of courses who understand student feedback systems that are currently in place or the courses whose feedback is being provided.""", question_id=Question.objects.filter(question_num=601)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 602
    Answers(id=3, short_answer_text="""""", question_id=Question.objects.filter(question_num=602)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),
    Answers(id=3, short_answer_text="""""", question_id=Question.objects.filter(question_num=602)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),
    Answers(id=3, short_answer_text="""""", question_id=Question.objects.filter(question_num=602)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),
])
