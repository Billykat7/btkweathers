
def input_get_input(request):

    _i = request.GET

    i = {

        'city'          :   _i.get('city'),
        'period_start'  :   _i.get('period_start'),
        'period_end'    :   _i.get('period_end'),

    }

    return i
