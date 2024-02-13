from .models import Test


class CRUDOperation:

    def create_op(dt, trade, coll_names, data):
        insert_data = Test.objects.filter(date=dt, trade_code=trade).create(
            coll_names=data
        )
        if insert_data:
            print("Row Created | Create Done")

        return "Created"

    def update_op(dt, trade, col_names, data):
        update_data = Test.objects.filter(date=dt, trade_code=trade).update(
            col_names=data
        )

        if update_data:
            print("Row Updated | Update Done")

        return "updated"

    def delete_op(dt, trade, col_names, data):
        delete_data = Test.objects.filter(date=dt, trade_code=trade).delete()

        if delete_data:
            print("Row Deleted | Delete Done")

        return "deleted"
    
    
    
