from .models import Member
from .forms import MemberForm

# context available in all templates
def site_defaults(request):
    add_member_form = MemberForm()
    contexts = {
        'add_member_form':add_member_form,
    }
    return contexts