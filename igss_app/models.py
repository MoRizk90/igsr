from django.db import models

# Create your models here.


class IgsrUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    user_email = models.CharField(max_length=250)
    Dept_id = models.ForeignKey('Deparments',on_delete=models.CASCADE)
    user_type = models.ForeignKey('Users_type',on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name


class MeetingAgenda(models.Model):
    Agenda_Id = models.AutoField(primary_key=True)
    Agenda_date = models.DateField(auto_now=False, auto_now_add=False)
    agenda_title = models.CharField(max_length=250)
    creator = models.ForeignKey('IgsrUser',on_delete=models.CASCADE)
    agenda_state_Id = models.ForeignKey('Agenda_State',on_delete=models.CASCADE)
    Dept_id = models.ForeignKey('Deparments',on_delete=models.CASCADE)
    # item_id = models.ForeignKey('Items', default='1', on_delete=models.CASCADE)

    def __str__(self):
        return self.agenda_title


class Users_type(models.Model):
    Type_Id = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=250)

    def __str__(self):
        return self.Type


class Deparments(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_type = models.CharField(max_length=250)

    def __str__(self):
        return self.dept_type


class Agenda_State(models.Model):
    State_id = models.AutoField(primary_key=True)
    State_type = models.CharField(max_length=250)

    def __str__(self):
        return self.State_type


class Items(models.Model):
    Item_id = models.AutoField(primary_key=True)
    Agenda_id = models.ForeignKey('MeetingAgenda',on_delete=models.CASCADE)
    Item_title = models.CharField(max_length=100)
    Item_subject = models.CharField(max_length=250)
    Item_action_id = models.ForeignKey('Actions', on_delete=models.CASCADE)

    def __str__(self):
        return self.Item_title


class Actions(models.Model):
    action_id = models.AutoField(primary_key=True)
    actions = models.CharField(max_length=100)

    def __str__(self):
        return self.actions



