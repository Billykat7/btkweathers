
def input_get_input(request):

    _i = request.GET

    i = {

        'city'          :   _i.get('city'),
        'period_start'  :   _i.get('period_start'),
        'period_end'    :   _i.get('period_end'),
        'search_city'   :   _i.get('search_city'),

    }

    return i
