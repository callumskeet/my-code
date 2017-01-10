# Alphabet
ab_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Swiss K model rotors
I_K = {'A': 'P', 'B': 'E', 'C': 'Z', 'D': 'U', 'E': 'O',
       'F': 'H', 'G': 'X', 'H': 'S', 'I': 'C', 'J': 'V',
       'K': 'F', 'L': 'M', 'M': 'T', 'N': 'B', 'O': 'G',
       'P': 'L', 'Q': 'R', 'R': 'I', 'S': 'N', 'T': 'Q',
       'U': 'J', 'V': 'W', 'W': 'A', 'X': 'Y', 'Y': 'D',
       'Z': 'K'}

II_K = {'A': 'Z', 'B': 'O', 'C': 'U', 'D': 'E', 'E': 'S',
        'F': 'Y', 'G': 'D', 'H': 'K', 'I': 'F', 'J': 'W',
        'K': 'P', 'L': 'C', 'M': 'I', 'N': 'Q', 'O': 'X',
        'P': 'H', 'Q': 'M', 'R': 'V', 'S': 'B', 'T': 'L',
        'U': 'G', 'V': 'N', 'W': 'J', 'X': 'R', 'Y': 'A',
        'Z': 'T'}

III_K = {'A': 'E', 'B': 'H', 'C': 'R', 'D': 'V', 'E': 'X',
         'F': 'G', 'G': 'A', 'H': 'O', 'I': 'B', 'J': 'Q',
         'K': 'U', 'L': 'S', 'M': 'I', 'N': 'M', 'O': 'Z',
         'P': 'F', 'Q': 'L', 'R': 'Y', 'S': 'N', 'T': 'W',
         'U': 'K', 'V': 'T', 'W': 'P', 'X': 'D', 'Y': 'J',
         'Z': 'C'}

# M3, M4 model rotors
I_roman = {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L',
           'F': 'G', 'G': 'D', 'H': 'Q', 'I': 'V', 'J': 'Z',
           'K': 'N', 'L': 'T', 'M': 'O', 'N': 'W', 'O': 'Y',
           'P': 'H', 'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P',
           'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R', 'Y': 'C',
           'Z': 'J', 'notch': 17}

II_roman = {'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K', 'E': 'S',
            'F': 'I', 'G': 'R', 'H': 'U', 'I': 'X', 'J': 'B',
            'K': 'L', 'L': 'H', 'M': 'W', 'N': 'T', 'O': 'M',
            'P': 'C', 'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N',
            'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V', 'Y': 'O',
            'Z': 'E', 'notch': 5}

III_roman = {'A': 'B', 'B': 'D', 'C': 'F', 'D': 'H', 'E': 'J',
             'F': 'L', 'G': 'C', 'H': 'P', 'I': 'R', 'J': 'T',
             'K': 'X', 'L': 'V', 'M': 'Z', 'N': 'N', 'O': 'Y',
             'P': 'E', 'Q': 'I', 'R': 'W', 'S': 'G', 'T': 'A',
             'U': 'K', 'V': 'M', 'W': 'U', 'X': 'S', 'Y': 'Q',
             'Z': 'O', 'notch': 22}

IV_roman = {'A': 'E', 'B': 'S', 'C': 'O', 'D': 'V', 'E': 'P',
            'F': 'Z', 'G': 'J', 'H': 'A', 'I': 'Y', 'J': 'Q',
            'K': 'U', 'L': 'I', 'M': 'R', 'N': 'H', 'O': 'X',
            'P': 'L', 'Q': 'N', 'R': 'F', 'S': 'T', 'T': 'G',
            'U': 'K', 'V': 'D', 'W': 'C', 'X': 'M', 'Y': 'W',
            'Z': 'B', 'notch': 10}

V_roman = {'A': 'V', 'B': 'Z', 'C': 'B', 'D': 'R', 'E': 'G',
           'F': 'I', 'G': 'T', 'H': 'Y', 'I': 'U', 'J': 'P',
           'K': 'S', 'L': 'D', 'M': 'N', 'N': 'H', 'O': 'L',
           'P': 'X', 'Q': 'A', 'R': 'W', 'S': 'M', 'T': 'J',
           'U': 'Q', 'V': 'O', 'W': 'F', 'X': 'E', 'Y': 'C',
           'Z': 'K', 'notch': 0}

VI_roman = {'A': 'J', 'B': 'P', 'C': 'G', 'D': 'V', 'E': 'O',
            'F': 'U', 'G': 'M', 'H': 'F', 'I': 'Y', 'J': 'Q',
            'K': 'B', 'L': 'E', 'M': 'N', 'N': 'H', 'O': 'Z',
            'P': 'R', 'Q': 'D', 'R': 'K', 'S': 'A', 'T': 'S',
            'U': 'X', 'V': 'L', 'W': 'I', 'X': 'C', 'Y': 'T',
            'Z': 'W'}

VII_roman = {'A': 'N', 'B': 'Z', 'C': 'J', 'D': 'H', 'E': 'G',
             'F': 'R', 'G': 'C', 'H': 'X', 'I': 'M', 'J': 'Y',
             'K': 'S', 'L': 'W', 'M': 'B', 'N': 'O', 'O': 'U',
             'P': 'F', 'Q': 'A', 'R': 'I', 'S': 'V', 'T': 'L',
             'U': 'P', 'V': 'E', 'W': 'K', 'X': 'Q', 'Y': 'D',
             'Z': 'T'}

VIII_roman = {'A': 'F', 'B': 'K', 'C': 'Q', 'D': 'H', 'E': 'T',
              'F': 'L', 'G': 'X', 'H': 'O', 'I': 'C', 'J': 'B',
              'K': 'J', 'L': 'S', 'M': 'P', 'N': 'D', 'O': 'Z',
              'P': 'R', 'Q': 'A', 'R': 'M', 'S': 'E', 'T': 'W',
              'U': 'N', 'V': 'I', 'W': 'U', 'X': 'Y', 'Y': 'G',
              'Z': 'V'}

# Reflectors
# M3 reflectors
rf_b = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q',
        'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X',
        'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M',
        'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z',
        'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A',
        'Z': 'T'}

rf_c = {'A': 'F', 'B': 'V', 'C': 'P', 'D': 'J', 'E': 'I',
        'F': 'A', 'G': 'O', 'H': 'Y', 'I': 'E', 'J': 'D',
        'K': 'R', 'L': 'Z', 'M': 'X', 'N': 'W', 'O': 'G',
        'P': 'C', 'Q': 'T', 'R': 'K', 'S': 'U', 'T': 'Q',
        'U': 'S', 'V': 'B', 'W': 'N', 'X': 'M', 'Y': 'H',
        'Z': 'L'}

# Swiss K reflectors
UKW_K = {'A': 'I', 'B': 'M', 'C': 'E', 'D': 'T', 'E': 'C',
         'F': 'G', 'G': 'F', 'H': 'R', 'I': 'A', 'J': 'Y',
         'K': 'S', 'L': 'Q', 'M': 'B', 'N': 'Z', 'O': 'X',
         'P': 'W', 'Q': 'L', 'R': 'H', 'S': 'K', 'T': 'D',
         'U': 'V', 'V': 'U', 'W': 'P', 'X': 'O', 'Y': 'J',
         'Z': 'N'}

ETW_K = {'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T',
         'F': 'Z', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'A',
         'K': 'S', 'L': 'D', 'M': 'F', 'N': 'G', 'O': 'H',
         'P': 'J', 'Q': 'K', 'R': 'P', 'S': 'Y', 'T': 'X',
         'U': 'C', 'V': 'V', 'W': 'B', 'X': 'N', 'Y': 'M',
         'Z': 'L'}
