
def account_delete_mark(deletion):
    deletion.user.is_active = False
    deletion.user.save()


def account_delete_expunge(deletion):
    deletion.user.delete()
    deletion.user = None
