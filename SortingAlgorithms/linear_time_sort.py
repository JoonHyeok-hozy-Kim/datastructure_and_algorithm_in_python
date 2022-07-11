def bucket_sort(S):
    max_key = None
    B = []

    for i in range(len(S)):
        e = S[i]
        if e < 0:
            raise ValueError('Key must be a positive integer.')
        S[i] = None

        if max_key is None:
            for j in range(e):
                B.append({
                    'key': j,
                    'value': [],
                })
                if e-1 == j:
                    B[j]['value'].append(e)
            max_key = e-1
        elif e-1 <= max_key:
            B[e-1]['value'].append(e)
        else:
            for j in range(max_key+1, e):
                B.append({
                    'key': j,
                    'value': [],
                })
                if e-1 == j:
                    B[j]['value'].append(e)
            max_key = e-1

    cnt = 0
    for bucket in B:
        if len(bucket['value']) > 0:
            for e in bucket['value']:
                S[cnt] = e
                cnt += 1

    return S

def radix_sort(S, num_keys=2):
    for i in range(num_keys):
        _bucket_sort_for_radix(S, num_keys-1-i)
    return S


def _bucket_sort_for_radix(S, key_idx):
    max_key = None
    B = []

    for i in range(len(S)):
        key_set = S[i]
        key = key_set[key_idx]
        if key < 0:
            raise ValueError('Key must be a positive integer.')
        S[i] = None

        if max_key is None:
            for j in range(key):
                B.append({
                    'key': j,
                    'value': [],
                })
                if key-1 == j:
                    B[j]['value'].append(key_set)
            max_key = key-1
        elif key-1 <= max_key:
            B[key-1]['value'].append(key_set)
        else:
            for j in range(max_key+1, key):
                B.append({
                    'key': j,
                    'value': [],
                })
                if key-1 == j:
                    B[j]['value'].append(key_set)
            max_key = key-1

    cnt = 0
    for bucket in B:
        if len(bucket['value']) > 0:
            for key_set in bucket['value']:
                S[cnt] = key_set
                cnt += 1

    return S