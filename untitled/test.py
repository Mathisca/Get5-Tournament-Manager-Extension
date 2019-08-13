openid_signed = request.GET.get('openid.signed').split(',')

for item in openid_signed:
    itemArg = 'openid.{0}'.format(item)
    if request.GET.get(itemArg) not in postArgs:
        postArgs[itemArg] = request.GET.get(itemArg)
