from app.models import SavingAccount

def sample():
    res = SavingAccount.objects.last()
    print(res)

sample()
