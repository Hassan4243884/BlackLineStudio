import csv

from django import forms
from django.contrib import admin
from django.http import HttpResponse

from contact.models import Form, Recipient, History, BlacklistItem, Subscriber, RegistrationCompleteEvent


class RecipientForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)
        self.fields['id'].value = self.instance.id

    class Meta:
        model = Recipient
        fields = '__all__'


class RecipientAdmin(admin.TabularInline):
    model = Recipient
    extra = 1
    form = RecipientForm


class FormAdminForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'


class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_subject')
    inlines = (RecipientAdmin, )
    form = FormAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        x = super(FormAdmin, self).formfield_for_dbfield(db_field,**kwargs)
        if db_field.name == 'name':
            x.help_text = 'Internal identifier. Do not change it!'
        elif db_field.name == 'sender':
            x.help_text = 'Default sender.'
        elif db_field.name == 'sender_field':
            x.help_text = 'Use visitor\'s e-mail as sender. Usually this field is called "email".'
        elif db_field.name == 'email_text':
            x.widget.attrs.update({
                'style': 'width:700px; height:300px;',
                'class': 'redactor'
            })
        return x

admin.site.register(Form, FormAdmin)


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('created', 'ip', 'form', 'sent')
    list_filter = ('form', 'seed', 'sent')
    date_hierarchy = 'created'
admin.site.register(History, HistoryAdmin)


class BlacklistItemForm(forms.ModelForm):
    class Meta:
        model = BlacklistItem
        fields = '__all__'

    def clean_ip(self):
        ip = self.cleaned_data['ip']
        l = ip.split('.')
        if len(l) != 4:
            raise forms.ValidationError('IP address has an invalid format.')
        ip = []
        for n in l:
            n = int(n)
            if n < 0 or n > 255:
                raise forms.ValidationError('IP address has an invalid format.')
            ip.append(str(n))
        return '.'.join(ip)


class BlacklistItemAdmin(admin.ModelAdmin):
    form = BlacklistItemForm
    list_display = ('ip', 'comment')


admin.site.register(BlacklistItem, BlacklistItemAdmin)


def export_csv(modeladmin, request, queryset):
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=email.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"email"),
    ])
    for obj in Subscriber.objects.all():
        if not obj.export:
            writer.writerow([smart_str(obj.email), ])
            obj.export =True
            obj.save()
    return response


export_csv.short_description = u"Export CSV"


class SubscriberBlogAdmin(admin.ModelAdmin):
    list_display = ['email', 'export']
    actions = [export_csv, ]

# admin.site.register(Subscriber, SubscriberBlogAdmin)


@admin.register(RegistrationCompleteEvent)
class RegistrationCompleteEventAdmin(admin.ModelAdmin):
    change_list_template = 'admin/registered_change_list.html'
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        response.context_data['summary'] = len(qs)

        return response
