usage = {"docs": 0, "reports": 0}

def charge_flexprice(item, count):
    usage[item] += count

def get_usage(item):
    return usage[item]
