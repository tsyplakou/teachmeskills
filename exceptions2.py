
class PermissionError(Exception):
    pass


# Мы можем создавать ошибки, но только во благо...
def delete_record_in_db(record_id, current_user_role):
    if current_user_role != 'admin':
        # return 'Only admin can delete the record'
        raise PermissionError('Only admin can delete the record')

    # ...

ValueError


def remove_all_records_in_db(current_user_role):
    for record in db_records:
        delete_record_in_db(record_id, current_user_role)



def remove_all():
    try:
        remove_all_records_in_db()
    except (ValueError, TypeError) as e:
        print(str(e))
    except PermissionError as e:
        return Response(str(e), 403)
    else:
        print('All records deleted')
    finally:
        print('All records deleted')



print('Hello world!')
raise ValueError('Invalid value')
print('Hello world!'*2)
