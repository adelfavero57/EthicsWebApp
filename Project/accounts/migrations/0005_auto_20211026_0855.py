# Generated by Django 3.2.7 on 2021-10-26 08:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_merge_20211026_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='PCF_rt',
            field=ckeditor.fields.RichTextField(blank=True, default='<p>Project Name:</p>\n\n<p>In giving my consent I acknowledge that:</p>\n\n<p>1. The procedures required for the project and the time involved have been explained to me, and any questions I have about the project have been answered to my satisfaction.</p>\n\n<p>2. I have read the Participant Information Statement and have been given the opportunity to discuss the information and my involvement in the project with the researcher/s.</p>\n\n<p>3. I understand that being in this study is completely voluntary - I am not under any obligation to consent.</p>\n\n<p>4. I understand that my involvement is strictly confidential. I understand that any research data gathered from the results of the study may be published however no information about me will be used in any way that is identifiable</p>\n\n<p>5. I understand that I can withdraw from the study at any time, without affecting my relationship with the researcher(s) or the University of Sydney now or in the future.</p>\n\n<p>6. I understand that I will be video and audio recorded as well as my screen interaction.</p>\n\n<p>7. I understand that this is the first time participating in this study.</p>\n\n<p>8. I agree that my rtecord of all clicks in my interaction on this interface will be shared on the Open Science Framework (OSF) platform so that other researchers can analyse them. This data will be de-identified so that it cannot be linked to me.</p>\n\n<p>9. I understand that my video and audio recordings will only be used for analysis and will not be released.</p>\n', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='PIS_rt',
            field=ckeditor.fields.RichTextField(blank=True, default='<p>Project Name:</p>\n\n<p>What is the study about?</p>\n\n<p>The following are important for the validity of the study:</p>\n\n<p>Who is carrying out the study?</p>\n\n<p>What does the study involve?</p>\n\n<p>How much time will the study take?</p>\n\n<p>Can I withdraw from the study?</p>\n\n<p>Will the study benefit me?</p>\n\n<p>How my data will be stored and my privacy preserved?</p>\n\n<p>Can I tell other people about the study?</p>\n\n<p>What if I require further information about the study or my involvement in it?</p>\n\n<p>What if I have a complaint or any concerns?</p>\n\n', null=True),
        ),
    ]
