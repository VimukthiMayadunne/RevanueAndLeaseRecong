def clear_buffer(data_buffer):

    data_buffer = data_buffer.replace('nan', '')
    data_buffer = data_buffer.replace('[', '')
    data_buffer = data_buffer.replace(']', '')
    data_buffer = data_buffer.replace("'", '')
    data_buffer = data_buffer.replace('[','')
    data_buffer = data_buffer.replace('.','. ')
    data_buffer = data_buffer.replace('LKR ','Rs.')
    data_buffer = data_buffer.replace('. 00','.00')
    data_buffer = data_buffer.replace('RSL ','RSL-')

    return data_buffer

