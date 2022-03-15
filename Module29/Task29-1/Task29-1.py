class PermissionError(BaseException):
    pass


def check_permission(name):
    def dec(func):
        def wrapped(*arg, **kwarg):
            try:
                if name in user_permissions:
                    func()
                else:
                    raise PermissionError
            except PermissionError:
                print('{error}: У пользователя недостаточно прав, чтобы выполнить функцию add_comment'.format(
                    error=PermissionError.__name__
                ))
            return

        return wrapped
    return dec

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


user_permissions = ['admin']
delete_site()
add_comment()